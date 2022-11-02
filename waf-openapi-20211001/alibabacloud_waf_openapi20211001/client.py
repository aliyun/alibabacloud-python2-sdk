# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20211001 import models as waf_openapi_20211001_models
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

    def clear_major_protection_black_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ClearMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_major_protection_black_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_major_protection_black_ip_with_options(request, runtime)

    def create_defense_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_defense_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_defense_resource_group_with_options(request, runtime)

    def create_defense_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_defense_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_defense_rule_with_options(request, runtime)

    def create_defense_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_origin):
            query['TemplateOrigin'] = request.template_origin
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_defense_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_defense_template_with_options(request, runtime)

    def create_domain_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.CreateDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.listen), 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.redirect), 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_major_protection_black_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.CreateMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    def create_major_protection_black_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_major_protection_black_ip_with_options(request, runtime)

    def delete_defense_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_defense_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_resource_group_with_options(request, runtime)

    def delete_defense_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_defense_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_rule_with_options(request, runtime)

    def delete_defense_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_defense_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_defense_template_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_major_protection_black_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DeleteMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_major_protection_black_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_major_protection_black_ip_with_options(request, runtime)

    def describe_defense_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resource_group_with_options(request, runtime)

    def describe_defense_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_resources_with_options(request, runtime)

    def describe_defense_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_rule_with_options(request, runtime)

    def describe_defense_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseRules',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_rules_with_options(request, runtime)

    def describe_defense_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_defense_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_template_with_options(request, runtime)

    def describe_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetail',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_with_options(request, runtime)

    def describe_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend):
            query['Backend'] = request.backend
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
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
            action='DescribeDomains',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    def describe_flow_chart_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowChart',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flow_chart(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_chart_with_options(request, runtime)

    def describe_flow_top_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flow_top_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_top_resource_with_options(request, runtime)

    def describe_flow_top_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeFlowTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flow_top_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_top_url_with_options(request, runtime)

    def describe_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    def describe_major_protection_black_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_like):
            query['IpLike'] = request.ip_like
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMajorProtectionBlackIps',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeMajorProtectionBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_major_protection_black_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_major_protection_black_ips_with_options(request, runtime)

    def describe_peak_trend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePeakTrend',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribePeakTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_peak_trend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_peak_trend_with_options(request, runtime)

    def describe_resource_log_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_log_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_log_status_with_options(request, runtime)

    def describe_resource_port_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_instance_id):
            query['ResourceInstanceId'] = request.resource_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePort',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResourcePortResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_port(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_port_with_options(request, runtime)

    def describe_response_code_trend_graph_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResponseCodeTrendGraph',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeResponseCodeTrendGraphResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_response_code_trend_graph(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_response_code_trend_graph_with_options(request, runtime)

    def describe_rule_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_groups_with_options(request, runtime)

    def describe_rule_hits_top_client_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopClientIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopClientIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hits_top_client_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_client_ip_with_options(request, runtime)

    def describe_rule_hits_top_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopResource',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hits_top_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_resource_with_options(request, runtime)

    def describe_rule_hits_top_rule_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopRuleId',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hits_top_rule_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_rule_id_with_options(request, runtime)

    def describe_rule_hits_top_tule_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopTuleType',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopTuleTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hits_top_tule_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_tule_type_with_options(request, runtime)

    def describe_rule_hits_top_ua_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUa',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hits_top_ua(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_ua_with_options(request, runtime)

    def describe_rule_hits_top_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHitsTopUrl',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeRuleHitsTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hits_top_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hits_top_url_with_options(request, runtime)

    def describe_template_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_template_resources_with_options(request, runtime)

    def describe_visit_top_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitTopIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_visit_top_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_visit_top_ip_with_options(request, runtime)

    def describe_visit_uas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVisitUas',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeVisitUasResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_visit_uas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_visit_uas_with_options(request, runtime)

    def describe_waf_source_ip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.DescribeWafSourceIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_waf_source_ip_segment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    def modify_defense_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_list):
            query['AddList'] = request.add_list
        if not UtilClient.is_unset(request.delete_list):
            query['DeleteList'] = request.delete_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseResourceGroup',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_defense_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_resource_group_with_options(request, runtime)

    def modify_defense_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_scene):
            query['DefenseScene'] = request.defense_scene
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRule',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_defense_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_with_options(request, runtime)

    def modify_defense_rule_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseRuleStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_defense_rule_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_rule_status_with_options(request, runtime)

    def modify_defense_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplate',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_defense_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_template_with_options(request, runtime)

    def modify_defense_template_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseTemplateStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDefenseTemplateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_defense_template_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_template_status_with_options(request, runtime)

    def modify_domain_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = waf_openapi_20211001_models.ModifyDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.listen):
            request.listen_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.listen), 'Listen', 'json')
        if not UtilClient.is_unset(tmp_req.redirect):
            request.redirect_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.redirect), 'Redirect', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.listen_shrink):
            query['Listen'] = request.listen_shrink
        if not UtilClient.is_unset(request.redirect_shrink):
            query['Redirect'] = request.redirect_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    def modify_major_protection_black_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMajorProtectionBlackIp',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyMajorProtectionBlackIpResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_major_protection_black_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_major_protection_black_ip_with_options(request, runtime)

    def modify_resource_log_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyResourceLogStatus',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyResourceLogStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_resource_log_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_log_status_with_options(request, runtime)

    def modify_template_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_resource_groups):
            query['BindResourceGroups'] = request.bind_resource_groups
        if not UtilClient.is_unset(request.bind_resources):
            query['BindResources'] = request.bind_resources
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unbind_resource_groups):
            query['UnbindResourceGroups'] = request.unbind_resource_groups
        if not UtilClient.is_unset(request.unbind_resources):
            query['UnbindResources'] = request.unbind_resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplateResources',
            version='2021-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20211001_models.ModifyTemplateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_template_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_template_resources_with_options(request, runtime)
