# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dcdn20180115 import models as dcdn_20180115_models
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
            'ap-northeast-1': 'dcdn.aliyuncs.com',
            'ap-northeast-2-pop': 'dcdn.aliyuncs.com',
            'ap-south-1': 'dcdn.aliyuncs.com',
            'ap-southeast-1': 'dcdn.aliyuncs.com',
            'ap-southeast-2': 'dcdn.aliyuncs.com',
            'ap-southeast-3': 'dcdn.aliyuncs.com',
            'ap-southeast-5': 'dcdn.aliyuncs.com',
            'cn-beijing': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-1': 'dcdn.aliyuncs.com',
            'cn-beijing-finance-pop': 'dcdn.aliyuncs.com',
            'cn-beijing-gov-1': 'dcdn.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dcdn.aliyuncs.com',
            'cn-chengdu': 'dcdn.aliyuncs.com',
            'cn-edge-1': 'dcdn.aliyuncs.com',
            'cn-fujian': 'dcdn.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dcdn.aliyuncs.com',
            'cn-hangzhou': 'dcdn.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dcdn.aliyuncs.com',
            'cn-hangzhou-finance': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dcdn.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dcdn.aliyuncs.com',
            'cn-hangzhou-test-306': 'dcdn.aliyuncs.com',
            'cn-hongkong': 'dcdn.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dcdn.aliyuncs.com',
            'cn-huhehaote': 'dcdn.aliyuncs.com',
            'cn-north-2-gov-1': 'dcdn.aliyuncs.com',
            'cn-qingdao': 'dcdn.aliyuncs.com',
            'cn-qingdao-nebula': 'dcdn.aliyuncs.com',
            'cn-shanghai': 'dcdn.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dcdn.aliyuncs.com',
            'cn-shanghai-finance-1': 'dcdn.aliyuncs.com',
            'cn-shanghai-inner': 'dcdn.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen': 'dcdn.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dcdn.aliyuncs.com',
            'cn-shenzhen-inner': 'dcdn.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dcdn.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dcdn.aliyuncs.com',
            'cn-wuhan': 'dcdn.aliyuncs.com',
            'cn-yushanfang': 'dcdn.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou': 'dcdn.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dcdn.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dcdn.aliyuncs.com',
            'eu-central-1': 'dcdn.aliyuncs.com',
            'eu-west-1': 'dcdn.aliyuncs.com',
            'eu-west-1-oxs': 'dcdn.aliyuncs.com',
            'me-east-1': 'dcdn.aliyuncs.com',
            'rus-west-1-pop': 'dcdn.aliyuncs.com',
            'us-east-1': 'dcdn.aliyuncs.com',
            'us-west-1': 'dcdn.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dcdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_dcdn_domain_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_domain_with_options(request, runtime)

    def add_dcdn_ipa_domain_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
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
            action='AddDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.AddDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_dcdn_ipa_domain_with_options(request, runtime)

    def batch_add_dcdn_domain_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchAddDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_dcdn_domain_with_options(request, runtime)

    def batch_delete_dcdn_domain_configs_with_options(self, request, runtime):
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
            action='BatchDeleteDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchDeleteDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_dcdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_dcdn_domain_configs_with_options(request, runtime)

    def batch_set_dcdn_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
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
            action='BatchSetDcdnDomainCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_dcdn_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_certificate_with_options(request, runtime)

    def batch_set_dcdn_domain_configs_with_options(self, request, runtime):
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
            action='BatchSetDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_dcdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_domain_configs_with_options(request, runtime)

    def batch_set_dcdn_ipa_domain_configs_with_options(self, request, runtime):
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
            action='BatchSetDcdnIpaDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchSetDcdnIpaDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_dcdn_ipa_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_dcdn_ipa_domain_configs_with_options(request, runtime)

    def batch_start_dcdn_domain_with_options(self, request, runtime):
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
            action='BatchStartDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStartDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_dcdn_domain_with_options(request, runtime)

    def batch_stop_dcdn_domain_with_options(self, request, runtime):
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
            action='BatchStopDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.BatchStopDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_dcdn_domain_with_options(request, runtime)

    def check_dcdn_project_exist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDcdnProjectExist',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CheckDcdnProjectExistResponse(),
            self.call_api(params, req, runtime)
        )

    def check_dcdn_project_exist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_dcdn_project_exist_with_options(request, runtime)

    def commit_staging_routine_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitStagingRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CommitStagingRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def commit_staging_routine_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.commit_staging_routine_code_with_options(request, runtime)

    def create_dcdn_certificate_signing_request_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sans):
            query['SANs'] = request.sans
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDcdnCertificateSigningRequest',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnCertificateSigningRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dcdn_certificate_signing_request(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_certificate_signing_request_with_options(request, runtime)

    def create_dcdn_deliver_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.deliver):
            body['Deliver'] = request.deliver
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reports):
            body['Reports'] = request.reports
        if not UtilClient.is_unset(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dcdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_deliver_task_with_options(request, runtime)

    def create_dcdn_slsreal_time_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not UtilClient.is_unset(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not UtilClient.is_unset(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not UtilClient.is_unset(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnSLSRealTimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSLSRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dcdn_slsreal_time_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_slsreal_time_log_delivery_with_options(request, runtime)

    def create_dcdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dcdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dcdn_sub_task_with_options(request, runtime)

    def create_routine_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.CreateRoutineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_routine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_routine_with_options(request, runtime)

    def create_slr_and_sls_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlrAndSlsProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.CreateSlrAndSlsProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_slr_and_sls_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_slr_and_sls_project_with_options(request, runtime)

    def delete_dcdn_deliver_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_deliver_task_with_options(request, runtime)

    def delete_dcdn_domain_with_options(self, request, runtime):
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
            action='DeleteDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_domain_with_options(request, runtime)

    def delete_dcdn_ipa_domain_with_options(self, request, runtime):
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
            action='DeleteDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_domain_with_options(request, runtime)

    def delete_dcdn_ipa_specific_config_with_options(self, request, runtime):
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
            action='DeleteDcdnIpaSpecificConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnIpaSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_ipa_specific_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_ipa_specific_config_with_options(request, runtime)

    def delete_dcdn_real_time_log_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnRealTimeLogProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnRealTimeLogProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_real_time_log_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_real_time_log_project_with_options(request, runtime)

    def delete_dcdn_specific_config_with_options(self, request, runtime):
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
            action='DeleteDcdnSpecificConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_specific_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_config_with_options(request, runtime)

    def delete_dcdn_specific_staging_config_with_options(self, request, runtime):
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
            action='DeleteDcdnSpecificStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_specific_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_specific_staging_config_with_options(request, runtime)

    def delete_dcdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dcdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dcdn_sub_task_with_options(request, runtime)

    def delete_routine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_routine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_with_options(request, runtime)

    def delete_routine_code_revision_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_routine_code_revision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_code_revision_with_options(request, runtime)

    def delete_routine_conf_envs_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.DeleteRoutineConfEnvsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineConfEnvs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DeleteRoutineConfEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_routine_conf_envs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_conf_envs_with_options(request, runtime)

    def describe_dcdn_acl_fields_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnAclFields',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnAclFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_acl_fields(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_acl_fields_with_options(request, runtime)

    def describe_dcdn_bgp_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBgpBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_bgp_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_bps_data_with_options(request, runtime)

    def describe_dcdn_bgp_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBgpTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBgpTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_bgp_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_bgp_traffic_data_with_options(request, runtime)

    def describe_dcdn_blocked_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnBlockedRegions',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnBlockedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_blocked_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_blocked_regions_with_options(request, runtime)

    def describe_dcdn_certificate_detail_with_options(self, request, runtime):
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
            action='DescribeDcdnCertificateDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_detail_with_options(request, runtime)

    def describe_dcdn_certificate_list_with_options(self, request, runtime):
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
            action='DescribeDcdnCertificateList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_certificate_list_with_options(request, runtime)

    def describe_dcdn_config_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_group_id):
            query['ConfigGroupId'] = request.config_group_id
        if not UtilClient.is_unset(request.config_group_name):
            query['ConfigGroupName'] = request.config_group_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnConfigGroupDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_config_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_config_group_detail_with_options(request, runtime)

    def describe_dcdn_config_of_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnConfigOfVersion',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_config_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_config_of_version_with_options(request, runtime)

    def describe_dcdn_deleted_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDeletedDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeletedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_deleted_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deleted_domains_with_options(request, runtime)

    def describe_dcdn_deliver_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deliver_id):
            query['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDeliverList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDeliverListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_deliver_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_deliver_list_with_options(request, runtime)

    def describe_dcdn_domain_bps_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_by_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainByCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainByCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_by_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_by_certificate_with_options(request, runtime)

    def describe_dcdn_domain_cc_activity_log_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trigger_object):
            query['TriggerObject'] = request.trigger_object
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCcActivityLog',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCcActivityLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_cc_activity_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cc_activity_log_with_options(request, runtime)

    def describe_dcdn_domain_certificate_info_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainCertificateInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_certificate_info_with_options(request, runtime)

    def describe_dcdn_domain_cname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainCname',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainCnameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_cname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_cname_with_options(request, runtime)

    def describe_dcdn_domain_configs_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_configs_with_options(request, runtime)

    def describe_dcdn_domain_detail_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_detail_with_options(request, runtime)

    def describe_dcdn_domain_hit_rate_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_hit_rate_data_with_options(request, runtime)

    def describe_dcdn_domain_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_ipa_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
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
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_ipa_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
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
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainIpaTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIpaTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_ipa_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_ipa_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_isp_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainIspData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainIspDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_isp_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_isp_data_with_options(request, runtime)

    def describe_dcdn_domain_log_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainLog',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_log_with_options(request, runtime)

    def describe_dcdn_domain_multi_usage_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainMultiUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainMultiUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_multi_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_multi_usage_data_with_options(request, runtime)

    def describe_dcdn_domain_origin_bps_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainOriginBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_origin_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_origin_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainOriginTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainOriginTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_origin_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_origin_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_property_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainProperty',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_property_with_options(request, runtime)

    def describe_dcdn_domain_pv_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainPvData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_pv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_pv_data_with_options(request, runtime)

    def describe_dcdn_domain_qps_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainQpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_qps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeByteHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_byte_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_detail_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeDetailData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_detail_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_detail_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainRealTimeHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeQpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_qps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_req_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainRealTimeReqHitRateData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_req_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_src_bps_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainRealTimeSrcBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_src_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainRealTimeSrcHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_src_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainRealTimeSrcTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_src_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_src_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_real_time_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainRealTimeTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_real_time_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_real_time_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_region_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainRegionData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_region_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_region_data_with_options(request, runtime)

    def describe_dcdn_domain_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnDomainStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_staging_config_with_options(request, runtime)

    def describe_dcdn_domain_top_refer_visit_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainTopReferVisit',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_top_refer_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_refer_visit_with_options(request, runtime)

    def describe_dcdn_domain_top_url_visit_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainTopUrlVisit',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_top_url_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_top_url_visit_with_options(request, runtime)

    def describe_dcdn_domain_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_traffic_data_with_options(request, runtime)

    def describe_dcdn_domain_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.data_protocol):
            query['DataProtocol'] = request.data_protocol
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
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
            action='DescribeDcdnDomainUsageData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_usage_data_with_options(request, runtime)

    def describe_dcdn_domain_uv_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainUvData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_uv_data_with_options(request, runtime)

    def describe_dcdn_domain_websocket_bps_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainWebsocketBpsData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_bps_data_with_options(request, runtime)

    def describe_dcdn_domain_websocket_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainWebsocketHttpCodeData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_http_code_data_with_options(request, runtime)

    def describe_dcdn_domain_websocket_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDcdnDomainWebsocketTrafficData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnDomainWebsocketTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_domain_websocket_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_domain_websocket_traffic_data_with_options(request, runtime)

    def describe_dcdn_es_exception_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnEsExceptionData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnEsExceptionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_es_exception_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_es_exception_data_with_options(request, runtime)

    def describe_dcdn_es_execute_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnEsExecuteData',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnEsExecuteDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_es_execute_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_es_execute_data_with_options(request, runtime)

    def describe_dcdn_https_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnHttpsDomainList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnHttpsDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_https_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_https_domain_list_with_options(request, runtime)

    def describe_dcdn_ip_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip):
            query['IP'] = request.ip
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_ip_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ip_info_with_options(request, runtime)

    def describe_dcdn_ipa_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDcdnIpaDomainConfigs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_configs_with_options(request, runtime)

    def describe_dcdn_ipa_domain_detail_with_options(self, request, runtime):
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
            action='DescribeDcdnIpaDomainDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_ipa_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_domain_detail_with_options(request, runtime)

    def describe_dcdn_ipa_service_with_options(self, request, runtime):
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
            action='DescribeDcdnIpaService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_ipa_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_service_with_options(request, runtime)

    def describe_dcdn_ipa_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not UtilClient.is_unset(request.func_id):
            query['FuncId'] = request.func_id
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnIpaUserDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnIpaUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_ipa_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_ipa_user_domains_with_options(request, runtime)

    def describe_dcdn_real_time_delivery_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_real_time_delivery_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_real_time_delivery_field_with_options(request, runtime)

    def describe_dcdn_refresh_quota_with_options(self, request, runtime):
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
            action='DescribeDcdnRefreshQuota',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_refresh_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_quota_with_options(request, runtime)

    def describe_dcdn_refresh_task_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnRefreshTaskById',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_refresh_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_task_by_id_with_options(request, runtime)

    def describe_dcdn_refresh_tasks_with_options(self, request, runtime):
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
            action='DescribeDcdnRefreshTasks',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_refresh_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_refresh_tasks_with_options(request, runtime)

    def describe_dcdn_region_and_isp_with_options(self, request, runtime):
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
            action='DescribeDcdnRegionAndIsp',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnRegionAndIspResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_region_and_isp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_region_and_isp_with_options(request, runtime)

    def describe_dcdn_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.http_code):
            query['HttpCode'] = request.http_code
        if not UtilClient.is_unset(request.is_overseas):
            query['IsOverseas'] = request.is_overseas
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnReport',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_with_options(request, runtime)

    def describe_dcdn_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnReportList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_report_list_with_options(request, runtime)

    def describe_dcdn_slsrealtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSLSRealtimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSLSRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_slsrealtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    def describe_dcdn_smcertificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSMCertificateDetail',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSMCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_smcertificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_smcertificate_detail_with_options(request, runtime)

    def describe_dcdn_smcertificate_list_with_options(self, request, runtime):
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
            action='DescribeDcdnSMCertificateList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSMCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_smcertificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_smcertificate_list_with_options(request, runtime)

    def describe_dcdn_sec_func_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sec_func_type):
            query['SecFuncType'] = request.sec_func_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSecFuncInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecFuncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_sec_func_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_func_info_with_options(request, runtime)

    def describe_dcdn_sec_spec_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSecSpecInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSecSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_sec_spec_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sec_spec_info_with_options(request, runtime)

    def describe_dcdn_service_with_options(self, request, runtime):
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
            action='DescribeDcdnService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_service_with_options(request, runtime)

    def describe_dcdn_staging_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnStagingIp',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnStagingIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_staging_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_staging_ip_with_options(request, runtime)

    def describe_dcdn_sub_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnSubList',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnSubListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_sub_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_sub_list_with_options(request, runtime)

    def describe_dcdn_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeDcdnTagResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_tag_resources_with_options(request, runtime)

    def describe_dcdn_top_domains_by_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnTopDomainsByFlow',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_top_domains_by_flow_with_options(request, runtime)

    def describe_dcdn_user_bill_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDcdnUserBillHistory',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_bill_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_history_with_options(request, runtime)

    def describe_dcdn_user_bill_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeDcdnUserBillType',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserBillTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_bill_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_bill_type_with_options(request, runtime)

    def describe_dcdn_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_end_time):
            query['ChangeEndTime'] = request.change_end_time
        if not UtilClient.is_unset(request.change_start_time):
            query['ChangeStartTime'] = request.change_start_time
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserDomains',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_with_options(request, runtime)

    def describe_dcdn_user_domains_by_func_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.func_filter):
            query['FuncFilter'] = request.func_filter
        if not UtilClient.is_unset(request.func_id):
            query['FuncId'] = request.func_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeDcdnUserDomainsByFunc',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserDomainsByFuncResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_domains_by_func(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_domains_by_func_with_options(request, runtime)

    def describe_dcdn_user_quota_with_options(self, request, runtime):
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
            action='DescribeDcdnUserQuota',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_quota_with_options(request, runtime)

    def describe_dcdn_user_real_time_delivery_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_real_time_delivery_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    def describe_dcdn_user_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserResourcePackage',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_resource_package_with_options(request, runtime)

    def describe_dcdn_user_sec_drop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sec_func):
            query['SecFunc'] = request.sec_func
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserSecDrop',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_sec_drop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_with_options(request, runtime)

    def describe_dcdn_user_sec_drop_by_minute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.object):
            query['Object'] = request.object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sec_func):
            query['SecFunc'] = request.sec_func
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserSecDropByMinute',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserSecDropByMinuteResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_sec_drop_by_minute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_sec_drop_by_minute_with_options(request, runtime)

    def describe_dcdn_user_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnUserTags',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_user_tags_with_options(request, runtime)

    def describe_dcdn_verify_content_with_options(self, request, runtime):
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
            action='DescribeDcdnVerifyContent',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_verify_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_verify_content_with_options(request, runtime)

    def describe_dcdn_waf_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDcdnWafDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnWafDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdn_waf_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdn_waf_domain_with_options(request, runtime)

    def describe_dcdnsec_service_with_options(self, request, runtime):
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
            action='DescribeDcdnsecService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeDcdnsecServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dcdnsec_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dcdnsec_service_with_options(request, runtime)

    def describe_routine_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRoutine',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_routine(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_with_options(request, runtime)

    def describe_routine_canary_envs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoutineCanaryEnvs',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCanaryEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_routine_canary_envs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_canary_envs_with_options(request, runtime)

    def describe_routine_code_revision_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_routine_code_revision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_code_revision_with_options(request, runtime)

    def describe_routine_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoutineSpec',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_routine_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_spec_with_options(request, runtime)

    def describe_routine_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoutineUserInfo',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeRoutineUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_routine_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_routine_user_info_with_options(request, runtime)

    def describe_user_dcdn_ipa_status_with_options(self, request, runtime):
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
            action='DescribeUserDcdnIpaStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnIpaStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_dcdn_ipa_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_ipa_status_with_options(request, runtime)

    def describe_user_dcdn_status_with_options(self, request, runtime):
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
            action='DescribeUserDcdnStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserDcdnStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_dcdn_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_dcdn_status_with_options(request, runtime)

    def describe_user_er_status_with_options(self, request, runtime):
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
            action='DescribeUserErStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserErStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_er_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_er_status_with_options(request, runtime)

    def describe_user_logservice_status_with_options(self, request, runtime):
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
            action='DescribeUserLogserviceStatus',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.DescribeUserLogserviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_logservice_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_logservice_status_with_options(request, runtime)

    def edit_routine_conf_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.EditRoutineConfShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env_conf):
            request.env_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env_conf, 'EnvConf', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf_shrink):
            body['EnvConf'] = request.env_conf_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditRoutineConf',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.EditRoutineConfResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_routine_conf(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_routine_conf_with_options(request, runtime)

    def list_dcdn_real_time_delivery_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDcdnRealTimeDeliveryProject',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ListDcdnRealTimeDeliveryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dcdn_real_time_delivery_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dcdn_real_time_delivery_project_with_options(request, runtime)

    def modify_dcdn_domain_schdm_by_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.property):
            query['Property'] = request.property
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDCdnDomainSchdmByProperty',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.ModifyDCdnDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dcdn_domain_schdm_by_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dcdn_domain_schdm_by_property_with_options(request, runtime)

    def open_dcdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.websocket_bill_type):
            query['WebsocketBillType'] = request.websocket_bill_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDcdnService',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.OpenDcdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_dcdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_dcdn_service_with_options(request, runtime)

    def preload_dcdn_object_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
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
            action='PreloadDcdnObjectCaches',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PreloadDcdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def preload_dcdn_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preload_dcdn_object_caches_with_options(request, runtime)

    def publish_dcdn_staging_config_to_production_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishDcdnStagingConfigToProduction',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishDcdnStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_dcdn_staging_config_to_production(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_dcdn_staging_config_to_production_with_options(request, runtime)

    def publish_routine_code_revision_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.PublishRoutineCodeRevisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.envs):
            request.envs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.envs, 'Envs', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.envs_shrink):
            body['Envs'] = request.envs_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.select_code_revision):
            body['SelectCodeRevision'] = request.select_code_revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRoutineCodeRevision',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.PublishRoutineCodeRevisionResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_routine_code_revision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_routine_code_revision_with_options(request, runtime)

    def refresh_dcdn_object_caches_with_options(self, request, runtime):
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
            action='RefreshDcdnObjectCaches',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RefreshDcdnObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_dcdn_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_dcdn_object_caches_with_options(request, runtime)

    def rollback_dcdn_staging_config_with_options(self, request, runtime):
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
            action='RollbackDcdnStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.RollbackDcdnStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_dcdn_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_dcdn_staging_config_with_options(request, runtime)

    def set_dcdn_config_of_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.function_args):
            query['FunctionArgs'] = request.function_args
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnConfigOfVersion',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_config_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_config_of_version_with_options(request, runtime)

    def set_dcdn_domain_csrcertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainCSRCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCSRCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_domain_csrcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_csrcertificate_with_options(request, runtime)

    def set_dcdn_domain_certificate_with_options(self, request, runtime):
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
            action='SetDcdnDomainCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_certificate_with_options(request, runtime)

    def set_dcdn_domain_smcertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainSMCertificate',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainSMCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_domain_smcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_smcertificate_with_options(request, runtime)

    def set_dcdn_domain_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDcdnDomainStagingConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_domain_staging_config_with_options(request, runtime)

    def set_dcdn_full_domains_block_ipwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.block_interval):
            body['BlockInterval'] = request.block_interval
        if not UtilClient.is_unset(request.iplist):
            body['IPList'] = request.iplist
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDcdnFullDomainsBlockIP',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnFullDomainsBlockIPResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_full_domains_block_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_full_domains_block_ipwith_options(request, runtime)

    def set_dcdn_user_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
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
            action='SetDcdnUserConfig',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetDcdnUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_dcdn_user_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_dcdn_user_config_with_options(request, runtime)

    def set_routine_subdomain_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dcdn_20180115_models.SetRoutineSubdomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.subdomains):
            request.subdomains_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subdomains, 'Subdomains', 'json')
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.subdomains_shrink):
            body['Subdomains'] = request.subdomains_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetRoutineSubdomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.SetRoutineSubdomainResponse(),
            self.call_api(params, req, runtime)
        )

    def set_routine_subdomain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_routine_subdomain_with_options(request, runtime)

    def start_dcdn_domain_with_options(self, request, runtime):
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
            action='StartDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_domain_with_options(request, runtime)

    def start_dcdn_ipa_domain_with_options(self, request, runtime):
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
            action='StartDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StartDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def start_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dcdn_ipa_domain_with_options(request, runtime)

    def stop_dcdn_domain_with_options(self, request, runtime):
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
            action='StopDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_domain_with_options(request, runtime)

    def stop_dcdn_ipa_domain_with_options(self, request, runtime):
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
            action='StopDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.StopDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dcdn_ipa_domain_with_options(request, runtime)

    def tag_dcdn_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='TagDcdnResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.TagDcdnResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_dcdn_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_dcdn_resources_with_options(request, runtime)

    def untag_dcdn_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='UntagDcdnResources',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UntagDcdnResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_dcdn_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_dcdn_resources_with_options(request, runtime)

    def update_dcdn_deliver_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.deliver):
            body['Deliver'] = request.deliver
        if not UtilClient.is_unset(request.deliver_id):
            body['DeliverId'] = request.deliver_id
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reports):
            body['Reports'] = request.reports
        if not UtilClient.is_unset(request.schedule):
            body['Schedule'] = request.schedule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnDeliverTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dcdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_deliver_task_with_options(request, runtime)

    def update_dcdn_domain_with_options(self, request, runtime):
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
            action='UpdateDcdnDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dcdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_domain_with_options(request, runtime)

    def update_dcdn_ipa_domain_with_options(self, request, runtime):
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
            action='UpdateDcdnIpaDomain',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnIpaDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dcdn_ipa_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_ipa_domain_with_options(request, runtime)

    def update_dcdn_slsrealtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.slslog_store):
            body['SLSLogStore'] = request.slslog_store
        if not UtilClient.is_unset(request.slsproject):
            body['SLSProject'] = request.slsproject
        if not UtilClient.is_unset(request.slsregion):
            body['SLSRegion'] = request.slsregion
        if not UtilClient.is_unset(request.sampling_rate):
            body['SamplingRate'] = request.sampling_rate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnSLSRealtimeLogDelivery',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSLSRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dcdn_slsrealtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_slsrealtime_log_delivery_with_options(request, runtime)

    def update_dcdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.report_ids):
            body['ReportIds'] = request.report_ids
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDcdnSubTask',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dcdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_sub_task_with_options(request, runtime)

    def update_dcdn_user_real_time_delivery_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDcdnUserRealTimeDeliveryField',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UpdateDcdnUserRealTimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dcdn_user_real_time_delivery_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dcdn_user_real_time_delivery_field_with_options(request, runtime)

    def upload_routine_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_routine_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_routine_code_with_options(request, runtime)

    def upload_staging_routine_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadStagingRoutineCode',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.UploadStagingRoutineCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_staging_routine_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_staging_routine_code_with_options(request, runtime)

    def verify_dcdn_domain_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyDcdnDomainOwner',
            version='2018-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dcdn_20180115_models.VerifyDcdnDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_dcdn_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_dcdn_domain_owner_with_options(request, runtime)
