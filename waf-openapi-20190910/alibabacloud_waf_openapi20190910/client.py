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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
        query = {}
        query['Certificate'] = request.certificate
        query['CertificateName'] = request.certificate_name
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCertificate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    def create_certificate_by_certificate_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CertificateId'] = request.certificate_id
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCertificateByCertificateId',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_certificate_by_certificate_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_by_certificate_id_with_options(request, runtime)

    def create_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessHeaderMode'] = request.access_header_mode
        query['AccessHeaders'] = request.access_headers
        query['AccessType'] = request.access_type
        query['CloudNativeInstances'] = request.cloud_native_instances
        query['ClusterType'] = request.cluster_type
        query['ConnectionTime'] = request.connection_time
        query['Domain'] = request.domain
        query['Http2Port'] = request.http_2port
        query['HttpPort'] = request.http_port
        query['HttpToUserIp'] = request.http_to_user_ip
        query['HttpsPort'] = request.https_port
        query['HttpsRedirect'] = request.https_redirect
        query['InstanceId'] = request.instance_id
        query['IpFollowStatus'] = request.ip_follow_status
        query['IsAccessProduct'] = request.is_access_product
        query['LoadBalancing'] = request.load_balancing
        query['LogHeaders'] = request.log_headers
        query['ReadTime'] = request.read_time
        query['ResourceGroupId'] = request.resource_group_id
        query['SniHost'] = request.sni_host
        query['SniStatus'] = request.sni_status
        query['SourceIps'] = request.source_ips
        query['WriteTime'] = request.write_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateProtectionModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_protection_module_rule_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_protection_module_rule_with_options(request, runtime)

    def describe_cert_match_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Certificate'] = request.certificate
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCertMatchStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertMatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cert_match_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cert_match_status_with_options(request, runtime)

    def describe_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCertificates',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certificates_with_options(request, runtime)

    def describe_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    def describe_domain_advance_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DomainList'] = request.domain_list
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainAdvanceConfigs',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_advance_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_advance_configs_with_options(request, runtime)

    def describe_domain_basic_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessType'] = request.access_type
        query['CloudNativeProductId'] = request.cloud_native_product_id
        query['DomainKey'] = request.domain_key
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainBasicConfigs',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_basic_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_basic_configs_with_options(request, runtime)

    def describe_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['DomainNames'] = request.domain_names
        query['InstanceId'] = request.instance_id
        query['IsSub'] = request.is_sub
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainList',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_list_with_options(request, runtime)

    def describe_domain_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainNames',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    def describe_domain_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomainRuleGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainRuleGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_rule_group_with_options(request, runtime)

    def describe_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceInfo',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_info_with_options(request, runtime)

    def describe_instance_spec_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecInfo',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_spec_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_info_with_options(request, runtime)

    def describe_log_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DomainNames'] = request.domain_names
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Region'] = request.region
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogServiceStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeLogServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_service_status_with_options(request, runtime)

    def describe_protection_module_code_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CodeType'] = request.code_type
        query['CodeValue'] = request.code_value
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleCodeConfig',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_protection_module_code_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_code_config_with_options(request, runtime)

    def describe_protection_module_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Query'] = request.query
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleRules',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_protection_module_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_rules_with_options(request, runtime)

    def describe_protection_module_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_protection_module_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_status_with_options(request, runtime)

    def describe_waf_source_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_waf_source_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    def modify_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccessHeaderMode'] = request.access_header_mode
        query['AccessHeaders'] = request.access_headers
        query['AccessType'] = request.access_type
        query['CloudNativeInstances'] = request.cloud_native_instances
        query['ClusterType'] = request.cluster_type
        query['ConnectionTime'] = request.connection_time
        query['Domain'] = request.domain
        query['Http2Port'] = request.http_2port
        query['HttpPort'] = request.http_port
        query['HttpToUserIp'] = request.http_to_user_ip
        query['HttpsPort'] = request.https_port
        query['HttpsRedirect'] = request.https_redirect
        query['InstanceId'] = request.instance_id
        query['InstanceId'] = request.instance_id
        query['IpFollowStatus'] = request.ip_follow_status
        query['IsAccessProduct'] = request.is_access_product
        query['LoadBalancing'] = request.load_balancing
        query['LogHeaders'] = request.log_headers
        query['ReadTime'] = request.read_time
        query['SniHost'] = request.sni_host
        query['SniStatus'] = request.sni_status
        query['SourceIps'] = request.source_ips
        query['WriteTime'] = request.write_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    def modify_domain_ipv_6status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['Enabled'] = request.enabled
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDomainIpv6Status',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_domain_ipv_6status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_ipv_6status_with_options(request, runtime)

    def modify_log_retrieval_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['Enabled'] = request.enabled
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLogRetrievalStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_log_retrieval_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_retrieval_status_with_options(request, runtime)

    def modify_log_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domain'] = request.domain
        query['Enabled'] = request.enabled
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLogServiceStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_log_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_service_status_with_options(request, runtime)

    def modify_protection_module_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleMode',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protection_module_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_mode_with_options(request, runtime)

    def modify_protection_module_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['LockVersion'] = request.lock_version
        query['Rule'] = request.rule
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protection_module_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_rule_with_options(request, runtime)

    def modify_protection_module_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['ModuleStatus'] = request.module_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protection_module_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_status_with_options(request, runtime)

    def modify_protection_rule_cache_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyProtectionRuleCacheStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protection_rule_cache_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_cache_status_with_options(request, runtime)

    def modify_protection_rule_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DefenseType'] = request.defense_type
        query['Domain'] = request.domain
        query['InstanceId'] = request.instance_id
        query['LockVersion'] = request.lock_version
        query['RuleId'] = request.rule_id
        query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyProtectionRuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_protection_rule_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_status_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def set_domain_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Domains'] = request.domains
        query['InstanceId'] = request.instance_id
        query['ResourceGroupId'] = request.resource_group_id
        query['RuleGroupId'] = request.rule_group_id
        query['WafVersion'] = request.waf_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainRuleGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.SetDomainRuleGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_rule_group_with_options(request, runtime)
