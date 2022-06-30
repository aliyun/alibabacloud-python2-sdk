# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddoscoo20200101 import models as ddoscoo_20200101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddoscoo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AddAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    def add_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_blacklist_with_options(request, runtime)

    def add_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AddAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def add_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_whitelist_with_options(request, runtime)

    def associate_web_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateWebCert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AssociateWebCertResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_web_cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_web_cert_with_options(request, runtime)

    def attach_scene_defense_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.AttachSceneDefenseObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_scene_defense_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_scene_defense_object_with_options(request, runtime)

    def config_l7rs_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigL7RsPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def config_l7rs_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_l7rs_policy_with_options(request, runtime)

    def config_layer_4remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4Remark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def config_layer_4remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4remark_with_options(request, runtime)

    def config_layer_4rule_bak_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bak_mode):
            query['BakMode'] = request.bak_mode
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RuleBakMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RuleBakModeResponse(),
            self.call_api(params, req, runtime)
        )

    def config_layer_4rule_bak_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_bak_mode_with_options(request, runtime)

    def config_layer_4rule_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigLayer4RulePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigLayer4RulePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def config_layer_4rule_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_policy_with_options(request, runtime)

    def config_network_region_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse(),
            self.call_api(params, req, runtime)
        )

    def config_network_region_block(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_network_region_block_with_options(request, runtime)

    def config_network_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def config_network_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_network_rules_with_options(request, runtime)

    def config_udp_reflect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigUdpReflect',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigUdpReflectResponse(),
            self.call_api(params, req, runtime)
        )

    def config_udp_reflect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_udp_reflect_with_options(request, runtime)

    def config_web_cctemplate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebCCTemplate',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebCCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def config_web_cctemplate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_web_cctemplate_with_options(request, runtime)

    def config_web_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_list):
            query['BlackList'] = request.black_list
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigWebIpSet',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ConfigWebIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def config_web_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_web_ip_set_with_options(request, runtime)

    def create_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_params):
            query['TaskParams'] = request.task_params
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    def create_domain_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_resource_with_options(request, runtime)

    def create_network_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_network_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_rules_with_options(request, runtime)

    def create_port_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreatePortResponse(),
            self.call_api(params, req, runtime)
        )

    def create_port(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_port_with_options(request, runtime)

    def create_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_defense_policy_with_options(request, runtime)

    def create_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scheduler_rule_with_options(request, runtime)

    def create_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tag_resources_with_options(request, runtime)

    def create_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_web_ccrule_with_options(request, runtime)

    def create_web_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_id):
            query['DefenseId'] = request.defense_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.CreateWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_web_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_web_rule_with_options(request, runtime)

    def delete_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncTask',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    def delete_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blacklist):
            query['Blacklist'] = request.blacklist
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_blacklist_with_options(request, runtime)

    def delete_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.whitelist):
            query['Whitelist'] = request.whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_whitelist_with_options(request, runtime)

    def delete_domain_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_resource_with_options(request, runtime)

    def delete_network_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rule):
            query['NetworkRule'] = request.network_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteNetworkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_network_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    def delete_port_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeletePortResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_port(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_port_with_options(request, runtime)

    def delete_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_defense_policy_with_options(request, runtime)

    def delete_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduler_rule_with_options(request, runtime)

    def delete_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_resources_with_options(request, runtime)

    def delete_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_ccrule_with_options(request, runtime)

    def delete_web_cache_custom_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_web_cache_custom_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_cache_custom_rule_with_options(request, runtime)

    def delete_web_precise_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_web_precise_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_precise_access_rule_with_options(request, runtime)

    def delete_web_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DeleteWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_web_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_rule_with_options(request, runtime)

    def describe_async_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAsyncTasks',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_async_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_async_tasks_with_options(request, runtime)

    def describe_attack_analysis_max_qps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackAnalysisMaxQps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAttackAnalysisMaxQpsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_attack_analysis_max_qps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_analysis_max_qps_with_options(request, runtime)

    def describe_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_blacklist_with_options(request, runtime)

    def describe_auto_cc_list_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcListCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcListCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_cc_list_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_list_count_with_options(request, runtime)

    def describe_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_whitelist_with_options(request, runtime)

    def describe_back_source_cidr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackSourceCidr',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBackSourceCidrResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_back_source_cidr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    def describe_blackhole_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBlackholeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_blackhole_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_blackhole_status_with_options(request, runtime)

    def describe_block_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeBlockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_block_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_block_status_with_options(request, runtime)

    def describe_certs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCerts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeCertsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_certs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    def describe_cname_reuses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCnameReuses',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeCnameReusesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cname_reuses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cname_reuses_with_options(request, runtime)

    def describe_ddo_sevents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDoSEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddo_sevents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    def describe_ddos_all_event_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosAllEventList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosAllEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_all_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_all_event_list_with_options(request, runtime)

    def describe_ddos_event_area_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventArea',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventAreaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event_area(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_area_with_options(request, runtime)

    def describe_ddos_event_attack_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventAttackType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event_attack_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_attack_type_with_options(request, runtime)

    def describe_ddos_event_isp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventIsp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventIspResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event_isp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_isp_with_options(request, runtime)

    def describe_ddos_event_max_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventMax',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventMaxResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event_max(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_max_with_options(request, runtime)

    def describe_ddos_event_src_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.range):
            query['Range'] = request.range
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDosEventSrcIp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event_src_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_src_ip_with_options(request, runtime)

    def describe_defense_count_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseCountStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_count_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    def describe_defense_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRecords',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDefenseRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_records_with_options(request, runtime)

    def describe_domain_attack_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAttackEvents',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainAttackEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_attack_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    def describe_domain_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainOverview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    def describe_domain_qpslist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQPSList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainQPSListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_qpslist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qpslist_with_options(request, runtime)

    def describe_domain_qps_with_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsWithCache',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_qps_with_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    def describe_domain_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resource_with_options(request, runtime)

    def describe_domain_status_code_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_status_code_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_count_with_options(request, runtime)

    def describe_domain_status_code_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainStatusCodeList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_status_code_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    def describe_domain_top_attack_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopAttackList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainTopAttackListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_top_attack_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_attack_list_with_options(request, runtime)

    def describe_domain_view_source_countries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_view_source_countries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_countries_with_options(request, runtime)

    def describe_domain_view_source_provinces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_view_source_provinces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_provinces_with_options(request, runtime)

    def describe_domain_view_top_cost_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopCostTime',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_view_top_cost_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_cost_time_with_options(request, runtime)

    def describe_domain_view_top_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.top):
            query['Top'] = request.top
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainViewTopUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_view_top_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_url_with_options(request, runtime)

    def describe_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomains',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticBandwidthSpec',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_elastic_bandwidth_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    def describe_health_check_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHealthCheckListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_health_check_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    def describe_health_check_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeHealthCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_health_check_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_with_options(request, runtime)

    def describe_instance_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDetails',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    def describe_instance_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIds',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ids_with_options(request, runtime)

    def describe_instance_specs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_specs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    def describe_instance_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatistics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    def describe_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.expire_end_time):
            query['ExpireEndTime'] = request.expire_end_time
        if not UtilClient.is_unset(request.expire_start_time):
            query['ExpireStartTime'] = request.expire_start_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_l7rs_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeL7RsPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeL7RsPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_l7rs_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_l7rs_policy_with_options(request, runtime)

    def describe_layer_4rule_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listeners):
            query['Listeners'] = request.listeners
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLayer4RulePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeLayer4RulePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_layer_4rule_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rule_policy_with_options(request, runtime)

    def describe_log_store_exist_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreExistStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_store_exist_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    def describe_network_region_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRegionBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_region_block(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_region_block_with_options(request, runtime)

    def describe_network_rule_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_rules):
            query['NetworkRules'] = request.network_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkRuleAttributes',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_rule_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rule_attributes_with_options(request, runtime)

    def describe_network_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
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
            action='DescribeNetworkRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeNetworkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rules_with_options(request, runtime)

    def describe_op_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeOpEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_op_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    def describe_port_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
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
            action='DescribePort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_with_options(request, runtime)

    def describe_port_attack_max_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortAttackMaxFlow',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_attack_max_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_attack_max_flow_with_options(request, runtime)

    def describe_port_auto_cc_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortAutoCcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_auto_cc_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_auto_cc_status_with_options(request, runtime)

    def describe_port_conns_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortConnsCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortConnsCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_conns_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_count_with_options(request, runtime)

    def describe_port_conns_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortConnsList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortConnsListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_conns_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_list_with_options(request, runtime)

    def describe_port_flow_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortFlowList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortFlowListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_flow_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_flow_list_with_options(request, runtime)

    def describe_port_max_conns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortMaxConns',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortMaxConnsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_max_conns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_max_conns_with_options(request, runtime)

    def describe_port_view_source_countries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceCountries',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_view_source_countries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_countries_with_options(request, runtime)

    def describe_port_view_source_isps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceIsps',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceIspsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_view_source_isps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_isps_with_options(request, runtime)

    def describe_port_view_source_provinces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePortViewSourceProvinces',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_port_view_source_provinces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_provinces_with_options(request, runtime)

    def describe_scene_defense_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefenseObjects',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_defense_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_objects_with_options(request, runtime)

    def describe_scene_defense_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneDefensePolicies',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_defense_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_policies_with_options(request, runtime)

    def describe_scheduler_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSchedulerRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSchedulerRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scheduler_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduler_rules_with_options(request, runtime)

    def describe_sls_auth_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsAuthStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sls_auth_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    def describe_sls_logstore_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsLogstoreInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sls_logstore_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    def describe_sls_open_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsOpenStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sls_open_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    def describe_sts_grant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStsGrantStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeStsGrantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sts_grant_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sts_grant_status_with_options(request, runtime)

    def describe_system_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_object):
            query['EntityObject'] = request.entity_object
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeSystemLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_system_log_with_options(request, runtime)

    def describe_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    def describe_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagResources',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    def describe_udp_reflect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUdpReflect',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUdpReflectResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_udp_reflect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_udp_reflect_with_options(request, runtime)

    def describe_un_blackhole_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnBlackholeCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUnBlackholeCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_un_blackhole_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_un_blackhole_count_with_options(request, runtime)

    def describe_un_block_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnBlockCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeUnBlockCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_un_block_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_un_block_count_with_options(request, runtime)

    def describe_web_access_log_dispatch_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogDispatchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_access_log_dispatch_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_dispatch_status_with_options(request, runtime)

    def describe_web_access_log_empty_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogEmptyCount',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_access_log_empty_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_empty_count_with_options(request, runtime)

    def describe_web_access_log_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessLogStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_access_log_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_status_with_options(request, runtime)

    def describe_web_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_mode_with_options(request, runtime)

    def describe_web_area_block_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebAreaBlockConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_area_block_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_area_block_configs_with_options(request, runtime)

    def describe_web_ccrules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCCRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCCRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_ccrules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_ccrules_with_options(request, runtime)

    def describe_web_cache_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCacheConfigs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCacheConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_cache_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cache_configs_with_options(request, runtime)

    def describe_web_cc_protect_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCcProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_cc_protect_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cc_protect_switch_with_options(request, runtime)

    def describe_web_custom_ports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebCustomPorts',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebCustomPortsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_custom_ports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_custom_ports_with_options(request, runtime)

    def describe_web_instance_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebInstanceRelations',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_instance_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_instance_relations_with_options(request, runtime)

    def describe_web_precise_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_precise_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_precise_access_rule_with_options(request, runtime)

    def describe_web_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname):
            query['Cname'] = request.cname
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_domain_pattern):
            query['QueryDomainPattern'] = request.query_domain_pattern
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebRules',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DescribeWebRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_web_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_rules_with_options(request, runtime)

    def detach_scene_defense_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachSceneDefenseObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DetachSceneDefenseObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_scene_defense_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_scene_defense_object_with_options(request, runtime)

    def disable_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_defense_policy_with_options(request, runtime)

    def disable_web_access_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebAccessLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_web_access_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_web_access_log_config_with_options(request, runtime)

    def disable_web_ccwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebCCResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_web_cc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccwith_options(request, runtime)

    def disable_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.DisableWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccrule_with_options(request, runtime)

    def empty_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcBlacklist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse(),
            self.call_api(params, req, runtime)
        )

    def empty_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_blacklist_with_options(request, runtime)

    def empty_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptyAutoCcWhitelist',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def empty_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_whitelist_with_options(request, runtime)

    def empty_sls_logstore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmptySlsLogstore',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EmptySlsLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    def empty_sls_logstore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    def enable_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableSceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_defense_policy_with_options(request, runtime)

    def enable_web_access_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebAccessLogConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebAccessLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_web_access_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_web_access_log_config_with_options(request, runtime)

    def enable_web_ccwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebCC',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebCCResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_web_cc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccwith_options(request, runtime)

    def enable_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.EnableWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccrule_with_options(request, runtime)

    def modify_blackhole_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.blackhole_status):
            query['BlackholeStatus'] = request.blackhole_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBlackholeStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBlackholeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_blackhole_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_blackhole_status_with_options(request, runtime)

    def modify_block_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lines):
            query['Lines'] = request.lines
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBlockStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyBlockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_block_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_block_status_with_options(request, runtime)

    def modify_cname_reuse_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cname):
            query['Cname'] = request.cname
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCnameReuse',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyCnameReuseResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cname_reuse(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cname_reuse_with_options(request, runtime)

    def modify_domain_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyDomainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_domain_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_resource_with_options(request, runtime)

    def modify_elastic_band_width_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_bandwidth):
            query['ElasticBandwidth'] = request.elastic_bandwidth
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticBandWidth',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyElasticBandWidthResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_elastic_band_width(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    def modify_full_log_ttl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFullLogTtl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyFullLogTtlResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_full_log_ttl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    def modify_health_check_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHealthCheckConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHealthCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_health_check_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_health_check_config_with_options(request, runtime)

    def modify_http_2enable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHttp2Enable',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyHttp2EnableResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_http_2enable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_http_2enable_with_options(request, runtime)

    def modify_instance_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRemark',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyInstanceRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    def modify_network_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.forward_protocol):
            query['ForwardProtocol'] = request.forward_protocol
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkRuleAttribute',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_network_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_rule_attribute_with_options(request, runtime)

    def modify_port_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_port):
            query['BackendPort'] = request.backend_port
        if not UtilClient.is_unset(request.frontend_port):
            query['FrontendPort'] = request.frontend_port
        if not UtilClient.is_unset(request.frontend_protocol):
            query['FrontendProtocol'] = request.frontend_protocol
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPort',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyPortResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_port(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_port_with_options(request, runtime)

    def modify_port_auto_cc_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.switch):
            query['Switch'] = request.switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPortAutoCcStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_port_auto_cc_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_port_auto_cc_status_with_options(request, runtime)

    def modify_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySceneDefensePolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifySceneDefensePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scene_defense_policy_with_options(request, runtime)

    def modify_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifySchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduler_rule_with_options(request, runtime)

    def modify_tls_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTlsConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyTlsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tls_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tls_config_with_options(request, runtime)

    def modify_web_aiprotect_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAIProtectModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_aiprotect_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_mode_with_options(request, runtime)

    def modify_web_aiprotect_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAIProtectSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_aiprotect_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_switch_with_options(request, runtime)

    def modify_web_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAccessMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAccessModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_access_mode_with_options(request, runtime)

    def modify_web_area_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.regions):
            query['Regions'] = request.regions
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlock',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAreaBlockResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_area_block(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_with_options(request, runtime)

    def modify_web_area_block_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebAreaBlockSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_area_block_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_switch_with_options(request, runtime)

    def modify_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.uri):
            query['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCCRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCCRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ccrule_with_options(request, runtime)

    def modify_web_cache_custom_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheCustomRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_cache_custom_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_custom_rule_with_options(request, runtime)

    def modify_web_cache_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheMode',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_cache_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_mode_with_options(request, runtime)

    def modify_web_cache_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebCacheSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebCacheSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_cache_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_switch_with_options(request, runtime)

    def modify_web_ip_set_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebIpSetSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_ip_set_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ip_set_switch_with_options(request, runtime)

    def modify_web_precise_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.expires):
            query['Expires'] = request.expires
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_precise_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_rule_with_options(request, runtime)

    def modify_web_precise_access_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebPreciseAccessSwitch',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_precise_access_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_switch_with_options(request, runtime)

    def modify_web_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.https_ext):
            query['HttpsExt'] = request.https_ext
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.proxy_types):
            query['ProxyTypes'] = request.proxy_types
        if not UtilClient.is_unset(request.real_servers):
            query['RealServers'] = request.real_servers
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rs_type):
            query['RsType'] = request.rs_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyWebRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ModifyWebRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_web_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_rule_with_options(request, runtime)

    def release_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    def switch_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.switch_data):
            query['SwitchData'] = request.switch_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSchedulerRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddoscoo_20200101_models.SwitchSchedulerRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_scheduler_rule_with_options(request, runtime)
