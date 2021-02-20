# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddoscoo20200101 import models as ddoscoo_20200101_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AddAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('AddAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_blacklist_with_options(request, runtime)

    def add_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AddAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('AddAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_auto_cc_whitelist_with_options(request, runtime)

    def associate_web_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AssociateWebCertResponse().from_map(
            self.do_rpcrequest('AssociateWebCert', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_web_cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_web_cert_with_options(request, runtime)

    def attach_scene_defense_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.AttachSceneDefenseObjectResponse().from_map(
            self.do_rpcrequest('AttachSceneDefenseObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_scene_defense_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_scene_defense_object_with_options(request, runtime)

    def config_l7rs_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigL7RsPolicyResponse().from_map(
            self.do_rpcrequest('ConfigL7RsPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_l7rs_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_l7rs_policy_with_options(request, runtime)

    def config_network_region_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigNetworkRegionBlockResponse().from_map(
            self.do_rpcrequest('ConfigNetworkRegionBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_network_region_block(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_network_region_block_with_options(request, runtime)

    def config_network_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigNetworkRulesResponse().from_map(
            self.do_rpcrequest('ConfigNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_network_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_network_rules_with_options(request, runtime)

    def config_web_cctemplate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigWebCCTemplateResponse().from_map(
            self.do_rpcrequest('ConfigWebCCTemplate', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_web_cctemplate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_web_cctemplate_with_options(request, runtime)

    def config_web_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ConfigWebIpSetResponse().from_map(
            self.do_rpcrequest('ConfigWebIpSet', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_web_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_web_ip_set_with_options(request, runtime)

    def create_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateAsyncTaskResponse().from_map(
            self.do_rpcrequest('CreateAsyncTask', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    def create_network_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateNetworkRulesResponse().from_map(
            self.do_rpcrequest('CreateNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_rules_with_options(request, runtime)

    def create_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('CreateSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_defense_policy_with_options(request, runtime)

    def create_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateSchedulerRuleResponse().from_map(
            self.do_rpcrequest('CreateSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scheduler_rule_with_options(request, runtime)

    def create_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateTagResourcesResponse().from_map(
            self.do_rpcrequest('CreateTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tag_resources_with_options(request, runtime)

    def create_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateWebCCRuleResponse().from_map(
            self.do_rpcrequest('CreateWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_web_ccrule_with_options(request, runtime)

    def create_web_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.CreateWebRuleResponse().from_map(
            self.do_rpcrequest('CreateWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_web_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_web_rule_with_options(request, runtime)

    def delete_async_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAsyncTaskResponse().from_map(
            self.do_rpcrequest('DeleteAsyncTask', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_async_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    def delete_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('DeleteAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_blacklist_with_options(request, runtime)

    def delete_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('DeleteAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_cc_whitelist_with_options(request, runtime)

    def delete_network_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteNetworkRuleResponse().from_map(
            self.do_rpcrequest('DeleteNetworkRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_rule_with_options(request, runtime)

    def delete_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('DeleteSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_defense_policy_with_options(request, runtime)

    def delete_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteSchedulerRuleResponse().from_map(
            self.do_rpcrequest('DeleteSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduler_rule_with_options(request, runtime)

    def delete_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteTagResourcesResponse().from_map(
            self.do_rpcrequest('DeleteTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_resources_with_options(request, runtime)

    def delete_web_cache_custom_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebCacheCustomRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebCacheCustomRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_cache_custom_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_cache_custom_rule_with_options(request, runtime)

    def delete_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebCCRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_ccrule_with_options(request, runtime)

    def delete_web_precise_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebPreciseAccessRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_precise_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_precise_access_rule_with_options(request, runtime)

    def delete_web_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DeleteWebRuleResponse().from_map(
            self.do_rpcrequest('DeleteWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_web_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_web_rule_with_options(request, runtime)

    def describe_async_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAsyncTasksResponse().from_map(
            self.do_rpcrequest('DescribeAsyncTasks', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_async_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_async_tasks_with_options(request, runtime)

    def describe_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('DescribeAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_blacklist_with_options(request, runtime)

    def describe_auto_cc_list_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcListCountResponse().from_map(
            self.do_rpcrequest('DescribeAutoCcListCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_cc_list_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_list_count_with_options(request, runtime)

    def describe_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_cc_whitelist_with_options(request, runtime)

    def describe_back_source_cidr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBackSourceCidrResponse().from_map(
            self.do_rpcrequest('DescribeBackSourceCidr', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_back_source_cidr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    def describe_blackhole_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBlackholeStatusResponse().from_map(
            self.do_rpcrequest('DescribeBlackholeStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_blackhole_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_blackhole_status_with_options(request, runtime)

    def describe_block_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeBlockStatusResponse().from_map(
            self.do_rpcrequest('DescribeBlockStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_block_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_block_status_with_options(request, runtime)

    def describe_certs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeCertsResponse().from_map(
            self.do_rpcrequest('DescribeCerts', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_certs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certs_with_options(request, runtime)

    def describe_cname_reuses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeCnameReusesResponse().from_map(
            self.do_rpcrequest('DescribeCnameReuses', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cname_reuses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cname_reuses_with_options(request, runtime)

    def describe_ddos_all_event_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosAllEventListResponse().from_map(
            self.do_rpcrequest('DescribeDDosAllEventList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_all_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_all_event_list_with_options(request, runtime)

    def describe_ddos_event_area_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventAreaResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventArea', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_area(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_area_with_options(request, runtime)

    def describe_ddos_event_attack_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventAttackTypeResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventAttackType', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_attack_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_attack_type_with_options(request, runtime)

    def describe_ddos_event_isp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventIspResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventIsp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_isp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_isp_with_options(request, runtime)

    def describe_ddos_event_max_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventMaxResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventMax', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_max(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_max_with_options(request, runtime)

    def describe_ddo_sevents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDoSEventsResponse().from_map(
            self.do_rpcrequest('DescribeDDoSEvents', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddo_sevents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    def describe_ddos_event_src_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDDosEventSrcIpResponse().from_map(
            self.do_rpcrequest('DescribeDDosEventSrcIp', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ddos_event_src_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_src_ip_with_options(request, runtime)

    def describe_defense_count_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDefenseCountStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeDefenseCountStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_defense_count_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    def describe_defense_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDefenseRecordsResponse().from_map(
            self.do_rpcrequest('DescribeDefenseRecords', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_defense_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_records_with_options(request, runtime)

    def describe_domain_attack_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainAttackEventsResponse().from_map(
            self.do_rpcrequest('DescribeDomainAttackEvents', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_attack_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    def describe_domain_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainOverviewResponse().from_map(
            self.do_rpcrequest('DescribeDomainOverview', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_overview_with_options(request, runtime)

    def describe_domain_qpslist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainQPSListResponse().from_map(
            self.do_rpcrequest('DescribeDomainQPSList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_qpslist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qpslist_with_options(request, runtime)

    def describe_domain_qps_with_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainQpsWithCacheResponse().from_map(
            self.do_rpcrequest('DescribeDomainQpsWithCache', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_qps_with_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    def describe_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDomains', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    def describe_domain_status_code_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainStatusCodeCountResponse().from_map(
            self.do_rpcrequest('DescribeDomainStatusCodeCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_status_code_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_count_with_options(request, runtime)

    def describe_domain_status_code_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainStatusCodeListResponse().from_map(
            self.do_rpcrequest('DescribeDomainStatusCodeList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_status_code_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_status_code_list_with_options(request, runtime)

    def describe_domain_top_attack_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainTopAttackListResponse().from_map(
            self.do_rpcrequest('DescribeDomainTopAttackList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_top_attack_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_attack_list_with_options(request, runtime)

    def describe_domain_view_source_countries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewSourceCountriesResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewSourceCountries', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_source_countries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_countries_with_options(request, runtime)

    def describe_domain_view_source_provinces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewSourceProvincesResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewSourceProvinces', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_source_provinces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_source_provinces_with_options(request, runtime)

    def describe_domain_view_top_cost_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewTopCostTimeResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewTopCostTime', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_top_cost_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_cost_time_with_options(request, runtime)

    def describe_domain_view_top_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeDomainViewTopUrlResponse().from_map(
            self.do_rpcrequest('DescribeDomainViewTopUrl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_view_top_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_view_top_url_with_options(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeElasticBandwidthSpecResponse().from_map(
            self.do_rpcrequest('DescribeElasticBandwidthSpec', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elastic_bandwidth_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    def describe_health_check_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeHealthCheckListResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    def describe_health_check_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeHealthCheckStatusResponse().from_map(
            self.do_rpcrequest('DescribeHealthCheckStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_check_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_with_options(request, runtime)

    def describe_instance_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceDetailsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceDetails', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    def describe_instance_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceIdsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceIds', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ids_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_instance_specs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceSpecsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceSpecs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_specs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    def describe_instance_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    def describe_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeInstanceStatusResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    def describe_l7rs_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeL7RsPolicyResponse().from_map(
            self.do_rpcrequest('DescribeL7RsPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_l7rs_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_l7rs_policy_with_options(request, runtime)

    def describe_log_store_exist_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeLogStoreExistStatusResponse().from_map(
            self.do_rpcrequest('DescribeLogStoreExistStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_store_exist_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    def describe_network_region_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRegionBlockResponse().from_map(
            self.do_rpcrequest('DescribeNetworkRegionBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_region_block(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_region_block_with_options(request, runtime)

    def describe_network_rule_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRuleAttributesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkRuleAttributes', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_rule_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rule_attributes_with_options(request, runtime)

    def describe_network_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeNetworkRulesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_rules_with_options(request, runtime)

    def describe_op_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeOpEntitiesResponse().from_map(
            self.do_rpcrequest('DescribeOpEntities', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_op_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    def describe_port_attack_max_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortAttackMaxFlowResponse().from_map(
            self.do_rpcrequest('DescribePortAttackMaxFlow', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_attack_max_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_attack_max_flow_with_options(request, runtime)

    def describe_port_auto_cc_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortAutoCcStatusResponse().from_map(
            self.do_rpcrequest('DescribePortAutoCcStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_auto_cc_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_auto_cc_status_with_options(request, runtime)

    def describe_port_conns_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortConnsCountResponse().from_map(
            self.do_rpcrequest('DescribePortConnsCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_conns_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_count_with_options(request, runtime)

    def describe_port_conns_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortConnsListResponse().from_map(
            self.do_rpcrequest('DescribePortConnsList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_conns_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_conns_list_with_options(request, runtime)

    def describe_port_flow_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortFlowListResponse().from_map(
            self.do_rpcrequest('DescribePortFlowList', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_flow_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_flow_list_with_options(request, runtime)

    def describe_port_max_conns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortMaxConnsResponse().from_map(
            self.do_rpcrequest('DescribePortMaxConns', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_max_conns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_max_conns_with_options(request, runtime)

    def describe_port_view_source_countries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceCountriesResponse().from_map(
            self.do_rpcrequest('DescribePortViewSourceCountries', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_view_source_countries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_countries_with_options(request, runtime)

    def describe_port_view_source_isps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceIspsResponse().from_map(
            self.do_rpcrequest('DescribePortViewSourceIsps', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_view_source_isps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_isps_with_options(request, runtime)

    def describe_port_view_source_provinces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribePortViewSourceProvincesResponse().from_map(
            self.do_rpcrequest('DescribePortViewSourceProvinces', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_port_view_source_provinces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_port_view_source_provinces_with_options(request, runtime)

    def describe_scene_defense_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSceneDefenseObjectsResponse().from_map(
            self.do_rpcrequest('DescribeSceneDefenseObjects', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scene_defense_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_objects_with_options(request, runtime)

    def describe_scene_defense_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSceneDefensePoliciesResponse().from_map(
            self.do_rpcrequest('DescribeSceneDefensePolicies', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scene_defense_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_defense_policies_with_options(request, runtime)

    def describe_scheduler_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSchedulerRulesResponse().from_map(
            self.do_rpcrequest('DescribeSchedulerRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scheduler_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduler_rules_with_options(request, runtime)

    def describe_sls_auth_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsAuthStatusResponse().from_map(
            self.do_rpcrequest('DescribeSlsAuthStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_auth_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    def describe_sls_logstore_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsLogstoreInfoResponse().from_map(
            self.do_rpcrequest('DescribeSlsLogstoreInfo', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_logstore_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    def describe_sls_open_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeSlsOpenStatusResponse().from_map(
            self.do_rpcrequest('DescribeSlsOpenStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sls_open_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    def describe_sts_grant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeStsGrantStatusResponse().from_map(
            self.do_rpcrequest('DescribeStsGrantStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sts_grant_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sts_grant_status_with_options(request, runtime)

    def describe_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeTagKeysResponse().from_map(
            self.do_rpcrequest('DescribeTagKeys', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    def describe_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeTagResourcesResponse().from_map(
            self.do_rpcrequest('DescribeTagResources', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    def describe_un_blackhole_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeUnBlackholeCountResponse().from_map(
            self.do_rpcrequest('DescribeUnBlackholeCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_un_blackhole_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_un_blackhole_count_with_options(request, runtime)

    def describe_un_block_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeUnBlockCountResponse().from_map(
            self.do_rpcrequest('DescribeUnBlockCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_un_block_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_un_block_count_with_options(request, runtime)

    def describe_web_access_log_dispatch_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogDispatchStatusResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessLogDispatchStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_log_dispatch_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_dispatch_status_with_options(request, runtime)

    def describe_web_access_log_empty_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogEmptyCountResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessLogEmptyCount', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_log_empty_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_empty_count_with_options(request, runtime)

    def describe_web_access_log_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessLogStatusResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessLogStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_log_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_log_status_with_options(request, runtime)

    def describe_web_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAccessModeResponse().from_map(
            self.do_rpcrequest('DescribeWebAccessMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_access_mode_with_options(request, runtime)

    def describe_web_area_block_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebAreaBlockConfigsResponse().from_map(
            self.do_rpcrequest('DescribeWebAreaBlockConfigs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_area_block_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_area_block_configs_with_options(request, runtime)

    def describe_web_cache_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCacheConfigsResponse().from_map(
            self.do_rpcrequest('DescribeWebCacheConfigs', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_cache_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cache_configs_with_options(request, runtime)

    def describe_web_cc_protect_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCcProtectSwitchResponse().from_map(
            self.do_rpcrequest('DescribeWebCcProtectSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_cc_protect_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_cc_protect_switch_with_options(request, runtime)

    def describe_web_ccrules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCCRulesResponse().from_map(
            self.do_rpcrequest('DescribeWebCCRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_ccrules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_ccrules_with_options(request, runtime)

    def describe_web_custom_ports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebCustomPortsResponse().from_map(
            self.do_rpcrequest('DescribeWebCustomPorts', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_custom_ports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_custom_ports_with_options(request, runtime)

    def describe_web_instance_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebInstanceRelationsResponse().from_map(
            self.do_rpcrequest('DescribeWebInstanceRelations', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_instance_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_instance_relations_with_options(request, runtime)

    def describe_web_precise_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebPreciseAccessRuleResponse().from_map(
            self.do_rpcrequest('DescribeWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_precise_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_precise_access_rule_with_options(request, runtime)

    def describe_web_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DescribeWebRulesResponse().from_map(
            self.do_rpcrequest('DescribeWebRules', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_web_rules_with_options(request, runtime)

    def detach_scene_defense_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DetachSceneDefenseObjectResponse().from_map(
            self.do_rpcrequest('DetachSceneDefenseObject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_scene_defense_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_scene_defense_object_with_options(request, runtime)

    def disable_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('DisableSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_defense_policy_with_options(request, runtime)

    def disable_web_access_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebAccessLogConfigResponse().from_map(
            self.do_rpcrequest('DisableWebAccessLogConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_web_access_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_web_access_log_config_with_options(request, runtime)

    def disable_web_ccwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebCCResponse().from_map(
            self.do_rpcrequest('DisableWebCC', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_web_cc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccwith_options(request, runtime)

    def disable_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.DisableWebCCRuleResponse().from_map(
            self.do_rpcrequest('DisableWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_web_ccrule_with_options(request, runtime)

    def empty_auto_cc_blacklist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptyAutoCcBlacklistResponse().from_map(
            self.do_rpcrequest('EmptyAutoCcBlacklist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_auto_cc_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_blacklist_with_options(request, runtime)

    def empty_auto_cc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptyAutoCcWhitelistResponse().from_map(
            self.do_rpcrequest('EmptyAutoCcWhitelist', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_auto_cc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_auto_cc_whitelist_with_options(request, runtime)

    def empty_sls_logstore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EmptySlsLogstoreResponse().from_map(
            self.do_rpcrequest('EmptySlsLogstore', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def empty_sls_logstore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    def enable_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableSceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('EnableSceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_defense_policy_with_options(request, runtime)

    def enable_web_access_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebAccessLogConfigResponse().from_map(
            self.do_rpcrequest('EnableWebAccessLogConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_web_access_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_web_access_log_config_with_options(request, runtime)

    def enable_web_ccwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebCCResponse().from_map(
            self.do_rpcrequest('EnableWebCC', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_web_cc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccwith_options(request, runtime)

    def enable_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.EnableWebCCRuleResponse().from_map(
            self.do_rpcrequest('EnableWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_web_ccrule_with_options(request, runtime)

    def modify_blackhole_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyBlackholeStatusResponse().from_map(
            self.do_rpcrequest('ModifyBlackholeStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_blackhole_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_blackhole_status_with_options(request, runtime)

    def modify_block_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyBlockStatusResponse().from_map(
            self.do_rpcrequest('ModifyBlockStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_block_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_block_status_with_options(request, runtime)

    def modify_cname_reuse_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyCnameReuseResponse().from_map(
            self.do_rpcrequest('ModifyCnameReuse', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cname_reuse(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cname_reuse_with_options(request, runtime)

    def modify_elastic_band_width_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyElasticBandWidthResponse().from_map(
            self.do_rpcrequest('ModifyElasticBandWidth', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elastic_band_width(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    def modify_full_log_ttl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyFullLogTtlResponse().from_map(
            self.do_rpcrequest('ModifyFullLogTtl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_full_log_ttl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    def modify_health_check_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyHealthCheckConfigResponse().from_map(
            self.do_rpcrequest('ModifyHealthCheckConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_health_check_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_health_check_config_with_options(request, runtime)

    def modify_http_2enable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyHttp2EnableResponse().from_map(
            self.do_rpcrequest('ModifyHttp2Enable', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_http_2enable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_http_2enable_with_options(request, runtime)

    def modify_instance_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyInstanceRemarkResponse().from_map(
            self.do_rpcrequest('ModifyInstanceRemark', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    def modify_network_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyNetworkRuleAttributeResponse().from_map(
            self.do_rpcrequest('ModifyNetworkRuleAttribute', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_rule_attribute_with_options(request, runtime)

    def modify_port_auto_cc_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyPortAutoCcStatusResponse().from_map(
            self.do_rpcrequest('ModifyPortAutoCcStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_port_auto_cc_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_port_auto_cc_status_with_options(request, runtime)

    def modify_scene_defense_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifySceneDefensePolicyResponse().from_map(
            self.do_rpcrequest('ModifySceneDefensePolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scene_defense_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scene_defense_policy_with_options(request, runtime)

    def modify_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifySchedulerRuleResponse().from_map(
            self.do_rpcrequest('ModifySchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduler_rule_with_options(request, runtime)

    def modify_tls_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyTlsConfigResponse().from_map(
            self.do_rpcrequest('ModifyTlsConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_tls_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tls_config_with_options(request, runtime)

    def modify_web_access_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAccessModeResponse().from_map(
            self.do_rpcrequest('ModifyWebAccessMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_access_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_access_mode_with_options(request, runtime)

    def modify_web_aiprotect_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAIProtectModeResponse().from_map(
            self.do_rpcrequest('ModifyWebAIProtectMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_aiprotect_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_mode_with_options(request, runtime)

    def modify_web_aiprotect_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAIProtectSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebAIProtectSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_aiprotect_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_aiprotect_switch_with_options(request, runtime)

    def modify_web_area_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAreaBlockResponse().from_map(
            self.do_rpcrequest('ModifyWebAreaBlock', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_area_block(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_with_options(request, runtime)

    def modify_web_area_block_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebAreaBlockSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebAreaBlockSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_area_block_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_area_block_switch_with_options(request, runtime)

    def modify_web_cache_custom_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheCustomRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebCacheCustomRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_cache_custom_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_custom_rule_with_options(request, runtime)

    def modify_web_cache_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheModeResponse().from_map(
            self.do_rpcrequest('ModifyWebCacheMode', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_cache_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_mode_with_options(request, runtime)

    def modify_web_cache_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCacheSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebCacheSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_cache_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_cache_switch_with_options(request, runtime)

    def modify_web_ccrule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebCCRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebCCRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_ccrule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ccrule_with_options(request, runtime)

    def modify_web_ip_set_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebIpSetSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebIpSetSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_ip_set_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_ip_set_switch_with_options(request, runtime)

    def modify_web_precise_access_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebPreciseAccessRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebPreciseAccessRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_precise_access_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_rule_with_options(request, runtime)

    def modify_web_precise_access_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebPreciseAccessSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWebPreciseAccessSwitch', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_precise_access_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_precise_access_switch_with_options(request, runtime)

    def modify_web_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ModifyWebRuleResponse().from_map(
            self.do_rpcrequest('ModifyWebRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_web_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_web_rule_with_options(request, runtime)

    def release_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.ReleaseInstanceResponse().from_map(
            self.do_rpcrequest('ReleaseInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    def switch_scheduler_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ddoscoo_20200101_models.SwitchSchedulerRuleResponse().from_map(
            self.do_rpcrequest('SwitchSchedulerRule', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_scheduler_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_scheduler_rule_with_options(request, runtime)
