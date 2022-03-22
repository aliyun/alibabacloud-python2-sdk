# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_scdn20171115 import models as scdn_20171115_models
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
            'ap-northeast-1': 'scdn.aliyuncs.com',
            'ap-northeast-2-pop': 'scdn.aliyuncs.com',
            'ap-south-1': 'scdn.aliyuncs.com',
            'ap-southeast-1': 'scdn.aliyuncs.com',
            'ap-southeast-2': 'scdn.aliyuncs.com',
            'ap-southeast-3': 'scdn.aliyuncs.com',
            'ap-southeast-5': 'scdn.aliyuncs.com',
            'cn-beijing': 'scdn.aliyuncs.com',
            'cn-beijing-finance-1': 'scdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'scdn.aliyuncs.com',
            'cn-beijing-gov-1': 'scdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'scdn.aliyuncs.com',
            'cn-chengdu': 'scdn.aliyuncs.com',
            'cn-edge-1': 'scdn.aliyuncs.com',
            'cn-fujian': 'scdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'scdn.aliyuncs.com',
            'cn-hangzhou': 'scdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'scdn.aliyuncs.com',
            'cn-hangzhou-finance': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'scdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'scdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'scdn.aliyuncs.com',
            'cn-hongkong': 'scdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'scdn.aliyuncs.com',
            'cn-huhehaote': 'scdn.aliyuncs.com',
            'cn-north-2-gov-1': 'scdn.aliyuncs.com',
            'cn-qingdao': 'scdn.aliyuncs.com',
            'cn-qingdao-nebula': 'scdn.aliyuncs.com',
            'cn-shanghai': 'scdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'scdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'scdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'scdn.aliyuncs.com',
            'cn-shanghai-inner': 'scdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'scdn.aliyuncs.com',
            'cn-shenzhen': 'scdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'scdn.aliyuncs.com',
            'cn-shenzhen-inner': 'scdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'scdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'scdn.aliyuncs.com',
            'cn-wuhan': 'scdn.aliyuncs.com',
            'cn-yushanfang': 'scdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'scdn.aliyuncs.com',
            'cn-zhangjiakou': 'scdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'scdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'scdn.aliyuncs.com',
            'eu-central-1': 'scdn.aliyuncs.com',
            'eu-west-1': 'scdn.aliyuncs.com',
            'eu-west-1-oxs': 'scdn.aliyuncs.com',
            'me-east-1': 'scdn.aliyuncs.com',
            'rus-west-1-pop': 'scdn.aliyuncs.com',
            'us-east-1': 'scdn.aliyuncs.com',
            'us-west-1': 'scdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('scdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.AddScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_scdn_domain_with_options(request, runtime)

    def batch_delete_scdn_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchDeleteScdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_scdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_scdn_domain_configs_with_options(request, runtime)

    def batch_set_scdn_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchSetScdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_scdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_scdn_domain_configs_with_options(request, runtime)

    def batch_start_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchStartScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_scdn_domain_with_options(request, runtime)

    def batch_stop_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchStopScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_scdn_domain_with_options(request, runtime)

    def batch_update_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.BatchUpdateScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_scdn_domain_with_options(request, runtime)

    def check_scdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.CheckScdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_scdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_scdn_service_with_options(request, runtime)

    def delete_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DeleteScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scdn_domain_with_options(request, runtime)

    def delete_scdn_specific_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScdnSpecificConfig',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DeleteScdnSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scdn_specific_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scdn_specific_config_with_options(request, runtime)

    def describe_scdn_cc_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_cc_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_info_with_options(request, runtime)

    def describe_scdn_cc_qps_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcQpsInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcQpsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_cc_qps_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_qps_info_with_options(request, runtime)

    def describe_scdn_cc_top_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcTopIp',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcTopIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_cc_top_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_top_ip_with_options(request, runtime)

    def describe_scdn_cc_top_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCcTopUrl',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCcTopUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_cc_top_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_cc_top_url_with_options(request, runtime)

    def describe_scdn_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCertificateDetail',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_certificate_detail_with_options(request, runtime)

    def describe_scdn_certificate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnCertificateList',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_certificate_list_with_options(request, runtime)

    def describe_scdn_ddo_sinfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDDoSInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDDoSInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_ddo_sinfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_ddo_sinfo_with_options(request, runtime)

    def describe_scdn_ddo_straffic_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDDoSTrafficInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDDoSTrafficInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_ddo_straffic_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_ddo_straffic_info_with_options(request, runtime)

    def describe_scdn_domain_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_bps_data_with_options(request, runtime)

    def describe_scdn_domain_certificate_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainCertificateInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_certificate_info_with_options(request, runtime)

    def describe_scdn_domain_cname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainCname',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_cname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_cname_with_options(request, runtime)

    def describe_scdn_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainConfigs',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_configs_with_options(request, runtime)

    def describe_scdn_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainDetail',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_detail_with_options(request, runtime)

    def describe_scdn_domain_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_hit_rate_data_with_options(request, runtime)

    def describe_scdn_domain_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainHttpCodeData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_http_code_data_with_options(request, runtime)

    def describe_scdn_domain_isp_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainIspData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainIspDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_isp_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_isp_data_with_options(request, runtime)

    def describe_scdn_domain_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeScdnDomainLog',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_log_with_options(request, runtime)

    def describe_scdn_domain_origin_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainOriginBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainOriginBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_origin_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_origin_bps_data_with_options(request, runtime)

    def describe_scdn_domain_origin_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainOriginTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainOriginTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_origin_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_origin_traffic_data_with_options(request, runtime)

    def describe_scdn_domain_pv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainPvData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_pv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_pv_data_with_options(request, runtime)

    def describe_scdn_domain_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainQpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_qps_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_bps_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_byte_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeByteHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_byte_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeHttpCodeData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_http_code_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeQpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_qps_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_req_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeReqHitRateData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_req_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_src_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeSrcBpsData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_src_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_src_bps_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_src_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeSrcTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_src_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    def describe_scdn_domain_real_time_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRealTimeTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_real_time_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_real_time_traffic_data_with_options(request, runtime)

    def describe_scdn_domain_region_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainRegionData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_region_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_region_data_with_options(request, runtime)

    def describe_scdn_domain_top_refer_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTopReferVisit',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_top_refer_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_top_refer_visit_with_options(request, runtime)

    def describe_scdn_domain_top_url_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTopUrlVisit',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_top_url_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_top_url_visit_with_options(request, runtime)

    def describe_scdn_domain_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainTrafficData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_traffic_data_with_options(request, runtime)

    def describe_scdn_domain_uv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnDomainUvData',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_domain_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_domain_uv_data_with_options(request, runtime)

    def describe_scdn_refresh_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnRefreshQuota',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_refresh_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_refresh_quota_with_options(request, runtime)

    def describe_scdn_refresh_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnRefreshTasks',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_refresh_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_refresh_tasks_with_options(request, runtime)

    def describe_scdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_service_with_options(request, runtime)

    def describe_scdn_top_domains_by_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnTopDomainsByFlow',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_top_domains_by_flow_with_options(request, runtime)

    def describe_scdn_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserDomains',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_domains_with_options(request, runtime)

    def describe_scdn_user_protect_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserProtectInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserProtectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_user_protect_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_protect_info_with_options(request, runtime)

    def describe_scdn_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScdnUserQuota',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.DescribeScdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scdn_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scdn_user_quota_with_options(request, runtime)

    def open_scdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cc_protection):
            query['CcProtection'] = request.cc_protection
        if not UtilClient.is_unset(request.ddo_sbasic):
            query['DDoSBasic'] = request.ddo_sbasic
        if not UtilClient.is_unset(request.domain_count):
            query['DomainCount'] = request.domain_count
        if not UtilClient.is_unset(request.elastic_protection):
            query['ElasticProtection'] = request.elastic_protection
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protect_type):
            query['ProtectType'] = request.protect_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenScdnService',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.OpenScdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_scdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_scdn_service_with_options(request, runtime)

    def preload_scdn_object_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreloadScdnObjectCaches',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.PreloadScdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def preload_scdn_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preload_scdn_object_caches_with_options(request, runtime)

    def refresh_scdn_object_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshScdnObjectCaches',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.RefreshScdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_scdn_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_scdn_object_caches_with_options(request, runtime)

    def set_scdn_bot_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnBotInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnBotInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scdn_bot_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_bot_info_with_options(request, runtime)

    def set_scdn_cc_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnCcInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnCcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scdn_cc_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_cc_info_with_options(request, runtime)

    def set_scdn_ddo_sinfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDDoSInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDDoSInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scdn_ddo_sinfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_ddo_sinfo_with_options(request, runtime)

    def set_scdn_domain_biz_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDomainBizInfo',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDomainBizInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scdn_domain_biz_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_domain_biz_info_with_options(request, runtime)

    def set_scdn_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetScdnDomainCertificate',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.SetScdnDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scdn_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scdn_domain_certificate_with_options(request, runtime)

    def start_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.StartScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def start_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_scdn_domain_with_options(request, runtime)

    def stop_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.StopScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_scdn_domain_with_options(request, runtime)

    def update_scdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScdnDomain',
            version='2017-11-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            scdn_20171115_models.UpdateScdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scdn_domain_with_options(request, runtime)
