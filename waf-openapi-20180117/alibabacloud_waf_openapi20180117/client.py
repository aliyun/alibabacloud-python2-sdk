# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20180117 import models as waf_openapi_20180117_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-wulanchabu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'wafopenapi.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('waf-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_acl_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateAclRuleResponse().from_map(
            self.do_rpcrequest('CreateAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_acl_rule_with_options(request, runtime)

    def create_cert_and_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateCertAndKeyResponse().from_map(
            self.do_rpcrequest('CreateCertAndKey', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cert_and_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cert_and_key_with_options(request, runtime)

    def create_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateDomainConfigResponse().from_map(
            self.do_rpcrequest('CreateDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_config_with_options(request, runtime)

    def create_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.CreateProtectionModuleRuleResponse().from_map(
            self.do_rpcrequest('CreateProtectionModuleRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_protection_module_rule_with_options(request, runtime)

    def delete_acl_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DeleteAclRuleResponse().from_map(
            self.do_rpcrequest('DeleteAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_rule_with_options(request, runtime)

    def delete_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DeleteDomainConfigResponse().from_map(
            self.do_rpcrequest('DeleteDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_config_with_options(request, runtime)

    def describe_acl_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeAclRulesResponse().from_map(
            self.do_rpcrequest('DescribeAclRules', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_acl_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_acl_rules_with_options(request, runtime)

    def describe_async_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeAsyncTaskStatusResponse().from_map(
            self.do_rpcrequest('DescribeAsyncTaskStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_async_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_async_task_status_with_options(request, runtime)

    def describe_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainConfigResponse().from_map(
            self.do_rpcrequest('DescribeDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_config_with_options(request, runtime)

    def describe_domain_config_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainConfigStatusResponse().from_map(
            self.do_rpcrequest('DescribeDomainConfigStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_config_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_config_status_with_options(request, runtime)

    def describe_domain_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeDomainNamesResponse().from_map(
            self.do_rpcrequest('DescribeDomainNames', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    def describe_pay_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribePayInfoResponse().from_map(
            self.do_rpcrequest('DescribePayInfo', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pay_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pay_info_with_options(request, runtime)

    def describe_protection_module_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeProtectionModuleRulesResponse().from_map(
            self.do_rpcrequest('DescribeProtectionModuleRules', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_rules_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_waf_source_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.DescribeWafSourceIpSegmentResponse().from_map(
            self.do_rpcrequest('DescribeWafSourceIpSegment', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_waf_source_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    def modify_acl_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyAclRuleResponse().from_map(
            self.do_rpcrequest('ModifyAclRule', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_acl_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_acl_rule_with_options(request, runtime)

    def modify_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyDomainConfigResponse().from_map(
            self.do_rpcrequest('ModifyDomainConfig', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_config_with_options(request, runtime)

    def modify_protection_rule_cache_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyProtectionRuleCacheStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionRuleCacheStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_cache_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_cache_status_with_options(request, runtime)

    def modify_protection_rule_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyProtectionRuleStatusResponse().from_map(
            self.do_rpcrequest('ModifyProtectionRuleStatus', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_status_with_options(request, runtime)

    def modify_waf_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return waf_openapi_20180117_models.ModifyWafSwitchResponse().from_map(
            self.do_rpcrequest('ModifyWafSwitch', '2018-01-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_waf_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_waf_switch_with_options(request, runtime)
