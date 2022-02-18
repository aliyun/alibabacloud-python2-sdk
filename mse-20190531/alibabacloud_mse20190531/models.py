# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GatewayOptionLogConfigDetails(TeaModel):
    def __init__(self, log_enabled=None, log_store_name=None, project_name=None):
        # 是否开启日志投递
        self.log_enabled = log_enabled  # type: bool
        # 投递的目标logstore
        self.log_store_name = log_store_name  # type: str
        # 投递的目标project
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GatewayOptionLogConfigDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GatewayOptionTraceDetails(TeaModel):
    def __init__(self, sample=None, trace_enabled=None):
        # trace 采样率
        self.sample = sample  # type: long
        # trace是否开启
        self.trace_enabled = trace_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GatewayOptionTraceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.trace_enabled is not None:
            result['TraceEnabled'] = self.trace_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('TraceEnabled') is not None:
            self.trace_enabled = m.get('TraceEnabled')
        return self


class GatewayOption(TeaModel):
    def __init__(self, disable_http_2alpn=None, enable_hardware_acceleration=None, log_config_details=None,
                 trace_details=None):
        # 是否禁用http
        self.disable_http_2alpn = disable_http_2alpn  # type: bool
        # 是否开启硬件加速
        self.enable_hardware_acceleration = enable_hardware_acceleration  # type: bool
        # 日志配置详情
        self.log_config_details = log_config_details  # type: GatewayOptionLogConfigDetails
        # xtrace config option
        self.trace_details = trace_details  # type: GatewayOptionTraceDetails

    def validate(self):
        if self.log_config_details:
            self.log_config_details.validate()
        if self.trace_details:
            self.trace_details.validate()

    def to_map(self):
        _map = super(GatewayOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_http_2alpn is not None:
            result['DisableHttp2Alpn'] = self.disable_http_2alpn
        if self.enable_hardware_acceleration is not None:
            result['EnableHardwareAcceleration'] = self.enable_hardware_acceleration
        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()
        if self.trace_details is not None:
            result['TraceDetails'] = self.trace_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisableHttp2Alpn') is not None:
            self.disable_http_2alpn = m.get('DisableHttp2Alpn')
        if m.get('EnableHardwareAcceleration') is not None:
            self.enable_hardware_acceleration = m.get('EnableHardwareAcceleration')
        if m.get('LogConfigDetails') is not None:
            temp_model = GatewayOptionLogConfigDetails()
            self.log_config_details = temp_model.from_map(m['LogConfigDetails'])
        if m.get('TraceDetails') is not None:
            temp_model = GatewayOptionTraceDetails()
            self.trace_details = temp_model.from_map(m['TraceDetails'])
        return self


class GatewayService(TeaModel):
    def __init__(self, gateway_traffic_policy=None, gateway_unique_id=None, group_name=None, id=None,
                 meta_info=None, name=None, namespace=None, source_type=None):
        # 服务的策略
        self.gateway_traffic_policy = gateway_traffic_policy  # type: TrafficPolicy
        # 网关uniqueId
        self.gateway_unique_id = gateway_unique_id  # type: str
        # 服务所属group
        self.group_name = group_name  # type: str
        # 服务id
        self.id = id  # type: long
        # 元信息
        self.meta_info = meta_info  # type: str
        # 服务名
        self.name = name  # type: str
        # 服务所属namesapce
        self.namespace = namespace  # type: str
        # 服务来源
        self.source_type = source_type  # type: str

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()

    def to_map(self):
        _map = super(GatewayService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = TrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m['GatewayTrafficPolicy'])
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie(TeaModel):
    def __init__(self, name=None, path=None, ttl=None):
        # cookie名
        self.name = name  # type: str
        # cookie path
        self.path = path  # type: str
        # cookie生命周期
        self.ttl = ttl  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.ttl is not None:
            result['TTL'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        return self


class TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig(TeaModel):
    def __init__(self, consistent_hash_lbtype=None, http_cookie=None, parameter_name=None):
        # HEADER, COOKIE, SOURCE_IP, QUERY_PARAMETER
        self.consistent_hash_lbtype = consistent_hash_lbtype  # type: str
        # 使用cookie时配置
        self.http_cookie = http_cookie  # type: TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie
        # 使用根据header和参数路由时生效
        self.parameter_name = parameter_name  # type: str

    def validate(self):
        if self.http_cookie:
            self.http_cookie.validate()

    def to_map(self):
        _map = super(TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistent_hash_lbtype is not None:
            result['ConsistentHashLBType'] = self.consistent_hash_lbtype
        if self.http_cookie is not None:
            result['HttpCookie'] = self.http_cookie.to_map()
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsistentHashLBType') is not None:
            self.consistent_hash_lbtype = m.get('ConsistentHashLBType')
        if m.get('HttpCookie') is not None:
            temp_model = TrafficPolicyLoadBalancerSettingsConsistentHashLBConfigHttpCookie()
            self.http_cookie = temp_model.from_map(m['HttpCookie'])
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        return self


class TrafficPolicyLoadBalancerSettings(TeaModel):
    def __init__(self, consistent_hash_lbconfig=None, loadbalancer_type=None):
        # 一致性hash相关配置
        self.consistent_hash_lbconfig = consistent_hash_lbconfig  # type: TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig
        # 负载均衡类型，枚举类可为ROUND_ROBIN, LEAST_CONN,RANDOM, CONSISTENT_HASH
        self.loadbalancer_type = loadbalancer_type  # type: str

    def validate(self):
        if self.consistent_hash_lbconfig:
            self.consistent_hash_lbconfig.validate()

    def to_map(self):
        _map = super(TrafficPolicyLoadBalancerSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consistent_hash_lbconfig is not None:
            result['ConsistentHashLBConfig'] = self.consistent_hash_lbconfig.to_map()
        if self.loadbalancer_type is not None:
            result['LoadbalancerType'] = self.loadbalancer_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsistentHashLBConfig') is not None:
            temp_model = TrafficPolicyLoadBalancerSettingsConsistentHashLBConfig()
            self.consistent_hash_lbconfig = temp_model.from_map(m['ConsistentHashLBConfig'])
        if m.get('LoadbalancerType') is not None:
            self.loadbalancer_type = m.get('LoadbalancerType')
        return self


class TrafficPolicyTlsSetting(TeaModel):
    def __init__(self, ca_cert_content=None, cert_id=None, sni=None, tls_mode=None):
        # ca证书内容
        self.ca_cert_content = ca_cert_content  # type: str
        # 使用的证书id，仅当为mutual时需要填写
        self.cert_id = cert_id  # type: str
        # 到后端服务些带
        self.sni = sni  # type: str
        # tls模式。为枚举类，可为NONE, SIMPLE, MUITUAL
        self.tls_mode = tls_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrafficPolicyTlsSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert_content is not None:
            result['CaCertContent'] = self.ca_cert_content
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.sni is not None:
            result['Sni'] = self.sni
        if self.tls_mode is not None:
            result['TlsMode'] = self.tls_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaCertContent') is not None:
            self.ca_cert_content = m.get('CaCertContent')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Sni') is not None:
            self.sni = m.get('Sni')
        if m.get('TlsMode') is not None:
            self.tls_mode = m.get('TlsMode')
        return self


class TrafficPolicy(TeaModel):
    def __init__(self, load_balancer_settings=None, tls_setting=None):
        # 负载均衡相关配置
        self.load_balancer_settings = load_balancer_settings  # type: TrafficPolicyLoadBalancerSettings
        # tls相关配置
        self.tls_setting = tls_setting  # type: TrafficPolicyTlsSetting

    def validate(self):
        if self.load_balancer_settings:
            self.load_balancer_settings.validate()
        if self.tls_setting:
            self.tls_setting.validate()

    def to_map(self):
        _map = super(TrafficPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_settings is not None:
            result['LoadBalancerSettings'] = self.load_balancer_settings.to_map()
        if self.tls_setting is not None:
            result['TlsSetting'] = self.tls_setting.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoadBalancerSettings') is not None:
            temp_model = TrafficPolicyLoadBalancerSettings()
            self.load_balancer_settings = temp_model.from_map(m['LoadBalancerSettings'])
        if m.get('TlsSetting') is not None:
            temp_model = TrafficPolicyTlsSetting()
            self.tls_setting = temp_model.from_map(m['TlsSetting'])
        return self


class AddAuthResourceRequest(TeaModel):
    def __init__(self, accept_language=None, auth_id=None, domain_id=None, gateway_unique_id=None, path=None):
        self.accept_language = accept_language  # type: str
        self.auth_id = auth_id  # type: long
        self.domain_id = domain_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAuthResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class AddAuthResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAuthResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAuthResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddAuthResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAuthResourceResponse, self).to_map()
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
            temp_model = AddAuthResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBlackWhiteListRequest(TeaModel):
    def __init__(self, accept_language=None, content=None, gateway_unique_id=None, is_white=None,
                 resource_type=None, status=None, type=None):
        self.accept_language = accept_language  # type: str
        self.content = content  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.is_white = is_white  # type: bool
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlackWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.content is not None:
            result['Content'] = self.content
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddBlackWhiteListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlackWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBlackWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddBlackWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddBlackWhiteListResponse, self).to_map()
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
            temp_model = AddBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayRequest(TeaModel):
    def __init__(self, accept_language=None, enterprise_security_group=None, internet_slb_spec=None, name=None,
                 region=None, replica=None, slb_spec=None, spec=None, v_switch_id=None, v_switch_id_2=None, vpc=None):
        self.accept_language = accept_language  # type: str
        # 是否企业安全组类型
        self.enterprise_security_group = enterprise_security_group  # type: bool
        # 外网SLB规格
        self.internet_slb_spec = internet_slb_spec  # type: str
        # 网关名称
        self.name = name  # type: str
        # 地域
        self.region = region  # type: str
        # 节点数量
        self.replica = replica  # type: int
        # 内网SLB规格
        self.slb_spec = slb_spec  # type: str
        # 节点规格
        self.spec = spec  # type: str
        # 主交换机ID
        self.v_switch_id = v_switch_id  # type: str
        # 备交换机ID
        self.v_switch_id_2 = v_switch_id_2  # type: str
        # 专有网络ID
        self.vpc = vpc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.enterprise_security_group is not None:
            result['EnterpriseSecurityGroup'] = self.enterprise_security_group
        if self.internet_slb_spec is not None:
            result['InternetSlbSpec'] = self.internet_slb_spec
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_id_2 is not None:
            result['VSwitchId2'] = self.v_switch_id_2
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('EnterpriseSecurityGroup') is not None:
            self.enterprise_security_group = m.get('EnterpriseSecurityGroup')
        if m.get('InternetSlbSpec') is not None:
            self.internet_slb_spec = m.get('InternetSlbSpec')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchId2') is not None:
            self.v_switch_id_2 = m.get('VSwitchId2')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        return self


class AddGatewayResponseBodyData(TeaModel):
    def __init__(self, gateway_unique_id=None):
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class AddGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: AddGatewayResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGatewayResponse, self).to_map()
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
            temp_model = AddGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayDomainRequest(TeaModel):
    def __init__(self, accept_language=None, cert_identifier=None, gateway_unique_id=None, must_https=None,
                 name=None, protocol=None):
        self.accept_language = accept_language  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.must_https = must_https  # type: bool
        self.name = name  # type: str
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class AddGatewayDomainResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGatewayDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGatewayDomainResponse, self).to_map()
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
            temp_model = AddGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayRouteRequestDirectResponseJSON(TeaModel):
    def __init__(self, body=None, code=None):
        self.body = body  # type: str
        self.code = code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteRequestDirectResponseJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddGatewayRouteRequestPredicatesHeaderPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteRequestPredicatesHeaderPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddGatewayRouteRequestPredicatesPathPredicates(TeaModel):
    def __init__(self, ignore_case=None, path=None, type=None):
        self.ignore_case = ignore_case  # type: bool
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteRequestPredicatesPathPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddGatewayRouteRequestPredicatesQueryPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteRequestPredicatesQueryPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddGatewayRouteRequestPredicates(TeaModel):
    def __init__(self, header_predicates=None, method_predicates=None, path_predicates=None, query_predicates=None):
        self.header_predicates = header_predicates  # type: list[AddGatewayRouteRequestPredicatesHeaderPredicates]
        self.method_predicates = method_predicates  # type: list[str]
        self.path_predicates = path_predicates  # type: AddGatewayRouteRequestPredicatesPathPredicates
        self.query_predicates = query_predicates  # type: list[AddGatewayRouteRequestPredicatesQueryPredicates]

    def validate(self):
        if self.header_predicates:
            for k in self.header_predicates:
                if k:
                    k.validate()
        if self.path_predicates:
            self.path_predicates.validate()
        if self.query_predicates:
            for k in self.query_predicates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddGatewayRouteRequestPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HeaderPredicates'] = []
        if self.header_predicates is not None:
            for k in self.header_predicates:
                result['HeaderPredicates'].append(k.to_map() if k else None)
        if self.method_predicates is not None:
            result['MethodPredicates'] = self.method_predicates
        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()
        result['QueryPredicates'] = []
        if self.query_predicates is not None:
            for k in self.query_predicates:
                result['QueryPredicates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.header_predicates = []
        if m.get('HeaderPredicates') is not None:
            for k in m.get('HeaderPredicates'):
                temp_model = AddGatewayRouteRequestPredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k))
        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')
        if m.get('PathPredicates') is not None:
            temp_model = AddGatewayRouteRequestPredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m['PathPredicates'])
        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k in m.get('QueryPredicates'):
                temp_model = AddGatewayRouteRequestPredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k))
        return self


class AddGatewayRouteRequestRedirectJSON(TeaModel):
    def __init__(self, code=None, host=None, path=None):
        self.code = code  # type: int
        self.host = host  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteRequestRedirectJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class AddGatewayRouteRequestServices(TeaModel):
    def __init__(self, group_name=None, name=None, namespace=None, percent=None, service_id=None, source_type=None,
                 version=None):
        self.group_name = group_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.percent = percent  # type: int
        self.service_id = service_id  # type: long
        self.source_type = source_type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteRequestServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AddGatewayRouteRequest(TeaModel):
    def __init__(self, accept_language=None, destination_type=None, direct_response_json=None, domain_id=None,
                 domain_id_list_json=None, gateway_id=None, gateway_unique_id=None, name=None, predicates=None, redirect_json=None,
                 route_order=None, services=None):
        self.accept_language = accept_language  # type: str
        self.destination_type = destination_type  # type: str
        self.direct_response_json = direct_response_json  # type: AddGatewayRouteRequestDirectResponseJSON
        self.domain_id = domain_id  # type: long
        self.domain_id_list_json = domain_id_list_json  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.name = name  # type: str
        self.predicates = predicates  # type: AddGatewayRouteRequestPredicates
        self.redirect_json = redirect_json  # type: AddGatewayRouteRequestRedirectJSON
        self.route_order = route_order  # type: int
        self.services = services  # type: list[AddGatewayRouteRequestServices]

    def validate(self):
        if self.direct_response_json:
            self.direct_response_json.validate()
        if self.predicates:
            self.predicates.validate()
        if self.redirect_json:
            self.redirect_json.validate()
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddGatewayRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direct_response_json is not None:
            result['DirectResponseJSON'] = self.direct_response_json.to_map()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_id_list_json is not None:
            result['DomainIdListJSON'] = self.domain_id_list_json
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates is not None:
            result['Predicates'] = self.predicates.to_map()
        if self.redirect_json is not None:
            result['RedirectJSON'] = self.redirect_json.to_map()
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DirectResponseJSON') is not None:
            temp_model = AddGatewayRouteRequestDirectResponseJSON()
            self.direct_response_json = temp_model.from_map(m['DirectResponseJSON'])
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainIdListJSON') is not None:
            self.domain_id_list_json = m.get('DomainIdListJSON')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            temp_model = AddGatewayRouteRequestPredicates()
            self.predicates = temp_model.from_map(m['Predicates'])
        if m.get('RedirectJSON') is not None:
            temp_model = AddGatewayRouteRequestRedirectJSON()
            self.redirect_json = temp_model.from_map(m['RedirectJSON'])
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = AddGatewayRouteRequestServices()
                self.services.append(temp_model.from_map(k))
        return self


class AddGatewayRouteShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, destination_type=None, direct_response_jsonshrink=None,
                 domain_id=None, domain_id_list_json=None, gateway_id=None, gateway_unique_id=None, name=None,
                 predicates_shrink=None, redirect_jsonshrink=None, route_order=None, services_shrink=None):
        self.accept_language = accept_language  # type: str
        self.destination_type = destination_type  # type: str
        self.direct_response_jsonshrink = direct_response_jsonshrink  # type: str
        self.domain_id = domain_id  # type: long
        self.domain_id_list_json = domain_id_list_json  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.name = name  # type: str
        self.predicates_shrink = predicates_shrink  # type: str
        self.redirect_jsonshrink = redirect_jsonshrink  # type: str
        self.route_order = route_order  # type: int
        self.services_shrink = services_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direct_response_jsonshrink is not None:
            result['DirectResponseJSON'] = self.direct_response_jsonshrink
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_id_list_json is not None:
            result['DomainIdListJSON'] = self.domain_id_list_json
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates_shrink is not None:
            result['Predicates'] = self.predicates_shrink
        if self.redirect_jsonshrink is not None:
            result['RedirectJSON'] = self.redirect_jsonshrink
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        if self.services_shrink is not None:
            result['Services'] = self.services_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DirectResponseJSON') is not None:
            self.direct_response_jsonshrink = m.get('DirectResponseJSON')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainIdListJSON') is not None:
            self.domain_id_list_json = m.get('DomainIdListJSON')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            self.predicates_shrink = m.get('Predicates')
        if m.get('RedirectJSON') is not None:
            self.redirect_jsonshrink = m.get('RedirectJSON')
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        if m.get('Services') is not None:
            self.services_shrink = m.get('Services')
        return self


class AddGatewayRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayRouteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGatewayRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGatewayRouteResponse, self).to_map()
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
            temp_model = AddGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewayServiceVersionRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, service_id=None, service_version=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.service_id = service_id  # type: long
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayServiceVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class AddGatewayServiceVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewayServiceVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewayServiceVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGatewayServiceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGatewayServiceVersionResponse, self).to_map()
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
            temp_model = AddGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGatewaySlbRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, slb_id=None, type=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.slb_id = slb_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewaySlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddGatewaySlbResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddGatewaySlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddGatewaySlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddGatewaySlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddGatewaySlbResponse, self).to_map()
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
            temp_model = AddGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMockRuleRequest(TeaModel):
    def __init__(self, accept_language=None, consumer_app_ids=None, dubbo_mock_items=None, enable=None,
                 extra_json=None, mock_type=None, name=None, provider_app_id=None, provider_app_name=None, region=None,
                 sc_mock_items=None, source=None):
        self.accept_language = accept_language  # type: str
        self.consumer_app_ids = consumer_app_ids  # type: str
        self.dubbo_mock_items = dubbo_mock_items  # type: str
        self.enable = enable  # type: bool
        self.extra_json = extra_json  # type: str
        self.mock_type = mock_type  # type: long
        self.name = name  # type: str
        self.provider_app_id = provider_app_id  # type: str
        self.provider_app_name = provider_app_name  # type: str
        self.region = region  # type: str
        self.sc_mock_items = sc_mock_items  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMockRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.consumer_app_ids is not None:
            result['ConsumerAppIds'] = self.consumer_app_ids
        if self.dubbo_mock_items is not None:
            result['DubboMockItems'] = self.dubbo_mock_items
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.mock_type is not None:
            result['MockType'] = self.mock_type
        if self.name is not None:
            result['Name'] = self.name
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.region is not None:
            result['Region'] = self.region
        if self.sc_mock_items is not None:
            result['ScMockItems'] = self.sc_mock_items
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ConsumerAppIds') is not None:
            self.consumer_app_ids = m.get('ConsumerAppIds')
        if m.get('DubboMockItems') is not None:
            self.dubbo_mock_items = m.get('DubboMockItems')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ScMockItems') is not None:
            self.sc_mock_items = m.get('ScMockItems')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class AddMockRuleResponseBodyData(TeaModel):
    def __init__(self, account_id=None, consumer_app_id=None, consumer_app_name=None, enable=None, extra_json=None,
                 id=None, mock_type=None, name=None, namespace_id=None, provider_app_id=None, provider_app_name=None,
                 region=None, sc_mock_item_json=None, source=None):
        self.account_id = account_id  # type: str
        self.consumer_app_id = consumer_app_id  # type: str
        self.consumer_app_name = consumer_app_name  # type: str
        self.enable = enable  # type: bool
        self.extra_json = extra_json  # type: str
        self.id = id  # type: long
        self.mock_type = mock_type  # type: long
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.provider_app_id = provider_app_id  # type: str
        self.provider_app_name = provider_app_name  # type: str
        self.region = region  # type: str
        self.sc_mock_item_json = sc_mock_item_json  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMockRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.consumer_app_id is not None:
            result['ConsumerAppId'] = self.consumer_app_id
        if self.consumer_app_name is not None:
            result['ConsumerAppName'] = self.consumer_app_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json
        if self.id is not None:
            result['Id'] = self.id
        if self.mock_type is not None:
            result['MockType'] = self.mock_type
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.provider_app_id is not None:
            result['ProviderAppId'] = self.provider_app_id
        if self.provider_app_name is not None:
            result['ProviderAppName'] = self.provider_app_name
        if self.region is not None:
            result['Region'] = self.region
        if self.sc_mock_item_json is not None:
            result['ScMockItemJson'] = self.sc_mock_item_json
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ConsumerAppId') is not None:
            self.consumer_app_id = m.get('ConsumerAppId')
        if m.get('ConsumerAppName') is not None:
            self.consumer_app_name = m.get('ConsumerAppName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MockType') is not None:
            self.mock_type = m.get('MockType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ProviderAppId') is not None:
            self.provider_app_id = m.get('ProviderAppId')
        if m.get('ProviderAppName') is not None:
            self.provider_app_name = m.get('ProviderAppName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ScMockItemJson') is not None:
            self.sc_mock_item_json = m.get('ScMockItemJson')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class AddMockRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: AddMockRuleResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddMockRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddMockRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMockRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddMockRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddMockRuleResponse, self).to_map()
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
            temp_model = AddMockRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSSLCertRequest(TeaModel):
    def __init__(self, accept_language=None, cert_identifier=None, domain_id=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.domain_id = domain_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSSLCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class AddSSLCertResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSSLCertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSSLCertResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddSSLCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSSLCertResponse, self).to_map()
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
            temp_model = AddSSLCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddServiceSourceRequest(TeaModel):
    def __init__(self, accept_language=None, address=None, gateway_unique_id=None, name=None, source=None, type=None):
        self.accept_language = accept_language  # type: str
        self.address = address  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddServiceSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.address is not None:
            result['Address'] = self.address
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddServiceSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddServiceSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddServiceSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddServiceSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddServiceSourceResponse, self).to_map()
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
            temp_model = AddServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyGatewayRouteRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, route_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.route_id = route_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyGatewayRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        return self


class ApplyGatewayRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyGatewayRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyGatewayRouteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyGatewayRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyGatewayRouteResponse, self).to_map()
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
            temp_model = ApplyGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, ids=None, instance_id=None, origin_namespace_id=None, policy=None,
                 target_namespace_id=None):
        self.accept_language = accept_language  # type: str
        self.ids = ids  # type: str
        self.instance_id = instance_id  # type: str
        self.origin_namespace_id = origin_namespace_id  # type: str
        self.policy = policy  # type: str
        self.target_namespace_id = target_namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.origin_namespace_id is not None:
            result['OriginNamespaceId'] = self.origin_namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.target_namespace_id is not None:
            result['TargetNamespaceId'] = self.target_namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginNamespaceId') is not None:
            self.origin_namespace_id = m.get('OriginNamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('TargetNamespaceId') is not None:
            self.target_namespace_id = m.get('TargetNamespaceId')
        return self


class CloneNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneNacosConfigResponseBodyDataFailData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneNacosConfigResponseBodyDataSkipData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class CloneNacosConfigResponseBodyData(TeaModel):
    def __init__(self, fail_data=None, skip_count=None, skip_data=None, succ_count=None):
        self.fail_data = fail_data  # type: list[CloneNacosConfigResponseBodyDataFailData]
        self.skip_count = skip_count  # type: int
        self.skip_data = skip_data  # type: list[CloneNacosConfigResponseBodyDataSkipData]
        self.succ_count = succ_count  # type: int

    def validate(self):
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CloneNacosConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = CloneNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = CloneNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        return self


class CloneNacosConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: CloneNacosConfigResponseBodyData
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CloneNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CloneNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloneNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloneNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneNacosConfigResponse, self).to_map()
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
            temp_model = CloneNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmRuleRequest(TeaModel):
    def __init__(self, accept_language=None, aggregates=None, alarm_alias_name=None, alarm_item=None,
                 alert_way=None, contact_group_ids=None, instance_id=None, nvalue=None, operator=None, value=None):
        self.accept_language = accept_language  # type: str
        self.aggregates = aggregates  # type: str
        self.alarm_alias_name = alarm_alias_name  # type: str
        self.alarm_item = alarm_item  # type: str
        self.alert_way = alert_way  # type: dict[str, any]
        self.contact_group_ids = contact_group_ids  # type: dict[str, any]
        self.instance_id = instance_id  # type: str
        self.nvalue = nvalue  # type: int
        self.operator = operator  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, aggregates=None, alarm_alias_name=None, alarm_item=None,
                 alert_way_shrink=None, contact_group_ids_shrink=None, instance_id=None, nvalue=None, operator=None, value=None):
        self.accept_language = accept_language  # type: str
        self.aggregates = aggregates  # type: str
        self.alarm_alias_name = alarm_alias_name  # type: str
        self.alarm_item = alarm_item  # type: str
        self.alert_way_shrink = alert_way_shrink  # type: str
        self.contact_group_ids_shrink = contact_group_ids_shrink  # type: str
        self.instance_id = instance_id  # type: str
        self.nvalue = nvalue  # type: int
        self.operator = operator  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alarm_alias_name is not None:
            result['AlarmAliasName'] = self.alarm_alias_name
        if self.alarm_item is not None:
            result['AlarmItem'] = self.alarm_item
        if self.alert_way_shrink is not None:
            result['AlertWay'] = self.alert_way_shrink
        if self.contact_group_ids_shrink is not None:
            result['ContactGroupIds'] = self.contact_group_ids_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('AlarmAliasName') is not None:
            self.alarm_alias_name = m.get('AlarmAliasName')
        if m.get('AlarmItem') is not None:
            self.alarm_item = m.get('AlarmItem')
        if m.get('AlertWay') is not None:
            self.alert_way_shrink = m.get('AlertWay')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids_shrink = m.get('ContactGroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateAlarmRuleResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAlarmRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAlarmRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlarmRuleResponse, self).to_map()
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
            temp_model = CreateAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, accept_language=None, app_name=None, extra_info=None, language=None, region=None, source=None):
        self.accept_language = accept_language  # type: str
        self.app_name = app_name  # type: str
        self.extra_info = extra_info  # type: str
        self.language = language  # type: str
        self.region = region  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.language is not None:
            result['Language'] = self.language
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, create_time=None, extra_info=None, language=None,
                 license_key=None, region_id=None, source=None, status=None, update_time=None, user_id=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.create_time = create_time  # type: long
        self.extra_info = extra_info  # type: str
        self.language = language  # type: str
        self.license_key = license_key  # type: str
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.status = status  # type: int
        self.update_time = update_time  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.language is not None:
            result['Language'] = self.language
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: CreateApplicationResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationResponse, self).to_map()
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_specification=None, cluster_type=None, cluster_version=None,
                 connection_type=None, disk_capacity=None, disk_type=None, instance_count=None, mse_version=None, net_type=None,
                 private_slb_specification=None, pub_network_flow=None, pub_slb_specification=None, region=None, request_pars=None,
                 v_switch_id=None, vpc_id=None):
        self.accept_language = accept_language  # type: str
        self.cluster_specification = cluster_specification  # type: str
        self.cluster_type = cluster_type  # type: str
        self.cluster_version = cluster_version  # type: str
        self.connection_type = connection_type  # type: str
        self.disk_capacity = disk_capacity  # type: int
        self.disk_type = disk_type  # type: str
        self.instance_count = instance_count  # type: int
        # 用于区分基础/专业版本
        self.mse_version = mse_version  # type: str
        self.net_type = net_type  # type: str
        self.private_slb_specification = private_slb_specification  # type: str
        self.pub_network_flow = pub_network_flow  # type: str
        self.pub_slb_specification = pub_slb_specification  # type: str
        self.region = region  # type: str
        self.request_pars = request_pars  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.private_slb_specification is not None:
            result['PrivateSlbSpecification'] = self.private_slb_specification
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.pub_slb_specification is not None:
            result['PubSlbSpecification'] = self.pub_slb_specification
        if self.region is not None:
            result['Region'] = self.region
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('PrivateSlbSpecification') is not None:
            self.private_slb_specification = m.get('PrivateSlbSpecification')
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('PubSlbSpecification') is not None:
            self.pub_slb_specification = m.get('PubSlbSpecification')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, instance_id=None, message=None, order_id=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.instance_id = instance_id  # type: str
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEngineNamespaceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, desc=None, instance_id=None, name=None,
                 service_count=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.desc = desc  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.service_count = service_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEngineNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class CreateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(self, config_count=None, namespace=None, namespace_desc=None, namespace_show_name=None, quota=None,
                 service_count=None, type=None):
        self.config_count = config_count  # type: int
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: int
        self.service_count = service_count  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEngineNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateEngineNamespaceResponseBody(TeaModel):
    def __init__(self, cluster_id=None, data=None, error_code=None, message=None, request_id=None, success=None):
        self.cluster_id = cluster_id  # type: str
        self.data = data  # type: CreateEngineNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEngineNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            temp_model = CreateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEngineNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEngineNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEngineNamespaceResponse, self).to_map()
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
            temp_model = CreateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, app_name=None, beta_ips=None, content=None, data_id=None, desc=None,
                 group=None, instance_id=None, namespace_id=None, tags=None, type=None):
        self.accept_language = accept_language  # type: str
        self.app_name = app_name  # type: str
        self.beta_ips = beta_ips  # type: str
        self.content = content  # type: str
        self.data_id = data_id  # type: str
        self.desc = desc  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.tags = tags  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateNacosConfigResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNacosConfigResponse, self).to_map()
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
            temp_model = CreateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosInstanceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_name=None, enabled=None, ephemeral=None, group_name=None,
                 instance_id=None, ip=None, metadata=None, namespace_id=None, port=None, service_name=None, weight=None):
        self.accept_language = accept_language  # type: str
        # Nacos集群名
        self.cluster_name = cluster_name  # type: str
        # 服务禁用标志
        self.enabled = enabled  # type: bool
        # 临时节点标志
        self.ephemeral = ephemeral  # type: bool
        # 分组名
        self.group_name = group_name  # type: str
        # 实例id
        self.instance_id = instance_id  # type: str
        # Nacos实例ip
        self.ip = ip  # type: str
        # 节点元数据
        self.metadata = metadata  # type: str
        # 命名空间id
        self.namespace_id = namespace_id  # type: str
        # Nacos实例端口
        self.port = port  # type: int
        # 服务名
        self.service_name = service_name  # type: str
        # 权重
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.port is not None:
            result['Port'] = self.port
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateNacosInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        # 响应码
        self.code = code  # type: int
        # 修改结果
        self.data = data  # type: str
        # http状态码
        self.http_status_code = http_status_code  # type: int
        # 响应信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 成功标志
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNacosInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNacosInstanceResponse, self).to_map()
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
            temp_model = CreateNacosInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNacosServiceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, ephemeral=None, group_name=None, instance_id=None,
                 namespace_id=None, protect_threshold=None, service_name=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.ephemeral = ephemeral  # type: bool
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.protect_threshold = protect_threshold  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateNacosServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNacosServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNacosServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNacosServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNacosServiceResponse, self).to_map()
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
            temp_model = CreateNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateSwimmingLaneRequestEntryRulesRestItems(TeaModel):
    def __init__(self, cond=None, datum=None, divisor=None, name=None, name_list=None, operator=None, rate=None,
                 remainder=None, type=None, value=None):
        self.cond = cond  # type: str
        self.datum = datum  # type: str
        self.divisor = divisor  # type: int
        self.name = name  # type: str
        self.name_list = name_list  # type: list[str]
        self.operator = operator  # type: str
        self.rate = rate  # type: int
        self.remainder = remainder  # type: int
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneRequestEntryRulesRestItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['Cond'] = self.cond
        if self.datum is not None:
            result['Datum'] = self.datum
        if self.divisor is not None:
            result['Divisor'] = self.divisor
        if self.name is not None:
            result['Name'] = self.name
        if self.name_list is not None:
            result['NameList'] = self.name_list
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.remainder is not None:
            result['Remainder'] = self.remainder
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cond') is not None:
            self.cond = m.get('Cond')
        if m.get('Datum') is not None:
            self.datum = m.get('Datum')
        if m.get('Divisor') is not None:
            self.divisor = m.get('Divisor')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Remainder') is not None:
            self.remainder = m.get('Remainder')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateSwimmingLaneRequestEntryRules(TeaModel):
    def __init__(self, condition=None, enable=None, path=None, priority=None, rest_items=None):
        self.condition = condition  # type: str
        self.enable = enable  # type: bool
        self.path = path  # type: str
        self.priority = priority  # type: int
        self.rest_items = rest_items  # type: list[CreateOrUpdateSwimmingLaneRequestEntryRulesRestItems]

    def validate(self):
        if self.rest_items:
            for k in self.rest_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneRequestEntryRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.path is not None:
            result['Path'] = self.path
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RestItems'] = []
        if self.rest_items is not None:
            for k in self.rest_items:
                result['RestItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rest_items = []
        if m.get('RestItems') is not None:
            for k in m.get('RestItems'):
                temp_model = CreateOrUpdateSwimmingLaneRequestEntryRulesRestItems()
                self.rest_items.append(temp_model.from_map(k))
        return self


class CreateOrUpdateSwimmingLaneRequest(TeaModel):
    def __init__(self, accept_language=None, enable=None, enable_rules=None, entry_rule=None, entry_rules=None,
                 gmt_create=None, gmt_modified=None, group_id=None, id=None, license_key=None, name=None, region_id=None,
                 source=None, status=None, tag=None, user_id=None):
        self.accept_language = accept_language  # type: str
        # 是否开启。
        self.enable = enable  # type: bool
        self.enable_rules = enable_rules  # type: bool
        # json string
        self.entry_rule = entry_rule  # type: str
        # SwimmingLane
        self.entry_rules = entry_rules  # type: list[CreateOrUpdateSwimmingLaneRequestEntryRules]
        # 创建时间
        self.gmt_create = gmt_create  # type: str
        # 更新时间
        self.gmt_modified = gmt_modified  # type: str
        # 所属泳道组
        self.group_id = group_id  # type: long
        # 主键ID。由SP生成(数据库自增主键)。
        self.id = id  # type: long
        # 格式为UUID。比如48bd91e9-41d5-4dae-8a9a-439611742b45
        self.license_key = license_key  # type: str
        # 名称
        self.name = name  # type: str
        # region
        self.region_id = region_id  # type: str
        # 来源。可选值为: EDAS。
        self.source = source  # type: str
        # 0 未生效
        self.status = status  # type: int
        # 标识
        self.tag = tag  # type: str
        # EDAS账号。格式为数字，比如1362469756373809。
        self.user_id = user_id  # type: str

    def validate(self):
        if self.entry_rules:
            for k in self.entry_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.enable_rules is not None:
            result['EnableRules'] = self.enable_rules
        if self.entry_rule is not None:
            result['EntryRule'] = self.entry_rule
        result['EntryRules'] = []
        if self.entry_rules is not None:
            for k in self.entry_rules:
                result['EntryRules'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EnableRules') is not None:
            self.enable_rules = m.get('EnableRules')
        if m.get('EntryRule') is not None:
            self.entry_rule = m.get('EntryRule')
        self.entry_rules = []
        if m.get('EntryRules') is not None:
            for k in m.get('EntryRules'):
                temp_model = CreateOrUpdateSwimmingLaneRequestEntryRules()
                self.entry_rules.append(temp_model.from_map(k))
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateOrUpdateSwimmingLaneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOrUpdateSwimmingLaneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOrUpdateSwimmingLaneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneResponse, self).to_map()
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
            temp_model = CreateOrUpdateSwimmingLaneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateSwimmingLaneGroupRequest(TeaModel):
    def __init__(self, accept_language=None, app_ids=None, enable=None, entry_app=None, gmt_create=None,
                 gmt_modified=None, id=None, license_key=None, name=None, region=None, source=None, status=None, user_id=None):
        self.accept_language = accept_language  # type: str
        # 应用集合。以 "," 分割应用 id
        self.app_ids = app_ids  # type: str
        # 是否开启。
        self.enable = enable  # type: bool
        # 入口应用。格式 "来源系统:id"，比如 EDAS:UUID 或者 CSB:UUID
        self.entry_app = entry_app  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: str
        # 更新时间
        self.gmt_modified = gmt_modified  # type: str
        # 主键ID。由SP生成(数据库自增主键)。
        self.id = id  # type: long
        # mse licenseKey
        self.license_key = license_key  # type: str
        # 名称
        self.name = name  # type: str
        # region
        self.region = region  # type: str
        # 来源。可选值为: EDAS。
        self.source = source  # type: str
        # 0 未生效
        self.status = status  # type: int
        # 阿里云账号。格式为数字，比如1362469756373809。
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.entry_app is not None:
            result['EntryApp'] = self.entry_app
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EntryApp') is not None:
            self.entry_app = m.get('EntryApp')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateOrUpdateSwimmingLaneGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOrUpdateSwimmingLaneGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOrUpdateSwimmingLaneGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrUpdateSwimmingLaneGroupResponse, self).to_map()
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
            temp_model = CreateOrUpdateSwimmingLaneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateZnodeRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, data=None, path=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data = data  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateZnodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateZnodeResponseBodyData(TeaModel):
    def __init__(self, data=None, dir=None, name=None, path=None):
        self.data = data  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateZnodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateZnodeResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: CreateZnodeResponseBodyData
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateZnodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateZnodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateZnodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateZnodeResponse, self).to_map()
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
            temp_model = CreateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmRuleRequest(TeaModel):
    def __init__(self, accept_language=None, alarm_rule_id=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.alarm_rule_id = alarm_rule_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class DeleteAlarmRuleResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAlarmRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAlarmRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlarmRuleResponse, self).to_map()
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
            temp_model = DeleteAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthResourceRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAuthResourceResponseBodyData(TeaModel):
    def __init__(self, auth_id=None, domain_id=None, domain_name=None, gateway_id=None, gateway_unique_id=None,
                 gmt_create=None, gmt_modified=None, id=None, is_white=None, path=None):
        self.auth_id = auth_id  # type: long
        self.domain_id = domain_id  # type: long
        self.domain_name = domain_name  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.is_white = is_white  # type: bool
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteAuthResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DeleteAuthResourceResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteAuthResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteAuthResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAuthResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAuthResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAuthResourceResponse, self).to_map()
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
            temp_model = DeleteAuthResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, accept_language=None, instance_id=None):
        self.accept_language = accept_language  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterResponse, self).to_map()
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEngineNamespaceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, id=None, instance_id=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEngineNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteEngineNamespaceResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEngineNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEngineNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEngineNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEngineNamespaceResponse, self).to_map()
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
            temp_model = DeleteEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRequest(TeaModel):
    def __init__(self, accept_language=None, delete_slb=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.delete_slb = delete_slb  # type: bool
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.delete_slb is not None:
            result['DeleteSlb'] = self.delete_slb
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DeleteSlb') is not None:
            self.delete_slb = m.get('DeleteSlb')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class DeleteGatewayResponseBodyData(TeaModel):
    def __init__(self, gateway_unique_id=None, gmt_create=None, gmt_modified=None, id=None, name=None,
                 primary_user=None, region=None, replica=None, security_group=None, spec=None, status=None, vpc=None, vswitch=None):
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.primary_user = primary_user  # type: str
        self.region = region  # type: str
        self.replica = replica  # type: int
        self.security_group = security_group  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: int
        self.vpc = vpc  # type: str
        self.vswitch = vswitch  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DeleteGatewayResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGatewayResponse, self).to_map()
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
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayDomainRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGatewayDomainResponseBodyData(TeaModel):
    def __init__(self, cert_identifier=None, gateway_id=None, gateway_unique_id=None, gmt_create=None,
                 gmt_modified=None, id=None, must_https=None, name=None, protocol=None):
        self.cert_identifier = cert_identifier  # type: int
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.must_https = must_https  # type: bool
        self.name = name  # type: str
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayDomainResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DeleteGatewayDomainResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DeleteGatewayDomainResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteGatewayDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteGatewayDomainResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGatewayDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGatewayDomainResponse, self).to_map()
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
            temp_model = DeleteGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRouteRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, route_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.route_id = route_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        return self


class DeleteGatewayRouteResponseBodyData(TeaModel):
    def __init__(self, default_service_id=None, gateway_id=None, gateway_unique_id=None, gmt_create=None,
                 gmt_modified=None, id=None, name=None, predicates=None, route_order=None, status=None):
        self.default_service_id = default_service_id  # type: long
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.predicates = predicates  # type: str
        self.route_order = route_order  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates is not None:
            result['Predicates'] = self.predicates
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            self.predicates = m.get('Predicates')
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteGatewayRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: DeleteGatewayRouteResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteGatewayRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteGatewayRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayRouteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGatewayRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGatewayRouteResponse, self).to_map()
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
            temp_model = DeleteGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayServiceVersionRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, service_id=None, service_version=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.service_id = service_id  # type: long
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayServiceVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class DeleteGatewayServiceVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewayServiceVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayServiceVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGatewayServiceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGatewayServiceVersionResponse, self).to_map()
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
            temp_model = DeleteGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewaySlbRequest(TeaModel):
    def __init__(self, accept_language=None, delete_slb=None, gateway_unique_id=None, id=None):
        self.accept_language = accept_language  # type: str
        self.delete_slb = delete_slb  # type: bool
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewaySlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.delete_slb is not None:
            result['DeleteSlb'] = self.delete_slb
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DeleteSlb') is not None:
            self.delete_slb = m.get('DeleteSlb')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGatewaySlbResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGatewaySlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewaySlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGatewaySlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGatewaySlbResponse, self).to_map()
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
            temp_model = DeleteGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, beta=None, data_id=None, group=None, instance_id=None,
                 namespace_id=None):
        self.accept_language = accept_language  # type: str
        self.beta = beta  # type: bool
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.beta is not None:
            result['Beta'] = self.beta
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Beta') is not None:
            self.beta = m.get('Beta')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNacosConfigResponse, self).to_map()
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
            temp_model = DeleteNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosConfigsRequest(TeaModel):
    def __init__(self, accept_language=None, ids=None, instance_id=None, namespace_id=None):
        self.accept_language = accept_language  # type: str
        self.ids = ids  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNacosConfigsResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNacosConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNacosConfigsResponse, self).to_map()
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
            temp_model = DeleteNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNacosServiceRequest(TeaModel):
    def __init__(self, accept_language=None, group_name=None, instance_id=None, namespace_id=None,
                 service_name=None):
        self.accept_language = accept_language  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DeleteNacosServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        # 响应码
        self.code = code  # type: int
        # 删除服务的结果
        self.data = data  # type: str
        # http状态码
        self.http_status_code = http_status_code  # type: int
        # 响应信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 成功标志
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNacosServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNacosServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNacosServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNacosServiceResponse, self).to_map()
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
            temp_model = DeleteNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceSourceRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, source_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.source_id = source_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class DeleteServiceSourceResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceSourceResponse, self).to_map()
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
            temp_model = DeleteServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSwimmingLaneRequest(TeaModel):
    def __init__(self, accept_language=None, lane_id=None):
        self.accept_language = accept_language  # type: str
        self.lane_id = lane_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSwimmingLaneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.lane_id is not None:
            result['LaneId'] = self.lane_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')
        return self


class DeleteSwimmingLaneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSwimmingLaneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSwimmingLaneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSwimmingLaneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSwimmingLaneResponse, self).to_map()
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
            temp_model = DeleteSwimmingLaneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSwimmingLaneGroupRequest(TeaModel):
    def __init__(self, accept_language=None, group_id=None):
        self.accept_language = accept_language  # type: str
        self.group_id = group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSwimmingLaneGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteSwimmingLaneGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSwimmingLaneGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSwimmingLaneGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSwimmingLaneGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSwimmingLaneGroupResponse, self).to_map()
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
            temp_model = DeleteSwimmingLaneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZnodeRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, path=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteZnodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class DeleteZnodeResponseBodyData(TeaModel):
    def __init__(self, data=None, dir=None, name=None, path=None):
        self.data = data  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteZnodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DeleteZnodeResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: DeleteZnodeResponseBodyData
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteZnodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteZnodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteZnodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteZnodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteZnodeResponse, self).to_map()
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
            temp_model = DeleteZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, app_name=None, data_id=None, group=None, ids=None, instance_id=None,
                 namespace_id=None):
        self.accept_language = accept_language  # type: str
        self.app_name = app_name  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.ids = ids  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ExportNacosConfigResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportNacosConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportNacosConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ExportNacosConfigResponseBodyData
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExportNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ExportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExportNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportNacosConfigResponse, self).to_map()
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
            temp_model = ExportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBlackWhiteListRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, is_white=None, resource_type=None, type=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.is_white = is_white  # type: bool
        self.resource_type = resource_type  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBlackWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetBlackWhiteListResponseBodyData(TeaModel):
    def __init__(self, content=None, gateway_id=None, gateway_unique_id=None, gmt_create=None, gmt_modified=None,
                 id=None, is_white=None, resource_id=None, resource_type=None, status=None, type=None):
        self.content = content  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.is_white = is_white  # type: bool
        self.resource_id = resource_id  # type: long
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBlackWhiteListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetBlackWhiteListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetBlackWhiteListResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetBlackWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetBlackWhiteListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBlackWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBlackWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBlackWhiteListResponse, self).to_map()
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
            temp_model = GetBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEngineNamepaceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, id=None, instance_id=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEngineNamepaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetEngineNamepaceResponseBody(TeaModel):
    def __init__(self, config_count=None, error_code=None, http_code=None, message=None, namespace=None,
                 namespace_desc=None, namespace_show_name=None, quota=None, request_id=None, success=None, type=None):
        self.config_count = config_count  # type: str
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEngineNamepaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetEngineNamepaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEngineNamepaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEngineNamepaceResponse, self).to_map()
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
            temp_model = GetEngineNamepaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetGatewayResponseBodyDataLogConfigDetails(TeaModel):
    def __init__(self, log_enabled=None, log_store_name=None, project_name=None):
        self.log_enabled = log_enabled  # type: bool
        self.log_store_name = log_store_name  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayResponseBodyDataLogConfigDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class GetGatewayResponseBodyDataXtraceDetails(TeaModel):
    def __init__(self, sample=None, trace_on=None):
        self.sample = sample  # type: int
        self.trace_on = trace_on  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayResponseBodyDataXtraceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.trace_on is not None:
            result['TraceOn'] = self.trace_on
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('TraceOn') is not None:
            self.trace_on = m.get('TraceOn')
        return self


class GetGatewayResponseBodyData(TeaModel):
    def __init__(self, charge_type=None, end_date=None, gateway_unique_id=None, gmt_create=None, gmt_modified=None,
                 id=None, instance_id=None, log_config_details=None, name=None, primary_user=None, region=None,
                 replica=None, security_group=None, spec=None, status=None, vpc=None, vswitch=None, vswitch_2=None,
                 xtrace_details=None):
        self.charge_type = charge_type  # type: str
        self.end_date = end_date  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str
        self.log_config_details = log_config_details  # type: GetGatewayResponseBodyDataLogConfigDetails
        self.name = name  # type: str
        self.primary_user = primary_user  # type: str
        self.region = region  # type: str
        self.replica = replica  # type: int
        self.security_group = security_group  # type: str
        self.spec = spec  # type: str
        self.status = status  # type: int
        self.vpc = vpc  # type: str
        self.vswitch = vswitch  # type: str
        self.vswitch_2 = vswitch_2  # type: str
        self.xtrace_details = xtrace_details  # type: GetGatewayResponseBodyDataXtraceDetails

    def validate(self):
        if self.log_config_details:
            self.log_config_details.validate()
        if self.xtrace_details:
            self.xtrace_details.validate()

    def to_map(self):
        _map = super(GetGatewayResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2
        if self.xtrace_details is not None:
            result['XtraceDetails'] = self.xtrace_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogConfigDetails') is not None:
            temp_model = GetGatewayResponseBodyDataLogConfigDetails()
            self.log_config_details = temp_model.from_map(m['LogConfigDetails'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')
        if m.get('XtraceDetails') is not None:
            temp_model = GetGatewayResponseBodyDataXtraceDetails()
            self.xtrace_details = temp_model.from_map(m['XtraceDetails'])
        return self


class GetGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetGatewayResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGatewayResponse, self).to_map()
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
            temp_model = GetGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayDomainDetailRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetGatewayDomainDetailResponseBodyData(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, cert_identifier=None, cert_name=None,
                 common_name=None, gateway_id=None, gateway_unique_id=None, gmt_after=None, gmt_before=None, gmt_create=None,
                 gmt_modified=None, id=None, issuer=None, must_https=None, name=None, protocol=None, sans=None):
        self.after_date = after_date  # type: long
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: long
        self.cert_identifier = cert_identifier  # type: int
        self.cert_name = cert_name  # type: str
        self.common_name = common_name  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_after = gmt_after  # type: str
        self.gmt_before = gmt_before  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.issuer = issuer  # type: str
        self.must_https = must_https  # type: bool
        self.name = name  # type: str
        self.protocol = protocol  # type: str
        self.sans = sans  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayDomainDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_after is not None:
            result['GmtAfter'] = self.gmt_after
        if self.gmt_before is not None:
            result['GmtBefore'] = self.gmt_before
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.sans is not None:
            result['Sans'] = self.sans
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtAfter') is not None:
            self.gmt_after = m.get('GmtAfter')
        if m.get('GmtBefore') is not None:
            self.gmt_before = m.get('GmtBefore')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        return self


class GetGatewayDomainDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetGatewayDomainDetailResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGatewayDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetGatewayDomainDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGatewayDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGatewayDomainDetailResponse, self).to_map()
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
            temp_model = GetGatewayDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayOptionRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetGatewayOptionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GatewayOption
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGatewayOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GatewayOption()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayOptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGatewayOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGatewayOptionResponse, self).to_map()
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
            temp_model = GetGatewayOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayRouteDetailRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, route_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.route_id = route_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        return self


class GetGatewayRouteDetailResponseBodyDataCors(TeaModel):
    def __init__(self, allow_credentials=None, allow_headers=None, allow_methods=None, allow_origins=None,
                 expose_headers=None, status=None, time_unit=None, unit_num=None):
        self.allow_credentials = allow_credentials  # type: bool
        self.allow_headers = allow_headers  # type: str
        self.allow_methods = allow_methods  # type: str
        self.allow_origins = allow_origins  # type: str
        self.expose_headers = expose_headers  # type: str
        self.status = status  # type: str
        self.time_unit = time_unit  # type: str
        self.unit_num = unit_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataCors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_credentials is not None:
            result['AllowCredentials'] = self.allow_credentials
        if self.allow_headers is not None:
            result['AllowHeaders'] = self.allow_headers
        if self.allow_methods is not None:
            result['AllowMethods'] = self.allow_methods
        if self.allow_origins is not None:
            result['AllowOrigins'] = self.allow_origins
        if self.expose_headers is not None:
            result['ExposeHeaders'] = self.expose_headers
        if self.status is not None:
            result['Status'] = self.status
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCredentials') is not None:
            self.allow_credentials = m.get('AllowCredentials')
        if m.get('AllowHeaders') is not None:
            self.allow_headers = m.get('AllowHeaders')
        if m.get('AllowMethods') is not None:
            self.allow_methods = m.get('AllowMethods')
        if m.get('AllowOrigins') is not None:
            self.allow_origins = m.get('AllowOrigins')
        if m.get('ExposeHeaders') is not None:
            self.expose_headers = m.get('ExposeHeaders')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class GetGatewayRouteDetailResponseBodyDataDirectResponse(TeaModel):
    def __init__(self, body=None, code=None):
        self.body = body  # type: str
        self.code = code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataDirectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetGatewayRouteDetailResponseBodyDataHTTPRewrite(TeaModel):
    def __init__(self, host=None, path=None, path_type=None, pattern=None, status=None, substitution=None):
        self.host = host  # type: str
        self.path = path  # type: str
        self.path_type = path_type  # type: str
        self.pattern = pattern  # type: str
        self.status = status  # type: str
        self.substitution = substitution  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataHTTPRewrite, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        if self.path_type is not None:
            result['PathType'] = self.path_type
        if self.pattern is not None:
            result['Pattern'] = self.pattern
        if self.status is not None:
            result['Status'] = self.status
        if self.substitution is not None:
            result['Substitution'] = self.substitution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Substitution') is not None:
            self.substitution = m.get('Substitution')
        return self


class GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems(TeaModel):
    def __init__(self, direction_type=None, key=None, op_type=None, value=None):
        self.direction_type = direction_type  # type: str
        self.key = key  # type: str
        self.op_type = op_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction_type is not None:
            result['DirectionType'] = self.direction_type
        if self.key is not None:
            result['Key'] = self.key
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirectionType') is not None:
            self.direction_type = m.get('DirectionType')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetGatewayRouteDetailResponseBodyDataHeaderOp(TeaModel):
    def __init__(self, header_op_items=None, status=None):
        self.header_op_items = header_op_items  # type: list[GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems]
        self.status = status  # type: str

    def validate(self):
        if self.header_op_items:
            for k in self.header_op_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataHeaderOp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HeaderOpItems'] = []
        if self.header_op_items is not None:
            for k in self.header_op_items:
                result['HeaderOpItems'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.header_op_items = []
        if m.get('HeaderOpItems') is not None:
            for k in m.get('HeaderOpItems'):
                temp_model = GetGatewayRouteDetailResponseBodyDataHeaderOpHeaderOpItems()
                self.header_op_items.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetGatewayRouteDetailResponseBodyDataRedirect(TeaModel):
    def __init__(self, code=None, host=None, path=None):
        self.code = code  # type: int
        self.host = host  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRedirect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetGatewayRouteDetailResponseBodyDataRetry(TeaModel):
    def __init__(self, attempts=None, http_codes=None, retry_on=None, status=None):
        self.attempts = attempts  # type: int
        self.http_codes = http_codes  # type: list[str]
        self.retry_on = retry_on  # type: list[str]
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRetry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempts is not None:
            result['Attempts'] = self.attempts
        if self.http_codes is not None:
            result['HttpCodes'] = self.http_codes
        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')
        if m.get('HttpCodes') is not None:
            self.http_codes = m.get('HttpCodes')
        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates(TeaModel):
    def __init__(self, ignore_case=None, path=None, type=None):
        self.ignore_case = ignore_case  # type: bool
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetGatewayRouteDetailResponseBodyDataRoutePredicates(TeaModel):
    def __init__(self, header_predicates=None, method_predicates=None, path_predicates=None, query_predicates=None):
        self.header_predicates = header_predicates  # type: list[GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates]
        self.method_predicates = method_predicates  # type: list[str]
        self.path_predicates = path_predicates  # type: GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates
        self.query_predicates = query_predicates  # type: list[GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates]

    def validate(self):
        if self.header_predicates:
            for k in self.header_predicates:
                if k:
                    k.validate()
        if self.path_predicates:
            self.path_predicates.validate()
        if self.query_predicates:
            for k in self.query_predicates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRoutePredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HeaderPredicates'] = []
        if self.header_predicates is not None:
            for k in self.header_predicates:
                result['HeaderPredicates'].append(k.to_map() if k else None)
        if self.method_predicates is not None:
            result['MethodPredicates'] = self.method_predicates
        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()
        result['QueryPredicates'] = []
        if self.query_predicates is not None:
            for k in self.query_predicates:
                result['QueryPredicates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.header_predicates = []
        if m.get('HeaderPredicates') is not None:
            for k in m.get('HeaderPredicates'):
                temp_model = GetGatewayRouteDetailResponseBodyDataRoutePredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k))
        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')
        if m.get('PathPredicates') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m['PathPredicates'])
        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k in m.get('QueryPredicates'):
                temp_model = GetGatewayRouteDetailResponseBodyDataRoutePredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k))
        return self


class GetGatewayRouteDetailResponseBodyDataRouteServices(TeaModel):
    def __init__(self, group_name=None, name=None, namespace=None, percent=None, service_id=None, service_name=None,
                 source_type=None, version=None):
        self.group_name = group_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.percent = percent  # type: int
        self.service_id = service_id  # type: long
        self.service_name = service_name  # type: str
        self.source_type = source_type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataRouteServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetGatewayRouteDetailResponseBodyDataTimeout(TeaModel):
    def __init__(self, status=None, time_unit=None, unit_num=None):
        self.status = status  # type: str
        self.time_unit = time_unit  # type: str
        self.unit_num = unit_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyDataTimeout, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class GetGatewayRouteDetailResponseBodyData(TeaModel):
    def __init__(self, cors=None, default_service_id=None, default_service_name=None, destination_type=None,
                 direct_response=None, domain_id=None, domain_id_list=None, domain_name=None, domain_name_list=None,
                 gateway_id=None, gateway_unique_id=None, gmt_create=None, gmt_modified=None, httprewrite=None, header_op=None,
                 id=None, name=None, predicates=None, redirect=None, retry=None, route_order=None,
                 route_predicates=None, route_services=None, services=None, status=None, timeout=None):
        self.cors = cors  # type: GetGatewayRouteDetailResponseBodyDataCors
        self.default_service_id = default_service_id  # type: long
        self.default_service_name = default_service_name  # type: str
        self.destination_type = destination_type  # type: str
        self.direct_response = direct_response  # type: GetGatewayRouteDetailResponseBodyDataDirectResponse
        self.domain_id = domain_id  # type: long
        self.domain_id_list = domain_id_list  # type: list[long]
        self.domain_name = domain_name  # type: str
        self.domain_name_list = domain_name_list  # type: list[str]
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.httprewrite = httprewrite  # type: GetGatewayRouteDetailResponseBodyDataHTTPRewrite
        self.header_op = header_op  # type: GetGatewayRouteDetailResponseBodyDataHeaderOp
        self.id = id  # type: long
        self.name = name  # type: str
        self.predicates = predicates  # type: str
        self.redirect = redirect  # type: GetGatewayRouteDetailResponseBodyDataRedirect
        self.retry = retry  # type: GetGatewayRouteDetailResponseBodyDataRetry
        self.route_order = route_order  # type: int
        self.route_predicates = route_predicates  # type: GetGatewayRouteDetailResponseBodyDataRoutePredicates
        self.route_services = route_services  # type: list[GetGatewayRouteDetailResponseBodyDataRouteServices]
        self.services = services  # type: str
        self.status = status  # type: int
        self.timeout = timeout  # type: GetGatewayRouteDetailResponseBodyDataTimeout

    def validate(self):
        if self.cors:
            self.cors.validate()
        if self.direct_response:
            self.direct_response.validate()
        if self.httprewrite:
            self.httprewrite.validate()
        if self.header_op:
            self.header_op.validate()
        if self.redirect:
            self.redirect.validate()
        if self.retry:
            self.retry.validate()
        if self.route_predicates:
            self.route_predicates.validate()
        if self.route_services:
            for k in self.route_services:
                if k:
                    k.validate()
        if self.timeout:
            self.timeout.validate()

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cors is not None:
            result['Cors'] = self.cors.to_map()
        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id
        if self.default_service_name is not None:
            result['DefaultServiceName'] = self.default_service_name
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direct_response is not None:
            result['DirectResponse'] = self.direct_response.to_map()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_id_list is not None:
            result['DomainIdList'] = self.domain_id_list
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_list is not None:
            result['DomainNameList'] = self.domain_name_list
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.httprewrite is not None:
            result['HTTPRewrite'] = self.httprewrite.to_map()
        if self.header_op is not None:
            result['HeaderOp'] = self.header_op.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates is not None:
            result['Predicates'] = self.predicates
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.retry is not None:
            result['Retry'] = self.retry.to_map()
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        if self.route_predicates is not None:
            result['RoutePredicates'] = self.route_predicates.to_map()
        result['RouteServices'] = []
        if self.route_services is not None:
            for k in self.route_services:
                result['RouteServices'].append(k.to_map() if k else None)
        if self.services is not None:
            result['Services'] = self.services
        if self.status is not None:
            result['Status'] = self.status
        if self.timeout is not None:
            result['Timeout'] = self.timeout.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cors') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataCors()
            self.cors = temp_model.from_map(m['Cors'])
        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')
        if m.get('DefaultServiceName') is not None:
            self.default_service_name = m.get('DefaultServiceName')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DirectResponse') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataDirectResponse()
            self.direct_response = temp_model.from_map(m['DirectResponse'])
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainIdList') is not None:
            self.domain_id_list = m.get('DomainIdList')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameList') is not None:
            self.domain_name_list = m.get('DomainNameList')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HTTPRewrite') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataHTTPRewrite()
            self.httprewrite = temp_model.from_map(m['HTTPRewrite'])
        if m.get('HeaderOp') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataHeaderOp()
            self.header_op = temp_model.from_map(m['HeaderOp'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            self.predicates = m.get('Predicates')
        if m.get('Redirect') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('Retry') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataRetry()
            self.retry = temp_model.from_map(m['Retry'])
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        if m.get('RoutePredicates') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataRoutePredicates()
            self.route_predicates = temp_model.from_map(m['RoutePredicates'])
        self.route_services = []
        if m.get('RouteServices') is not None:
            for k in m.get('RouteServices'):
                temp_model = GetGatewayRouteDetailResponseBodyDataRouteServices()
                self.route_services.append(temp_model.from_map(k))
        if m.get('Services') is not None:
            self.services = m.get('Services')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timeout') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyDataTimeout()
            self.timeout = temp_model.from_map(m['Timeout'])
        return self


class GetGatewayRouteDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetGatewayRouteDetailResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetGatewayRouteDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayRouteDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGatewayRouteDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGatewayRouteDetailResponse, self).to_map()
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
            temp_model = GetGatewayRouteDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGatewayServiceDetailRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, service_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayServiceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetGatewayServiceDetailResponseBodyDataLabelDetails(TeaModel):
    def __init__(self, key=None, values=None):
        self.key = key  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBodyDataLabelDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels, self).to_map()
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


class GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion(TeaModel):
    def __init__(self, labels=None, name=None):
        self.labels = labels  # type: list[GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels]
        self.name = name  # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersionLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetGatewayServiceDetailResponseBodyDataVersionDetails(TeaModel):
    def __init__(self, endpoint_num=None, endpoint_num_percent=None, service_version=None):
        self.endpoint_num = endpoint_num  # type: int
        self.endpoint_num_percent = endpoint_num_percent  # type: str
        self.service_version = service_version  # type: GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion

    def validate(self):
        if self.service_version:
            self.service_version.validate()

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBodyDataVersionDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_num is not None:
            result['EndpointNum'] = self.endpoint_num
        if self.endpoint_num_percent is not None:
            result['EndpointNumPercent'] = self.endpoint_num_percent
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointNum') is not None:
            self.endpoint_num = m.get('EndpointNum')
        if m.get('EndpointNumPercent') is not None:
            self.endpoint_num_percent = m.get('EndpointNumPercent')
        if m.get('ServiceVersion') is not None:
            temp_model = GetGatewayServiceDetailResponseBodyDataVersionDetailsServiceVersion()
            self.service_version = temp_model.from_map(m['ServiceVersion'])
        return self


class GetGatewayServiceDetailResponseBodyDataVersions(TeaModel):
    def __init__(self, label=None, type=None, value=None):
        self.label = label  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBodyDataVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetGatewayServiceDetailResponseBodyData(TeaModel):
    def __init__(self, gateway_id=None, gateway_traffic_policy=None, gateway_unique_id=None, gmt_create=None,
                 gmt_modified=None, group_name=None, id=None, ips=None, label_details=None, meta_info=None, name=None,
                 namespace=None, service_name_in_registry=None, source_id=None, source_type=None, version_details=None,
                 versions=None):
        self.gateway_id = gateway_id  # type: long
        self.gateway_traffic_policy = gateway_traffic_policy  # type: TrafficPolicy
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: long
        self.ips = ips  # type: list[str]
        self.label_details = label_details  # type: list[GetGatewayServiceDetailResponseBodyDataLabelDetails]
        self.meta_info = meta_info  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.service_name_in_registry = service_name_in_registry  # type: str
        self.source_id = source_id  # type: long
        self.source_type = source_type  # type: str
        self.version_details = version_details  # type: list[GetGatewayServiceDetailResponseBodyDataVersionDetails]
        self.versions = versions  # type: list[GetGatewayServiceDetailResponseBodyDataVersions]

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()
        if self.label_details:
            for k in self.label_details:
                if k:
                    k.validate()
        if self.version_details:
            for k in self.version_details:
                if k:
                    k.validate()
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.ips is not None:
            result['Ips'] = self.ips
        result['LabelDetails'] = []
        if self.label_details is not None:
            for k in self.label_details:
                result['LabelDetails'].append(k.to_map() if k else None)
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name_in_registry is not None:
            result['ServiceNameInRegistry'] = self.service_name_in_registry
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['VersionDetails'] = []
        if self.version_details is not None:
            for k in self.version_details:
                result['VersionDetails'].append(k.to_map() if k else None)
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = TrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m['GatewayTrafficPolicy'])
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        self.label_details = []
        if m.get('LabelDetails') is not None:
            for k in m.get('LabelDetails'):
                temp_model = GetGatewayServiceDetailResponseBodyDataLabelDetails()
                self.label_details.append(temp_model.from_map(k))
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('ServiceNameInRegistry')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.version_details = []
        if m.get('VersionDetails') is not None:
            for k in m.get('VersionDetails'):
                temp_model = GetGatewayServiceDetailResponseBodyDataVersionDetails()
                self.version_details.append(temp_model.from_map(k))
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = GetGatewayServiceDetailResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class GetGatewayServiceDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetGatewayServiceDetailResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetGatewayServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGatewayServiceDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGatewayServiceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGatewayServiceDetailResponse, self).to_map()
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
            temp_model = GetGatewayServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, region_id=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetGovernanceKubernetesClusterResponseBodyDataNamespaces(TeaModel):
    def __init__(self, name=None, tags=None):
        self.name = name  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterResponseBodyDataNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetGovernanceKubernetesClusterResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, k_8s_version=None, namespace_infos=None, namespaces=None,
                 pilot_start_time=None, region=None, update_time=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.k_8s_version = k_8s_version  # type: str
        self.namespace_infos = namespace_infos  # type: str
        self.namespaces = namespaces  # type: list[GetGovernanceKubernetesClusterResponseBodyDataNamespaces]
        self.pilot_start_time = pilot_start_time  # type: str
        self.region = region  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.region is not None:
            result['Region'] = self.region
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = GetGovernanceKubernetesClusterResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetGovernanceKubernetesClusterResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGovernanceKubernetesClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterResponse, self).to_map()
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
            temp_model = GetGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGovernanceKubernetesClusterListRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, cluster_name=None, page_number=None, page_size=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetGovernanceKubernetesClusterListResponseBodyDataResult(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, k_8s_version=None, namespace_infos=None,
                 pilot_start_time=None, region=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.k_8s_version = k_8s_version  # type: str
        self.namespace_infos = namespace_infos  # type: str
        self.pilot_start_time = pilot_start_time  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterListResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetGovernanceKubernetesClusterListResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, result=None, total_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: list[GetGovernanceKubernetesClusterListResponseBodyDataResult]
        self.total_size = total_size  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetGovernanceKubernetesClusterListResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class GetGovernanceKubernetesClusterListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetGovernanceKubernetesClusterListResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetGovernanceKubernetesClusterListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGovernanceKubernetesClusterListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGovernanceKubernetesClusterListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGovernanceKubernetesClusterListResponse, self).to_map()
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
            temp_model = GetGovernanceKubernetesClusterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(self, accept_language=None, version_code=None):
        self.accept_language = accept_language  # type: str
        # 集群版本
        self.version_code = version_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class GetImageResponseBodyData(TeaModel):
    def __init__(self, current_version_full_show_name=None, max_version_changelog_url=None, max_version_code=None,
                 max_version_full_show_name=None):
        # 当前集群镜像版本的4位全名
        self.current_version_full_show_name = current_version_full_show_name  # type: str
        # 可升级的最大版本变更日志url
        self.max_version_changelog_url = max_version_changelog_url  # type: str
        # 可升级的增量版本Code
        self.max_version_code = max_version_code  # type: str
        # 可升级的增量版本全名
        self.max_version_full_show_name = max_version_full_show_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version_full_show_name is not None:
            result['CurrentVersionFullShowName'] = self.current_version_full_show_name
        if self.max_version_changelog_url is not None:
            result['MaxVersionChangelogUrl'] = self.max_version_changelog_url
        if self.max_version_code is not None:
            result['MaxVersionCode'] = self.max_version_code
        if self.max_version_full_show_name is not None:
            result['MaxVersionFullShowName'] = self.max_version_full_show_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentVersionFullShowName') is not None:
            self.current_version_full_show_name = m.get('CurrentVersionFullShowName')
        if m.get('MaxVersionChangelogUrl') is not None:
            self.max_version_changelog_url = m.get('MaxVersionChangelogUrl')
        if m.get('MaxVersionCode') is not None:
            self.max_version_code = m.get('MaxVersionCode')
        if m.get('MaxVersionFullShowName') is not None:
            self.max_version_full_show_name = m.get('MaxVersionFullShowName')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: GetImageResponseBodyData
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageResponse, self).to_map()
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImportFileUrlRequest(TeaModel):
    def __init__(self, accept_language=None, content_type=None, instance_id=None, namespace_id=None):
        self.accept_language = accept_language  # type: str
        self.content_type = content_type  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImportFileUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetImportFileUrlResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImportFileUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetImportFileUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GetImportFileUrlResponseBodyData
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetImportFileUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetImportFileUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetImportFileUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetImportFileUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImportFileUrlResponse, self).to_map()
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
            temp_model = GetImportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKubernetesSourceRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKubernetesSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetKubernetesSourceResponseBodyData(TeaModel):
    def __init__(self, cluster=None, name=None):
        self.cluster = cluster  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKubernetesSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetKubernetesSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[GetKubernetesSourceResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetKubernetesSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetKubernetesSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetKubernetesSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetKubernetesSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetKubernetesSourceResponse, self).to_map()
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
            temp_model = GetKubernetesSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMseFeatureSwitchRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMseFeatureSwitchRequest, self).to_map()
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


class GetMseFeatureSwitchResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: dict[str, any]
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMseFeatureSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMseFeatureSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMseFeatureSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMseFeatureSwitchResponse, self).to_map()
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
            temp_model = GetMseFeatureSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMseSourceRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMseSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class GetMseSourceResponseBodyData(TeaModel):
    def __init__(self, address=None, cluster_id=None, instance_id=None, name=None, type=None):
        self.address = address  # type: str
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMseSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMseSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[GetMseSourceResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMseSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetMseSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMseSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMseSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMseSourceResponse, self).to_map()
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
            temp_model = GetMseSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, beta=None, data_id=None, group=None, instance_id=None,
                 namespace_id=None):
        self.accept_language = accept_language  # type: str
        self.beta = beta  # type: bool
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.beta is not None:
            result['Beta'] = self.beta
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Beta') is not None:
            self.beta = m.get('Beta')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetNacosConfigResponseBodyConfiguration(TeaModel):
    def __init__(self, app_name=None, beta_ips=None, content=None, data_id=None, desc=None, encrypted_data_key=None,
                 group=None, md_5=None, tags=None, type=None):
        self.app_name = app_name  # type: str
        self.beta_ips = beta_ips  # type: str
        self.content = content  # type: str
        self.data_id = data_id  # type: str
        self.desc = desc  # type: str
        self.encrypted_data_key = encrypted_data_key  # type: str
        self.group = group  # type: str
        self.md_5 = md_5  # type: str
        self.tags = tags  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosConfigResponseBodyConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.group is not None:
            result['Group'] = self.group
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNacosConfigResponseBody(TeaModel):
    def __init__(self, configuration=None, error_code=None, message=None, request_id=None, success=None):
        self.configuration = configuration  # type: GetNacosConfigResponseBodyConfiguration
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super(GetNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configuration') is not None:
            temp_model = GetNacosConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNacosConfigResponse, self).to_map()
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
            temp_model = GetNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNacosHistoryConfigRequest(TeaModel):
    def __init__(self, accept_language=None, data_id=None, group=None, instance_id=None, namespace_id=None, nid=None):
        self.accept_language = accept_language  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.nid = nid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosHistoryConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nid is not None:
            result['Nid'] = self.nid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Nid') is not None:
            self.nid = m.get('Nid')
        return self


class GetNacosHistoryConfigResponseBodyConfiguration(TeaModel):
    def __init__(self, app_name=None, content=None, data_id=None, encrypted_data_key=None, group=None, md_5=None,
                 op_type=None):
        self.app_name = app_name  # type: str
        self.content = content  # type: str
        self.data_id = data_id  # type: str
        self.encrypted_data_key = encrypted_data_key  # type: str
        self.group = group  # type: str
        self.md_5 = md_5  # type: str
        self.op_type = op_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNacosHistoryConfigResponseBodyConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.group is not None:
            result['Group'] = self.group
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class GetNacosHistoryConfigResponseBody(TeaModel):
    def __init__(self, configuration=None, error_code=None, message=None, request_id=None, success=None):
        self.configuration = configuration  # type: GetNacosHistoryConfigResponseBodyConfiguration
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        _map = super(GetNacosHistoryConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configuration') is not None:
            temp_model = GetNacosHistoryConfigResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNacosHistoryConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNacosHistoryConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNacosHistoryConfigResponse, self).to_map()
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
            temp_model = GetNacosHistoryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOverviewRequest(TeaModel):
    def __init__(self, accept_language=None, period=None, region=None):
        self.accept_language = accept_language  # type: str
        self.period = period  # type: int
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetOverviewResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOverviewResponse, self).to_map()
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
            temp_model = GetOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagsBySwimmingLaneGroupIdRequest(TeaModel):
    def __init__(self, accept_language=None, group_id=None):
        self.accept_language = accept_language  # type: str
        self.group_id = group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagsBySwimmingLaneGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class GetTagsBySwimmingLaneGroupIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagsBySwimmingLaneGroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTagsBySwimmingLaneGroupIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTagsBySwimmingLaneGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTagsBySwimmingLaneGroupIdResponse, self).to_map()
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
            temp_model = GetTagsBySwimmingLaneGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, file_url=None, instance_id=None, namespace_id=None, policy=None):
        self.accept_language = accept_language  # type: str
        self.file_url = file_url  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.policy = policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class ImportNacosConfigResponseBodyDataFailData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNacosConfigResponseBodyDataFailData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyDataSkipData(TeaModel):
    def __init__(self, data_id=None, group=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNacosConfigResponseBodyDataSkipData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class ImportNacosConfigResponseBodyData(TeaModel):
    def __init__(self, fail_data=None, skip_count=None, skip_data=None, succ_count=None):
        self.fail_data = fail_data  # type: list[ImportNacosConfigResponseBodyDataFailData]
        self.skip_count = skip_count  # type: int
        self.skip_data = skip_data  # type: list[ImportNacosConfigResponseBodyDataSkipData]
        self.succ_count = succ_count  # type: int

    def validate(self):
        if self.fail_data:
            for k in self.fail_data:
                if k:
                    k.validate()
        if self.skip_data:
            for k in self.skip_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportNacosConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailData'] = []
        if self.fail_data is not None:
            for k in self.fail_data:
                result['FailData'].append(k.to_map() if k else None)
        if self.skip_count is not None:
            result['SkipCount'] = self.skip_count
        result['SkipData'] = []
        if self.skip_data is not None:
            for k in self.skip_data:
                result['SkipData'].append(k.to_map() if k else None)
        if self.succ_count is not None:
            result['SuccCount'] = self.succ_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fail_data = []
        if m.get('FailData') is not None:
            for k in m.get('FailData'):
                temp_model = ImportNacosConfigResponseBodyDataFailData()
                self.fail_data.append(temp_model.from_map(k))
        if m.get('SkipCount') is not None:
            self.skip_count = m.get('SkipCount')
        self.skip_data = []
        if m.get('SkipData') is not None:
            for k in m.get('SkipData'):
                temp_model = ImportNacosConfigResponseBodyDataSkipData()
                self.skip_data.append(temp_model.from_map(k))
        if m.get('SuccCount') is not None:
            self.succ_count = m.get('SuccCount')
        return self


class ImportNacosConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ImportNacosConfigResponseBodyData
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImportNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ImportNacosConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportNacosConfigResponse, self).to_map()
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
            temp_model = ImportNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportServicesRequestServiceList(TeaModel):
    def __init__(self, group_name=None, ips=None, name=None, namespace=None, service_port=None,
                 service_protocol=None):
        self.group_name = group_name  # type: str
        self.ips = ips  # type: list[str]
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        # 服务的端口
        self.service_port = service_port  # type: long
        # 服务的协议版本
        self.service_protocol = service_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServicesRequestServiceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_port is not None:
            result['ServicePort'] = self.service_port
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        return self


class ImportServicesRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, service_list=None, source_id=None,
                 source_type=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.service_list = service_list  # type: list[ImportServicesRequestServiceList]
        self.source_id = source_id  # type: str
        # 服务来源
        self.source_type = source_type  # type: str

    def validate(self):
        if self.service_list:
            for k in self.service_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        result['ServiceList'] = []
        if self.service_list is not None:
            for k in self.service_list:
                result['ServiceList'].append(k.to_map() if k else None)
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        self.service_list = []
        if m.get('ServiceList') is not None:
            for k in m.get('ServiceList'):
                temp_model = ImportServicesRequestServiceList()
                self.service_list.append(temp_model.from_map(k))
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ImportServicesShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, service_list_shrink=None, source_id=None,
                 source_type=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.service_list_shrink = service_list_shrink  # type: str
        self.source_id = source_id  # type: str
        # 服务来源
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServicesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_list_shrink is not None:
            result['ServiceList'] = self.service_list_shrink
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceList') is not None:
            self.service_list_shrink = m.get('ServiceList')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ImportServicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportServicesResponse, self).to_map()
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
            temp_model = ImportServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmContactGroupsRequest(TeaModel):
    def __init__(self, accept_language=None, page_num=None, page_size=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmContactGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmContactGroupsResponseBodyData(TeaModel):
    def __init__(self, contact_group_id=None, contact_group_name=None):
        self.contact_group_id = contact_group_id  # type: str
        self.contact_group_name = contact_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmContactGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        return self


class ListAlarmContactGroupsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListAlarmContactGroupsResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmContactGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmContactGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmContactGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmContactGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmContactGroupsResponse, self).to_map()
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
            temp_model = ListAlarmContactGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(self, accept_language=None, alarm_mse_type=None, alarm_name=None, end_time=None, page_num=None,
                 page_size=None, request_pars=None, start_time=None):
        self.accept_language = accept_language  # type: str
        self.alarm_mse_type = alarm_mse_type  # type: str
        self.alarm_name = alarm_name  # type: str
        self.end_time = end_time  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAlarmHistoriesResponseBodyData(TeaModel):
    def __init__(self, alarm_content=None, alarm_ding_ding=None, alarm_email=None, alarm_name=None,
                 alarm_phone=None, alarm_time=None):
        self.alarm_content = alarm_content  # type: str
        self.alarm_ding_ding = alarm_ding_ding  # type: str
        self.alarm_email = alarm_email  # type: str
        self.alarm_name = alarm_name  # type: str
        self.alarm_phone = alarm_phone  # type: str
        self.alarm_time = alarm_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmHistoriesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.alarm_ding_ding is not None:
            result['AlarmDingDing'] = self.alarm_ding_ding
        if self.alarm_email is not None:
            result['AlarmEmail'] = self.alarm_email
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_phone is not None:
            result['AlarmPhone'] = self.alarm_phone
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('AlarmDingDing') is not None:
            self.alarm_ding_ding = m.get('AlarmDingDing')
        if m.get('AlarmEmail') is not None:
            self.alarm_email = m.get('AlarmEmail')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmPhone') is not None:
            self.alarm_phone = m.get('AlarmPhone')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListAlarmHistoriesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmHistoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmHistoriesResponse, self).to_map()
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
            temp_model = ListAlarmHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmItemsRequest(TeaModel):
    def __init__(self, accept_language=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmItemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmItemsResponseBodyData(TeaModel):
    def __init__(self, alarm_code=None, alarm_desc=None, cluster_type=None):
        self.alarm_code = alarm_code  # type: str
        self.alarm_desc = alarm_desc  # type: str
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmItemsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_code is not None:
            result['AlarmCode'] = self.alarm_code
        if self.alarm_desc is not None:
            result['AlarmDesc'] = self.alarm_desc
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmCode') is not None:
            self.alarm_code = m.get('AlarmCode')
        if m.get('AlarmDesc') is not None:
            self.alarm_desc = m.get('AlarmDesc')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListAlarmItemsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListAlarmItemsResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmItemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmItemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmItemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmItemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmItemsResponse, self).to_map()
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
            temp_model = ListAlarmItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmRulesRequest(TeaModel):
    def __init__(self, accept_language=None, alarm_mse_type=None, page_num=None, page_size=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.alarm_mse_type = alarm_mse_type  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.alarm_mse_type is not None:
            result['AlarmMseType'] = self.alarm_mse_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AlarmMseType') is not None:
            self.alarm_mse_type = m.get('AlarmMseType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListAlarmRulesResponseBodyData(TeaModel):
    def __init__(self, alarm_name=None, alarm_rule_detail=None, alarm_rule_id=None, alarm_status=None,
                 create_time=None):
        self.alarm_name = alarm_name  # type: str
        self.alarm_rule_detail = alarm_rule_detail  # type: str
        self.alarm_rule_id = alarm_rule_id  # type: str
        self.alarm_status = alarm_status  # type: str
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlarmRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_rule_detail is not None:
            result['AlarmRuleDetail'] = self.alarm_rule_detail
        if self.alarm_rule_id is not None:
            result['AlarmRuleId'] = self.alarm_rule_id
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmRuleDetail') is not None:
            self.alarm_rule_detail = m.get('AlarmRuleDetail')
        if m.get('AlarmRuleId') is not None:
            self.alarm_rule_id = m.get('AlarmRuleId')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListAlarmRulesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListAlarmRulesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlarmRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAlarmRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlarmRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlarmRulesResponse, self).to_map()
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
            temp_model = ListAlarmRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsInstancesRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, cluster_name=None, group_name=None, instance_id=None,
                 namespace_id=None, page_num=None, page_size=None, request_pars=None, service_name=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListAnsInstancesResponseBodyData(TeaModel):
    def __init__(self, app=None, cluster_name=None, datum_key=None, default_key=None, enabled=None, ephemeral=None,
                 fail_count=None, healthy=None, instance_heart_beat_interval=None, instance_heart_beat_time_out=None,
                 instance_id=None, ip=None, ip_delete_timeout=None, last_beat=None, marked=None, metadata=None, ok_count=None,
                 port=None, service_name=None, weight=None):
        self.app = app  # type: str
        self.cluster_name = cluster_name  # type: str
        self.datum_key = datum_key  # type: str
        self.default_key = default_key  # type: str
        self.enabled = enabled  # type: bool
        self.ephemeral = ephemeral  # type: bool
        self.fail_count = fail_count  # type: int
        self.healthy = healthy  # type: bool
        self.instance_heart_beat_interval = instance_heart_beat_interval  # type: int
        self.instance_heart_beat_time_out = instance_heart_beat_time_out  # type: int
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: str
        self.ip_delete_timeout = ip_delete_timeout  # type: int
        self.last_beat = last_beat  # type: long
        self.marked = marked  # type: bool
        self.metadata = metadata  # type: dict[str, any]
        self.ok_count = ok_count  # type: int
        self.port = port  # type: int
        self.service_name = service_name  # type: str
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.datum_key is not None:
            result['DatumKey'] = self.datum_key
        if self.default_key is not None:
            result['DefaultKey'] = self.default_key
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.healthy is not None:
            result['Healthy'] = self.healthy
        if self.instance_heart_beat_interval is not None:
            result['InstanceHeartBeatInterval'] = self.instance_heart_beat_interval
        if self.instance_heart_beat_time_out is not None:
            result['InstanceHeartBeatTimeOut'] = self.instance_heart_beat_time_out
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_delete_timeout is not None:
            result['IpDeleteTimeout'] = self.ip_delete_timeout
        if self.last_beat is not None:
            result['LastBeat'] = self.last_beat
        if self.marked is not None:
            result['Marked'] = self.marked
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.ok_count is not None:
            result['OkCount'] = self.ok_count
        if self.port is not None:
            result['Port'] = self.port
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DatumKey') is not None:
            self.datum_key = m.get('DatumKey')
        if m.get('DefaultKey') is not None:
            self.default_key = m.get('DefaultKey')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('Healthy') is not None:
            self.healthy = m.get('Healthy')
        if m.get('InstanceHeartBeatInterval') is not None:
            self.instance_heart_beat_interval = m.get('InstanceHeartBeatInterval')
        if m.get('InstanceHeartBeatTimeOut') is not None:
            self.instance_heart_beat_time_out = m.get('InstanceHeartBeatTimeOut')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpDeleteTimeout') is not None:
            self.ip_delete_timeout = m.get('IpDeleteTimeout')
        if m.get('LastBeat') is not None:
            self.last_beat = m.get('LastBeat')
        if m.get('Marked') is not None:
            self.marked = m.get('Marked')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListAnsInstancesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListAnsInstancesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnsInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnsInstancesResponse, self).to_map()
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
            temp_model = ListAnsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServiceClustersRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, cluster_name=None, group_name=None, instance_id=None,
                 namespace_id=None, page_num=None, page_size=None, request_pars=None, service_name=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServiceClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListAnsServiceClustersResponseBodyDataClusters(TeaModel):
    def __init__(self, default_check_port=None, default_port=None, health_checker_type=None, metadata=None,
                 name=None, service_name=None, use_ipport_4check=None):
        self.default_check_port = default_check_port  # type: int
        self.default_port = default_port  # type: int
        self.health_checker_type = health_checker_type  # type: str
        self.metadata = metadata  # type: dict[str, any]
        self.name = name  # type: str
        self.service_name = service_name  # type: str
        self.use_ipport_4check = use_ipport_4check  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServiceClustersResponseBodyDataClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_check_port is not None:
            result['DefaultCheckPort'] = self.default_check_port
        if self.default_port is not None:
            result['DefaultPort'] = self.default_port
        if self.health_checker_type is not None:
            result['HealthCheckerType'] = self.health_checker_type
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.name is not None:
            result['Name'] = self.name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.use_ipport_4check is not None:
            result['UseIPPort4Check'] = self.use_ipport_4check
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultCheckPort') is not None:
            self.default_check_port = m.get('DefaultCheckPort')
        if m.get('DefaultPort') is not None:
            self.default_port = m.get('DefaultPort')
        if m.get('HealthCheckerType') is not None:
            self.health_checker_type = m.get('HealthCheckerType')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('UseIPPort4Check') is not None:
            self.use_ipport_4check = m.get('UseIPPort4Check')
        return self


class ListAnsServiceClustersResponseBodyData(TeaModel):
    def __init__(self, clusters=None, ephemeral=None, group_name=None, metadata=None, name=None,
                 protect_threshold=None, selector_type=None):
        self.clusters = clusters  # type: list[ListAnsServiceClustersResponseBodyDataClusters]
        self.ephemeral = ephemeral  # type: bool
        self.group_name = group_name  # type: str
        self.metadata = metadata  # type: dict[str, any]
        self.name = name  # type: str
        self.protect_threshold = protect_threshold  # type: float
        self.selector_type = selector_type  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnsServiceClustersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.name is not None:
            result['Name'] = self.name
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.selector_type is not None:
            result['SelectorType'] = self.selector_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListAnsServiceClustersResponseBodyDataClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('SelectorType') is not None:
            self.selector_type = m.get('SelectorType')
        return self


class ListAnsServiceClustersResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: ListAnsServiceClustersResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAnsServiceClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAnsServiceClustersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnsServiceClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnsServiceClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnsServiceClustersResponse, self).to_map()
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
            temp_model = ListAnsServiceClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnsServicesRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, group_name=None, has_ip_count=None, instance_id=None,
                 namespace_id=None, page_num=None, page_size=None, request_pars=None, service_name=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.has_ip_count = has_ip_count  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_ip_count is not None:
            result['HasIpCount'] = self.has_ip_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasIpCount') is not None:
            self.has_ip_count = m.get('HasIpCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListAnsServicesResponseBodyData(TeaModel):
    def __init__(self, cluster_count=None, group_name=None, healthy_instance_count=None, ip_count=None, name=None):
        self.cluster_count = cluster_count  # type: int
        self.group_name = group_name  # type: str
        self.healthy_instance_count = healthy_instance_count  # type: int
        self.ip_count = ip_count  # type: int
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAnsServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.healthy_instance_count is not None:
            result['HealthyInstanceCount'] = self.healthy_instance_count
        if self.ip_count is not None:
            result['IpCount'] = self.ip_count
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HealthyInstanceCount') is not None:
            self.healthy_instance_count = m.get('HealthyInstanceCount')
        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAnsServicesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListAnsServicesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAnsServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAnsServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnsServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAnsServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAnsServicesResponse, self).to_map()
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
            temp_model = ListAnsServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppBySwimmingLaneGroupTagRequest(TeaModel):
    def __init__(self, accept_language=None, group_id=None, tag=None):
        self.accept_language = accept_language  # type: str
        self.group_id = group_id  # type: long
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppBySwimmingLaneGroupTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListAppBySwimmingLaneGroupTagResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppBySwimmingLaneGroupTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppBySwimmingLaneGroupTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppBySwimmingLaneGroupTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppBySwimmingLaneGroupTagResponse, self).to_map()
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
            temp_model = ListAppBySwimmingLaneGroupTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterConnectionTypesRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterConnectionTypesRequest, self).to_map()
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


class ListClusterConnectionTypesResponseBodyData(TeaModel):
    def __init__(self, show_name=None):
        self.show_name = show_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterConnectionTypesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterConnectionTypesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListClusterConnectionTypesResponseBodyData]
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterConnectionTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterConnectionTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterConnectionTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterConnectionTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterConnectionTypesResponse, self).to_map()
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
            temp_model = ListClusterConnectionTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTypesRequest(TeaModel):
    def __init__(self, accept_language=None, connect_type=None, region_id=None):
        self.accept_language = accept_language  # type: str
        # 网络连接类型
        self.connect_type = connect_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClusterTypesResponseBodyData(TeaModel):
    def __init__(self, show_name=None):
        self.show_name = show_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterTypesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListClusterTypesResponseBodyData]
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterTypesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterTypesResponse, self).to_map()
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
            temp_model = ListClusterTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterVersionsRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_type=None):
        self.accept_language = accept_language  # type: str
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterVersionsResponseBodyData(TeaModel):
    def __init__(self, cluster_type=None, code=None, show_name=None):
        self.cluster_type = cluster_type  # type: str
        self.code = code  # type: str
        self.show_name = show_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.code is not None:
            result['Code'] = self.code
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListClusterVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListClusterVersionsResponseBodyData]
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClusterVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListClusterVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterVersionsResponse, self).to_map()
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
            temp_model = ListClusterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_alias_name=None, page_num=None, page_size=None, region_id=None,
                 request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(self, app_version=None, can_update=None, charge_type=None, cluster_alias_name=None,
                 cluster_name=None, cluster_type=None, create_time=None, end_date=None, init_status=None, instance_count=None,
                 instance_id=None, internet_address=None, internet_domain=None, intranet_address=None, intranet_domain=None,
                 version_code=None):
        self.app_version = app_version  # type: str
        self.can_update = can_update  # type: bool
        self.charge_type = charge_type  # type: str
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.create_time = create_time  # type: str
        self.end_date = end_date  # type: str
        self.init_status = init_status  # type: str
        self.instance_count = instance_count  # type: long
        self.instance_id = instance_id  # type: str
        self.internet_address = internet_address  # type: str
        self.internet_domain = internet_domain  # type: str
        self.intranet_address = intranet_address  # type: str
        self.intranet_domain = intranet_domain  # type: str
        self.version_code = version_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.can_update is not None:
            result['CanUpdate'] = self.can_update
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListClustersResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClustersResponse, self).to_map()
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
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEngineNamespacesRequest(TeaModel):
    def __init__(self, accept_language=None, instance_id=None):
        self.accept_language = accept_language  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEngineNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListEngineNamespacesResponseBodyData(TeaModel):
    def __init__(self, config_count=None, namespace=None, namespace_desc=None, namespace_show_name=None, quota=None,
                 service_count=None, type=None):
        self.config_count = config_count  # type: int
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: int
        self.service_count = service_count  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEngineNamespacesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEngineNamespacesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListEngineNamespacesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEngineNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEngineNamespacesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEngineNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEngineNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEngineNamespacesResponse, self).to_map()
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
            temp_model = ListEngineNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaInstancesRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, page_num=None, page_size=None, request_pars=None,
                 service_name=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_pars = request_pars  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListEurekaInstancesResponseBodyData(TeaModel):
    def __init__(self, app=None, duration_in_secs=None, home_page_url=None, host_name=None, instance_id=None,
                 ip_addr=None, last_dirty_timestamp=None, last_updated_timestamp=None, metadata=None, port=None,
                 renewal_interval_in_secs=None, secure_port=None, status=None, vip_address=None):
        self.app = app  # type: str
        self.duration_in_secs = duration_in_secs  # type: int
        self.home_page_url = home_page_url  # type: str
        self.host_name = host_name  # type: str
        self.instance_id = instance_id  # type: str
        self.ip_addr = ip_addr  # type: str
        self.last_dirty_timestamp = last_dirty_timestamp  # type: long
        self.last_updated_timestamp = last_updated_timestamp  # type: long
        self.metadata = metadata  # type: dict[str, any]
        self.port = port  # type: int
        self.renewal_interval_in_secs = renewal_interval_in_secs  # type: int
        self.secure_port = secure_port  # type: int
        self.status = status  # type: str
        self.vip_address = vip_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.duration_in_secs is not None:
            result['DurationInSecs'] = self.duration_in_secs
        if self.home_page_url is not None:
            result['HomePageUrl'] = self.home_page_url
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr
        if self.last_dirty_timestamp is not None:
            result['LastDirtyTimestamp'] = self.last_dirty_timestamp
        if self.last_updated_timestamp is not None:
            result['LastUpdatedTimestamp'] = self.last_updated_timestamp
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.port is not None:
            result['Port'] = self.port
        if self.renewal_interval_in_secs is not None:
            result['RenewalIntervalInSecs'] = self.renewal_interval_in_secs
        if self.secure_port is not None:
            result['SecurePort'] = self.secure_port
        if self.status is not None:
            result['Status'] = self.status
        if self.vip_address is not None:
            result['VipAddress'] = self.vip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('DurationInSecs') is not None:
            self.duration_in_secs = m.get('DurationInSecs')
        if m.get('HomePageUrl') is not None:
            self.home_page_url = m.get('HomePageUrl')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')
        if m.get('LastDirtyTimestamp') is not None:
            self.last_dirty_timestamp = m.get('LastDirtyTimestamp')
        if m.get('LastUpdatedTimestamp') is not None:
            self.last_updated_timestamp = m.get('LastUpdatedTimestamp')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RenewalIntervalInSecs') is not None:
            self.renewal_interval_in_secs = m.get('RenewalIntervalInSecs')
        if m.get('SecurePort') is not None:
            self.secure_port = m.get('SecurePort')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VipAddress') is not None:
            self.vip_address = m.get('VipAddress')
        return self


class ListEurekaInstancesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListEurekaInstancesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEurekaInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEurekaInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEurekaInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEurekaInstancesResponse, self).to_map()
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
            temp_model = ListEurekaInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEurekaServicesRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, page_num=None, page_size=None, region_id=None,
                 request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListEurekaServicesResponseBodyData(TeaModel):
    def __init__(self, instances_id=None, name=None, up_status=None):
        self.instances_id = instances_id  # type: list[str]
        self.name = name  # type: str
        self.up_status = up_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEurekaServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances_id is not None:
            result['InstancesId'] = self.instances_id
        if self.name is not None:
            result['Name'] = self.name
        if self.up_status is not None:
            result['UpStatus'] = self.up_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstancesId') is not None:
            self.instances_id = m.get('InstancesId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpStatus') is not None:
            self.up_status = m.get('UpStatus')
        return self


class ListEurekaServicesResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, http_code=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None, total_count=None):
        self.data = data  # type: list[ListEurekaServicesResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEurekaServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEurekaServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEurekaServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEurekaServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEurekaServicesResponse, self).to_map()
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
            temp_model = ListEurekaServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayRequestFilterParams(TeaModel):
    def __init__(self, gateway_type=None, gateway_unique_id=None, instance_id=None, name=None, vpc=None):
        self.gateway_type = gateway_type  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.vpc = vpc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRequestFilterParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.vpc is not None:
            result['Vpc'] = self.vpc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')
        return self


class ListGatewayRequest(TeaModel):
    def __init__(self, accept_language=None, desc_sort=None, filter_params=None, order_item=None, page_number=None,
                 page_size=None):
        self.accept_language = accept_language  # type: str
        self.desc_sort = desc_sort  # type: bool
        self.filter_params = filter_params  # type: ListGatewayRequestFilterParams
        self.order_item = order_item  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        _map = super(ListGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params is not None:
            result['FilterParams'] = self.filter_params.to_map()
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            temp_model = ListGatewayRequestFilterParams()
            self.filter_params = temp_model.from_map(m['FilterParams'])
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, desc_sort=None, filter_params_shrink=None, order_item=None,
                 page_number=None, page_size=None):
        self.accept_language = accept_language  # type: str
        self.desc_sort = desc_sort  # type: bool
        self.filter_params_shrink = filter_params_shrink  # type: str
        self.order_item = order_item  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            self.filter_params_shrink = m.get('FilterParams')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayResponseBodyDataResultInternetSlb(TeaModel):
    def __init__(self, gateway_slb_mode=None, gateway_slb_status=None, internet_network_flow=None, slb_id=None,
                 slb_ip=None, slb_port=None, slb_spec=None, status_desc=None, type=None):
        self.gateway_slb_mode = gateway_slb_mode  # type: str
        self.gateway_slb_status = gateway_slb_status  # type: str
        self.internet_network_flow = internet_network_flow  # type: str
        self.slb_id = slb_id  # type: str
        self.slb_ip = slb_ip  # type: str
        self.slb_port = slb_port  # type: str
        self.slb_spec = slb_spec  # type: str
        self.status_desc = status_desc  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayResponseBodyDataResultInternetSlb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.internet_network_flow is not None:
            result['InternetNetworkFlow'] = self.internet_network_flow
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('InternetNetworkFlow') is not None:
            self.internet_network_flow = m.get('InternetNetworkFlow')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewayResponseBodyDataResultSlb(TeaModel):
    def __init__(self, gateway_slb_mode=None, gateway_slb_status=None, slb_id=None, slb_ip=None, slb_port=None,
                 slb_spec=None, status_desc=None, type=None):
        self.gateway_slb_mode = gateway_slb_mode  # type: str
        self.gateway_slb_status = gateway_slb_status  # type: str
        self.slb_id = slb_id  # type: str
        self.slb_ip = slb_ip  # type: str
        self.slb_port = slb_port  # type: str
        self.slb_spec = slb_spec  # type: str
        self.status_desc = status_desc  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayResponseBodyDataResultSlb, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewayResponseBodyDataResult(TeaModel):
    def __init__(self, ahas_on=None, arms_on=None, charge_type=None, current_version=None, end_date=None,
                 gateway_type=None, gateway_unique_id=None, gmt_create=None, gmt_modified=None, id=None, instance_id=None,
                 internet_slb=None, latest_version=None, must_upgrade=None, name=None, primary_user=None, region=None,
                 replica=None, slb=None, spec=None, status=None, status_desc=None, tag=None, upgrade=None, vswitch_2=None):
        self.ahas_on = ahas_on  # type: bool
        self.arms_on = arms_on  # type: bool
        self.charge_type = charge_type  # type: str
        self.current_version = current_version  # type: str
        self.end_date = end_date  # type: str
        self.gateway_type = gateway_type  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.instance_id = instance_id  # type: str
        self.internet_slb = internet_slb  # type: list[ListGatewayResponseBodyDataResultInternetSlb]
        self.latest_version = latest_version  # type: str
        self.must_upgrade = must_upgrade  # type: bool
        self.name = name  # type: str
        self.primary_user = primary_user  # type: str
        self.region = region  # type: str
        self.replica = replica  # type: int
        self.slb = slb  # type: list[ListGatewayResponseBodyDataResultSlb]
        self.spec = spec  # type: str
        self.status = status  # type: int
        self.status_desc = status_desc  # type: str
        self.tag = tag  # type: str
        self.upgrade = upgrade  # type: bool
        self.vswitch_2 = vswitch_2  # type: str

    def validate(self):
        if self.internet_slb:
            for k in self.internet_slb:
                if k:
                    k.validate()
        if self.slb:
            for k in self.slb:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ahas_on is not None:
            result['AhasOn'] = self.ahas_on
        if self.arms_on is not None:
            result['ArmsOn'] = self.arms_on
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['InternetSlb'] = []
        if self.internet_slb is not None:
            for k in self.internet_slb:
                result['InternetSlb'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.must_upgrade is not None:
            result['MustUpgrade'] = self.must_upgrade
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user
        if self.region is not None:
            result['Region'] = self.region
        if self.replica is not None:
            result['Replica'] = self.replica
        result['Slb'] = []
        if self.slb is not None:
            for k in self.slb:
                result['Slb'].append(k.to_map() if k else None)
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.status is not None:
            result['Status'] = self.status
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AhasOn') is not None:
            self.ahas_on = m.get('AhasOn')
        if m.get('ArmsOn') is not None:
            self.arms_on = m.get('ArmsOn')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.internet_slb = []
        if m.get('InternetSlb') is not None:
            for k in m.get('InternetSlb'):
                temp_model = ListGatewayResponseBodyDataResultInternetSlb()
                self.internet_slb.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('MustUpgrade') is not None:
            self.must_upgrade = m.get('MustUpgrade')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Replica') is not None:
            self.replica = m.get('Replica')
        self.slb = []
        if m.get('Slb') is not None:
            for k in m.get('Slb'):
                temp_model = ListGatewayResponseBodyDataResultSlb()
                self.slb.append(temp_model.from_map(k))
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')
        return self


class ListGatewayResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, result=None, total_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: list[ListGatewayResponseBodyDataResult]
        self.total_size = total_size  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGatewayResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGatewayResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListGatewayResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListGatewayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGatewayResponse, self).to_map()
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
            temp_model = ListGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayDomainRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListGatewayDomainResponseBodyData(TeaModel):
    def __init__(self, cert_before_date=None, cert_identifier=None, gateway_id=None, gmt_create=None,
                 gmt_modified=None, id=None, must_https=None, name=None, protocol=None):
        self.cert_before_date = cert_before_date  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.must_https = must_https  # type: bool
        self.name = name  # type: str
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayDomainResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_before_date is not None:
            result['CertBeforeDate'] = self.cert_before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.name is not None:
            result['Name'] = self.name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertBeforeDate') is not None:
            self.cert_before_date = m.get('CertBeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class ListGatewayDomainResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListGatewayDomainResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGatewayDomainResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGatewayDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGatewayDomainResponse, self).to_map()
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
            temp_model = ListGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayRouteRequestFilterParams(TeaModel):
    def __init__(self, default_service_id=None, domain_id=None, gateway_id=None, gateway_unique_id=None, name=None,
                 route_order=None, status=None):
        self.default_service_id = default_service_id  # type: long
        self.domain_id = domain_id  # type: long
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.name = name  # type: str
        self.route_order = route_order  # type: int
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteRequestFilterParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListGatewayRouteRequest(TeaModel):
    def __init__(self, accept_language=None, desc_sort=None, filter_params=None, order_item=None, page_number=None,
                 page_size=None):
        self.accept_language = accept_language  # type: str
        self.desc_sort = desc_sort  # type: bool
        self.filter_params = filter_params  # type: ListGatewayRouteRequestFilterParams
        self.order_item = order_item  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        _map = super(ListGatewayRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params is not None:
            result['FilterParams'] = self.filter_params.to_map()
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            temp_model = ListGatewayRouteRequestFilterParams()
            self.filter_params = temp_model.from_map(m['FilterParams'])
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayRouteShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, desc_sort=None, filter_params_shrink=None, order_item=None,
                 page_number=None, page_size=None):
        self.accept_language = accept_language  # type: str
        self.desc_sort = desc_sort  # type: bool
        self.filter_params_shrink = filter_params_shrink  # type: str
        self.order_item = order_item  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            self.filter_params_shrink = m.get('FilterParams')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayRouteResponseBodyDataResultDirectResponse(TeaModel):
    def __init__(self, body=None, code=None):
        self.body = body  # type: str
        self.code = code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultDirectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListGatewayRouteResponseBodyDataResultRedirect(TeaModel):
    def __init__(self, code=None, host=None, path=None):
        self.code = code  # type: int
        self.host = host  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultRedirect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates(TeaModel):
    def __init__(self, ignore_case=None, path=None, type=None):
        self.ignore_case = ignore_case  # type: bool
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListGatewayRouteResponseBodyDataResultRoutePredicates(TeaModel):
    def __init__(self, header_predicates=None, method_predicates=None, path_predicates=None, query_predicates=None):
        self.header_predicates = header_predicates  # type: list[ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates]
        self.method_predicates = method_predicates  # type: list[str]
        self.path_predicates = path_predicates  # type: ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates
        self.query_predicates = query_predicates  # type: list[ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates]

    def validate(self):
        if self.header_predicates:
            for k in self.header_predicates:
                if k:
                    k.validate()
        if self.path_predicates:
            self.path_predicates.validate()
        if self.query_predicates:
            for k in self.query_predicates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultRoutePredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HeaderPredicates'] = []
        if self.header_predicates is not None:
            for k in self.header_predicates:
                result['HeaderPredicates'].append(k.to_map() if k else None)
        if self.method_predicates is not None:
            result['MethodPredicates'] = self.method_predicates
        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()
        result['QueryPredicates'] = []
        if self.query_predicates is not None:
            for k in self.query_predicates:
                result['QueryPredicates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.header_predicates = []
        if m.get('HeaderPredicates') is not None:
            for k in m.get('HeaderPredicates'):
                temp_model = ListGatewayRouteResponseBodyDataResultRoutePredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k))
        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')
        if m.get('PathPredicates') is not None:
            temp_model = ListGatewayRouteResponseBodyDataResultRoutePredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m['PathPredicates'])
        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k in m.get('QueryPredicates'):
                temp_model = ListGatewayRouteResponseBodyDataResultRoutePredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k))
        return self


class ListGatewayRouteResponseBodyDataResultRouteServices(TeaModel):
    def __init__(self, group_name=None, name=None, namespace=None, percent=None, service_id=None, service_name=None,
                 source_type=None, version=None):
        self.group_name = group_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.percent = percent  # type: int
        self.service_id = service_id  # type: long
        self.service_name = service_name  # type: str
        self.source_type = source_type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResultRouteServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListGatewayRouteResponseBodyDataResult(TeaModel):
    def __init__(self, default_service_id=None, default_service_name=None, destination_type=None,
                 direct_response=None, domain_id=None, domain_id_list=None, domain_name=None, domain_name_list=None,
                 gateway_id=None, gateway_unique_id=None, gmt_create=None, gmt_modified=None, id=None, name=None,
                 predicates=None, redirect=None, route_order=None, route_predicates=None, route_services=None, services=None,
                 status=None):
        self.default_service_id = default_service_id  # type: long
        self.default_service_name = default_service_name  # type: str
        self.destination_type = destination_type  # type: str
        self.direct_response = direct_response  # type: ListGatewayRouteResponseBodyDataResultDirectResponse
        self.domain_id = domain_id  # type: long
        self.domain_id_list = domain_id_list  # type: list[long]
        self.domain_name = domain_name  # type: str
        self.domain_name_list = domain_name_list  # type: list[str]
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.predicates = predicates  # type: str
        self.redirect = redirect  # type: ListGatewayRouteResponseBodyDataResultRedirect
        self.route_order = route_order  # type: int
        self.route_predicates = route_predicates  # type: ListGatewayRouteResponseBodyDataResultRoutePredicates
        self.route_services = route_services  # type: list[ListGatewayRouteResponseBodyDataResultRouteServices]
        self.services = services  # type: str
        self.status = status  # type: int

    def validate(self):
        if self.direct_response:
            self.direct_response.validate()
        if self.redirect:
            self.redirect.validate()
        if self.route_predicates:
            self.route_predicates.validate()
        if self.route_services:
            for k in self.route_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_service_id is not None:
            result['DefaultServiceId'] = self.default_service_id
        if self.default_service_name is not None:
            result['DefaultServiceName'] = self.default_service_name
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direct_response is not None:
            result['DirectResponse'] = self.direct_response.to_map()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_id_list is not None:
            result['DomainIdList'] = self.domain_id_list
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_list is not None:
            result['DomainNameList'] = self.domain_name_list
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates is not None:
            result['Predicates'] = self.predicates
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        if self.route_predicates is not None:
            result['RoutePredicates'] = self.route_predicates.to_map()
        result['RouteServices'] = []
        if self.route_services is not None:
            for k in self.route_services:
                result['RouteServices'].append(k.to_map() if k else None)
        if self.services is not None:
            result['Services'] = self.services
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultServiceId') is not None:
            self.default_service_id = m.get('DefaultServiceId')
        if m.get('DefaultServiceName') is not None:
            self.default_service_name = m.get('DefaultServiceName')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DirectResponse') is not None:
            temp_model = ListGatewayRouteResponseBodyDataResultDirectResponse()
            self.direct_response = temp_model.from_map(m['DirectResponse'])
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainIdList') is not None:
            self.domain_id_list = m.get('DomainIdList')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameList') is not None:
            self.domain_name_list = m.get('DomainNameList')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            self.predicates = m.get('Predicates')
        if m.get('Redirect') is not None:
            temp_model = ListGatewayRouteResponseBodyDataResultRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        if m.get('RoutePredicates') is not None:
            temp_model = ListGatewayRouteResponseBodyDataResultRoutePredicates()
            self.route_predicates = temp_model.from_map(m['RoutePredicates'])
        self.route_services = []
        if m.get('RouteServices') is not None:
            for k in m.get('RouteServices'):
                temp_model = ListGatewayRouteResponseBodyDataResultRouteServices()
                self.route_services.append(temp_model.from_map(k))
        if m.get('Services') is not None:
            self.services = m.get('Services')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListGatewayRouteResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, result=None, total_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: list[ListGatewayRouteResponseBodyDataResult]
        self.total_size = total_size  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGatewayRouteResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGatewayRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListGatewayRouteResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListGatewayRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListGatewayRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayRouteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGatewayRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGatewayRouteResponse, self).to_map()
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
            temp_model = ListGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayServiceRequestFilterParams(TeaModel):
    def __init__(self, gateway_unique_id=None, group_name=None, name=None, namespace=None, source_type=None):
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.group_name = group_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayServiceRequestFilterParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class ListGatewayServiceRequest(TeaModel):
    def __init__(self, accept_language=None, desc_sort=None, filter_params=None, order_item=None, page_number=None,
                 page_size=None):
        self.accept_language = accept_language  # type: str
        self.desc_sort = desc_sort  # type: bool
        self.filter_params = filter_params  # type: ListGatewayServiceRequestFilterParams
        self.order_item = order_item  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.filter_params:
            self.filter_params.validate()

    def to_map(self):
        _map = super(ListGatewayServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params is not None:
            result['FilterParams'] = self.filter_params.to_map()
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            temp_model = ListGatewayServiceRequestFilterParams()
            self.filter_params = temp_model.from_map(m['FilterParams'])
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayServiceShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, desc_sort=None, filter_params_shrink=None, order_item=None,
                 page_number=None, page_size=None):
        self.accept_language = accept_language  # type: str
        self.desc_sort = desc_sort  # type: bool
        self.filter_params_shrink = filter_params_shrink  # type: str
        self.order_item = order_item  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayServiceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort
        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink
        if self.order_item is not None:
            result['OrderItem'] = self.order_item
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')
        if m.get('FilterParams') is not None:
            self.filter_params_shrink = m.get('FilterParams')
        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayServiceResponseBodyDataResultVersions(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewayServiceResponseBodyDataResultVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListGatewayServiceResponseBodyDataResult(TeaModel):
    def __init__(self, gateway_id=None, gateway_unique_id=None, gmt_create=None, gmt_modified=None, group_name=None,
                 id=None, ips=None, meta_info=None, name=None, namespace=None, service_name_in_registry=None,
                 service_port=None, service_protocol=None, source_id=None, source_type=None, versions=None):
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: long
        self.ips = ips  # type: list[str]
        self.meta_info = meta_info  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.service_name_in_registry = service_name_in_registry  # type: str
        self.service_port = service_port  # type: long
        self.service_protocol = service_protocol  # type: str
        self.source_id = source_id  # type: long
        self.source_type = source_type  # type: str
        self.versions = versions  # type: list[ListGatewayServiceResponseBodyDataResultVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayServiceResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name_in_registry is not None:
            result['ServiceNameInRegistry'] = self.service_name_in_registry
        if self.service_port is not None:
            result['ServicePort'] = self.service_port
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceNameInRegistry') is not None:
            self.service_name_in_registry = m.get('ServiceNameInRegistry')
        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListGatewayServiceResponseBodyDataResultVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListGatewayServiceResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, result=None, total_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: list[ListGatewayServiceResponseBodyDataResult]
        self.total_size = total_size  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewayServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGatewayServiceResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGatewayServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: ListGatewayServiceResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListGatewayServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListGatewayServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewayServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGatewayServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGatewayServiceResponse, self).to_map()
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
            temp_model = ListGatewayServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewaySlbRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewaySlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListGatewaySlbResponseBodyData(TeaModel):
    def __init__(self, gateway_id=None, gateway_slb_mode=None, gateway_slb_status=None, gmt_create=None, id=None,
                 slb_id=None, slb_ip=None, slb_port=None, status_desc=None, type=None):
        self.gateway_id = gateway_id  # type: str
        self.gateway_slb_mode = gateway_slb_mode  # type: str
        self.gateway_slb_status = gateway_slb_status  # type: str
        self.gmt_create = gmt_create  # type: str
        self.id = id  # type: str
        self.slb_id = slb_id  # type: str
        self.slb_ip = slb_ip  # type: str
        self.slb_port = slb_port  # type: str
        self.status_desc = status_desc  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGatewaySlbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode
        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip
        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')
        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')
        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListGatewaySlbResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListGatewaySlbResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGatewaySlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGatewaySlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGatewaySlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGatewaySlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGatewaySlbResponse, self).to_map()
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
            temp_model = ListGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByConfigRequest(TeaModel):
    def __init__(self, accept_language=None, data_id=None, group=None, instance_id=None, namespace_id=None,
                 request_pars=None):
        self.accept_language = accept_language  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListListenersByConfigResponseBodyListeners(TeaModel):
    def __init__(self, ip=None, md_5=None):
        self.ip = ip  # type: str
        self.md_5 = md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByConfigResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListListenersByConfigResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, listeners=None, message=None, page_number=None,
                 page_size=None, request_id=None, success=None, total_count=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.listeners = listeners  # type: list[ListListenersByConfigResponseBodyListeners]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersByConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByConfigResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersByConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListListenersByConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersByConfigResponse, self).to_map()
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
            temp_model = ListListenersByConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersByIpRequest(TeaModel):
    def __init__(self, accept_language=None, instance_id=None, ip=None, namespace_id=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: str
        self.namespace_id = namespace_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListListenersByIpResponseBodyListeners(TeaModel):
    def __init__(self, data_id=None, group=None, md_5=None):
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.md_5 = md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersByIpResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListListenersByIpResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, listeners=None, message=None, page_number=None,
                 page_size=None, request_id=None, success=None, total_count=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.listeners = listeners  # type: list[ListListenersByIpResponseBodyListeners]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersByIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersByIpResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersByIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListListenersByIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersByIpResponse, self).to_map()
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
            temp_model = ListListenersByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosConfigsRequest(TeaModel):
    def __init__(self, accept_language=None, app_name=None, data_id=None, group=None, instance_id=None,
                 namespace_id=None, page_num=None, page_size=None, region_id=None, request_pars=None, tags=None):
        self.accept_language = accept_language  # type: str
        self.app_name = app_name  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.request_pars = request_pars  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListNacosConfigsResponseBodyConfigurations(TeaModel):
    def __init__(self, app_name=None, data_id=None, group=None, id=None):
        self.app_name = app_name  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosConfigsResponseBodyConfigurations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListNacosConfigsResponseBody(TeaModel):
    def __init__(self, code=None, configurations=None, error_code=None, http_code=None, message=None,
                 page_number=None, page_size=None, request_id=None, success=None, total_count=None):
        self.code = code  # type: int
        self.configurations = configurations  # type: list[ListNacosConfigsResponseBodyConfigurations]
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNacosConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['Configurations'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.configurations = []
        if m.get('Configurations') is not None:
            for k in m.get('Configurations'):
                temp_model = ListNacosConfigsResponseBodyConfigurations()
                self.configurations.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNacosConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNacosConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNacosConfigsResponse, self).to_map()
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
            temp_model = ListNacosConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNacosHistoryConfigsRequest(TeaModel):
    def __init__(self, accept_language=None, data_id=None, group=None, instance_id=None, namespace_id=None,
                 page_num=None, page_size=None, region_id=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosHistoryConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class ListNacosHistoryConfigsResponseBodyHistoryItems(TeaModel):
    def __init__(self, app_name=None, data_id=None, group=None, id=None, last_modified_time=None, op_type=None):
        self.app_name = app_name  # type: str
        self.data_id = data_id  # type: str
        self.group = group  # type: str
        self.id = id  # type: long
        self.last_modified_time = last_modified_time  # type: long
        self.op_type = op_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNacosHistoryConfigsResponseBodyHistoryItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.group is not None:
            result['Group'] = self.group
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class ListNacosHistoryConfigsResponseBody(TeaModel):
    def __init__(self, error_code=None, history_items=None, http_code=None, message=None, page_number=None,
                 page_size=None, request_id=None, success=None, total_count=None):
        self.error_code = error_code  # type: str
        self.history_items = history_items  # type: list[ListNacosHistoryConfigsResponseBodyHistoryItems]
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.history_items:
            for k in self.history_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNacosHistoryConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['HistoryItems'] = []
        if self.history_items is not None:
            for k in self.history_items:
                result['HistoryItems'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k in m.get('HistoryItems'):
                temp_model = ListNacosHistoryConfigsResponseBodyHistoryItems()
                self.history_items.append(temp_model.from_map(k))
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNacosHistoryConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNacosHistoryConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNacosHistoryConfigsResponse, self).to_map()
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
            temp_model = ListNacosHistoryConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSSLCertRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSSLCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListSSLCertResponseBodyData(TeaModel):
    def __init__(self, after_date=None, algorithm=None, before_date=None, cert_identifier=None, cert_name=None,
                 common_name=None, gmt_after=None, gmt_before=None, issuer=None, sans=None):
        self.after_date = after_date  # type: str
        self.algorithm = algorithm  # type: str
        self.before_date = before_date  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.cert_name = cert_name  # type: str
        self.common_name = common_name  # type: str
        self.gmt_after = gmt_after  # type: str
        self.gmt_before = gmt_before  # type: str
        self.issuer = issuer  # type: str
        self.sans = sans  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSSLCertResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_date is not None:
            result['AfterDate'] = self.after_date
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.before_date is not None:
            result['BeforeDate'] = self.before_date
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.gmt_after is not None:
            result['GmtAfter'] = self.gmt_after
        if self.gmt_before is not None:
            result['GmtBefore'] = self.gmt_before
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.sans is not None:
            result['Sans'] = self.sans
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('GmtAfter') is not None:
            self.gmt_after = m.get('GmtAfter')
        if m.get('GmtBefore') is not None:
            self.gmt_before = m.get('GmtBefore')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        return self


class ListSSLCertResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListSSLCertResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSSLCertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSSLCertResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSSLCertResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSSLCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSSLCertResponse, self).to_map()
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
            temp_model = ListSSLCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceSourceRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class ListServiceSourceResponseBodyData(TeaModel):
    def __init__(self, address=None, binding_with_gateway=None, gateway_id=None, gmt_create=None, gmt_modified=None,
                 id=None, name=None, source=None, source_unique_id=None, type=None):
        self.address = address  # type: str
        self.binding_with_gateway = binding_with_gateway  # type: int
        self.gateway_id = gateway_id  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.source = source  # type: str
        self.source_unique_id = source_unique_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.binding_with_gateway is not None:
            result['BindingWithGateway'] = self.binding_with_gateway
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.source_unique_id is not None:
            result['SourceUniqueId'] = self.source_unique_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BindingWithGateway') is not None:
            self.binding_with_gateway = m.get('BindingWithGateway')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUniqueId') is not None:
            self.source_unique_id = m.get('SourceUniqueId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListServiceSourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[ListServiceSourceResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListServiceSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListServiceSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceSourceResponse, self).to_map()
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
            temp_model = ListServiceSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZnodeChildrenRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, path=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZnodeChildrenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListZnodeChildrenResponseBodyData(TeaModel):
    def __init__(self, data=None, dir=None, name=None, path=None):
        self.data = data  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZnodeChildrenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListZnodeChildrenResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[ListZnodeChildrenResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListZnodeChildrenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListZnodeChildrenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZnodeChildrenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListZnodeChildrenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListZnodeChildrenResponse, self).to_map()
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
            temp_model = ListZnodeChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, namespace_infos=None, region_id=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.namespace_infos = namespace_infos  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGovernanceKubernetesClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGovernanceKubernetesClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyGovernanceKubernetesClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyGovernanceKubernetesClusterResponse, self).to_map()
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
            temp_model = ModifyGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineGatewayRouteRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, route_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.route_id = route_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineGatewayRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        return self


class OfflineGatewayRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineGatewayRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OfflineGatewayRouteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OfflineGatewayRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OfflineGatewayRouteResponse, self).to_map()
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
            temp_model = OfflineGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullServicesRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, source_id=None, source_type=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.source_id = source_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class PullServicesResponseBodyDataServices(TeaModel):
    def __init__(self, group_name=None, name=None, namespace=None, source_id=None, source_type=None):
        self.group_name = group_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.source_id = source_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullServicesResponseBodyDataServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class PullServicesResponseBodyData(TeaModel):
    def __init__(self, group_name=None, namespace=None, services=None):
        self.group_name = group_name  # type: str
        self.namespace = namespace  # type: str
        self.services = services  # type: list[PullServicesResponseBodyDataServices]

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PullServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = PullServicesResponseBodyDataServices()
                self.services.append(temp_model.from_map(k))
        return self


class PullServicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[PullServicesResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PullServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = PullServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PullServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PullServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PullServicesResponse, self).to_map()
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
            temp_model = PullServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllSwimmingLaneRequest(TeaModel):
    def __init__(self, accept_language=None, group_id=None):
        self.accept_language = accept_language  # type: str
        self.group_id = group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAllSwimmingLaneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class QueryAllSwimmingLaneResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAllSwimmingLaneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAllSwimmingLaneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAllSwimmingLaneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAllSwimmingLaneResponse, self).to_map()
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
            temp_model = QueryAllSwimmingLaneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllSwimmingLaneGroupRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAllSwimmingLaneGroupRequest, self).to_map()
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


class QueryAllSwimmingLaneGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAllSwimmingLaneGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAllSwimmingLaneGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAllSwimmingLaneGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAllSwimmingLaneGroupResponse, self).to_map()
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
            temp_model = QueryAllSwimmingLaneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBusinessLocationsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBusinessLocationsRequest, self).to_map()
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


class QueryBusinessLocationsResponseBodyData(TeaModel):
    def __init__(self, cn_name=None, description=None, district_cn_name=None, district_en_name=None,
                 district_id=None, district_ordering=None, district_show_name=None, en_description=None, en_name=None,
                 name=None, ordering=None, show_name=None, type=None):
        self.cn_name = cn_name  # type: str
        self.description = description  # type: str
        self.district_cn_name = district_cn_name  # type: str
        self.district_en_name = district_en_name  # type: str
        self.district_id = district_id  # type: str
        self.district_ordering = district_ordering  # type: int
        self.district_show_name = district_show_name  # type: str
        self.en_description = en_description  # type: str
        self.en_name = en_name  # type: str
        self.name = name  # type: str
        self.ordering = ordering  # type: int
        self.show_name = show_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBusinessLocationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_name is not None:
            result['CnName'] = self.cn_name
        if self.description is not None:
            result['Description'] = self.description
        if self.district_cn_name is not None:
            result['DistrictCnName'] = self.district_cn_name
        if self.district_en_name is not None:
            result['DistrictEnName'] = self.district_en_name
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_ordering is not None:
            result['DistrictOrdering'] = self.district_ordering
        if self.district_show_name is not None:
            result['DistrictShowName'] = self.district_show_name
        if self.en_description is not None:
            result['EnDescription'] = self.en_description
        if self.en_name is not None:
            result['EnName'] = self.en_name
        if self.name is not None:
            result['Name'] = self.name
        if self.ordering is not None:
            result['Ordering'] = self.ordering
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DistrictCnName') is not None:
            self.district_cn_name = m.get('DistrictCnName')
        if m.get('DistrictEnName') is not None:
            self.district_en_name = m.get('DistrictEnName')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictOrdering') is not None:
            self.district_ordering = m.get('DistrictOrdering')
        if m.get('DistrictShowName') is not None:
            self.district_show_name = m.get('DistrictShowName')
        if m.get('EnDescription') is not None:
            self.en_description = m.get('EnDescription')
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ordering') is not None:
            self.ordering = m.get('Ordering')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryBusinessLocationsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[QueryBusinessLocationsResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryBusinessLocationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryBusinessLocationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBusinessLocationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryBusinessLocationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBusinessLocationsResponse, self).to_map()
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
            temp_model = QueryBusinessLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDetailRequest(TeaModel):
    def __init__(self, accept_language=None, instance_id=None, order_id=None):
        self.accept_language = accept_language  # type: str
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryClusterDetailResponseBodyDataInstanceModels(TeaModel):
    def __init__(self, creation_timestamp=None, health_status=None, internet_ip=None, ip=None, pod_name=None,
                 role=None, single_tunnel_vip=None):
        self.creation_timestamp = creation_timestamp  # type: str
        self.health_status = health_status  # type: str
        self.internet_ip = internet_ip  # type: str
        self.ip = ip  # type: str
        self.pod_name = pod_name  # type: str
        self.role = role  # type: str
        self.single_tunnel_vip = single_tunnel_vip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyDataInstanceModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.role is not None:
            result['Role'] = self.role
        if self.single_tunnel_vip is not None:
            result['SingleTunnelVip'] = self.single_tunnel_vip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SingleTunnelVip') is not None:
            self.single_tunnel_vip = m.get('SingleTunnelVip')
        return self


class QueryClusterDetailResponseBodyData(TeaModel):
    def __init__(self, acl_entry_list=None, acl_id=None, app_version=None, charge_type=None,
                 cluster_alias_name=None, cluster_name=None, cluster_specification=None, cluster_type=None, cluster_version=None,
                 connection_type=None, cpu=None, create_time=None, disk_capacity=None, disk_type=None, health_status=None,
                 init_cost_time=None, init_status=None, instance_count=None, instance_id=None, instance_models=None,
                 internet_address=None, internet_domain=None, internet_port=None, intranet_address=None, intranet_domain=None,
                 intranet_port=None, memory_capacity=None, mse_version=None, net_type=None, pay_info=None, pub_network_flow=None,
                 region_id=None, v_switch_id=None, vpc_id=None):
        self.acl_entry_list = acl_entry_list  # type: str
        self.acl_id = acl_id  # type: str
        self.app_version = app_version  # type: str
        self.charge_type = charge_type  # type: str
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_specification = cluster_specification  # type: str
        self.cluster_type = cluster_type  # type: str
        self.cluster_version = cluster_version  # type: str
        self.connection_type = connection_type  # type: str
        self.cpu = cpu  # type: int
        self.create_time = create_time  # type: str
        self.disk_capacity = disk_capacity  # type: long
        self.disk_type = disk_type  # type: str
        self.health_status = health_status  # type: str
        self.init_cost_time = init_cost_time  # type: long
        self.init_status = init_status  # type: str
        self.instance_count = instance_count  # type: int
        self.instance_id = instance_id  # type: str
        self.instance_models = instance_models  # type: list[QueryClusterDetailResponseBodyDataInstanceModels]
        self.internet_address = internet_address  # type: str
        self.internet_domain = internet_domain  # type: str
        self.internet_port = internet_port  # type: str
        self.intranet_address = intranet_address  # type: str
        self.intranet_domain = intranet_domain  # type: str
        self.intranet_port = intranet_port  # type: str
        self.memory_capacity = memory_capacity  # type: long
        self.mse_version = mse_version  # type: str
        self.net_type = net_type  # type: str
        self.pay_info = pay_info  # type: str
        self.pub_network_flow = pub_network_flow  # type: str
        self.region_id = region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.instance_models:
            for k in self.instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.init_cost_time is not None:
            result['InitCostTime'] = self.init_cost_time
        if self.init_status is not None:
            result['InitStatus'] = self.init_status
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['InstanceModels'] = []
        if self.instance_models is not None:
            for k in self.instance_models:
                result['InstanceModels'].append(k.to_map() if k else None)
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.pay_info is not None:
            result['PayInfo'] = self.pay_info
        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('InitCostTime') is not None:
            self.init_cost_time = m.get('InitCostTime')
        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.instance_models = []
        if m.get('InstanceModels') is not None:
            for k in m.get('InstanceModels'):
                temp_model = QueryClusterDetailResponseBodyDataInstanceModels()
                self.instance_models.append(temp_model.from_map(k))
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('PayInfo') is not None:
            self.pay_info = m.get('PayInfo')
        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class QueryClusterDetailResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: QueryClusterDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryClusterDetailResponse, self).to_map()
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
            temp_model = QueryClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterDiskSpecificationRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_type=None):
        self.accept_language = accept_language  # type: str
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class QueryClusterDiskSpecificationResponseBodyData(TeaModel):
    def __init__(self, max=None, min=None, step=None):
        self.max = max  # type: int
        self.min = min  # type: int
        self.step = step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class QueryClusterDiskSpecificationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: QueryClusterDiskSpecificationResponseBodyData
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryClusterDiskSpecificationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterDiskSpecificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryClusterDiskSpecificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryClusterDiskSpecificationResponse, self).to_map()
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
            temp_model = QueryClusterDiskSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryClusterSpecificationRequest(TeaModel):
    def __init__(self, accept_language=None, connect_type=None):
        self.accept_language = accept_language  # type: str
        # 网络连接类型
        self.connect_type = connect_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterSpecificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        return self


class QueryClusterSpecificationResponseBodyData(TeaModel):
    def __init__(self, cluster_specification_name=None, cpu_capacity=None, disk_capacity=None, instance_count=None,
                 max_con=None, max_tps=None, memory_capacity=None):
        self.cluster_specification_name = cluster_specification_name  # type: str
        self.cpu_capacity = cpu_capacity  # type: str
        self.disk_capacity = disk_capacity  # type: str
        self.instance_count = instance_count  # type: str
        self.max_con = max_con  # type: str
        self.max_tps = max_tps  # type: str
        self.memory_capacity = memory_capacity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryClusterSpecificationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_specification_name is not None:
            result['ClusterSpecificationName'] = self.cluster_specification_name
        if self.cpu_capacity is not None:
            result['CpuCapacity'] = self.cpu_capacity
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.max_con is not None:
            result['MaxCon'] = self.max_con
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterSpecificationName') is not None:
            self.cluster_specification_name = m.get('ClusterSpecificationName')
        if m.get('CpuCapacity') is not None:
            self.cpu_capacity = m.get('CpuCapacity')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('MaxCon') is not None:
            self.max_con = m.get('MaxCon')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        return self


class QueryClusterSpecificationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, http_status_code=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: int
        self.data = data  # type: list[QueryClusterSpecificationResponseBodyData]
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryClusterSpecificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryClusterSpecificationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryClusterSpecificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryClusterSpecificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryClusterSpecificationResponse, self).to_map()
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
            temp_model = QueryClusterSpecificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryConfigRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, config_type=None, instance_id=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.config_type = config_type  # type: str
        self.instance_id = instance_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class QueryConfigResponseBodyData(TeaModel):
    def __init__(self, autopurge_purge_interval=None, autopurge_snap_retain_count=None, cluster_name=None,
                 config_auth_enabled=None, config_auth_supported=None, config_secret_enabled=None, config_secret_supported=None,
                 init_limit=None, jute_maxbuffer=None, jvm_flags_custom=None, mcpenabled=None, mcpsupported=None,
                 max_client_cnxns=None, max_session_timeout=None, min_session_timeout=None, naming_create_service_supported=None,
                 open_super_acl=None, pass_word=None, restart_flag=None, sync_limit=None, tick_time=None, user_name=None):
        self.autopurge_purge_interval = autopurge_purge_interval  # type: str
        self.autopurge_snap_retain_count = autopurge_snap_retain_count  # type: str
        self.cluster_name = cluster_name  # type: str
        self.config_auth_enabled = config_auth_enabled  # type: bool
        self.config_auth_supported = config_auth_supported  # type: bool
        self.config_secret_enabled = config_secret_enabled  # type: bool
        self.config_secret_supported = config_secret_supported  # type: bool
        self.init_limit = init_limit  # type: str
        self.jute_maxbuffer = jute_maxbuffer  # type: str
        self.jvm_flags_custom = jvm_flags_custom  # type: str
        self.mcpenabled = mcpenabled  # type: bool
        self.mcpsupported = mcpsupported  # type: bool
        self.max_client_cnxns = max_client_cnxns  # type: str
        # 最大超时时间
        self.max_session_timeout = max_session_timeout  # type: str
        # 最小超时时间
        self.min_session_timeout = min_session_timeout  # type: str
        self.naming_create_service_supported = naming_create_service_supported  # type: bool
        self.open_super_acl = open_super_acl  # type: bool
        self.pass_word = pass_word  # type: str
        self.restart_flag = restart_flag  # type: bool
        self.sync_limit = sync_limit  # type: str
        self.tick_time = tick_time  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.config_auth_supported is not None:
            result['ConfigAuthSupported'] = self.config_auth_supported
        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled
        if self.config_secret_supported is not None:
            result['ConfigSecretSupported'] = self.config_secret_supported
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.jvm_flags_custom is not None:
            result['JvmFlagsCustom'] = self.jvm_flags_custom
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.mcpsupported is not None:
            result['MCPSupported'] = self.mcpsupported
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.max_session_timeout is not None:
            result['MaxSessionTimeout'] = self.max_session_timeout
        if self.min_session_timeout is not None:
            result['MinSessionTimeout'] = self.min_session_timeout
        if self.naming_create_service_supported is not None:
            result['NamingCreateServiceSupported'] = self.naming_create_service_supported
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.restart_flag is not None:
            result['RestartFlag'] = self.restart_flag
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('ConfigAuthSupported') is not None:
            self.config_auth_supported = m.get('ConfigAuthSupported')
        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')
        if m.get('ConfigSecretSupported') is not None:
            self.config_secret_supported = m.get('ConfigSecretSupported')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('JvmFlagsCustom') is not None:
            self.jvm_flags_custom = m.get('JvmFlagsCustom')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('MCPSupported') is not None:
            self.mcpsupported = m.get('MCPSupported')
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('MaxSessionTimeout') is not None:
            self.max_session_timeout = m.get('MaxSessionTimeout')
        if m.get('MinSessionTimeout') is not None:
            self.min_session_timeout = m.get('MinSessionTimeout')
        if m.get('NamingCreateServiceSupported') is not None:
            self.naming_create_service_supported = m.get('NamingCreateServiceSupported')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('RestartFlag') is not None:
            self.restart_flag = m.get('RestartFlag')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: QueryConfigResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryConfigResponse, self).to_map()
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
            temp_model = QueryConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGatewayRegionRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGatewayRegionRequest, self).to_map()
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


class QueryGatewayRegionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[str]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGatewayRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGatewayRegionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryGatewayRegionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGatewayRegionResponse, self).to_map()
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
            temp_model = QueryGatewayRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGatewayTypeRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGatewayTypeRequest, self).to_map()
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


class QueryGatewayTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[str]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGatewayTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGatewayTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryGatewayTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGatewayTypeResponse, self).to_map()
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
            temp_model = QueryGatewayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGovernanceKubernetesClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, cluster_name=None, page_number=None, page_size=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGovernanceKubernetesClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryGovernanceKubernetesClusterResponseBodyDataResult(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, k_8s_version=None, namespace_infos=None,
                 pilot_start_time=None, region=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.k_8s_version = k_8s_version  # type: str
        self.namespace_infos = namespace_infos  # type: str
        self.pilot_start_time = pilot_start_time  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGovernanceKubernetesClusterResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version
        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos
        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')
        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')
        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class QueryGovernanceKubernetesClusterResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, result=None, total_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: list[QueryGovernanceKubernetesClusterResponseBodyDataResult]
        self.total_size = total_size  # type: int

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryGovernanceKubernetesClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryGovernanceKubernetesClusterResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class QueryGovernanceKubernetesClusterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: QueryGovernanceKubernetesClusterResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryGovernanceKubernetesClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGovernanceKubernetesClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryGovernanceKubernetesClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGovernanceKubernetesClusterResponse, self).to_map()
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
            temp_model = QueryGovernanceKubernetesClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorRequest(TeaModel):
    def __init__(self, accept_language=None, end_time=None, instance_id=None, monitor_type=None, request_pars=None,
                 start_time=None, step=None):
        self.accept_language = accept_language  # type: str
        self.end_time = end_time  # type: long
        self.instance_id = instance_id  # type: str
        self.monitor_type = monitor_type  # type: str
        self.request_pars = request_pars  # type: str
        self.start_time = start_time  # type: long
        self.step = step  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class QueryMonitorResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonitorResponse, self).to_map()
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
            temp_model = QueryMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySlbSpecRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySlbSpecRequest, self).to_map()
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


class QuerySlbSpecResponseBodyData(TeaModel):
    def __init__(self, id=None, max_connection=None, name=None, new_connection_per_second=None, qps=None, spec=None):
        self.id = id  # type: int
        self.max_connection = max_connection  # type: str
        self.name = name  # type: str
        self.new_connection_per_second = new_connection_per_second  # type: str
        self.qps = qps  # type: str
        self.spec = spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySlbSpecResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection
        if self.name is not None:
            result['Name'] = self.name
        if self.new_connection_per_second is not None:
            result['NewConnectionPerSecond'] = self.new_connection_per_second
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewConnectionPerSecond') is not None:
            self.new_connection_per_second = m.get('NewConnectionPerSecond')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class QuerySlbSpecResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[QuerySlbSpecResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySlbSpecResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySlbSpecResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySlbSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySlbSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySlbSpecResponse, self).to_map()
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
            temp_model = QuerySlbSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySwimmingLaneByIdRequest(TeaModel):
    def __init__(self, accept_language=None, lane_id=None):
        self.accept_language = accept_language  # type: str
        self.lane_id = lane_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySwimmingLaneByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.lane_id is not None:
            result['LaneId'] = self.lane_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')
        return self


class QuerySwimmingLaneByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, dynamic_message=None, error_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        # code仅仅用来和success同步
        self.code = code  # type: int
        self.data = data  # type: any
        # 动态错误信息中的占位符
        self.dynamic_message = dynamic_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySwimmingLaneByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySwimmingLaneByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySwimmingLaneByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySwimmingLaneByIdResponse, self).to_map()
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
            temp_model = QuerySwimmingLaneByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryZnodeDetailRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, path=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.path = path  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryZnodeDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.path is not None:
            result['Path'] = self.path
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class QueryZnodeDetailResponseBodyData(TeaModel):
    def __init__(self, data=None, dir=None, name=None, path=None):
        self.data = data  # type: str
        self.dir = dir  # type: bool
        self.name = name  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryZnodeDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class QueryZnodeDetailResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: QueryZnodeDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryZnodeDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryZnodeDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryZnodeDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryZnodeDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryZnodeDetailResponse, self).to_map()
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
            temp_model = QueryZnodeDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, instance_id=None, pod_name_list=None,
                 request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str
        self.pod_name_list = pod_name_list  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pod_name_list is not None:
            result['PodNameList'] = self.pod_name_list
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PodNameList') is not None:
            self.pod_name_list = m.get('PodNameList')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class RestartClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartClusterResponse, self).to_map()
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
            temp_model = RestartClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryClusterRequest(TeaModel):
    def __init__(self, accept_language=None, instance_id=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.instance_id = instance_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class RetryClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RetryClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryClusterResponse, self).to_map()
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
            temp_model = RetryClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScalingClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_specification=None, cpu=None, instance_count=None,
                 instance_id=None, memory_capacity=None):
        self.accept_language = accept_language  # type: str
        self.cluster_specification = cluster_specification  # type: str
        self.cpu = cpu  # type: int
        self.instance_count = instance_count  # type: int
        self.instance_id = instance_id  # type: str
        self.memory_capacity = memory_capacity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        return self


class ScalingClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScalingClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScalingClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ScalingClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScalingClusterResponse, self).to_map()
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
            temp_model = ScalingClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectGatewaySlbRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, name=None, type=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SelectGatewaySlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SelectGatewaySlbResponseBodyData(TeaModel):
    def __init__(self, slb_id=None, slb_name=None):
        self.slb_id = slb_id  # type: str
        self.slb_name = slb_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SelectGatewaySlbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_name is not None:
            result['SlbName'] = self.slb_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')
        return self


class SelectGatewaySlbResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[SelectGatewaySlbResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SelectGatewaySlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SelectGatewaySlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectGatewaySlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SelectGatewaySlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SelectGatewaySlbResponse, self).to_map()
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
            temp_model = SelectGatewaySlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclRequest(TeaModel):
    def __init__(self, accept_language=None, acl_entry_list=None, instance_id=None):
        self.accept_language = accept_language  # type: str
        self.acl_entry_list = acl_entry_list  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.acl_entry_list is not None:
            result['AclEntryList'] = self.acl_entry_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AclEntryList') is not None:
            self.acl_entry_list = m.get('AclEntryList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAclResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAclResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAclResponse, self).to_map()
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
            temp_model = UpdateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBlackWhiteListRequest(TeaModel):
    def __init__(self, accept_language=None, content=None, gateway_unique_id=None, id=None, is_white=None,
                 resource_type=None, status=None, type=None):
        self.accept_language = accept_language  # type: str
        self.content = content  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.is_white = is_white  # type: bool
        self.resource_type = resource_type  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBlackWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.content is not None:
            result['Content'] = self.content
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.is_white is not None:
            result['IsWhite'] = self.is_white
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateBlackWhiteListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBlackWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBlackWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateBlackWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBlackWhiteListResponse, self).to_map()
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
            temp_model = UpdateBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_alias_name=None, instance_id=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_alias_name = cluster_alias_name  # type: str
        self.instance_id = instance_id  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClusterResponse, self).to_map()
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
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigRequest(TeaModel):
    def __init__(self, accept_language=None, autopurge_purge_interval=None, autopurge_snap_retain_count=None,
                 cluster_id=None, config_auth_enabled=None, config_secret_enabled=None, config_type=None, init_limit=None,
                 instance_id=None, jute_maxbuffer=None, mcpenabled=None, max_client_cnxns=None, max_session_timeout=None,
                 min_session_timeout=None, open_super_acl=None, pass_word=None, request_pars=None, sync_limit=None, tick_time=None,
                 user_name=None):
        self.accept_language = accept_language  # type: str
        self.autopurge_purge_interval = autopurge_purge_interval  # type: str
        self.autopurge_snap_retain_count = autopurge_snap_retain_count  # type: str
        self.cluster_id = cluster_id  # type: str
        self.config_auth_enabled = config_auth_enabled  # type: bool
        self.config_secret_enabled = config_secret_enabled  # type: bool
        self.config_type = config_type  # type: str
        self.init_limit = init_limit  # type: str
        self.instance_id = instance_id  # type: str
        self.jute_maxbuffer = jute_maxbuffer  # type: str
        self.mcpenabled = mcpenabled  # type: bool
        self.max_client_cnxns = max_client_cnxns  # type: str
        # 最大超时时间
        self.max_session_timeout = max_session_timeout  # type: str
        # 最小超时时间
        self.min_session_timeout = min_session_timeout  # type: str
        self.open_super_acl = open_super_acl  # type: str
        self.pass_word = pass_word  # type: str
        self.request_pars = request_pars  # type: str
        self.sync_limit = sync_limit  # type: str
        self.tick_time = tick_time  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval
        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled
        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer
        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled
        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns
        if self.max_session_timeout is not None:
            result['MaxSessionTimeout'] = self.max_session_timeout
        if self.min_session_timeout is not None:
            result['MinSessionTimeout'] = self.min_session_timeout
        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit
        if self.tick_time is not None:
            result['TickTime'] = self.tick_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')
        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')
        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')
        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')
        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')
        if m.get('MaxSessionTimeout') is not None:
            self.max_session_timeout = m.get('MaxSessionTimeout')
        if m.get('MinSessionTimeout') is not None:
            self.min_session_timeout = m.get('MinSessionTimeout')
        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')
        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateConfigResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConfigResponse, self).to_map()
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
            temp_model = UpdateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEngineNamespaceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, desc=None, id=None, instance_id=None, name=None,
                 service_count=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.desc = desc  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.service_count = service_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEngineNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.service_count is not None:
            result['ServiceCount'] = self.service_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCount') is not None:
            self.service_count = m.get('ServiceCount')
        return self


class UpdateEngineNamespaceResponseBodyData(TeaModel):
    def __init__(self, config_count=None, namespace=None, namespace_desc=None, namespace_show_name=None, quota=None,
                 type=None):
        self.config_count = config_count  # type: int
        self.namespace = namespace  # type: str
        self.namespace_desc = namespace_desc  # type: str
        self.namespace_show_name = namespace_show_name  # type: str
        self.quota = quota  # type: int
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEngineNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_count is not None:
            result['ConfigCount'] = self.config_count
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.namespace_desc is not None:
            result['NamespaceDesc'] = self.namespace_desc
        if self.namespace_show_name is not None:
            result['NamespaceShowName'] = self.namespace_show_name
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigCount') is not None:
            self.config_count = m.get('ConfigCount')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NamespaceDesc') is not None:
            self.namespace_desc = m.get('NamespaceDesc')
        if m.get('NamespaceShowName') is not None:
            self.namespace_show_name = m.get('NamespaceShowName')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateEngineNamespaceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, message=None, request_id=None, success=None):
        self.data = data  # type: UpdateEngineNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateEngineNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateEngineNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEngineNamespaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEngineNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEngineNamespaceResponse, self).to_map()
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
            temp_model = UpdateEngineNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayDomainRequest(TeaModel):
    def __init__(self, accept_language=None, cert_identifier=None, gateway_unique_id=None, id=None, must_https=None,
                 protocol=None):
        self.accept_language = accept_language  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.must_https = must_https  # type: bool
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.must_https is not None:
            result['MustHttps'] = self.must_https
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class UpdateGatewayDomainResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayDomainResponse, self).to_map()
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
            temp_model = UpdateGatewayDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayNameRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, name=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateGatewayNameResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayNameResponse, self).to_map()
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
            temp_model = UpdateGatewayNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayOptionRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_option=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_option = gateway_option  # type: GatewayOption
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        if self.gateway_option:
            self.gateway_option.validate()

    def to_map(self):
        _map = super(UpdateGatewayOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_option is not None:
            result['GatewayOption'] = self.gateway_option.to_map()
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayOption') is not None:
            temp_model = GatewayOption()
            self.gateway_option = temp_model.from_map(m['GatewayOption'])
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class UpdateGatewayOptionShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_option_shrink=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_option_shrink = gateway_option_shrink  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayOptionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_option_shrink is not None:
            result['GatewayOption'] = self.gateway_option_shrink
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayOption') is not None:
            self.gateway_option_shrink = m.get('GatewayOption')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class UpdateGatewayOptionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: GatewayOption
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateGatewayOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GatewayOption()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayOptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayOptionResponse, self).to_map()
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
            temp_model = UpdateGatewayOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteRequestDirectResponseJSON(TeaModel):
    def __init__(self, body=None, code=None):
        self.body = body  # type: str
        self.code = code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestDirectResponseJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateGatewayRouteRequestPredicatesHeaderPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestPredicatesHeaderPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateGatewayRouteRequestPredicatesPathPredicates(TeaModel):
    def __init__(self, ignore_case=None, path=None, type=None):
        self.ignore_case = ignore_case  # type: bool
        self.path = path  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestPredicatesPathPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_case is not None:
            result['IgnoreCase'] = self.ignore_case
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IgnoreCase') is not None:
            self.ignore_case = m.get('IgnoreCase')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateGatewayRouteRequestPredicatesQueryPredicates(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestPredicatesQueryPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateGatewayRouteRequestPredicates(TeaModel):
    def __init__(self, header_predicates=None, method_predicates=None, path_predicates=None, query_predicates=None):
        self.header_predicates = header_predicates  # type: list[UpdateGatewayRouteRequestPredicatesHeaderPredicates]
        self.method_predicates = method_predicates  # type: list[str]
        self.path_predicates = path_predicates  # type: UpdateGatewayRouteRequestPredicatesPathPredicates
        self.query_predicates = query_predicates  # type: list[UpdateGatewayRouteRequestPredicatesQueryPredicates]

    def validate(self):
        if self.header_predicates:
            for k in self.header_predicates:
                if k:
                    k.validate()
        if self.path_predicates:
            self.path_predicates.validate()
        if self.query_predicates:
            for k in self.query_predicates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestPredicates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HeaderPredicates'] = []
        if self.header_predicates is not None:
            for k in self.header_predicates:
                result['HeaderPredicates'].append(k.to_map() if k else None)
        if self.method_predicates is not None:
            result['MethodPredicates'] = self.method_predicates
        if self.path_predicates is not None:
            result['PathPredicates'] = self.path_predicates.to_map()
        result['QueryPredicates'] = []
        if self.query_predicates is not None:
            for k in self.query_predicates:
                result['QueryPredicates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.header_predicates = []
        if m.get('HeaderPredicates') is not None:
            for k in m.get('HeaderPredicates'):
                temp_model = UpdateGatewayRouteRequestPredicatesHeaderPredicates()
                self.header_predicates.append(temp_model.from_map(k))
        if m.get('MethodPredicates') is not None:
            self.method_predicates = m.get('MethodPredicates')
        if m.get('PathPredicates') is not None:
            temp_model = UpdateGatewayRouteRequestPredicatesPathPredicates()
            self.path_predicates = temp_model.from_map(m['PathPredicates'])
        self.query_predicates = []
        if m.get('QueryPredicates') is not None:
            for k in m.get('QueryPredicates'):
                temp_model = UpdateGatewayRouteRequestPredicatesQueryPredicates()
                self.query_predicates.append(temp_model.from_map(k))
        return self


class UpdateGatewayRouteRequestRedirectJSON(TeaModel):
    def __init__(self, code=None, host=None, path=None):
        self.code = code  # type: int
        self.host = host  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestRedirectJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host is not None:
            result['Host'] = self.host
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class UpdateGatewayRouteRequestServices(TeaModel):
    def __init__(self, group_name=None, name=None, namespace=None, percent=None, service_id=None, source_type=None,
                 version=None):
        self.group_name = group_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.percent = percent  # type: int
        self.service_id = service_id  # type: long
        self.source_type = source_type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRequestServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateGatewayRouteRequest(TeaModel):
    def __init__(self, accept_language=None, destination_type=None, direct_response_json=None,
                 domain_id_list_json=None, gateway_id=None, gateway_unique_id=None, id=None, name=None, predicates=None,
                 redirect_json=None, route_order=None, services=None):
        self.accept_language = accept_language  # type: str
        self.destination_type = destination_type  # type: str
        self.direct_response_json = direct_response_json  # type: UpdateGatewayRouteRequestDirectResponseJSON
        self.domain_id_list_json = domain_id_list_json  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.predicates = predicates  # type: UpdateGatewayRouteRequestPredicates
        self.redirect_json = redirect_json  # type: UpdateGatewayRouteRequestRedirectJSON
        self.route_order = route_order  # type: int
        self.services = services  # type: list[UpdateGatewayRouteRequestServices]

    def validate(self):
        if self.direct_response_json:
            self.direct_response_json.validate()
        if self.predicates:
            self.predicates.validate()
        if self.redirect_json:
            self.redirect_json.validate()
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direct_response_json is not None:
            result['DirectResponseJSON'] = self.direct_response_json.to_map()
        if self.domain_id_list_json is not None:
            result['DomainIdListJSON'] = self.domain_id_list_json
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates is not None:
            result['Predicates'] = self.predicates.to_map()
        if self.redirect_json is not None:
            result['RedirectJSON'] = self.redirect_json.to_map()
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DirectResponseJSON') is not None:
            temp_model = UpdateGatewayRouteRequestDirectResponseJSON()
            self.direct_response_json = temp_model.from_map(m['DirectResponseJSON'])
        if m.get('DomainIdListJSON') is not None:
            self.domain_id_list_json = m.get('DomainIdListJSON')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            temp_model = UpdateGatewayRouteRequestPredicates()
            self.predicates = temp_model.from_map(m['Predicates'])
        if m.get('RedirectJSON') is not None:
            temp_model = UpdateGatewayRouteRequestRedirectJSON()
            self.redirect_json = temp_model.from_map(m['RedirectJSON'])
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = UpdateGatewayRouteRequestServices()
                self.services.append(temp_model.from_map(k))
        return self


class UpdateGatewayRouteShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, destination_type=None, direct_response_jsonshrink=None,
                 domain_id_list_json=None, gateway_id=None, gateway_unique_id=None, id=None, name=None, predicates_shrink=None,
                 redirect_jsonshrink=None, route_order=None, services_shrink=None):
        self.accept_language = accept_language  # type: str
        self.destination_type = destination_type  # type: str
        self.direct_response_jsonshrink = direct_response_jsonshrink  # type: str
        self.domain_id_list_json = domain_id_list_json  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.predicates_shrink = predicates_shrink  # type: str
        self.redirect_jsonshrink = redirect_jsonshrink  # type: str
        self.route_order = route_order  # type: int
        self.services_shrink = services_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direct_response_jsonshrink is not None:
            result['DirectResponseJSON'] = self.direct_response_jsonshrink
        if self.domain_id_list_json is not None:
            result['DomainIdListJSON'] = self.domain_id_list_json
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.predicates_shrink is not None:
            result['Predicates'] = self.predicates_shrink
        if self.redirect_jsonshrink is not None:
            result['RedirectJSON'] = self.redirect_jsonshrink
        if self.route_order is not None:
            result['RouteOrder'] = self.route_order
        if self.services_shrink is not None:
            result['Services'] = self.services_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DirectResponseJSON') is not None:
            self.direct_response_jsonshrink = m.get('DirectResponseJSON')
        if m.get('DomainIdListJSON') is not None:
            self.domain_id_list_json = m.get('DomainIdListJSON')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Predicates') is not None:
            self.predicates_shrink = m.get('Predicates')
        if m.get('RedirectJSON') is not None:
            self.redirect_jsonshrink = m.get('RedirectJSON')
        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')
        if m.get('Services') is not None:
            self.services_shrink = m.get('Services')
        return self


class UpdateGatewayRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteResponse, self).to_map()
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
            temp_model = UpdateGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteCORSRequestCorsJSON(TeaModel):
    def __init__(self, allow_credentials=None, allow_headers=None, allow_methods=None, allow_origins=None,
                 expose_headers=None, status=None, time_unit=None, unit_num=None):
        self.allow_credentials = allow_credentials  # type: bool
        self.allow_headers = allow_headers  # type: str
        self.allow_methods = allow_methods  # type: str
        self.allow_origins = allow_origins  # type: str
        self.expose_headers = expose_headers  # type: str
        self.status = status  # type: str
        self.time_unit = time_unit  # type: str
        self.unit_num = unit_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteCORSRequestCorsJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_credentials is not None:
            result['AllowCredentials'] = self.allow_credentials
        if self.allow_headers is not None:
            result['AllowHeaders'] = self.allow_headers
        if self.allow_methods is not None:
            result['AllowMethods'] = self.allow_methods
        if self.allow_origins is not None:
            result['AllowOrigins'] = self.allow_origins
        if self.expose_headers is not None:
            result['ExposeHeaders'] = self.expose_headers
        if self.status is not None:
            result['Status'] = self.status
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCredentials') is not None:
            self.allow_credentials = m.get('AllowCredentials')
        if m.get('AllowHeaders') is not None:
            self.allow_headers = m.get('AllowHeaders')
        if m.get('AllowMethods') is not None:
            self.allow_methods = m.get('AllowMethods')
        if m.get('AllowOrigins') is not None:
            self.allow_origins = m.get('AllowOrigins')
        if m.get('ExposeHeaders') is not None:
            self.expose_headers = m.get('ExposeHeaders')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class UpdateGatewayRouteCORSRequest(TeaModel):
    def __init__(self, accept_language=None, cors_json=None, gateway_id=None, gateway_unique_id=None, id=None):
        self.accept_language = accept_language  # type: str
        self.cors_json = cors_json  # type: UpdateGatewayRouteCORSRequestCorsJSON
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long

    def validate(self):
        if self.cors_json:
            self.cors_json.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteCORSRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cors_json is not None:
            result['CorsJSON'] = self.cors_json.to_map()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CorsJSON') is not None:
            temp_model = UpdateGatewayRouteCORSRequestCorsJSON()
            self.cors_json = temp_model.from_map(m['CorsJSON'])
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateGatewayRouteCORSShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, cors_jsonshrink=None, gateway_id=None, gateway_unique_id=None, id=None):
        self.accept_language = accept_language  # type: str
        self.cors_jsonshrink = cors_jsonshrink  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteCORSShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cors_jsonshrink is not None:
            result['CorsJSON'] = self.cors_jsonshrink
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CorsJSON') is not None:
            self.cors_jsonshrink = m.get('CorsJSON')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateGatewayRouteCORSResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteCORSResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteCORSResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayRouteCORSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteCORSResponse, self).to_map()
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
            temp_model = UpdateGatewayRouteCORSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteHTTPRewriteRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None, http_rewrite_json=None,
                 id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.http_rewrite_json = http_rewrite_json  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteHTTPRewriteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.http_rewrite_json is not None:
            result['HttpRewriteJSON'] = self.http_rewrite_json
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('HttpRewriteJSON') is not None:
            self.http_rewrite_json = m.get('HttpRewriteJSON')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateGatewayRouteHTTPRewriteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteHTTPRewriteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteHTTPRewriteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayRouteHTTPRewriteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteHTTPRewriteResponse, self).to_map()
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
            temp_model = UpdateGatewayRouteHTTPRewriteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteHeaderOpRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None, header_op_json=None, id=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.header_op_json = header_op_json  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteHeaderOpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.header_op_json is not None:
            result['HeaderOpJSON'] = self.header_op_json
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('HeaderOpJSON') is not None:
            self.header_op_json = m.get('HeaderOpJSON')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateGatewayRouteHeaderOpResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteHeaderOpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteHeaderOpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayRouteHeaderOpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteHeaderOpResponse, self).to_map()
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
            temp_model = UpdateGatewayRouteHeaderOpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteRetryRequestRetryJSON(TeaModel):
    def __init__(self, attempts=None, http_codes=None, retry_on=None, status=None):
        self.attempts = attempts  # type: int
        self.http_codes = http_codes  # type: list[str]
        self.retry_on = retry_on  # type: list[str]
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRetryRequestRetryJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempts is not None:
            result['Attempts'] = self.attempts
        if self.http_codes is not None:
            result['HttpCodes'] = self.http_codes
        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')
        if m.get('HttpCodes') is not None:
            self.http_codes = m.get('HttpCodes')
        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateGatewayRouteRetryRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None, id=None, retry_json=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.retry_json = retry_json  # type: UpdateGatewayRouteRetryRequestRetryJSON

    def validate(self):
        if self.retry_json:
            self.retry_json.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteRetryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.retry_json is not None:
            result['RetryJSON'] = self.retry_json.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RetryJSON') is not None:
            temp_model = UpdateGatewayRouteRetryRequestRetryJSON()
            self.retry_json = temp_model.from_map(m['RetryJSON'])
        return self


class UpdateGatewayRouteRetryShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None, id=None,
                 retry_jsonshrink=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.retry_jsonshrink = retry_jsonshrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRetryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.retry_jsonshrink is not None:
            result['RetryJSON'] = self.retry_jsonshrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RetryJSON') is not None:
            self.retry_jsonshrink = m.get('RetryJSON')
        return self


class UpdateGatewayRouteRetryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteRetryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteRetryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayRouteRetryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteRetryResponse, self).to_map()
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
            temp_model = UpdateGatewayRouteRetryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRouteTimeoutRequestTimeoutJSON(TeaModel):
    def __init__(self, status=None, time_unit=None, unit_num=None):
        self.status = status  # type: str
        self.time_unit = time_unit  # type: str
        self.unit_num = unit_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteTimeoutRequestTimeoutJSON, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class UpdateGatewayRouteTimeoutRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None, id=None, timeout_json=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.timeout_json = timeout_json  # type: UpdateGatewayRouteTimeoutRequestTimeoutJSON

    def validate(self):
        if self.timeout_json:
            self.timeout_json.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteTimeoutRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.timeout_json is not None:
            result['TimeoutJSON'] = self.timeout_json.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TimeoutJSON') is not None:
            temp_model = UpdateGatewayRouteTimeoutRequestTimeoutJSON()
            self.timeout_json = temp_model.from_map(m['TimeoutJSON'])
        return self


class UpdateGatewayRouteTimeoutShrinkRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_id=None, gateway_unique_id=None, id=None,
                 timeout_jsonshrink=None):
        self.accept_language = accept_language  # type: str
        self.gateway_id = gateway_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.id = id  # type: long
        self.timeout_jsonshrink = timeout_jsonshrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteTimeoutShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.id is not None:
            result['Id'] = self.id
        if self.timeout_jsonshrink is not None:
            result['TimeoutJSON'] = self.timeout_jsonshrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TimeoutJSON') is not None:
            self.timeout_jsonshrink = m.get('TimeoutJSON')
        return self


class UpdateGatewayRouteTimeoutResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayRouteTimeoutResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayRouteTimeoutResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayRouteTimeoutResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayRouteTimeoutResponse, self).to_map()
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
            temp_model = UpdateGatewayRouteTimeoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayServiceVersionRequest(TeaModel):
    def __init__(self, accept_language=None, gateway_unique_id=None, service_id=None, service_version=None):
        self.accept_language = accept_language  # type: str
        self.gateway_unique_id = gateway_unique_id  # type: str
        self.service_id = service_id  # type: long
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayServiceVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class UpdateGatewayServiceVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGatewayServiceVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGatewayServiceVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateGatewayServiceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGatewayServiceVersionResponse, self).to_map()
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
            temp_model = UpdateGatewayServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, version_code=None):
        self.accept_language = accept_language  # type: str
        # 目标集群的id
        self.cluster_id = cluster_id  # type: str
        # 想修改的镜像版本code
        self.version_code = version_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateImageResponse, self).to_map()
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
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosClusterRequest(TeaModel):
    def __init__(self, accept_language=None, check_port=None, cluster_name=None, group_name=None,
                 health_checker=None, instance_id=None, namespace_id=None, service_name=None, use_instance_port_for_check=None):
        self.accept_language = accept_language  # type: str
        # 健康检查端口
        self.check_port = check_port  # type: int
        # Nacos集群名
        self.cluster_name = cluster_name  # type: str
        # 分组名
        self.group_name = group_name  # type: str
        # 健康检查类型
        self.health_checker = health_checker  # type: str
        # 实例id
        self.instance_id = instance_id  # type: str
        # 命名空间id
        self.namespace_id = namespace_id  # type: str
        # 服务名
        self.service_name = service_name  # type: str
        # 是否使用实例端口进行健康检查
        self.use_instance_port_for_check = use_instance_port_for_check  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.check_port is not None:
            result['CheckPort'] = self.check_port
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.health_checker is not None:
            result['HealthChecker'] = self.health_checker
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.use_instance_port_for_check is not None:
            result['UseInstancePortForCheck'] = self.use_instance_port_for_check
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CheckPort') is not None:
            self.check_port = m.get('CheckPort')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HealthChecker') is not None:
            self.health_checker = m.get('HealthChecker')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('UseInstancePortForCheck') is not None:
            self.use_instance_port_for_check = m.get('UseInstancePortForCheck')
        return self


class UpdateNacosClusterResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        # 响应码
        self.code = code  # type: int
        # 修改结果
        self.data = data  # type: str
        # http状态码
        self.http_status_code = http_status_code  # type: int
        # 响应信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 成功标志
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateNacosClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNacosClusterResponse, self).to_map()
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
            temp_model = UpdateNacosClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosConfigRequest(TeaModel):
    def __init__(self, accept_language=None, app_name=None, beta_ips=None, content=None, data_id=None, desc=None,
                 encrypted_data_key=None, group=None, instance_id=None, md_5=None, namespace_id=None, tags=None, type=None):
        self.accept_language = accept_language  # type: str
        self.app_name = app_name  # type: str
        self.beta_ips = beta_ips  # type: str
        self.content = content  # type: str
        self.data_id = data_id  # type: str
        self.desc = desc  # type: str
        self.encrypted_data_key = encrypted_data_key  # type: str
        self.group = group  # type: str
        self.instance_id = instance_id  # type: str
        self.md_5 = md_5  # type: str
        self.namespace_id = namespace_id  # type: str
        self.tags = tags  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.beta_ips is not None:
            result['BetaIps'] = self.beta_ips
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.encrypted_data_key is not None:
            result['EncryptedDataKey'] = self.encrypted_data_key
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BetaIps') is not None:
            self.beta_ips = m.get('BetaIps')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('EncryptedDataKey') is not None:
            self.encrypted_data_key = m.get('EncryptedDataKey')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateNacosConfigResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateNacosConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNacosConfigResponse, self).to_map()
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
            temp_model = UpdateNacosConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosInstanceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_name=None, enabled=None, ephemeral=None, group_name=None,
                 instance_id=None, ip=None, metadata=None, namespace_id=None, port=None, service_name=None, weight=None):
        self.accept_language = accept_language  # type: str
        # Nacos集群名
        self.cluster_name = cluster_name  # type: str
        # 服务禁用标志
        self.enabled = enabled  # type: bool
        # 临时节点标志
        self.ephemeral = ephemeral  # type: bool
        # 分组名
        self.group_name = group_name  # type: str
        # 实例id
        self.instance_id = instance_id  # type: str
        # Nacos实例ip
        self.ip = ip  # type: str
        # 节点元数据
        self.metadata = metadata  # type: str
        # 命名空间id
        self.namespace_id = namespace_id  # type: str
        # Nacos实例端口
        self.port = port  # type: int
        # 服务名
        self.service_name = service_name  # type: str
        # 权重
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.port is not None:
            result['Port'] = self.port
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateNacosInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        # 响应码
        self.code = code  # type: int
        # 修改结果
        self.data = data  # type: str
        # http状态码
        self.http_status_code = http_status_code  # type: int
        # 响应信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 成功标志
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateNacosInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNacosInstanceResponse, self).to_map()
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
            temp_model = UpdateNacosInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNacosServiceRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, group_name=None, instance_id=None, namespace_id=None,
                 protect_threshold=None, service_name=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.protect_threshold = protect_threshold  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateNacosServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNacosServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNacosServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateNacosServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNacosServiceResponse, self).to_map()
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
            temp_model = UpdateNacosServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSSLCertRequest(TeaModel):
    def __init__(self, accept_language=None, cert_identifier=None, domain_id=None, gateway_unique_id=None):
        self.accept_language = accept_language  # type: str
        self.cert_identifier = cert_identifier  # type: str
        self.domain_id = domain_id  # type: long
        self.gateway_unique_id = gateway_unique_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSSLCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')
        return self


class UpdateSSLCertResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSSLCertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSSLCertResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSSLCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSSLCertResponse, self).to_map()
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
            temp_model = UpdateSSLCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZnodeRequest(TeaModel):
    def __init__(self, accept_language=None, cluster_id=None, data=None, path=None, request_pars=None):
        self.accept_language = accept_language  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data = data  # type: str
        self.path = path  # type: str
        self.request_pars = request_pars  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateZnodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data is not None:
            result['Data'] = self.data
        if self.path is not None:
            result['Path'] = self.path
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        return self


class UpdateZnodeResponseBody(TeaModel):
    def __init__(self, error_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateZnodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateZnodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateZnodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateZnodeResponse, self).to_map()
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
            temp_model = UpdateZnodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(self, accept_language=None, instance_id=None, request_pars=None, upgrade_version=None):
        self.accept_language = accept_language  # type: str
        self.instance_id = instance_id  # type: str
        self.request_pars = request_pars  # type: str
        self.upgrade_version = upgrade_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars
        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')
        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')
        return self


class UpgradeClusterResponseBody(TeaModel):
    def __init__(self, error_code=None, http_code=None, message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.http_code = http_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeClusterResponse, self).to_map()
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
            temp_model = UpgradeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


