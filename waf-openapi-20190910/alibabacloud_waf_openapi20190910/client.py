# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20190910 import models as waf_openapi_20190910_models
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

    def create_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateResponse(),
            self.do_rpcrequest('CreateCertificate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    def create_certificate_by_certificate_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse(),
            self.do_rpcrequest('CreateCertificateByCertificateId', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_certificate_by_certificate_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_by_certificate_id_with_options(request, runtime)

    def create_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateDomainResponse(),
            self.do_rpcrequest('CreateDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateProtectionModuleRuleResponse(),
            self.do_rpcrequest('CreateProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_protection_module_rule_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteDomainResponse(),
            self.do_rpcrequest('DeleteDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse(),
            self.do_rpcrequest('DeleteProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_protection_module_rule_with_options(request, runtime)

    def describe_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertificatesResponse(),
            self.do_rpcrequest('DescribeCertificates', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certificates_with_options(request, runtime)

    def describe_cert_match_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertMatchStatusResponse(),
            self.do_rpcrequest('DescribeCertMatchStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cert_match_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cert_match_status_with_options(request, runtime)

    def describe_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainResponse(),
            self.do_rpcrequest('DescribeDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    def describe_domain_advance_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse(),
            self.do_rpcrequest('DescribeDomainAdvanceConfigs', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_advance_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_advance_configs_with_options(request, runtime)

    def describe_domain_basic_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse(),
            self.do_rpcrequest('DescribeDomainBasicConfigs', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_basic_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_basic_configs_with_options(request, runtime)

    def describe_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainListResponse(),
            self.do_rpcrequest('DescribeDomainList', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_list_with_options(request, runtime)

    def describe_domain_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainNamesResponse(),
            self.do_rpcrequest('DescribeDomainNames', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    def describe_domain_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainRuleGroupResponse(),
            self.do_rpcrequest('DescribeDomainRuleGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_rule_group_with_options(request, runtime)

    def describe_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceInfoResponse(),
            self.do_rpcrequest('DescribeInstanceInfo', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_info_with_options(request, runtime)

    def describe_instance_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceInfosResponse(),
            self.do_rpcrequest('DescribeInstanceInfos', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_infos_with_options(request, runtime)

    def describe_instance_spec_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse(),
            self.do_rpcrequest('DescribeInstanceSpecInfo', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_spec_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_info_with_options(request, runtime)

    def describe_log_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeLogServiceStatusResponse(),
            self.do_rpcrequest('DescribeLogServiceStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_service_status_with_options(request, runtime)

    def describe_protection_module_code_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse(),
            self.do_rpcrequest('DescribeProtectionModuleCodeConfig', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_code_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_code_config_with_options(request, runtime)

    def describe_protection_module_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleModeResponse(),
            self.do_rpcrequest('DescribeProtectionModuleMode', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_mode_with_options(request, runtime)

    def describe_protection_module_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse(),
            self.do_rpcrequest('DescribeProtectionModuleRules', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_rules_with_options(request, runtime)

    def describe_protection_module_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse(),
            self.do_rpcrequest('DescribeProtectionModuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_protection_module_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_status_with_options(request, runtime)

    def describe_waf_source_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse(),
            self.do_rpcrequest('DescribeWafSourceIpSegment', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_waf_source_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    def modify_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainResponse(),
            self.do_rpcrequest('ModifyDomain', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    def modify_domain_ipv_6status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse(),
            self.do_rpcrequest('ModifyDomainIpv6Status', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_domain_ipv_6status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_ipv_6status_with_options(request, runtime)

    def modify_log_retrieval_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse(),
            self.do_rpcrequest('ModifyLogRetrievalStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_retrieval_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_retrieval_status_with_options(request, runtime)

    def modify_log_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogServiceStatusResponse(),
            self.do_rpcrequest('ModifyLogServiceStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_service_status_with_options(request, runtime)

    def modify_protection_module_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleModeResponse(),
            self.do_rpcrequest('ModifyProtectionModuleMode', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_module_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_mode_with_options(request, runtime)

    def modify_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse(),
            self.do_rpcrequest('ModifyProtectionModuleRule', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_rule_with_options(request, runtime)

    def modify_protection_module_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse(),
            self.do_rpcrequest('ModifyProtectionModuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_module_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_status_with_options(request, runtime)

    def modify_protection_rule_cache_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse(),
            self.do_rpcrequest('ModifyProtectionRuleCacheStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_cache_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_cache_status_with_options(request, runtime)

    def modify_protection_rule_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse(),
            self.do_rpcrequest('ModifyProtectionRuleStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_protection_rule_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_status_with_options(request, runtime)

    def set_domain_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.SetDomainRuleGroupResponse(),
            self.do_rpcrequest('SetDomainRuleGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_rule_group_with_options(request, runtime)
