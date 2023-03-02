# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mse20190531 import models as mse_20190531_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('mse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_auth_resource_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.AddAuthResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_resource_header_list):
            request.auth_resource_header_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_resource_header_list, 'AuthResourceHeaderList', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.auth_id):
            query['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.auth_resource_header_list_shrink):
            query['AuthResourceHeaderList'] = request.auth_resource_header_list_shrink
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.ignore_case):
            query['IgnoreCase'] = request.ignore_case
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAuthResource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddAuthResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_auth_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_auth_resource_with_options(request, runtime)

    def add_black_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.is_white):
            query['IsWhite'] = request.is_white
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.resource_id_json_list):
            query['ResourceIdJsonList'] = request.resource_id_json_list
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlackWhiteList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_black_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_black_white_list_with_options(request, runtime)

    def add_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.enable_hardware_acceleration):
            query['EnableHardwareAcceleration'] = request.enable_hardware_acceleration
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.enable_xtrace):
            query['EnableXtrace'] = request.enable_xtrace
        if not UtilClient.is_unset(request.enterprise_security_group):
            query['EnterpriseSecurityGroup'] = request.enterprise_security_group
        if not UtilClient.is_unset(request.internet_slb_spec):
            query['InternetSlbSpec'] = request.internet_slb_spec
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.replica):
            query['Replica'] = request.replica
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.slb_spec):
            query['SlbSpec'] = request.slb_spec
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_id_2):
            query['VSwitchId2'] = request.v_switch_id_2
        if not UtilClient.is_unset(request.vpc):
            query['Vpc'] = request.vpc
        if not UtilClient.is_unset(request.xtrace_ratio):
            query['XtraceRatio'] = request.xtrace_ratio
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gateway_with_options(request, runtime)

    def add_gateway_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.http_2):
            query['Http2'] = request.http_2
        if not UtilClient.is_unset(request.must_https):
            query['MustHttps'] = request.must_https
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_max):
            query['TlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            query['TlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGatewayDomain',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gateway_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gateway_domain_with_options(request, runtime)

    def add_gateway_route_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.AddGatewayRouteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.direct_response_json):
            request.direct_response_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.direct_response_json, 'DirectResponseJSON', 'json')
        if not UtilClient.is_unset(tmp_req.fallback_services):
            request.fallback_services_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fallback_services, 'FallbackServices', 'json')
        if not UtilClient.is_unset(tmp_req.predicates):
            request.predicates_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.predicates, 'Predicates', 'json')
        if not UtilClient.is_unset(tmp_req.redirect_json):
            request.redirect_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect_json, 'RedirectJSON', 'json')
        if not UtilClient.is_unset(tmp_req.services):
            request.services_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.services, 'Services', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.direct_response_jsonshrink):
            query['DirectResponseJSON'] = request.direct_response_jsonshrink
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_id_list_json):
            query['DomainIdListJSON'] = request.domain_id_list_json
        if not UtilClient.is_unset(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not UtilClient.is_unset(request.fallback):
            query['Fallback'] = request.fallback
        if not UtilClient.is_unset(request.fallback_services_shrink):
            query['FallbackServices'] = request.fallback_services_shrink
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policies):
            query['Policies'] = request.policies
        if not UtilClient.is_unset(request.predicates_shrink):
            query['Predicates'] = request.predicates_shrink
        if not UtilClient.is_unset(request.redirect_jsonshrink):
            query['RedirectJSON'] = request.redirect_jsonshrink
        if not UtilClient.is_unset(request.route_order):
            query['RouteOrder'] = request.route_order
        if not UtilClient.is_unset(request.route_type):
            query['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.services_shrink):
            query['Services'] = request.services_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGatewayRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gateway_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gateway_route_with_options(request, runtime)

    def add_gateway_service_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGatewayServiceVersion',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gateway_service_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gateway_service_version_with_options(request, runtime)

    def add_gateway_slb_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_vserver_group_id):
            query['HttpsVServerGroupId'] = request.https_vserver_group_id
        if not UtilClient.is_unset(request.service_weight):
            query['ServiceWeight'] = request.service_weight
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGatewaySlb',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    def add_gateway_slb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_gateway_slb_with_options(request, runtime)

    def add_migration_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.origin_instance_address):
            query['OriginInstanceAddress'] = request.origin_instance_address
        if not UtilClient.is_unset(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not UtilClient.is_unset(request.origin_instance_namespace):
            query['OriginInstanceNamespace'] = request.origin_instance_namespace
        if not UtilClient.is_unset(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.target_cluster_name):
            query['TargetClusterName'] = request.target_cluster_name
        if not UtilClient.is_unset(request.target_cluster_url):
            query['TargetClusterUrl'] = request.target_cluster_url
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMigrationTask',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def add_migration_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_migration_task_with_options(request, runtime)

    def add_mock_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.consumer_app_ids):
            query['ConsumerAppIds'] = request.consumer_app_ids
        if not UtilClient.is_unset(request.dubbo_mock_items):
            query['DubboMockItems'] = request.dubbo_mock_items
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.extra_json):
            query['ExtraJson'] = request.extra_json
        if not UtilClient.is_unset(request.mock_type):
            query['MockType'] = request.mock_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.provider_app_id):
            query['ProviderAppId'] = request.provider_app_id
        if not UtilClient.is_unset(request.provider_app_name):
            query['ProviderAppName'] = request.provider_app_name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sc_mock_items):
            query['ScMockItems'] = request.sc_mock_items
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMockRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMockRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_mock_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mock_rule_with_options(request, runtime)

    def add_sslcert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSSLCert',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddSSLCertResponse(),
            self.call_api(params, req, runtime)
        )

    def add_sslcert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_sslcert_with_options(request, runtime)

    def add_security_group_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSecurityGroupRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_security_group_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_security_group_rule_with_options(request, runtime)

    def add_service_source_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.AddServiceSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_list):
            request.group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_list, 'GroupList', 'json')
        if not UtilClient.is_unset(tmp_req.ingress_options_request):
            request.ingress_options_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ingress_options_request, 'IngressOptionsRequest', 'json')
        if not UtilClient.is_unset(tmp_req.path_list):
            request.path_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.path_list, 'PathList', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.group_list_shrink):
            query['GroupList'] = request.group_list_shrink
        if not UtilClient.is_unset(request.ingress_options_request_shrink):
            query['IngressOptionsRequest'] = request.ingress_options_request_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.path_list_shrink):
            query['PathList'] = request.path_list_shrink
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServiceSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_service_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_service_source_with_options(request, runtime)

    def apply_gateway_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyGatewayRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ApplyGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_gateway_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_gateway_route_with_options(request, runtime)

    def apply_tag_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyTagPolicies',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ApplyTagPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_tag_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_tag_policies_with_options(request, runtime)

    def clone_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CloneNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CloneNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.origin_namespace_id):
            query['OriginNamespaceId'] = request.origin_namespace_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.target_namespace_id):
            query['TargetNamespaceId'] = request.target_namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CloneNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CloneNacosConfigRequest

        @return: CloneNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clone_nacos_config_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        """
        Before you call this API operation, you must make sure that you fully understand the billing method and pricing of MSE.
        

        @param request: CreateClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_specification):
            query['ClusterSpecification'] = request.cluster_specification
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['ClusterVersion'] = request.cluster_version
        if not UtilClient.is_unset(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.private_slb_specification):
            query['PrivateSlbSpecification'] = request.private_slb_specification
        if not UtilClient.is_unset(request.pub_network_flow):
            query['PubNetworkFlow'] = request.pub_network_flow
        if not UtilClient.is_unset(request.pub_slb_specification):
            query['PubSlbSpecification'] = request.pub_slb_specification
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        """
        Before you call this API operation, you must make sure that you fully understand the billing method and pricing of MSE.
        

        @param request: CreateClusterRequest

        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_engine_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_count):
            query['ServiceCount'] = request.service_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_engine_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_engine_namespace_with_options(request, runtime)

    def create_mse_service_application_with_options(self, request, runtime):
        """
        @deprecated : CreateMseServiceApplication is deprecated, please use mse::2019-05-31::CreateApplication instead.
        

        @param request: CreateMseServiceApplicationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMseServiceApplicationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMseServiceApplication',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateMseServiceApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mse_service_application(self, request):
        """
        @deprecated : CreateMseServiceApplication is deprecated, please use mse::2019-05-31::CreateApplication instead.
        

        @param request: CreateMseServiceApplicationRequest

        @return: CreateMseServiceApplicationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mse_service_application_with_options(request, runtime)

    def create_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CreateNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.beta_ips):
            query['BetaIps'] = request.beta_ips
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CreateNacosConfigRequest

        @return: CreateNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_nacos_config_with_options(request, runtime)

    def create_nacos_instance_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CreateNacosInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNacosInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        body = {}
        if not UtilClient.is_unset(request.metadata):
            body['Metadata'] = request.metadata
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNacosInstance',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_nacos_instance(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CreateNacosInstanceRequest

        @return: CreateNacosInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_nacos_instance_with_options(request, runtime)

    def create_nacos_service_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CreateNacosServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNacosServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.protect_threshold):
            query['ProtectThreshold'] = request.protect_threshold
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNacosService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_nacos_service(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: CreateNacosServiceRequest

        @return: CreateNacosServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_nacos_service_with_options(request, runtime)

    def create_or_update_swimming_lane_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.CreateOrUpdateSwimmingLaneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_swimming_lane_route_json):
            request.gateway_swimming_lane_route_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_swimming_lane_route_json, 'GatewaySwimmingLaneRouteJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not UtilClient.is_unset(request.entry_rule):
            query['EntryRule'] = request.entry_rule
        if not UtilClient.is_unset(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not UtilClient.is_unset(request.gateway_swimming_lane_route_json_shrink):
            query['GatewaySwimmingLaneRouteJson'] = request.gateway_swimming_lane_route_json_shrink
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.license_key):
            query['LicenseKey'] = request.license_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateSwimmingLane',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateOrUpdateSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_swimming_lane(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_swimming_lane_with_options(request, runtime)

    def create_or_update_swimming_lane_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.db_gray_enable):
            query['DbGrayEnable'] = request.db_gray_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.license_key):
            query['LicenseKey'] = request.license_key
        if not UtilClient.is_unset(request.message_queue_filter_side):
            query['MessageQueueFilterSide'] = request.message_queue_filter_side
        if not UtilClient.is_unset(request.message_queue_gray_enable):
            query['MessageQueueGrayEnable'] = request.message_queue_gray_enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateSwimmingLaneGroup',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateOrUpdateSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_swimming_lane_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_swimming_lane_group_with_options(request, runtime)

    def create_znode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_znode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_znode_with_options(request, runtime)

    def delete_auth_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthResource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteAuthResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auth_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auth_resource_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def delete_engine_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_engine_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_engine_namespace_with_options(request, runtime)

    def delete_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.delete_slb):
            query['DeleteSlb'] = request.delete_slb
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_with_options(request, runtime)

    def delete_gateway_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayDomain',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gateway_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_domain_with_options(request, runtime)

    def delete_gateway_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gateway_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_route_with_options(request, runtime)

    def delete_gateway_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gateway_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_service_with_options(request, runtime)

    def delete_gateway_service_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewayServiceVersion',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gateway_service_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_service_version_with_options(request, runtime)

    def delete_gateway_slb_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.delete_slb):
            query['DeleteSlb'] = request.delete_slb
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySlb',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gateway_slb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_slb_with_options(request, runtime)

    def delete_migration_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationTask',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_migration_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_task_with_options(request, runtime)

    def delete_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.beta):
            query['Beta'] = request.beta
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosConfigRequest

        @return: DeleteNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_config_with_options(request, runtime)

    def delete_nacos_configs_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNacosConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNacosConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nacos_configs(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosConfigsRequest

        @return: DeleteNacosConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_configs_with_options(request, runtime)

    def delete_nacos_instance_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNacosInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNacosInstance',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nacos_instance(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosInstanceRequest

        @return: DeleteNacosInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_instance_with_options(request, runtime)

    def delete_nacos_service_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNacosServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNacosService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nacos_service(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: DeleteNacosServiceRequest

        @return: DeleteNacosServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_service_with_options(request, runtime)

    def delete_security_group_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroupRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_security_group_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_rule_with_options(request, runtime)

    def delete_service_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_source_with_options(request, runtime)

    def delete_swimming_lane_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.lane_id):
            query['LaneId'] = request.lane_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSwimmingLane',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_swimming_lane(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_swimming_lane_with_options(request, runtime)

    def delete_swimming_lane_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSwimmingLaneGroup',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_swimming_lane_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_swimming_lane_group_with_options(request, runtime)

    def delete_znode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_znode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_znode_with_options(request, runtime)

    def export_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ExportNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def export_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ExportNacosConfigRequest

        @return: ExportNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_nacos_config_with_options(request, runtime)

    def export_zookeeper_data_with_options(self, request, runtime):
        """
        Only one task can run at a time.
        

        @param request: ExportZookeeperDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportZookeeperDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportZookeeperData',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportZookeeperDataResponse(),
            self.call_api(params, req, runtime)
        )

    def export_zookeeper_data(self, request):
        """
        Only one task can run at a time.
        

        @param request: ExportZookeeperDataRequest

        @return: ExportZookeeperDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_zookeeper_data_with_options(request, runtime)

    def fetch_lossless_rule_list_with_options(self, request, runtime):
        """
        You can call this operation to query the rules for graceful start and shutdown.
        

        @param request: FetchLosslessRuleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: FetchLosslessRuleListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchLosslessRuleList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.FetchLosslessRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def fetch_lossless_rule_list(self, request):
        """
        You can call this operation to query the rules for graceful start and shutdown.
        

        @param request: FetchLosslessRuleListRequest

        @return: FetchLosslessRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_lossless_rule_list_with_options(request, runtime)

    def get_app_message_queue_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppMessageQueueRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetAppMessageQueueRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_message_queue_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_message_queue_route_with_options(request, runtime)

    def get_application_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sentinel_enable):
            query['SentinelEnable'] = request.sentinel_enable
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.switch_enable):
            query['SwitchEnable'] = request.switch_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetApplicationListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_list_with_options(request, runtime)

    def get_application_list_with_metircs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationListWithMetircs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetApplicationListWithMetircsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_list_with_metircs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_list_with_metircs_with_options(request, runtime)

    def get_black_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.is_white):
            query['IsWhite'] = request.is_white
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBlackWhiteList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_black_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_black_white_list_with_options(request, runtime)

    def get_engine_namepace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEngineNamepace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetEngineNamepaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_engine_namepace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_engine_namepace_with_options(request, runtime)

    def get_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_with_options(request, runtime)

    def get_gateway_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGatewayDomainDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gateway_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_domain_detail_with_options(request, runtime)

    def get_gateway_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGatewayOption',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gateway_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_option_with_options(request, runtime)

    def get_gateway_route_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGatewayRouteDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayRouteDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gateway_route_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_route_detail_with_options(request, runtime)

    def get_gateway_service_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGatewayServiceDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gateway_service_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_service_detail_with_options(request, runtime)

    def get_governance_kubernetes_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_governance_kubernetes_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_governance_kubernetes_cluster_with_options(request, runtime)

    def get_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    def get_import_file_url_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: GetImportFileUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetImportFileUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImportFileUrl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_import_file_url(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: GetImportFileUrlRequest

        @return: GetImportFileUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_import_file_url_with_options(request, runtime)

    def get_kubernetes_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKubernetesSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetKubernetesSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_kubernetes_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_kubernetes_source_with_options(request, runtime)

    def get_mse_feature_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMseFeatureSwitch',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetMseFeatureSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mse_feature_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mse_feature_switch_with_options(request, runtime)

    def get_mse_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMseSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetMseSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mse_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mse_source_with_options(request, runtime)

    def get_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: GetNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.beta):
            query['Beta'] = request.beta
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: GetNacosConfigRequest

        @return: GetNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_nacos_config_with_options(request, runtime)

    def get_nacos_history_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: GetNacosHistoryConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNacosHistoryConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nid):
            query['Nid'] = request.nid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNacosHistoryConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosHistoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_nacos_history_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: GetNacosHistoryConfigRequest

        @return: GetNacosHistoryConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_nacos_history_config_with_options(request, runtime)

    def get_overview_with_options(self, request, runtime):
        """
        You can call the GetOverview operation to query overview information about service governance.
        

        @param request: GetOverviewRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOverview',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_overview(self, request):
        """
        You can call the GetOverview operation to query overview information about service governance.
        

        @param request: GetOverviewRequest

        @return: GetOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_overview_with_options(request, runtime)

    def get_plugin_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPluginConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetPluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_plugin_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_plugin_config_with_options(request, runtime)

    def get_plugins_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable_only):
            query['EnableOnly'] = request.enable_only
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPlugins',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_plugins(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_plugins_with_options(request, runtime)

    def get_service_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_list_with_options(request, runtime)

    def get_service_listeners_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.has_ip_count):
            query['HasIpCount'] = request.has_ip_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceListeners',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetServiceListenersResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_listeners(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_listeners_with_options(request, runtime)

    def get_tags_by_swimming_lane_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagsBySwimmingLaneGroupId',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetTagsBySwimmingLaneGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tags_by_swimming_lane_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_tags_by_swimming_lane_group_id_with_options(request, runtime)

    def get_zookeeper_data_import_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetZookeeperDataImportUrl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetZookeeperDataImportUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_zookeeper_data_import_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_zookeeper_data_import_url_with_options(request, runtime)

    def import_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ImportNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def import_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ImportNacosConfigRequest

        @return: ImportNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_nacos_config_with_options(request, runtime)

    def import_services_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.ImportServicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.service_list):
            request.service_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_list, 'ServiceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_list_shrink):
            query['ServiceList'] = request.service_list_shrink
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.tls_setting):
            query['TlsSetting'] = request.tls_setting
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_services_with_options(request, runtime)

    def import_zookeeper_data_with_options(self, request, runtime):
        """
        *\
        **Danger** This operation clears existing data. Exercise caution when you call this API operation.
        

        @param request: ImportZookeeperDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportZookeeperDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportZookeeperData',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportZookeeperDataResponse(),
            self.call_api(params, req, runtime)
        )

    def import_zookeeper_data(self, request):
        """
        *\
        **Danger** This operation clears existing data. Exercise caution when you call this API operation.
        

        @param request: ImportZookeeperDataRequest

        @return: ImportZookeeperDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_zookeeper_data_with_options(request, runtime)

    def list_ans_instances_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListAnsInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAnsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsInstances',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ans_instances(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListAnsInstancesRequest

        @return: ListAnsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ans_instances_with_options(request, runtime)

    def list_ans_service_clusters_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListAnsServiceClustersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAnsServiceClustersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsServiceClusters',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServiceClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ans_service_clusters(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListAnsServiceClustersRequest

        @return: ListAnsServiceClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ans_service_clusters_with_options(request, runtime)

    def list_ans_services_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListAnsServicesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAnsServicesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ans_services(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListAnsServicesRequest

        @return: ListAnsServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ans_services_with_options(request, runtime)

    def list_app_by_swimming_lane_group_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppBySwimmingLaneGroupTag',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAppBySwimmingLaneGroupTagResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_by_swimming_lane_group_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_by_swimming_lane_group_tag_with_options(request, runtime)

    def list_applications_with_tag_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsWithTagRules',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListApplicationsWithTagRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications_with_tag_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_tag_rules_with_options(request, runtime)

    def list_cluster_connection_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterConnectionTypes',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterConnectionTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_connection_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_connection_types_with_options(request, runtime)

    def list_cluster_health_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterHealthCheckTask',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterHealthCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_health_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_health_check_task_with_options(request, runtime)

    def list_cluster_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterTypes',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_types_with_options(request, runtime)

    def list_cluster_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterVersions',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_versions_with_options(request, runtime)

    def list_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def list_config_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigTrack',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListConfigTrackResponse(),
            self.call_api(params, req, runtime)
        )

    def list_config_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_config_track_with_options(request, runtime)

    def list_engine_namespaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEngineNamespaces',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEngineNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_engine_namespaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_engine_namespaces_with_options(request, runtime)

    def list_eureka_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEurekaInstances',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_eureka_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_eureka_instances_with_options(request, runtime)

    def list_eureka_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEurekaServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_eureka_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_eureka_services_with_options(request, runtime)

    def list_export_zookeeper_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExportZookeeperData',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListExportZookeeperDataResponse(),
            self.call_api(params, req, runtime)
        )

    def list_export_zookeeper_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_export_zookeeper_data_with_options(request, runtime)

    def list_gateway_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.ListGatewayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_params):
            request.filter_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not UtilClient.is_unset(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not UtilClient.is_unset(request.order_item):
            query['OrderItem'] = request.order_item
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def list_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_with_options(request, runtime)

    def list_gateway_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayDomain',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def list_gateway_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_domain_with_options(request, runtime)

    def list_gateway_route_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.ListGatewayRouteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_params):
            request.filter_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not UtilClient.is_unset(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not UtilClient.is_unset(request.order_item):
            query['OrderItem'] = request.order_item
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def list_gateway_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_route_with_options(request, runtime)

    def list_gateway_service_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.ListGatewayServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_params):
            request.filter_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_params, 'FilterParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.desc_sort):
            query['DescSort'] = request.desc_sort
        if not UtilClient.is_unset(request.filter_params_shrink):
            query['FilterParams'] = request.filter_params_shrink
        if not UtilClient.is_unset(request.order_item):
            query['OrderItem'] = request.order_item
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewayService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_gateway_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_service_with_options(request, runtime)

    def list_gateway_slb_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGatewaySlb',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    def list_gateway_slb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_slb_with_options(request, runtime)

    def list_instance_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceCount',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListInstanceCountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_count_with_options(request, runtime)

    def list_listeners_by_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListListenersByConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListListenersByConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenersByConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_listeners_by_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListListenersByConfigRequest

        @return: ListListenersByConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_by_config_with_options(request, runtime)

    def list_listeners_by_ip_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListListenersByIpRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListListenersByIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenersByIp',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByIpResponse(),
            self.call_api(params, req, runtime)
        )

    def list_listeners_by_ip(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListListenersByIpRequest

        @return: ListListenersByIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_by_ip_with_options(request, runtime)

    def list_migration_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMigrationTask',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_migration_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_migration_task_with_options(request, runtime)

    def list_nacos_configs_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListNacosConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNacosConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNacosConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nacos_configs(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListNacosConfigsRequest

        @return: ListNacosConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nacos_configs_with_options(request, runtime)

    def list_nacos_history_configs_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListNacosHistoryConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNacosHistoryConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNacosHistoryConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosHistoryConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nacos_history_configs(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: ListNacosHistoryConfigsRequest

        @return: ListNacosHistoryConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nacos_history_configs_with_options(request, runtime)

    def list_naming_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamingTrack',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNamingTrackResponse(),
            self.call_api(params, req, runtime)
        )

    def list_naming_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_naming_track_with_options(request, runtime)

    def list_sslcert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSSLCert',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListSSLCertResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sslcert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sslcert_with_options(request, runtime)

    def list_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityGroup',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_security_group_with_options(request, runtime)

    def list_security_group_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityGroupRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_security_group_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_security_group_rule_with_options(request, runtime)

    def list_service_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_source_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_zk_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZkTrack',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZkTrackResponse(),
            self.call_api(params, req, runtime)
        )

    def list_zk_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_zk_track_with_options(request, runtime)

    def list_znode_children_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZnodeChildren',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZnodeChildrenResponse(),
            self.call_api(params, req, runtime)
        )

    def list_znode_children(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_znode_children_with_options(request, runtime)

    def modify_governance_kubernetes_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace_infos):
            query['NamespaceInfos'] = request.namespace_infos
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ModifyGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_governance_kubernetes_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_governance_kubernetes_cluster_with_options(request, runtime)

    def modify_lossless_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.aligned):
            query['Aligned'] = request.aligned
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.delay_time):
            query['DelayTime'] = request.delay_time
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.func_type):
            query['FuncType'] = request.func_type
        if not UtilClient.is_unset(request.loss_less_detail):
            query['LossLessDetail'] = request.loss_less_detail
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.notice):
            query['Notice'] = request.notice
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.related):
            query['Related'] = request.related
        if not UtilClient.is_unset(request.shutdown_wait_seconds):
            query['ShutdownWaitSeconds'] = request.shutdown_wait_seconds
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.warmup_time):
            query['WarmupTime'] = request.warmup_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLosslessRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ModifyLosslessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_lossless_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_lossless_rule_with_options(request, runtime)

    def offline_gateway_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OfflineGatewayRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.OfflineGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def offline_gateway_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.offline_gateway_route_with_options(request, runtime)

    def order_cluster_health_check_risk_notice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mute):
            query['Mute'] = request.mute
        if not UtilClient.is_unset(request.notice_type):
            query['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.risk_code):
            query['RiskCode'] = request.risk_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderClusterHealthCheckRiskNotice',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.OrderClusterHealthCheckRiskNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def order_cluster_health_check_risk_notice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.order_cluster_health_check_risk_notice_with_options(request, runtime)

    def pull_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.PullServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def pull_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pull_services_with_options(request, runtime)

    def put_cluster_health_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutClusterHealthCheckTask',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.PutClusterHealthCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def put_cluster_health_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_cluster_health_check_task_with_options(request, runtime)

    def query_all_swimming_lane_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllSwimmingLane',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryAllSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    def query_all_swimming_lane(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_all_swimming_lane_with_options(request, runtime)

    def query_all_swimming_lane_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllSwimmingLaneGroup',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryAllSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_all_swimming_lane_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_all_swimming_lane_group_with_options(request, runtime)

    def query_business_locations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBusinessLocations',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryBusinessLocationsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_business_locations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_business_locations_with_options(request, runtime)

    def query_cluster_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.acl_switch):
            query['AclSwitch'] = request.acl_switch
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cluster_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_detail_with_options(request, runtime)

    def query_cluster_disk_specification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterDiskSpecification',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDiskSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cluster_disk_specification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_disk_specification_with_options(request, runtime)

    def query_cluster_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.acl_switch):
            query['AclSwitch'] = request.acl_switch
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterInfo',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cluster_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_info_with_options(request, runtime)

    def query_cluster_specification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterSpecification',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cluster_specification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_specification_with_options(request, runtime)

    def query_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def query_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_config_with_options(request, runtime)

    def query_gateway_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGatewayRegion',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_gateway_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_gateway_region_with_options(request, runtime)

    def query_gateway_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGatewayType',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_gateway_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_gateway_type_with_options(request, runtime)

    def query_governance_kubernetes_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def query_governance_kubernetes_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_governance_kubernetes_cluster_with_options(request, runtime)

    def query_instances_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstancesInfo',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryInstancesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_instances_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_instances_info_with_options(request, runtime)

    def query_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonitor',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def query_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monitor_with_options(request, runtime)

    def query_slb_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlbSpec',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QuerySlbSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def query_slb_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_slb_spec_with_options(request, runtime)

    def query_swimming_lane_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.lane_id):
            query['LaneId'] = request.lane_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySwimmingLaneById',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QuerySwimmingLaneByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_swimming_lane_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_swimming_lane_by_id_with_options(request, runtime)

    def query_znode_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryZnodeDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryZnodeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_znode_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_znode_detail_with_options(request, runtime)

    def restart_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pod_name_list):
            query['PodNameList'] = request.pod_name_list
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.RestartClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_cluster_with_options(request, runtime)

    def retry_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.RetryClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_cluster_with_options(request, runtime)

    def select_gateway_slb_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SelectGatewaySlb',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.SelectGatewaySlbResponse(),
            self.call_api(params, req, runtime)
        )

    def select_gateway_slb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.select_gateway_slb_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.acl_entry_list):
            query['AclEntryList'] = request.acl_entry_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAcl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateAclResponse(),
            self.call_api(params, req, runtime)
        )

    def update_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_acl_with_options(request, runtime)

    def update_black_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.is_white):
            query['IsWhite'] = request.is_white
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.resource_id_json_list):
            query['ResourceIdJsonList'] = request.resource_id_json_list
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBlackWhiteList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateBlackWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def update_black_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_black_white_list_with_options(request, runtime)

    def update_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_alias_name):
            query['ClusterAliasName'] = request.cluster_alias_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    def update_cluster_spec_with_options(self, request, runtime):
        """
        You can call this operation to update the number or specifications of nodes in a pay-as-you-go MSE instance. You are charged when you add nodes or upgrade node specifications. For more information, see \\[Pricing] (`~~1806469~~`).
        

        @param request: UpdateClusterSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateClusterSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_specification):
            query['ClusterSpecification'] = request.cluster_specification
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mse_version):
            query['MseVersion'] = request.mse_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterSpec',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster_spec(self, request):
        """
        You can call this operation to update the number or specifications of nodes in a pay-as-you-go MSE instance. You are charged when you add nodes or upgrade node specifications. For more information, see \\[Pricing] (`~~1806469~~`).
        

        @param request: UpdateClusterSpecRequest

        @return: UpdateClusterSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_spec_with_options(request, runtime)

    def update_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.autopurge_purge_interval):
            query['AutopurgePurgeInterval'] = request.autopurge_purge_interval
        if not UtilClient.is_unset(request.autopurge_snap_retain_count):
            query['AutopurgeSnapRetainCount'] = request.autopurge_snap_retain_count
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_auth_enabled):
            query['ConfigAuthEnabled'] = request.config_auth_enabled
        if not UtilClient.is_unset(request.config_secret_enabled):
            query['ConfigSecretEnabled'] = request.config_secret_enabled
        if not UtilClient.is_unset(request.config_type):
            query['ConfigType'] = request.config_type
        if not UtilClient.is_unset(request.eureka_supported):
            query['EurekaSupported'] = request.eureka_supported
        if not UtilClient.is_unset(request.extended_types_enable):
            query['ExtendedTypesEnable'] = request.extended_types_enable
        if not UtilClient.is_unset(request.init_limit):
            query['InitLimit'] = request.init_limit
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.jute_maxbuffer):
            query['JuteMaxbuffer'] = request.jute_maxbuffer
        if not UtilClient.is_unset(request.mcpenabled):
            query['MCPEnabled'] = request.mcpenabled
        if not UtilClient.is_unset(request.max_client_cnxns):
            query['MaxClientCnxns'] = request.max_client_cnxns
        if not UtilClient.is_unset(request.max_session_timeout):
            query['MaxSessionTimeout'] = request.max_session_timeout
        if not UtilClient.is_unset(request.min_session_timeout):
            query['MinSessionTimeout'] = request.min_session_timeout
        if not UtilClient.is_unset(request.naming_auth_enabled):
            query['NamingAuthEnabled'] = request.naming_auth_enabled
        if not UtilClient.is_unset(request.pass_word):
            query['PassWord'] = request.pass_word
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.snapshot_count):
            query['SnapshotCount'] = request.snapshot_count
        if not UtilClient.is_unset(request.sync_limit):
            query['SyncLimit'] = request.sync_limit
        if not UtilClient.is_unset(request.tick_time):
            query['TickTime'] = request.tick_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not UtilClient.is_unset(request.open_super_acl):
            body['OpenSuperAcl'] = request.open_super_acl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_config_with_options(request, runtime)

    def update_engine_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_count):
            query['ServiceCount'] = request.service_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_engine_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_engine_namespace_with_options(request, runtime)

    def update_gateway_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.http_2):
            query['Http2'] = request.http_2
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.must_https):
            query['MustHttps'] = request.must_https
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.tls_max):
            query['TlsMax'] = request.tls_max
        if not UtilClient.is_unset(request.tls_min):
            query['TlsMin'] = request.tls_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayDomain',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_domain_with_options(request, runtime)

    def update_gateway_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayName',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_name_with_options(request, runtime)

    def update_gateway_option_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayOptionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_option):
            request.gateway_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_option, 'GatewayOption', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_option_shrink):
            query['GatewayOption'] = request.gateway_option_shrink
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayOption',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayOptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_option_with_options(request, runtime)

    def update_gateway_route_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayRouteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.direct_response_json):
            request.direct_response_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.direct_response_json, 'DirectResponseJSON', 'json')
        if not UtilClient.is_unset(tmp_req.fallback_services):
            request.fallback_services_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fallback_services, 'FallbackServices', 'json')
        if not UtilClient.is_unset(tmp_req.predicates):
            request.predicates_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.predicates, 'Predicates', 'json')
        if not UtilClient.is_unset(tmp_req.redirect_json):
            request.redirect_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.redirect_json, 'RedirectJSON', 'json')
        if not UtilClient.is_unset(tmp_req.services):
            request.services_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.services, 'Services', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.direct_response_jsonshrink):
            query['DirectResponseJSON'] = request.direct_response_jsonshrink
        if not UtilClient.is_unset(request.domain_id_list_json):
            query['DomainIdListJSON'] = request.domain_id_list_json
        if not UtilClient.is_unset(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not UtilClient.is_unset(request.fallback):
            query['Fallback'] = request.fallback
        if not UtilClient.is_unset(request.fallback_services_shrink):
            query['FallbackServices'] = request.fallback_services_shrink
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.predicates_shrink):
            query['Predicates'] = request.predicates_shrink
        if not UtilClient.is_unset(request.redirect_jsonshrink):
            query['RedirectJSON'] = request.redirect_jsonshrink
        if not UtilClient.is_unset(request.route_order):
            query['RouteOrder'] = request.route_order
        if not UtilClient.is_unset(request.services_shrink):
            query['Services'] = request.services_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_with_options(request, runtime)

    def update_gateway_route_corswith_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayRouteCORSShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cors_json):
            request.cors_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cors_json, 'CorsJSON', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cors_jsonshrink):
            query['CorsJSON'] = request.cors_jsonshrink
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteCORS',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteCORSResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route_cors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_corswith_options(request, runtime)

    def update_gateway_route_httprewrite_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.http_rewrite_json):
            query['HttpRewriteJSON'] = request.http_rewrite_json
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteHTTPRewrite',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route_httprewrite(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_httprewrite_with_options(request, runtime)

    def update_gateway_route_header_op_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.header_op_json):
            query['HeaderOpJSON'] = request.header_op_json
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteHeaderOp',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteHeaderOpResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route_header_op(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_header_op_with_options(request, runtime)

    def update_gateway_route_retry_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayRouteRetryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_json):
            request.retry_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_json, 'RetryJSON', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.retry_jsonshrink):
            query['RetryJSON'] = request.retry_jsonshrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteRetry',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteRetryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route_retry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_retry_with_options(request, runtime)

    def update_gateway_route_timeout_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayRouteTimeoutShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.timeout_json):
            request.timeout_jsonshrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timeout_json, 'TimeoutJSON', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.timeout_jsonshrink):
            query['TimeoutJSON'] = request.timeout_jsonshrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteTimeout',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route_timeout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_timeout_with_options(request, runtime)

    def update_gateway_route_waf_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.enable_waf):
            query['EnableWaf'] = request.enable_waf
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteWafStatus',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteWafStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_route_waf_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_waf_status_with_options(request, runtime)

    def update_gateway_service_traffic_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayServiceTrafficPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_traffic_policy):
            request.gateway_traffic_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_traffic_policy, 'GatewayTrafficPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_traffic_policy_shrink):
            query['GatewayTrafficPolicy'] = request.gateway_traffic_policy_shrink
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayServiceTrafficPolicy',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayServiceTrafficPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_service_traffic_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_service_traffic_policy_with_options(request, runtime)

    def update_gateway_service_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayServiceVersion',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_service_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_service_version_with_options(request, runtime)

    def update_gateway_spec_with_options(self, request, runtime):
        """
        You can call this operation to update the number or specifications of nodes in a pay-as-you-go cloud-native gateway. You are charged when you add nodes or upgrade node specifications. For more information, see [Pricing](~~250950~~).
        

        @param request: UpdateGatewaySpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateGatewaySpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.replica):
            query['Replica'] = request.replica
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewaySpec',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewaySpecResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gateway_spec(self, request):
        """
        You can call this operation to update the number or specifications of nodes in a pay-as-you-go cloud-native gateway. You are charged when you add nodes or upgrade node specifications. For more information, see [Pricing](~~250950~~).
        

        @param request: UpdateGatewaySpecRequest

        @return: UpdateGatewaySpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_spec_with_options(request, runtime)

    def update_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.version_code):
            query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    def update_message_queue_route_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateMessageQueueRouteShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.filter_side):
            query['FilterSide'] = request.filter_side
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMessageQueueRoute',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateMessageQueueRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_message_queue_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_message_queue_route_with_options(request, runtime)

    def update_migration_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.origin_instance_address):
            query['OriginInstanceAddress'] = request.origin_instance_address
        if not UtilClient.is_unset(request.origin_instance_name):
            query['OriginInstanceName'] = request.origin_instance_name
        if not UtilClient.is_unset(request.origin_instance_namespace):
            query['OriginInstanceNamespace'] = request.origin_instance_namespace
        if not UtilClient.is_unset(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.target_cluster_name):
            query['TargetClusterName'] = request.target_cluster_name
        if not UtilClient.is_unset(request.target_cluster_url):
            query['TargetClusterUrl'] = request.target_cluster_url
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMigrationTask',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_migration_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_migration_task_with_options(request, runtime)

    def update_nacos_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.check_port):
            query['CheckPort'] = request.check_port
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.health_checker):
            query['HealthChecker'] = request.health_checker
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.use_instance_port_for_check):
            query['UseInstancePortForCheck'] = request.use_instance_port_for_check
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNacosCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_nacos_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_cluster_with_options(request, runtime)

    def update_nacos_config_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: UpdateNacosConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateNacosConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.beta_ips):
            query['BetaIps'] = request.beta_ips
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.encrypted_data_key):
            query['EncryptedDataKey'] = request.encrypted_data_key
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_nacos_config(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: UpdateNacosConfigRequest

        @return: UpdateNacosConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_config_with_options(request, runtime)

    def update_nacos_instance_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: UpdateNacosInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateNacosInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.ephemeral):
            query['Ephemeral'] = request.ephemeral
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        body = {}
        if not UtilClient.is_unset(request.metadata):
            body['Metadata'] = request.metadata
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNacosInstance',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_nacos_instance(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: UpdateNacosInstanceRequest

        @return: UpdateNacosInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_instance_with_options(request, runtime)

    def update_nacos_service_with_options(self, request, runtime):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: UpdateNacosServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateNacosServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.protect_threshold):
            query['ProtectThreshold'] = request.protect_threshold
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNacosService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_nacos_service(self, request):
        """
        > The operation is not provided in Nacos SDKs. For information about Nacos SDKs, see the [official documentation](https://nacos.io/zh-cn/docs/sdk.html).
        

        @param request: UpdateNacosServiceRequest

        @return: UpdateNacosServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_service_with_options(request, runtime)

    def update_plugin_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.gmt_create):
            query['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            query['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePluginConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdatePluginConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_plugin_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_plugin_config_with_options(request, runtime)

    def update_sslcert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSSLCert',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateSSLCertResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sslcert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sslcert_with_options(request, runtime)

    def update_service_source_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateServiceSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ingress_options_request):
            request.ingress_options_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ingress_options_request, 'IngressOptionsRequest', 'json')
        if not UtilClient.is_unset(tmp_req.path_list):
            request.path_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.path_list, 'PathList', 'json')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.gateway_id):
            query['GatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['GatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ingress_options_request_shrink):
            query['IngressOptionsRequest'] = request.ingress_options_request_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.path_list_shrink):
            query['PathList'] = request.path_list_shrink
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_source_with_options(request, runtime)

    def update_znode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_znode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_znode_with_options(request, runtime)

    def upgrade_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.request_pars):
            query['RequestPars'] = request.request_pars
        if not UtilClient.is_unset(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cluster_with_options(request, runtime)
