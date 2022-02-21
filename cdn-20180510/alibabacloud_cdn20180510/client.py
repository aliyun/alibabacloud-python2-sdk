# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdn20180510 import models as cdn_20180510_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'cdn.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action='AddCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.AddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cdn_domain_with_options(request, runtime)

    def add_fctrigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not UtilClient.is_unset(request.event_meta_name):
            body['EventMetaName'] = request.event_meta_name
        if not UtilClient.is_unset(request.event_meta_version):
            body['EventMetaVersion'] = request.event_meta_version
        if not UtilClient.is_unset(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not UtilClient.is_unset(request.notes):
            body['Notes'] = request.notes
        if not UtilClient.is_unset(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.AddFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def add_fctrigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_fctrigger_with_options(request, runtime)

    def batch_add_cdn_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
            action='BatchAddCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchAddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_cdn_domain_with_options(request, runtime)

    def batch_delete_cdn_domain_config_with_options(self, request, runtime):
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
            action='BatchDeleteCdnDomainConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchDeleteCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_cdn_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_cdn_domain_config_with_options(request, runtime)

    def batch_set_cdn_domain_config_with_options(self, request, runtime):
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
            action='BatchSetCdnDomainConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchSetCdnDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_cdn_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_cdn_domain_config_with_options(request, runtime)

    def batch_set_cdn_domain_server_certificate_with_options(self, request, runtime):
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
            action='BatchSetCdnDomainServerCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchSetCdnDomainServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_cdn_domain_server_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_cdn_domain_server_certificate_with_options(request, runtime)

    def batch_start_cdn_domain_with_options(self, request, runtime):
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
            action='BatchStartCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchStartCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_cdn_domain_with_options(request, runtime)

    def batch_stop_cdn_domain_with_options(self, request, runtime):
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
            action='BatchStopCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchStopCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_cdn_domain_with_options(request, runtime)

    def batch_update_cdn_domain_with_options(self, request, runtime):
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
            action='BatchUpdateCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.BatchUpdateCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_cdn_domain_with_options(request, runtime)

    def create_cdn_certificate_signing_request_with_options(self, request, runtime):
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
            action='CreateCdnCertificateSigningRequest',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnCertificateSigningRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cdn_certificate_signing_request(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_certificate_signing_request_with_options(request, runtime)

    def create_cdn_compute_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdnComputeDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnComputeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cdn_compute_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_compute_domain_with_options(request, runtime)

    def create_cdn_deliver_task_with_options(self, request, runtime):
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
            action='CreateCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_deliver_task_with_options(request, runtime)

    def create_cdn_sub_task_with_options(self, request, runtime):
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
            action='CreateCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cdn_sub_task_with_options(request, runtime)

    def create_illegal_url_export_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIllegalUrlExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateIllegalUrlExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_illegal_url_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_illegal_url_export_task_with_options(request, runtime)

    def create_real_time_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRealTimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_real_time_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_real_time_log_delivery_with_options(request, runtime)

    def create_usage_detail_data_export_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group):
            query['Group'] = request.group
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_usage_detail_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_usage_detail_data_export_task_with_options(request, runtime)

    def create_user_usage_data_export_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.CreateUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_usage_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_usage_data_export_task_with_options(request, runtime)

    def delete_cdn_deliver_task_with_options(self, request, runtime):
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
            action='DeleteCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_deliver_task_with_options(request, runtime)

    def delete_cdn_domain_with_options(self, request, runtime):
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
            action='DeleteCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_domain_with_options(request, runtime)

    def delete_cdn_sub_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cdn_sub_task_with_options(request, runtime)

    def delete_fctrigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_fctrigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_fctrigger_with_options(request, runtime)

    def delete_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_realtime_log_delivery_with_options(request, runtime)

    def delete_specific_config_with_options(self, request, runtime):
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
            action='DeleteSpecificConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_specific_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_specific_config_with_options(request, runtime)

    def delete_specific_staging_config_with_options(self, request, runtime):
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
            action='DeleteSpecificStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_specific_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_specific_staging_config_with_options(request, runtime)

    def delete_usage_detail_data_export_task_with_options(self, request, runtime):
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
            action='DeleteUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_usage_detail_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_usage_detail_data_export_task_with_options(request, runtime)

    def delete_user_usage_data_export_task_with_options(self, request, runtime):
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
            action='DeleteUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DeleteUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_usage_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_usage_data_export_task_with_options(request, runtime)

    def describe_active_version_of_config_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_group_id):
            query['ConfigGroupId'] = request.config_group_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveVersionOfConfigGroup',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeActiveVersionOfConfigGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_active_version_of_config_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_version_of_config_group_with_options(request, runtime)

    def describe_blocked_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlockedRegions',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeBlockedRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_blocked_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_blocked_regions_with_options(request, runtime)

    def describe_cdn_certificate_detail_with_options(self, request, runtime):
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
            action='DescribeCdnCertificateDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_detail_with_options(request, runtime)

    def describe_cdn_certificate_list_with_options(self, request, runtime):
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
            action='DescribeCdnCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_certificate_list_with_options(request, runtime)

    def describe_cdn_compute_user_domain_with_options(self, request, runtime):
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
            action='DescribeCdnComputeUserDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnComputeUserDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_compute_user_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_compute_user_domain_with_options(request, runtime)

    def describe_cdn_deleted_domains_with_options(self, request, runtime):
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
            action='DescribeCdnDeletedDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDeletedDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_deleted_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_deleted_domains_with_options(request, runtime)

    def describe_cdn_deliver_list_with_options(self, request, runtime):
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
            action='DescribeCdnDeliverList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDeliverListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_deliver_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_deliver_list_with_options(request, runtime)

    def describe_cdn_domain_by_certificate_with_options(self, request, runtime):
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
            action='DescribeCdnDomainByCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainByCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_domain_by_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_by_certificate_with_options(request, runtime)

    def describe_cdn_domain_configs_with_options(self, request, runtime):
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
            action='DescribeCdnDomainConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_configs_with_options(request, runtime)

    def describe_cdn_domain_detail_with_options(self, request, runtime):
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
            action='DescribeCdnDomainDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_detail_with_options(request, runtime)

    def describe_cdn_domain_logs_with_options(self, request, runtime):
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
            action='DescribeCdnDomainLogs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_domain_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_logs_with_options(request, runtime)

    def describe_cdn_domain_staging_config_with_options(self, request, runtime):
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
            action='DescribeCdnDomainStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_staging_config_with_options(request, runtime)

    def describe_cdn_https_domain_list_with_options(self, request, runtime):
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
            action='DescribeCdnHttpsDomainList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnHttpsDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_https_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_https_domain_list_with_options(request, runtime)

    def describe_cdn_region_and_isp_with_options(self, request, runtime):
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
            action='DescribeCdnRegionAndIsp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnRegionAndIspResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_region_and_isp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_region_and_isp_with_options(request, runtime)

    def describe_cdn_report_with_options(self, request, runtime):
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
            action='DescribeCdnReport',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_report_with_options(request, runtime)

    def describe_cdn_report_list_with_options(self, request, runtime):
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
            action='DescribeCdnReportList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnReportListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_report_list_with_options(request, runtime)

    def describe_cdn_smcertificate_detail_with_options(self, request, runtime):
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
            action='DescribeCdnSMCertificateDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSMCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_smcertificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_smcertificate_detail_with_options(request, runtime)

    def describe_cdn_smcertificate_list_with_options(self, request, runtime):
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
            action='DescribeCdnSMCertificateList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSMCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_smcertificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_smcertificate_list_with_options(request, runtime)

    def describe_cdn_service_with_options(self, request, runtime):
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
            action='DescribeCdnService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_service_with_options(request, runtime)

    def describe_cdn_sub_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnSubList',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnSubListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_sub_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_sub_list_with_options(request, runtime)

    def describe_cdn_user_bill_history_with_options(self, request, runtime):
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
            action='DescribeCdnUserBillHistory',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_bill_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_history_with_options(request, runtime)

    def describe_cdn_user_bill_prediction_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
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
            action='DescribeCdnUserBillPrediction',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillPredictionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_bill_prediction(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_prediction_with_options(request, runtime)

    def describe_cdn_user_bill_type_with_options(self, request, runtime):
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
            action='DescribeCdnUserBillType',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserBillTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_bill_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_bill_type_with_options(request, runtime)

    def describe_cdn_user_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnUserConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_configs_with_options(request, runtime)

    def describe_cdn_user_domains_by_func_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeCdnUserDomainsByFunc',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserDomainsByFuncResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_domains_by_func(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_domains_by_func_with_options(request, runtime)

    def describe_cdn_user_quota_with_options(self, request, runtime):
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
            action='DescribeCdnUserQuota',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_quota_with_options(request, runtime)

    def describe_cdn_user_resource_package_with_options(self, request, runtime):
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
            action='DescribeCdnUserResourcePackage',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_user_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_user_resource_package_with_options(request, runtime)

    def describe_cdn_waf_domain_with_options(self, request, runtime):
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
            action='DescribeCdnWafDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCdnWafDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cdn_waf_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_waf_domain_with_options(request, runtime)

    def describe_certificate_info_by_idwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificateInfoByID',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCertificateInfoByIDResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_certificate_info_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_info_by_idwith_options(request, runtime)

    def describe_config_group_detail_with_options(self, request, runtime):
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
            action='DescribeConfigGroupDetail',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeConfigGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_config_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_config_group_detail_with_options(request, runtime)

    def describe_config_of_version_with_options(self, request, runtime):
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
            action='DescribeConfigOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_config_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_config_of_version_with_options(request, runtime)

    def describe_custom_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_log_config_with_options(request, runtime)

    def describe_domain_average_response_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
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
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAverageResponseTime',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainAverageResponseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_average_response_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_average_response_time_with_options(request, runtime)

    def describe_domain_bps_data_with_options(self, request, runtime):
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
            action='DescribeDomainBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_with_options(request, runtime)

    def describe_domain_bps_data_by_layer_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
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
            action='DescribeDomainBpsDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_bps_data_by_layer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_layer_with_options(request, runtime)

    def describe_domain_bps_data_by_time_stamp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByTimeStamp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainBpsDataByTimeStampResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_bps_data_by_time_stamp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_time_stamp_with_options(request, runtime)

    def describe_domain_cc_activity_log_with_options(self, request, runtime):
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
            action='DescribeDomainCcActivityLog',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCcActivityLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_cc_activity_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_cc_activity_log_with_options(request, runtime)

    def describe_domain_certificate_info_with_options(self, request, runtime):
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
            action='DescribeDomainCertificateInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_certificate_info_with_options(request, runtime)

    def describe_domain_custom_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_custom_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_custom_log_config_with_options(request, runtime)

    def describe_domain_detail_data_by_layer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainDetailDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainDetailDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_detail_data_by_layer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_detail_data_by_layer_with_options(request, runtime)

    def describe_domain_file_size_proportion_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFileSizeProportionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainFileSizeProportionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_file_size_proportion_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_file_size_proportion_data_with_options(request, runtime)

    def describe_domain_hit_rate_data_with_options(self, request, runtime):
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
            action='DescribeDomainHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_hit_rate_data_with_options(request, runtime)

    def describe_domain_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDomainHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_with_options(request, runtime)

    def describe_domain_http_code_data_by_layer_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
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
            action='DescribeDomainHttpCodeDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainHttpCodeDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_http_code_data_by_layer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_by_layer_with_options(request, runtime)

    def describe_domain_ispdata_with_options(self, request, runtime):
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
            action='DescribeDomainISPData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainISPDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_ispdata(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ispdata_with_options(request, runtime)

    def describe_domain_max_95bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle):
            query['Cycle'] = request.cycle
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainMax95BpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainMax95BpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_max_95bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_max_95bps_data_with_options(request, runtime)

    def describe_domain_multi_usage_data_with_options(self, request, runtime):
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
            action='DescribeDomainMultiUsageData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainMultiUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_multi_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_multi_usage_data_with_options(request, runtime)

    def describe_domain_names_of_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNamesOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainNamesOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_names_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_of_version_with_options(request, runtime)

    def describe_domain_path_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainPathData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainPathDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_path_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_path_data_with_options(request, runtime)

    def describe_domain_pv_data_with_options(self, request, runtime):
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
            action='DescribeDomainPvData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_pv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_pv_data_with_options(request, runtime)

    def describe_domain_qps_data_with_options(self, request, runtime):
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
            action='DescribeDomainQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_with_options(request, runtime)

    def describe_domain_qps_data_by_layer_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
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
            action='DescribeDomainQpsDataByLayer',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainQpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_qps_data_by_layer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_by_layer_with_options(request, runtime)

    def describe_domain_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_bps_data_with_options(request, runtime)

    def describe_domain_real_time_byte_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeByteHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_byte_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    def describe_domain_real_time_detail_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeDetailData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_detail_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_detail_data_with_options(request, runtime)

    def describe_domain_real_time_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDomainRealTimeHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_http_code_data_with_options(request, runtime)

    def describe_domain_real_time_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_qps_data_with_options(request, runtime)

    def describe_domain_real_time_req_hit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealTimeReqHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_req_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    def describe_domain_real_time_src_bps_data_with_options(self, request, runtime):
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
            action='DescribeDomainRealTimeSrcBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_src_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_bps_data_with_options(request, runtime)

    def describe_domain_real_time_src_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDomainRealTimeSrcHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_src_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_http_code_data_with_options(request, runtime)

    def describe_domain_real_time_src_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDomainRealTimeSrcTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_src_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_src_traffic_data_with_options(request, runtime)

    def describe_domain_real_time_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDomainRealTimeTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_real_time_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_real_time_traffic_data_with_options(request, runtime)

    def describe_domain_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_realtime_log_delivery_with_options(request, runtime)

    def describe_domain_region_data_with_options(self, request, runtime):
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
            action='DescribeDomainRegionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_region_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_region_data_with_options(request, runtime)

    def describe_domain_req_hit_rate_data_with_options(self, request, runtime):
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
            action='DescribeDomainReqHitRateData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_req_hit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_req_hit_rate_data_with_options(request, runtime)

    def describe_domain_src_bps_data_with_options(self, request, runtime):
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
            action='DescribeDomainSrcBpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_src_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_bps_data_with_options(request, runtime)

    def describe_domain_src_http_code_data_with_options(self, request, runtime):
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
            action='DescribeDomainSrcHttpCodeData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_src_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_http_code_data_with_options(request, runtime)

    def describe_domain_src_qps_data_with_options(self, request, runtime):
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
            action='DescribeDomainSrcQpsData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_src_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_qps_data_with_options(request, runtime)

    def describe_domain_src_top_url_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDomainSrcTopUrlVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_src_top_url_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_top_url_visit_with_options(request, runtime)

    def describe_domain_src_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDomainSrcTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_src_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_traffic_data_with_options(request, runtime)

    def describe_domain_top_client_ip_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
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
            action='DescribeDomainTopClientIpVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopClientIpVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_top_client_ip_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_client_ip_visit_with_options(request, runtime)

    def describe_domain_top_refer_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.percent):
            query['Percent'] = request.percent
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainTopReferVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopReferVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_top_refer_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_refer_visit_with_options(request, runtime)

    def describe_domain_top_url_visit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDomainTopUrlVisit',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTopUrlVisitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_top_url_visit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_top_url_visit_with_options(request, runtime)

    def describe_domain_traffic_data_with_options(self, request, runtime):
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
            action='DescribeDomainTrafficData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_traffic_data_with_options(request, runtime)

    def describe_domain_usage_data_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUsageData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_usage_data_with_options(request, runtime)

    def describe_domain_uv_data_with_options(self, request, runtime):
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
            action='DescribeDomainUvData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_uv_data_with_options(request, runtime)

    def describe_domains_by_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsBySource',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainsBySourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domains_by_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_by_source_with_options(request, runtime)

    def describe_domains_usage_by_day_with_options(self, request, runtime):
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
            action='DescribeDomainsUsageByDay',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeDomainsUsageByDayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domains_usage_by_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_usage_by_day_with_options(request, runtime)

    def describe_es_exception_data_with_options(self, request, runtime):
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
            action='DescribeEsExceptionData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeEsExceptionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_es_exception_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_es_exception_data_with_options(request, runtime)

    def describe_es_execute_data_with_options(self, request, runtime):
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
            action='DescribeEsExecuteData',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeEsExecuteDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_es_execute_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_es_execute_data_with_options(request, runtime)

    def describe_fctrigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fctrigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fctrigger_with_options(request, runtime)

    def describe_illegal_url_export_task_with_options(self, request, runtime):
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
            action='DescribeIllegalUrlExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeIllegalUrlExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_illegal_url_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_illegal_url_export_task_with_options(request, runtime)

    def describe_ip_info_with_options(self, request, runtime):
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
            action='DescribeIpInfo',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeIpInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_info_with_options(request, runtime)

    def describe_l2vips_by_domain_with_options(self, request, runtime):
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
            action='DescribeL2VipsByDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeL2VipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_l2vips_by_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_l2vips_by_domain_with_options(request, runtime)

    def describe_range_data_by_locate_and_isp_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRangeDataByLocateAndIspService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRangeDataByLocateAndIspServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_range_data_by_locate_and_isp_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_range_data_by_locate_and_isp_service_with_options(request, runtime)

    def describe_realtime_delivery_acc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRealtimeDeliveryAcc',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRealtimeDeliveryAccResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_realtime_delivery_acc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_realtime_delivery_acc_with_options(request, runtime)

    def describe_refresh_quota_with_options(self, request, runtime):
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
            action='DescribeRefreshQuota',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_refresh_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_quota_with_options(request, runtime)

    def describe_refresh_task_by_id_with_options(self, request, runtime):
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
            action='DescribeRefreshTaskById',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshTaskByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_refresh_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_task_by_id_with_options(request, runtime)

    def describe_refresh_tasks_with_options(self, request, runtime):
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
            action='DescribeRefreshTasks',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_refresh_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_tasks_with_options(request, runtime)

    def describe_staging_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStagingIp',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeStagingIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_staging_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_staging_ip_with_options(request, runtime)

    def describe_tag_resources_with_options(self, request, runtime):
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
            action='DescribeTagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_resources_with_options(request, runtime)

    def describe_top_domains_by_flow_with_options(self, request, runtime):
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
            action='DescribeTopDomainsByFlow',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_domains_by_flow_with_options(request, runtime)

    def describe_user_certificate_expire_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserCertificateExpireCount',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserCertificateExpireCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_certificate_expire_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_certificate_expire_count_with_options(request, runtime)

    def describe_user_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserConfigs',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_configs_with_options(request, runtime)

    def describe_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
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
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_domains_with_options(request, runtime)

    def describe_user_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserTags',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_tags_with_options(request, runtime)

    def describe_user_usage_data_export_task_with_options(self, request, runtime):
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
            action='DescribeUserUsageDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserUsageDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_usage_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_usage_data_export_task_with_options(request, runtime)

    def describe_user_usage_detail_data_export_task_with_options(self, request, runtime):
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
            action='DescribeUserUsageDetailDataExportTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserUsageDetailDataExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_usage_detail_data_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_usage_detail_data_export_task_with_options(request, runtime)

    def describe_user_vips_by_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserVipsByDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeUserVipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_vips_by_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_vips_by_domain_with_options(request, runtime)

    def describe_verify_content_with_options(self, request, runtime):
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
            action='DescribeVerifyContent',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DescribeVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_verify_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_content_with_options(request, runtime)

    def disable_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.DisableRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_realtime_log_delivery_with_options(request, runtime)

    def enable_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.EnableRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_realtime_log_delivery_with_options(request, runtime)

    def list_domains_by_log_config_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomainsByLogConfigId',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListDomainsByLogConfigIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_domains_by_log_config_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_domains_by_log_config_id_with_options(request, runtime)

    def list_fctrigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def list_fctrigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_fctrigger_with_options(request, runtime)

    def list_realtime_log_delivery_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRealtimeLogDeliveryDomains',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListRealtimeLogDeliveryDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_realtime_log_delivery_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_log_delivery_domains_with_options(request, runtime)

    def list_realtime_log_delivery_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRealtimeLogDeliveryInfos',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListRealtimeLogDeliveryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_realtime_log_delivery_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_log_delivery_infos_with_options(request, runtime)

    def list_user_custom_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ListUserCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_custom_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_custom_log_config_with_options(request, runtime)

    def modify_cdn_domain_with_options(self, request, runtime):
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
            action='ModifyCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_with_options(request, runtime)

    def modify_cdn_domain_schdm_by_property_with_options(self, request, runtime):
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
            action='ModifyCdnDomainSchdmByProperty',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyCdnDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cdn_domain_schdm_by_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cdn_domain_schdm_by_property_with_options(request, runtime)

    def modify_domain_custom_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyDomainCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_domain_custom_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_custom_log_config_with_options(request, runtime)

    def modify_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRealtimeLogDelivery',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_realtime_log_delivery_with_options(request, runtime)

    def modify_user_custom_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserCustomLogConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.ModifyUserCustomLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_custom_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_custom_log_config_with_options(request, runtime)

    def open_cdn_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCdnService',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.OpenCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_cdn_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_cdn_service_with_options(request, runtime)

    def publish_staging_config_to_production_with_options(self, request, runtime):
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
            action='PublishStagingConfigToProduction',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.PublishStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_staging_config_to_production(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_staging_config_to_production_with_options(request, runtime)

    def push_object_cache_with_options(self, request, runtime):
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
            action='PushObjectCache',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.PushObjectCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def push_object_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_object_cache_with_options(request, runtime)

    def refresh_object_caches_with_options(self, request, runtime):
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
            action='RefreshObjectCaches',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RefreshObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_object_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_object_caches_with_options(request, runtime)

    def rollback_staging_config_with_options(self, request, runtime):
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
            action='RollbackStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.RollbackStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_staging_config_with_options(request, runtime)

    def set_cc_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ips):
            query['AllowIps'] = request.allow_ips
        if not UtilClient.is_unset(request.block_ips):
            query['BlockIps'] = request.block_ips
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
            action='SetCcConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCcConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cc_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cc_config_with_options(request, runtime)

    def set_cdn_domain_csrcertificate_with_options(self, request, runtime):
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
            action='SetCdnDomainCSRCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainCSRCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cdn_domain_csrcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_csrcertificate_with_options(request, runtime)

    def set_cdn_domain_smcertificate_with_options(self, request, runtime):
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
            action='SetCdnDomainSMCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainSMCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cdn_domain_smcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_smcertificate_with_options(request, runtime)

    def set_cdn_domain_staging_config_with_options(self, request, runtime):
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
            action='SetCdnDomainStagingConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetCdnDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cdn_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cdn_domain_staging_config_with_options(request, runtime)

    def set_config_of_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.function_args):
            query['FunctionArgs'] = request.function_args
        if not UtilClient.is_unset(request.function_id):
            query['FunctionId'] = request.function_id
        if not UtilClient.is_unset(request.function_matches):
            query['FunctionMatches'] = request.function_matches
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
            action='SetConfigOfVersion',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetConfigOfVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_config_of_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_config_of_version_with_options(request, runtime)

    def set_domain_green_manager_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainGreenManagerConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetDomainGreenManagerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_green_manager_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_green_manager_config_with_options(request, runtime)

    def set_domain_server_certificate_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.server_certificate_status):
            query['ServerCertificateStatus'] = request.server_certificate_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainServerCertificate',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetDomainServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_server_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_server_certificate_with_options(request, runtime)

    def set_error_page_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_url):
            query['CustomPageUrl'] = request.custom_page_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_type):
            query['PageType'] = request.page_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetErrorPageConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetErrorPageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_error_page_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_error_page_config_with_options(request, runtime)

    def set_file_cache_expired_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_content):
            query['CacheContent'] = request.cache_content
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.ttl):
            query['TTL'] = request.ttl
        if not UtilClient.is_unset(request.weight):
            query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFileCacheExpiredConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetFileCacheExpiredConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_file_cache_expired_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_file_cache_expired_config_with_options(request, runtime)

    def set_force_redirect_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.redirect_type):
            query['RedirectType'] = request.redirect_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForceRedirectConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetForceRedirectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_force_redirect_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_force_redirect_config_with_options(request, runtime)

    def set_forward_scheme_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scheme_origin):
            query['SchemeOrigin'] = request.scheme_origin
        if not UtilClient.is_unset(request.scheme_origin_port):
            query['SchemeOriginPort'] = request.scheme_origin_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForwardSchemeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetForwardSchemeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_forward_scheme_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_forward_scheme_config_with_options(request, runtime)

    def set_http_error_page_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.error_code):
            query['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_url):
            query['PageUrl'] = request.page_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpErrorPageConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpErrorPageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_http_error_page_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_http_error_page_config_with_options(request, runtime)

    def set_http_header_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.header_key):
            query['HeaderKey'] = request.header_key
        if not UtilClient.is_unset(request.header_value):
            query['HeaderValue'] = request.header_value
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpHeaderConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpHeaderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_http_header_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_http_header_config_with_options(request, runtime)

    def set_https_option_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.http_2):
            query['Http2'] = request.http_2
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpsOptionConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetHttpsOptionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_https_option_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_https_option_config_with_options(request, runtime)

    def set_ignore_query_string_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.hash_key_args):
            query['HashKeyArgs'] = request.hash_key_args
        if not UtilClient.is_unset(request.keep_oss_args):
            query['KeepOssArgs'] = request.keep_oss_args
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIgnoreQueryStringConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIgnoreQueryStringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_ignore_query_string_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_ignore_query_string_config_with_options(request, runtime)

    def set_ip_allow_list_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_ips):
            query['AllowIps'] = request.allow_ips
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
            action='SetIpAllowListConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIpAllowListConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_ip_allow_list_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_ip_allow_list_config_with_options(request, runtime)

    def set_ip_black_list_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_ips):
            query['BlockIps'] = request.block_ips
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIpBlackListConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetIpBlackListConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_ip_black_list_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_ip_black_list_config_with_options(request, runtime)

    def set_optimize_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOptimizeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetOptimizeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_optimize_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_optimize_config_with_options(request, runtime)

    def set_page_compress_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPageCompressConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetPageCompressConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_page_compress_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_page_compress_config_with_options(request, runtime)

    def set_range_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRangeConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRangeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_range_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_range_config_with_options(request, runtime)

    def set_referer_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_empty):
            query['AllowEmpty'] = request.allow_empty
        if not UtilClient.is_unset(request.disable_ast):
            query['DisableAst'] = request.disable_ast
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.refer_list):
            query['ReferList'] = request.refer_list
        if not UtilClient.is_unset(request.refer_type):
            query['ReferType'] = request.refer_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRefererConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRefererConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_referer_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_referer_config_with_options(request, runtime)

    def set_remove_query_string_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_remove_args):
            query['AliRemoveArgs'] = request.ali_remove_args
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.keep_oss_args):
            query['KeepOssArgs'] = request.keep_oss_args
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRemoveQueryStringConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetRemoveQueryStringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_remove_query_string_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_remove_query_string_config_with_options(request, runtime)

    def set_req_auth_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_remote_desc):
            query['AuthRemoteDesc'] = request.auth_remote_desc
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_1):
            query['Key1'] = request.key_1
        if not UtilClient.is_unset(request.key_2):
            query['Key2'] = request.key_2
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.time_out):
            query['TimeOut'] = request.time_out
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetReqAuthConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetReqAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_req_auth_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_req_auth_config_with_options(request, runtime)

    def set_req_header_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetReqHeaderConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetReqHeaderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_req_header_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_req_header_config_with_options(request, runtime)

    def set_source_host_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.back_src_domain):
            query['BackSrcDomain'] = request.back_src_domain
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSourceHostConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetSourceHostConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_source_host_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_source_host_config_with_options(request, runtime)

    def set_user_green_manager_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        if not UtilClient.is_unset(request.ratio):
            query['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserGreenManagerConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetUserGreenManagerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_user_green_manager_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_green_manager_config_with_options(request, runtime)

    def set_waiting_room_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_pct):
            query['AllowPct'] = request.allow_pct
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.gap_time):
            query['GapTime'] = request.gap_time
        if not UtilClient.is_unset(request.max_time_wait):
            query['MaxTimeWait'] = request.max_time_wait
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.wait_uri):
            query['WaitUri'] = request.wait_uri
        if not UtilClient.is_unset(request.wait_url):
            query['WaitUrl'] = request.wait_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWaitingRoomConfig',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.SetWaitingRoomConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_waiting_room_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_waiting_room_config_with_options(request, runtime)

    def start_cdn_domain_with_options(self, request, runtime):
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
            action='StartCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.StartCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def start_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_cdn_domain_with_options(request, runtime)

    def stop_cdn_domain_with_options(self, request, runtime):
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
            action='StopCdnDomain',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.StopCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_cdn_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cdn_domain_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
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
            action='TagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
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
            action='UntagResources',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_cdn_deliver_task_with_options(self, request, runtime):
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
            action='UpdateCdnDeliverTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateCdnDeliverTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cdn_deliver_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cdn_deliver_task_with_options(request, runtime)

    def update_cdn_sub_task_with_options(self, request, runtime):
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
            action='UpdateCdnSubTask',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateCdnSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cdn_sub_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cdn_sub_task_with_options(request, runtime)

    def update_fctrigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.trigger_arn):
            query['TriggerARN'] = request.trigger_arn
        body = {}
        if not UtilClient.is_unset(request.function_arn):
            body['FunctionARN'] = request.function_arn
        if not UtilClient.is_unset(request.notes):
            body['Notes'] = request.notes
        if not UtilClient.is_unset(request.role_arn):
            body['RoleARN'] = request.role_arn
        if not UtilClient.is_unset(request.source_arn):
            body['SourceARN'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFCTrigger',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.UpdateFCTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_fctrigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_fctrigger_with_options(request, runtime)

    def verify_domain_owner_with_options(self, request, runtime):
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
            action='VerifyDomainOwner',
            version='2018-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20180510_models.VerifyDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)
