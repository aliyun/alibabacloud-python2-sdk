# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vod20170321 import models as vod_20170321_models
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
        self._endpoint_map = {
            'ap-northeast-2-pop': 'vod.aliyuncs.com',
            'ap-southeast-2': 'vod.aliyuncs.com',
            'ap-southeast-3': 'vod.aliyuncs.com',
            'cn-beijing-finance-1': 'vod.aliyuncs.com',
            'cn-beijing-finance-pop': 'vod.aliyuncs.com',
            'cn-beijing-gov-1': 'vod.aliyuncs.com',
            'cn-beijing-nu16-b01': 'vod.aliyuncs.com',
            'cn-chengdu': 'vod.aliyuncs.com',
            'cn-edge-1': 'vod.aliyuncs.com',
            'cn-fujian': 'vod.aliyuncs.com',
            'cn-haidian-cm12-c01': 'vod.aliyuncs.com',
            'cn-hangzhou': 'vod.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'vod.aliyuncs.com',
            'cn-hangzhou-finance': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'vod.aliyuncs.com',
            'cn-hangzhou-test-306': 'vod.aliyuncs.com',
            'cn-hongkong': 'vod.aliyuncs.com',
            'cn-hongkong-finance-pop': 'vod.aliyuncs.com',
            'cn-huhehaote': 'vod.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'vod.aliyuncs.com',
            'cn-qingdao': 'vod.aliyuncs.com',
            'cn-qingdao-nebula': 'vod.aliyuncs.com',
            'cn-shanghai-et15-b01': 'vod.aliyuncs.com',
            'cn-shanghai-et2-b01': 'vod.aliyuncs.com',
            'cn-shanghai-finance-1': 'vod.aliyuncs.com',
            'cn-shanghai-inner': 'vod.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'vod.aliyuncs.com',
            'cn-shenzhen-finance-1': 'vod.aliyuncs.com',
            'cn-shenzhen-inner': 'vod.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'vod.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'vod.aliyuncs.com',
            'cn-wuhan': 'vod.aliyuncs.com',
            'cn-wulanchabu': 'vod.aliyuncs.com',
            'cn-yushanfang': 'vod.aliyuncs.com',
            'cn-zhangbei': 'vod.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'vod.aliyuncs.com',
            'cn-zhangjiakou': 'vod.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'vod.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'vod.aliyuncs.com',
            'eu-west-1': 'vod.aliyuncs.com',
            'eu-west-1-oxs': 'vod.aliyuncs.com',
            'me-east-1': 'vod.aliyuncs.com',
            'rus-west-1-pop': 'vod.aliyuncs.com',
            'us-east-1': 'vod.aliyuncs.com',
            'us-west-1': 'vod.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('vod', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_aitemplate_with_options(self, request, runtime):
        """
        The type of the AI template. Valid values:
        *   **AIMediaAudit**: automated review
        *   **AIImage**: smart thumbnail
        

        @param request: AddAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_aitemplate(self, request):
        """
        The type of the AI template. Valid values:
        *   **AIMediaAudit**: automated review
        *   **AIImage**: smart thumbnail
        

        @param request: AddAITemplateRequest

        @return: AddAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_aitemplate_with_options(request, runtime)

    def add_category_with_options(self, request, runtime):
        """
        The level of the category. A value of *0** indicates a level 1 category.
        

        @param request: AddCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_name):
            query['CateName'] = request.cate_name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCategory',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_category(self, request):
        """
        The level of the category. A value of *0** indicates a level 1 category.
        

        @param request: AddCategoryRequest

        @return: AddCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    def add_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.division):
            query['Division'] = request.division
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEditingProject',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def add_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_with_options(request, runtime)

    def add_transcode_template_group_with_options(self, request, runtime):
        """
        The ID of the transcoding template group.
        

        @param request: AddTranscodeTemplateGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTranscodeTemplateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not UtilClient.is_unset(request.transcode_template_list):
            query['TranscodeTemplateList'] = request.transcode_template_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTranscodeTemplateGroup',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_transcode_template_group(self, request):
        """
        The ID of the transcoding template group.
        

        @param request: AddTranscodeTemplateGroupRequest

        @return: AddTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_transcode_template_group_with_options(request, runtime)

    def add_vod_domain_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: AddVodDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddVodDomainResponse
        """
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
            action='AddVodDomain',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_vod_domain(self, request):
        """
        The ID of the request.
        

        @param request: AddVodDomainRequest

        @return: AddVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vod_domain_with_options(request, runtime)

    def add_vod_template_with_options(self, request, runtime):
        """
        The type of the template. Set the value to *Snapshot**.
        

        @param request: AddVodTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddVodTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVodTemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_vod_template(self, request):
        """
        The type of the template. Set the value to *Snapshot**.
        

        @param request: AddVodTemplateRequest

        @return: AddVodTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vod_template_with_options(request, runtime)

    def add_watermark_with_options(self, request, runtime):
        """
        The name of the watermark. Only letters and digits are supported.
        *   The name can be up to 128 bytes in length.
        *   The value must be encoded in UTF-8.
        

        @param request: AddWatermarkRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.watermark_config):
            query['WatermarkConfig'] = request.watermark_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWatermark',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def add_watermark(self, request):
        """
        The name of the watermark. Only letters and digits are supported.
        *   The name can be up to 128 bytes in length.
        *   The value must be encoded in UTF-8.
        

        @param request: AddWatermarkRequest

        @return: AddWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_watermark_with_options(request, runtime)

    def attach_app_policy_to_identity_with_options(self, request, runtime):
        """
        The name of the policy that was not found.
        

        @param request: AttachAppPolicyToIdentityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachAppPolicyToIdentityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAppPolicyToIdentity',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AttachAppPolicyToIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_app_policy_to_identity(self, request):
        """
        The name of the policy that was not found.
        

        @param request: AttachAppPolicyToIdentityRequest

        @return: AttachAppPolicyToIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_app_policy_to_identity_with_options(request, runtime)

    def batch_set_vod_domain_configs_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: BatchSetVodDomainConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchSetVodDomainConfigsResponse
        """
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
            action='BatchSetVodDomainConfigs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchSetVodDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_vod_domain_configs(self, request):
        """
        The ID of the request.
        

        @param request: BatchSetVodDomainConfigsRequest

        @return: BatchSetVodDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vod_domain_configs_with_options(request, runtime)

    def batch_start_vod_domain_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *BatchStartVodDomain**.
        

        @param request: BatchStartVodDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchStartVodDomainResponse
        """
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
            action='BatchStartVodDomain',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchStartVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_vod_domain(self, request):
        """
        The operation that you want to perform. Set the value to *BatchStartVodDomain**.
        

        @param request: BatchStartVodDomainRequest

        @return: BatchStartVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_start_vod_domain_with_options(request, runtime)

    def batch_stop_vod_domain_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *BatchStopVodDomain**.
        

        @param request: BatchStopVodDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchStopVodDomainResponse
        """
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
            action='BatchStopVodDomain',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.BatchStopVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_vod_domain(self, request):
        """
        The operation that you want to perform. Set the value to *BatchStopVodDomain**.
        

        @param request: BatchStopVodDomainRequest

        @return: BatchStopVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_vod_domain_with_options(request, runtime)

    def cancel_url_upload_jobs_with_options(self, request, runtime):
        """
        The upload URLs of source files. Separate multiple URLs with commas (,). You can specify a maximum of 10 URLs.
        > *   You must encode the URLs before you use the URLs.
        > *   You must set one of the JobIds and the UploadUrls parameters. If you set both the JobIds and UploadUrls parameters, only the value of the JobIds parameter takes effect.
        

        @param request: CancelUrlUploadJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelUrlUploadJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadUrls'] = request.upload_urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelUrlUploadJobs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.CancelUrlUploadJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_url_upload_jobs(self, request):
        """
        The upload URLs of source files. Separate multiple URLs with commas (,). You can specify a maximum of 10 URLs.
        > *   You must encode the URLs before you use the URLs.
        > *   You must set one of the JobIds and the UploadUrls parameters. If you set both the JobIds and UploadUrls parameters, only the value of the JobIds parameter takes effect.
        

        @param request: CancelUrlUploadJobsRequest

        @return: CancelUrlUploadJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_url_upload_jobs_with_options(request, runtime)

    def create_app_info_with_options(self, request, runtime):
        """
        The description of the application.
        - The description can contain up to 512 characters in length.
        - The description can contain only UTF-8 characters.
        

        @param request: CreateAppInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_info(self, request):
        """
        The description of the application.
        - The description can contain up to 512 characters in length.
        - The description can contain only UTF-8 characters.
        

        @param request: CreateAppInfoRequest

        @return: CreateAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_info_with_options(request, runtime)

    def create_audit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_content):
            query['AuditContent'] = request.audit_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAudit',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    def create_audit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_audit_with_options(request, runtime)

    def create_upload_attached_media_with_options(self, request, runtime):
        """
        The type of the media asset. Valid values:
        *   **watermark**\
        *   **subtitle**\
        *   **material**\
        

        @param request: CreateUploadAttachedMediaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateUploadAttachedMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_ids):
            query['CateIds'] = request.cate_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.media_ext):
            query['MediaExt'] = request.media_ext
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadAttachedMedia',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadAttachedMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def create_upload_attached_media(self, request):
        """
        The type of the media asset. Valid values:
        *   **watermark**\
        *   **subtitle**\
        *   **material**\
        

        @param request: CreateUploadAttachedMediaRequest

        @return: CreateUploadAttachedMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_upload_attached_media_with_options(request, runtime)

    def create_upload_image_with_options(self, request, runtime):
        """
        The custom configurations. For example, you can specify callback configurations and upload acceleration configurations. The value is a JSON string. For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](~~86952~~) topic.
        > *   The callback configurations take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](~~86071~~).
        > *   To use the upload acceleration feature, submit a [ticket](https://ticket-intl.console.aliyun.com/#/ticket/createIndex) to enable this feature. For more information, see [Overview](~~55396~~).
        

        @param request: CreateUploadImageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateUploadImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_ext):
            query['ImageExt'] = request.image_ext
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.original_file_name):
            query['OriginalFileName'] = request.original_file_name
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadImage',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadImageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_upload_image(self, request):
        """
        The custom configurations. For example, you can specify callback configurations and upload acceleration configurations. The value is a JSON string. For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](~~86952~~) topic.
        > *   The callback configurations take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](~~86071~~).
        > *   To use the upload acceleration feature, submit a [ticket](https://ticket-intl.console.aliyun.com/#/ticket/createIndex) to enable this feature. For more information, see [Overview](~~55396~~).
        

        @param request: CreateUploadImageRequest

        @return: CreateUploadImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_upload_image_with_options(request, runtime)

    def create_upload_video_with_options(self, request, runtime):
        """
        Obtains the upload URLs and credentials for media files and creates media assets in ApsaraVideo VOD.
        

        @param request: CreateUploadVideoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateUploadVideoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            query['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadVideo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.CreateUploadVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_upload_video(self, request):
        """
        Obtains the upload URLs and credentials for media files and creates media assets in ApsaraVideo VOD.
        

        @param request: CreateUploadVideoRequest

        @return: CreateUploadVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_upload_video_with_options(request, runtime)

    def decrypt_kmsdata_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cipher_text):
            query['CipherText'] = request.cipher_text
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecryptKMSDataKey',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DecryptKMSDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def decrypt_kmsdata_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decrypt_kmsdata_key_with_options(request, runtime)

    def delete_aiimage_infos_with_options(self, request, runtime):
        """
        This operation deletes only information about images that are submitted for AI processing. The image files are not deleted.
        - The smart thumbnail feature is not supported. You cannot call this operation.
        - This operation deletes only information about images that are submitted for AI processing. The image files are not deleted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: DeleteAIImageInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAIImageInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aiimage_info_ids):
            query['AIImageInfoIds'] = request.aiimage_info_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAIImageInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAIImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiimage_infos(self, request):
        """
        This operation deletes only information about images that are submitted for AI processing. The image files are not deleted.
        - The smart thumbnail feature is not supported. You cannot call this operation.
        - This operation deletes only information about images that are submitted for AI processing. The image files are not deleted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: DeleteAIImageInfosRequest

        @return: DeleteAIImageInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aiimage_infos_with_options(request, runtime)

    def delete_aitemplate_with_options(self, request, runtime):
        """
        The ID of the AI template. You can use one of the following methods to obtain the ID of the AI template:
        *   Call the [AddAITemplate](~~102930~~) operation to add an AI template if no AI template exists. The value of TemplateId from the response is the ID of the AI template.
        *   Call the [ListAITemplate](~~102936~~) operation if the template already exists. The value of TemplateId from the response is the ID of the AI template.
        

        @param request: DeleteAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aitemplate(self, request):
        """
        The ID of the AI template. You can use one of the following methods to obtain the ID of the AI template:
        *   Call the [AddAITemplate](~~102930~~) operation to add an AI template if no AI template exists. The value of TemplateId from the response is the ID of the AI template.
        *   Call the [ListAITemplate](~~102936~~) operation if the template already exists. The value of TemplateId from the response is the ID of the AI template.
        

        @param request: DeleteAITemplateRequest

        @return: DeleteAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aitemplate_with_options(request, runtime)

    def delete_app_info_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteAppInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_info(self, request):
        """
        The ID of the request.
        

        @param request: DeleteAppInfoRequest

        @return: DeleteAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_info_with_options(request, runtime)

    def delete_attached_media_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteAttachedMediaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAttachedMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAttachedMedia',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteAttachedMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_attached_media(self, request):
        """
        The ID of the request.
        

        @param request: DeleteAttachedMediaRequest

        @return: DeleteAttachedMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_attached_media_with_options(request, runtime)

    def delete_category_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteCategoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_category(self, request):
        """
        The ID of the request.
        

        @param request: DeleteCategoryRequest

        @return: DeleteCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    def delete_dynamic_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_image_ids):
            query['DynamicImageIds'] = request.dynamic_image_ids
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicImage',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteDynamicImageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dynamic_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_image_with_options(request, runtime)

    def delete_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProject',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        """
        The URL of the image.
        *   This parameter only takes effect when the **DeleteImageType** parameter is set to **ImageURL**. In this case, you must set this parameter.
        *   Encode multiple image URLs and separate them with commas (,).
        *   The use of special characters in image URLs may lead to the failure to delete the images. To prevent such failure, you must encode the image URLs before you concatenate them into a string with commas (,).
        

        @param request: DeleteImageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_image_type):
            query['DeleteImageType'] = request.delete_image_type
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_urls):
            query['ImageURLs'] = request.image_urls
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image(self, request):
        """
        The URL of the image.
        *   This parameter only takes effect when the **DeleteImageType** parameter is set to **ImageURL**. In this case, you must set this parameter.
        *   Encode multiple image URLs and separate them with commas (,).
        *   The use of special characters in image URLs may lead to the failure to delete the images. To prevent such failure, you must encode the image URLs before you concatenate them into a string with commas (,).
        

        @param request: DeleteImageRequest

        @return: DeleteImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_message_callback_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *DeleteMessageCallback**.
        

        @param request: DeleteMessageCallbackRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageCallback',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_message_callback(self, request):
        """
        The operation that you want to perform. Set the value to *DeleteMessageCallback**.
        

        @param request: DeleteMessageCallbackRequest

        @return: DeleteMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    def delete_mezzanines_with_options(self, request, runtime):
        """
        The IDs of the videos that do not exist.
        

        @param request: DeleteMezzaninesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMezzaninesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMezzanines',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMezzaninesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mezzanines(self, request):
        """
        The IDs of the videos that do not exist.
        

        @param request: DeleteMezzaninesRequest

        @return: DeleteMezzaninesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mezzanines_with_options(request, runtime)

    def delete_multipart_upload_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteMultipartUploadRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteMultipartUploadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMultipartUpload',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteMultipartUploadResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_multipart_upload(self, request):
        """
        The ID of the request.
        

        @param request: DeleteMultipartUploadRequest

        @return: DeleteMultipartUploadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_multipart_upload_with_options(request, runtime)

    def delete_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStream',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_with_options(request, runtime)

    def delete_transcode_template_group_with_options(self, request, runtime):
        """
        Specifies whether to forcibly delete the entire transcoding template group. Valid values:
        *   **true**: deletes the entire transcoding template group and its transcoding templates.
        *   **false**: removes the specified transcoding templates from the transcoding template group. This is the default value.
        

        @param request: DeleteTranscodeTemplateGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTranscodeTemplateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_del_group):
            query['ForceDelGroup'] = request.force_del_group
        if not UtilClient.is_unset(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not UtilClient.is_unset(request.transcode_template_ids):
            query['TranscodeTemplateIds'] = request.transcode_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTranscodeTemplateGroup',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transcode_template_group(self, request):
        """
        Specifies whether to forcibly delete the entire transcoding template group. Valid values:
        *   **true**: deletes the entire transcoding template group and its transcoding templates.
        *   **false**: removes the specified transcoding templates from the transcoding template group. This is the default value.
        

        @param request: DeleteTranscodeTemplateGroupRequest

        @return: DeleteTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transcode_template_group_with_options(request, runtime)

    def delete_video_with_options(self, request, runtime):
        """
        The list of video IDs. Separate multiple IDs with commas (,). A maximum of 20 IDs can be specified. You can obtain a video ID in one of the following ways:
        *   If the video is uploaded by using the [ApsaraVideo VOD console](https://vod.console.aliyun.com), log on to the console and choose **Media Files** > **Audio/Video** to view the ID of the video.
        *   If the video is uploaded by calling the [CreateUploadVideo](~~55407~~) operation, the video ID is the VideoId value in the response.
        *   You can also call the [SearchMedia](~~86044~~) operation to obtain the video ID, which is the VideoId value in the response.
        

        @param request: DeleteVideoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVideoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_video(self, request):
        """
        The list of video IDs. Separate multiple IDs with commas (,). A maximum of 20 IDs can be specified. You can obtain a video ID in one of the following ways:
        *   If the video is uploaded by using the [ApsaraVideo VOD console](https://vod.console.aliyun.com), log on to the console and choose **Media Files** > **Audio/Video** to view the ID of the video.
        *   If the video is uploaded by calling the [CreateUploadVideo](~~55407~~) operation, the video ID is the VideoId value in the response.
        *   You can also call the [SearchMedia](~~86044~~) operation to obtain the video ID, which is the VideoId value in the response.
        

        @param request: DeleteVideoRequest

        @return: DeleteVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    def delete_vod_domain_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteVodDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVodDomainResponse
        """
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
            action='DeleteVodDomain',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vod_domain(self, request):
        """
        The ID of the request.
        

        @param request: DeleteVodDomainRequest

        @return: DeleteVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_domain_with_options(request, runtime)

    def delete_vod_specific_config_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteVodSpecificConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVodSpecificConfigResponse
        """
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
            action='DeleteVodSpecificConfig',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vod_specific_config(self, request):
        """
        The ID of the request.
        

        @param request: DeleteVodSpecificConfigRequest

        @return: DeleteVodSpecificConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_specific_config_with_options(request, runtime)

    def delete_vod_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVodTemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vod_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_template_with_options(request, runtime)

    def delete_watermark_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteWatermarkRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWatermark',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_watermark(self, request):
        """
        The ID of the request.
        

        @param request: DeleteWatermarkRequest

        @return: DeleteWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    def describe_play_top_videos_with_options(self, request, runtime):
        """
        The number of entries to return on each page. Default value: *100**. Maximum value: **1000**.
        

        @param request: DescribePlayTopVideosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePlayTopVideosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_date):
            query['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayTopVideos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayTopVideosResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_play_top_videos(self, request):
        """
        The number of entries to return on each page. Default value: *100**. Maximum value: **1000**.
        

        @param request: DescribePlayTopVideosRequest

        @return: DescribePlayTopVideosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_top_videos_with_options(request, runtime)

    def describe_play_user_avg_with_options(self, request, runtime):
        """
        The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        

        @param request: DescribePlayUserAvgRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePlayUserAvgResponse
        """
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
            action='DescribePlayUserAvg',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayUserAvgResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_play_user_avg(self, request):
        """
        The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        

        @param request: DescribePlayUserAvgRequest

        @return: DescribePlayUserAvgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_avg_with_options(request, runtime)

    def describe_play_user_total_with_options(self, request, runtime):
        """
        The total number of unique visitors who use ApsaraVideo Player SDK for Flash.
        

        @param request: DescribePlayUserTotalRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePlayUserTotalResponse
        """
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
            action='DescribePlayUserTotal',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayUserTotalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_play_user_total(self, request):
        """
        The total number of unique visitors who use ApsaraVideo Player SDK for Flash.
        

        @param request: DescribePlayUserTotalRequest

        @return: DescribePlayUserTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_total_with_options(request, runtime)

    def describe_play_video_statis_with_options(self, request, runtime):
        """
        The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        

        @param request: DescribePlayVideoStatisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePlayVideoStatisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayVideoStatis',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribePlayVideoStatisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_play_video_statis(self, request):
        """
        The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        

        @param request: DescribePlayVideoStatisRequest

        @return: DescribePlayVideoStatisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_video_statis_with_options(request, runtime)

    def describe_vod_aidata_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        >*   If the time range to query is less than or equal to seven days, the system returns the statistics collected on an hourly basis. If the time range to query is greater than seven days, the system returns the statistics collected on a daily basis. The maximum time range that you can specify to query is 31 days.
        

        @param request: DescribeVodAIDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodAIDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aitype):
            query['AIType'] = request.aitype
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodAIData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodAIDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_aidata(self, request):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        >*   If the time range to query is less than or equal to seven days, the system returns the statistics collected on an hourly basis. If the time range to query is greater than seven days, the system returns the statistics collected on a daily basis. The maximum time range that you can specify to query is 31 days.
        

        @param request: DescribeVodAIDataRequest

        @return: DescribeVodAIDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_aidata_with_options(request, runtime)

    def describe_vod_certificate_list_with_options(self, request, runtime):
        """
        The domain name for CDN.
        

        @param request: DescribeVodCertificateListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodCertificateListResponse
        """
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
            action='DescribeVodCertificateList',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_certificate_list(self, request):
        """
        The domain name for CDN.
        

        @param request: DescribeVodCertificateListRequest

        @return: DescribeVodCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_certificate_list_with_options(request, runtime)

    def describe_vod_domain_bps_data_with_options(self, request, runtime):
        """
        The domain name for CDN.
        

        @param request: DescribeVodDomainBpsDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainBpsDataResponse
        """
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
            action='DescribeVodDomainBpsData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_bps_data(self, request):
        """
        The domain name for CDN.
        

        @param request: DescribeVodDomainBpsDataRequest

        @return: DescribeVodDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_bps_data_with_options(request, runtime)

    def describe_vod_domain_certificate_info_with_options(self, request, runtime):
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
            action='DescribeVodDomainCertificateInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_certificate_info_with_options(request, runtime)

    def describe_vod_domain_configs_with_options(self, request, runtime):
        """
        The name of the function.
        

        @param request: DescribeVodDomainConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainConfigsResponse
        """
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
            action='DescribeVodDomainConfigs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_configs(self, request):
        """
        The name of the function.
        

        @param request: DescribeVodDomainConfigsRequest

        @return: DescribeVodDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_configs_with_options(request, runtime)

    def describe_vod_domain_detail_with_options(self, request, runtime):
        """
        The description of the domain name for CDN.
        

        @param request: DescribeVodDomainDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainDetailResponse
        """
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
            action='DescribeVodDomainDetail',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_detail(self, request):
        """
        The description of the domain name for CDN.
        

        @param request: DescribeVodDomainDetailRequest

        @return: DescribeVodDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_detail_with_options(request, runtime)

    def describe_vod_domain_log_with_options(self, request, runtime):
        """
        The total number of entries returned on the current page.
        

        @param request: DescribeVodDomainLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainLogResponse
        """
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
            action='DescribeVodDomainLog',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_log(self, request):
        """
        The total number of entries returned on the current page.
        

        @param request: DescribeVodDomainLogRequest

        @return: DescribeVodDomainLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_log_with_options(request, runtime)

    def describe_vod_domain_src_bps_data_with_options(self, request, runtime):
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
            action='DescribeVodDomainSrcBpsData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_src_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_src_bps_data_with_options(request, runtime)

    def describe_vod_domain_src_traffic_data_with_options(self, request, runtime):
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
            action='DescribeVodDomainSrcTrafficData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_src_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_src_traffic_data_with_options(request, runtime)

    def describe_vod_domain_traffic_data_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   You can specify multiple accelerated domain names in a request.
        *   If you do not specify the StartTime or EndTime parameter, data of the last 24 hours is returned. You can specify the StartTime and EndTime parameters to query data that is generated in the specified time range. You can query data of the last 90 days.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on API operations](~~342790~~).
        

        @param request: DescribeVodDomainTrafficDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainTrafficDataResponse
        """
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
            action='DescribeVodDomainTrafficData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_traffic_data(self, request):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   You can specify multiple accelerated domain names in a request.
        *   If you do not specify the StartTime or EndTime parameter, data of the last 24 hours is returned. You can specify the StartTime and EndTime parameters to query data that is generated in the specified time range. You can query data of the last 90 days.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on API operations](~~342790~~).
        

        @param request: DescribeVodDomainTrafficDataRequest

        @return: DescribeVodDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_traffic_data_with_options(request, runtime)

    def describe_vod_domain_usage_data_with_options(self, request, runtime):
        """
        >
        *   This operation is available only in the **China (Shanghai)** region.
        *   You can specify up to 100 accelerated domain names in a request. Separate multiple domain names with commas (,). If you do not specify an accelerated domain name, the data of all accelerated domain names within your Alibaba Cloud account is returned.
        *   You can query data in the last year. The maximum time range that can be queried is three months. If you specify a time range of one to three days, the system returns data on an hourly basis. If you specify a time range of four days or more, the system returns data on a daily basis.
        

        @param request: DescribeVodDomainUsageDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
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
            action='DescribeVodDomainUsageData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_domain_usage_data(self, request):
        """
        >
        *   This operation is available only in the **China (Shanghai)** region.
        *   You can specify up to 100 accelerated domain names in a request. Separate multiple domain names with commas (,). If you do not specify an accelerated domain name, the data of all accelerated domain names within your Alibaba Cloud account is returned.
        *   You can query data in the last year. The maximum time range that can be queried is three months. If you specify a time range of one to three days, the system returns data on an hourly basis. If you specify a time range of four days or more, the system returns data on a daily basis.
        

        @param request: DescribeVodDomainUsageDataRequest

        @return: DescribeVodDomainUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_usage_data_with_options(request, runtime)

    def describe_vod_refresh_quota_with_options(self, request, runtime):
        """
        The maximum number of URLs of files that can be refreshed each day.
        

        @param request: DescribeVodRefreshQuotaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodRefreshQuotaResponse
        """
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
            action='DescribeVodRefreshQuota',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_refresh_quota(self, request):
        """
        The maximum number of URLs of files that can be refreshed each day.
        

        @param request: DescribeVodRefreshQuotaRequest

        @return: DescribeVodRefreshQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_quota_with_options(request, runtime)

    def describe_vod_refresh_tasks_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        >*   If you do not specify the TaskId or ObjectPath parameter, the data in the last three days is returned on the first page. By default, one page displays a maximum of 20 entries. You can specify the TaskId and ObjectPath parameters at the same time.
        

        @param request: DescribeVodRefreshTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodRefreshTasksResponse
        """
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
            action='DescribeVodRefreshTasks',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_refresh_tasks(self, request):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        >*   If you do not specify the TaskId or ObjectPath parameter, the data in the last three days is returned on the first page. By default, one page displays a maximum of 20 entries. You can specify the TaskId and ObjectPath parameters at the same time.
        

        @param request: DescribeVodRefreshTasksRequest

        @return: DescribeVodRefreshTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_tasks_with_options(request, runtime)

    def describe_vod_storage_data_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        >*   If the time range to query is less than or equal to seven days, the system returns the statistics collected on an hourly basis. If the time range to query is greater than seven days, the system returns the statistics collected on a daily basis. The maximum time range that you can specify to query is 31 days.
        

        @param request: DescribeVodStorageDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodStorageDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodStorageData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodStorageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_storage_data(self, request):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        >*   If the time range to query is less than or equal to seven days, the system returns the statistics collected on an hourly basis. If the time range to query is greater than seven days, the system returns the statistics collected on a daily basis. The maximum time range that you can specify to query is 31 days.
        

        @param request: DescribeVodStorageDataRequest

        @return: DescribeVodStorageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_storage_data_with_options(request, runtime)

    def describe_vod_transcode_data_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   If the time range to query is less than or equal to seven days, the system returns the statistics collected on an hourly basis. If the time range to query is greater than seven days, the system returns the statistics collected on a daily basis. The maximum time range that you can specify to query is 31 days.
        

        @param request: DescribeVodTranscodeDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodTranscodeDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodTranscodeData',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodTranscodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_transcode_data(self, request):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   If the time range to query is less than or equal to seven days, the system returns the statistics collected on an hourly basis. If the time range to query is greater than seven days, the system returns the statistics collected on a daily basis. The maximum time range that you can specify to query is 31 days.
        

        @param request: DescribeVodTranscodeDataRequest

        @return: DescribeVodTranscodeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_transcode_data_with_options(request, runtime)

    def describe_vod_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodUserDomains',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_user_domains_with_options(request, runtime)

    def describe_vod_verify_content_with_options(self, request, runtime):
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
            action='DescribeVodVerifyContent',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DescribeVodVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_verify_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_verify_content_with_options(request, runtime)

    def detach_app_policy_from_identity_with_options(self, request, runtime):
        """
        The name of the policy that was not found.
        

        @param request: DetachAppPolicyFromIdentityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachAppPolicyFromIdentityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAppPolicyFromIdentity',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DetachAppPolicyFromIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_app_policy_from_identity(self, request):
        """
        The name of the policy that was not found.
        

        @param request: DetachAppPolicyFromIdentityRequest

        @return: DetachAppPolicyFromIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_app_policy_from_identity_with_options(request, runtime)

    def generate_kmsdata_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateKMSDataKey',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GenerateKMSDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_kmsdata_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_kmsdata_key_with_options(request, runtime)

    def get_aiimage_jobs_with_options(self, request, runtime):
        """
        The image AI processing jobs.
        

        @param request: GetAIImageJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAIImageJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAIImageJobs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIImageJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aiimage_jobs(self, request):
        """
        The image AI processing jobs.
        

        @param request: GetAIImageJobsRequest

        @return: GetAIImageJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aiimage_jobs_with_options(request, runtime)

    def get_aimedia_audit_job_with_options(self, request, runtime):
        """
        The recommendation for review results. Valid values:
        *   **block**: The content violates the regulations.
        *   **review**: The content may violate the regulations.
        *   **pass**: The content passes the review.
        

        @param request: GetAIMediaAuditJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAIMediaAuditJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAIMediaAuditJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIMediaAuditJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aimedia_audit_job(self, request):
        """
        The recommendation for review results. Valid values:
        *   **block**: The content violates the regulations.
        *   **review**: The content may violate the regulations.
        *   **pass**: The content passes the review.
        

        @param request: GetAIMediaAuditJobRequest

        @return: GetAIMediaAuditJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aimedia_audit_job_with_options(request, runtime)

    def get_aitemplate_with_options(self, request, runtime):
        """
        The detailed configurations of the AI template. The value is a JSON string. For more information, see [AITemplateConfig](https://help.aliyun.com/document_detail/89863.html#title-vd3-499-o36).
        

        @param request: GetAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aitemplate(self, request):
        """
        The detailed configurations of the AI template. The value is a JSON string. For more information, see [AITemplateConfig](https://help.aliyun.com/document_detail/89863.html#title-vd3-499-o36).
        

        @param request: GetAITemplateRequest

        @return: GetAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aitemplate_with_options(request, runtime)

    def get_aivideo_tag_result_with_options(self, request, runtime):
        """
        Milliseconds
        

        @param request: GetAIVideoTagResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAIVideoTagResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAIVideoTagResult',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAIVideoTagResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aivideo_tag_result(self, request):
        """
        Milliseconds
        

        @param request: GetAIVideoTagResultRequest

        @return: GetAIVideoTagResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aivideo_tag_result_with_options(request, runtime)

    def get_app_infos_with_options(self, request, runtime):
        """
        The description of the application.
        

        @param request: GetAppInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAppInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAppInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_infos(self, request):
        """
        The description of the application.
        

        @param request: GetAppInfosRequest

        @return: GetAppInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_infos_with_options(request, runtime)

    def get_attached_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAttachedMediaInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAttachedMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_attached_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_attached_media_info_with_options(request, runtime)

    def get_audit_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditHistory',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetAuditHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_audit_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audit_history_with_options(request, runtime)

    def get_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategories',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_categories_with_options(request, runtime)

    def get_default_aitemplate_with_options(self, request, runtime):
        """
        The detailed configurations of the AI template. The value is a JSON string. For more information, see [AITemplateConfig](https://help.aliyun.com/document_detail/89863.html#title-vd3-499-o36).
        

        @param request: GetDefaultAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDefaultAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDefaultAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDefaultAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_default_aitemplate(self, request):
        """
        The detailed configurations of the AI template. The value is a JSON string. For more information, see [AITemplateConfig](https://help.aliyun.com/document_detail/89863.html#title-vd3-499-o36).
        

        @param request: GetDefaultAITemplateRequest

        @return: GetDefaultAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_default_aitemplate_with_options(request, runtime)

    def get_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProject',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    def get_editing_project_materials_with_options(self, request, runtime):
        """
        The time when the material was last updated. The time follows the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        

        @param request: GetEditingProjectMaterialsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetEditingProjectMaterialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProjectMaterials',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_editing_project_materials(self, request):
        """
        The time when the material was last updated. The time follows the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        

        @param request: GetEditingProjectMaterialsRequest

        @return: GetEditingProjectMaterialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    def get_image_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetImageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_image_info_with_options(request, runtime)

    def get_image_infos_with_options(self, request, runtime):
        """
        You can call this operation to query the basic information about multiple images at a time, such as the image title, type, creation time, tags, and URL.
        ### Limits
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on an API operation in ApsaraVideo Live](~~342790~~).
        

        @param request: GetImageInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetImageInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_infos(self, request):
        """
        You can call this operation to query the basic information about multiple images at a time, such as the image title, type, creation time, tags, and URL.
        ### Limits
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on an API operation in ApsaraVideo Live](~~342790~~).
        

        @param request: GetImageInfosRequest

        @return: GetImageInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_infos_with_options(request, runtime)

    def get_media_audit_audio_result_detail_with_options(self, request, runtime):
        """
        The start time of the audio that failed the review. Unit: seconds.
        

        @param request: GetMediaAuditAudioResultDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMediaAuditAudioResultDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaAuditAudioResultDetail',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditAudioResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_audit_audio_result_detail(self, request):
        """
        The start time of the audio that failed the review. Unit: seconds.
        

        @param request: GetMediaAuditAudioResultDetailRequest

        @return: GetMediaAuditAudioResultDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_audio_result_detail_with_options(request, runtime)

    def get_media_audit_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaAuditResult',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_audit_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_with_options(request, runtime)

    def get_media_audit_result_detail_with_options(self, request, runtime):
        """
        Details about review results.
        

        @param request: GetMediaAuditResultDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMediaAuditResultDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaAuditResultDetail',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_audit_result_detail(self, request):
        """
        Details about review results.
        

        @param request: GetMediaAuditResultDetailRequest

        @return: GetMediaAuditResultDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_detail_with_options(request, runtime)

    def get_media_audit_result_timeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaAuditResultTimeline',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaAuditResultTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_audit_result_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_timeline_with_options(request, runtime)

    def get_media_dnaresult_with_options(self, request, runtime):
        """
        The details of the matched video. Information such as the location and duration of the video is returned.
        

        @param request: GetMediaDNAResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMediaDNAResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaDNAResult',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaDNAResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_dnaresult(self, request):
        """
        The details of the matched video. Information such as the location and duration of the video is returned.
        

        @param request: GetMediaDNAResultRequest

        @return: GetMediaDNAResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_media_dnaresult_with_options(request, runtime)

    def get_media_refresh_jobs_with_options(self, request, runtime):
        """
        You can query the information about all media files or a specific media file in a refresh or prefetch job.
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: GetMediaRefreshJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMediaRefreshJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaRefreshJobs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMediaRefreshJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_refresh_jobs(self, request):
        """
        You can query the information about all media files or a specific media file in a refresh or prefetch job.
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: GetMediaRefreshJobsRequest

        @return: GetMediaRefreshJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_media_refresh_jobs_with_options(request, runtime)

    def get_message_callback_with_options(self, request, runtime):
        """
        The type of the callback event.
        

        @param request: GetMessageCallbackRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessageCallback',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_callback(self, request):
        """
        The type of the callback event.
        

        @param request: GetMessageCallbackRequest

        @return: GetMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_message_callback_with_options(request, runtime)

    def get_mezzanine_info_with_options(self, request, runtime):
        """
        The sampling format.
        

        @param request: GetMezzanineInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMezzanineInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not UtilClient.is_unset(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMezzanineInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetMezzanineInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mezzanine_info(self, request):
        """
        The sampling format.
        

        @param request: GetMezzanineInfoRequest

        @return: GetMezzanineInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mezzanine_info_with_options(request, runtime)

    def get_play_info_with_options(self, request, runtime):
        """
        The ID of the media file.
        

        @param request: GetPlayInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPlayInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not UtilClient.is_unset(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        if not UtilClient.is_unset(request.play_config):
            query['PlayConfig'] = request.play_config
        if not UtilClient.is_unset(request.re_auth_info):
            query['ReAuthInfo'] = request.re_auth_info
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPlayInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_play_info(self, request):
        """
        The ID of the media file.
        

        @param request: GetPlayInfoRequest

        @return: GetPlayInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    def get_transcode_summary_with_options(self, request, runtime):
        """
        A media file may be transcoded multiple times. This operation returns only the latest transcoding summary.
        *   You can query transcoding summaries for a maximum of 10 media files in one request.
        *   You can call the [ListTranscodeTask](~~109120~~) operation to query historical transcoding tasks.
        *   **You can call this operation to query information only about transcoding tasks created within the past year.**\
        

        @param request: GetTranscodeSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTranscodeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranscodeSummary',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_transcode_summary(self, request):
        """
        A media file may be transcoded multiple times. This operation returns only the latest transcoding summary.
        *   You can query transcoding summaries for a maximum of 10 media files in one request.
        *   You can call the [ListTranscodeTask](~~109120~~) operation to query historical transcoding tasks.
        *   **You can call this operation to query information only about transcoding tasks created within the past year.**\
        

        @param request: GetTranscodeSummaryRequest

        @return: GetTranscodeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_summary_with_options(request, runtime)

    def get_transcode_task_with_options(self, request, runtime):
        """
        The video resolution. Valid values:
        *   **LD**: low definition
        *   **SD**: standard definition
        *   **HD**: high definition
        *   **FHD**: ultra high definition
        *   **OD**: original definition
        *   **2K**: 2K
        *   **4K**: 4K
        *   **SQ**: standard sound quality
        *   **HQ**: high sound quality
        *   **AUTO**: adaptive bitrate Adaptive bitrate streams are returned only if PackageSetting is set in the transcoding template. For more information, see [Basic structures](~~52839~~).
        > This parameter indicates the definition that is configured in the transcoding template and does not indicate the actual resolution of the output video.
        

        @param request: GetTranscodeTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTranscodeTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.transcode_task_id):
            query['TranscodeTaskId'] = request.transcode_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranscodeTask',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_transcode_task(self, request):
        """
        The video resolution. Valid values:
        *   **LD**: low definition
        *   **SD**: standard definition
        *   **HD**: high definition
        *   **FHD**: ultra high definition
        *   **OD**: original definition
        *   **2K**: 2K
        *   **4K**: 4K
        *   **SQ**: standard sound quality
        *   **HQ**: high sound quality
        *   **AUTO**: adaptive bitrate Adaptive bitrate streams are returned only if PackageSetting is set in the transcoding template. For more information, see [Basic structures](~~52839~~).
        > This parameter indicates the definition that is configured in the transcoding template and does not indicate the actual resolution of the output video.
        

        @param request: GetTranscodeTaskRequest

        @return: GetTranscodeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_task_with_options(request, runtime)

    def get_transcode_template_group_with_options(self, request, runtime):
        """
        Valid values for the definition of a common transcoding template:
        *   **LD**: low definition.
        *   **SD**: standard definition.
        *   **HD**: high definition.
        *   **FHD**: ultra high definition.
        *   **OD**: original quality.
        *   **2K**\
        *   **4K**\
        *   **SQ**: standard sound quality.
        *   **HQ**: high sound quality.
        Valid values for the definition of a Narrowband HD™ 1.0 transcoding template:
        *   **LD-NBV1**: low definition.
        *   **SD-NBV1**: standard definition.
        *   **HD-NBV1**: high definition.
        *   **FHD-NBV1**: ultra high definition.
        *   **2K-NBV1**\
        *   **4K-NBV1**\
        >*   You cannot modify the definition of transcoding templates.
        >*   You cannot modify the system parameters, such as the video resolution, audio resolution, and bitrate, of Narrowband HD™ 1.0 transcoding templates.
        >*   You can create only Narrowband HD™ 1.0 transcoding templates that support the FLV, M3U8 (HLS), and MP4 output formats.
        

        @param request: GetTranscodeTemplateGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTranscodeTemplateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranscodeTemplateGroup',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_transcode_template_group(self, request):
        """
        Valid values for the definition of a common transcoding template:
        *   **LD**: low definition.
        *   **SD**: standard definition.
        *   **HD**: high definition.
        *   **FHD**: ultra high definition.
        *   **OD**: original quality.
        *   **2K**\
        *   **4K**\
        *   **SQ**: standard sound quality.
        *   **HQ**: high sound quality.
        Valid values for the definition of a Narrowband HD™ 1.0 transcoding template:
        *   **LD-NBV1**: low definition.
        *   **SD-NBV1**: standard definition.
        *   **HD-NBV1**: high definition.
        *   **FHD-NBV1**: ultra high definition.
        *   **2K-NBV1**\
        *   **4K-NBV1**\
        >*   You cannot modify the definition of transcoding templates.
        >*   You cannot modify the system parameters, such as the video resolution, audio resolution, and bitrate, of Narrowband HD™ 1.0 transcoding templates.
        >*   You can create only Narrowband HD™ 1.0 transcoding templates that support the FLV, M3U8 (HLS), and MP4 output formats.
        

        @param request: GetTranscodeTemplateGroupRequest

        @return: GetTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_template_group_with_options(request, runtime)

    def get_urlupload_infos_with_options(self, request, runtime):
        """
        The size of the uploaded media file. Unit: byte.
        

        @param request: GetURLUploadInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetURLUploadInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetURLUploadInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetURLUploadInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def get_urlupload_infos(self, request):
        """
        The size of the uploaded media file. Unit: byte.
        

        @param request: GetURLUploadInfosRequest

        @return: GetURLUploadInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_urlupload_infos_with_options(request, runtime)

    def get_upload_details_with_options(self, request, runtime):
        """
        The type of the media file. Set the value to *video**, which indicates audio and video files.
        

        @param request: GetUploadDetailsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetUploadDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadDetails',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetUploadDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_upload_details(self, request):
        """
        The type of the media file. Set the value to *video**, which indicates audio and video files.
        

        @param request: GetUploadDetailsRequest

        @return: GetUploadDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_details_with_options(request, runtime)

    def get_video_info_with_options(self, request, runtime):
        """
        The video snapshot URLs.
        

        @param request: GetVideoInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetVideoInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_info(self, request):
        """
        The video snapshot URLs.
        

        @param request: GetVideoInfoRequest

        @return: GetVideoInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_info_with_options(request, runtime)

    def get_video_infos_with_options(self, request, runtime):
        """
        The duration of the video. Unit: seconds.
        

        @param request: GetVideoInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetVideoInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_infos(self, request):
        """
        The duration of the video. Unit: seconds.
        

        @param request: GetVideoInfosRequest

        @return: GetVideoInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_infos_with_options(request, runtime)

    def get_video_list_with_options(self, request, runtime):
        """
        You can call this operation to query information about media files based on the filter conditions that you specify, such as video status and category ID. Information about a maximum of *5,000** media files can be returned for each request. We recommend that you set the StartTime and EndTime parameters to specify a time range for each request. For more information about how to query information about more media files or even all media files, see [SearchMedia](~~86044~~).
        

        @param request: GetVideoListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetVideoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoList',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_list(self, request):
        """
        You can call this operation to query information about media files based on the filter conditions that you specify, such as video status and category ID. Information about a maximum of *5,000** media files can be returned for each request. We recommend that you set the StartTime and EndTime parameters to specify a time range for each request. For more information about how to query information about more media files or even all media files, see [SearchMedia](~~86044~~).
        

        @param request: GetVideoListRequest

        @return: GetVideoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_list_with_options(request, runtime)

    def get_video_play_auth_with_options(self, request, runtime):
        """
        The thumbnail URL of the audio or video file.
        

        @param request: GetVideoPlayAuthRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetVideoPlayAuthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_version):
            query['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.auth_info_timeout):
            query['AuthInfoTimeout'] = request.auth_info_timeout
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoPlayAuth',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVideoPlayAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_play_auth(self, request):
        """
        The thumbnail URL of the audio or video file.
        

        @param request: GetVideoPlayAuthRequest

        @return: GetVideoPlayAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_play_auth_with_options(request, runtime)

    def get_vod_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVodTemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vod_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vod_template_with_options(request, runtime)

    def get_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWatermark',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def get_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_watermark_with_options(request, runtime)

    def list_aiimage_info_with_options(self, request, runtime):
        """
        You can call this operation to query AI processing results about images of a specified video. Images of different videos cannot be queried in one request.
        - The smart thumbnail feature is not supported. You cannot call this operation.
        - You can call this operation to query AI processing results about images of a specified video. Images of different videos cannot be queried in one request.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: ListAIImageInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAIImageInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAIImageInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAIImageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_aiimage_info(self, request):
        """
        You can call this operation to query AI processing results about images of a specified video. Images of different videos cannot be queried in one request.
        - The smart thumbnail feature is not supported. You cannot call this operation.
        - You can call this operation to query AI processing results about images of a specified video. Images of different videos cannot be queried in one request.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: ListAIImageInfoRequest

        @return: ListAIImageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aiimage_info_with_options(request, runtime)

    def list_aijob_with_options(self, request, runtime):
        """
        The IDs of the jobs that do not exist.
        

        @param request: ListAIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAIJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAIJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def list_aijob(self, request):
        """
        The IDs of the jobs that do not exist.
        

        @param request: ListAIJobRequest

        @return: ListAIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aijob_with_options(request, runtime)

    def list_aitemplate_with_options(self, request, runtime):
        """
        The returned result.
        

        @param request: ListAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_aitemplate(self, request):
        """
        The returned result.
        

        @param request: ListAITemplateRequest

        @return: ListAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aitemplate_with_options(request, runtime)

    def list_app_info_with_options(self, request, runtime):
        """
        The description of the application.
        

        @param request: ListAppInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_info(self, request):
        """
        The description of the application.
        

        @param request: ListAppInfoRequest

        @return: ListAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_info_with_options(request, runtime)

    def list_app_policies_for_identity_with_options(self, request, runtime):
        """
        The name of the identity.
        *   Specifies the ID of the RAM user when the IdentityType parameter is set to RamUser.
        *   Specifies the name of the RAM role when the IdentityType parameter is set to RamRole.
        

        @param request: ListAppPoliciesForIdentityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAppPoliciesForIdentityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppPoliciesForIdentity',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAppPoliciesForIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_policies_for_identity(self, request):
        """
        The name of the identity.
        *   Specifies the ID of the RAM user when the IdentityType parameter is set to RamUser.
        *   Specifies the name of the RAM role when the IdentityType parameter is set to RamRole.
        

        @param request: ListAppPoliciesForIdentityRequest

        @return: ListAppPoliciesForIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_policies_for_identity_with_options(request, runtime)

    def list_audit_security_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuditSecurityIp',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListAuditSecurityIpResponse(),
            self.call_api(params, req, runtime)
        )

    def list_audit_security_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_audit_security_ip_with_options(request, runtime)

    def list_dynamic_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicImage',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListDynamicImageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dynamic_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_image_with_options(request, runtime)

    def list_live_record_video_with_options(self, request, runtime):
        """
        The ID of the video category.
        

        @param request: ListLiveRecordVideoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLiveRecordVideoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordVideo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListLiveRecordVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_record_video(self, request):
        """
        The ID of the video category.
        

        @param request: ListLiveRecordVideoRequest

        @return: ListLiveRecordVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_video_with_options(request, runtime)

    def list_snapshots_with_options(self, request, runtime):
        """
        The type of snapshots that are returned. Valid values:
        *   **CoverSnapshot**: thumbnail snapshot
        *   **NormalSnapshot**: normal snapshot
        *   **SpriteSnapshot**: sprite snapshot
        *   **SpriteOriginSnapshot**: sprite source snapshot
        *   **WebVttSnapshot**: WebVTT snapshot
        

        @param request: ListSnapshotsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_snapshots(self, request):
        """
        The type of snapshots that are returned. Valid values:
        *   **CoverSnapshot**: thumbnail snapshot
        *   **NormalSnapshot**: normal snapshot
        *   **SpriteSnapshot**: sprite snapshot
        *   **SpriteOriginSnapshot**: sprite source snapshot
        *   **WebVttSnapshot**: WebVTT snapshot
        

        @param request: ListSnapshotsRequest

        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    def list_transcode_task_with_options(self, request, runtime):
        """
        The time when the transcoding task was created. The time follows the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        

        @param request: ListTranscodeTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTranscodeTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTranscodeTask',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListTranscodeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transcode_task(self, request):
        """
        The time when the transcoding task was created. The time follows the ISO 8601 standard in the yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        

        @param request: ListTranscodeTaskRequest

        @return: ListTranscodeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_task_with_options(request, runtime)

    def list_transcode_template_group_with_options(self, request, runtime):
        """
        The ID of the application. Default value: *app-1000000**. For more information, see [Overview](~~113600~~).
        

        @param request: ListTranscodeTemplateGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTranscodeTemplateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTranscodeTemplateGroup',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transcode_template_group(self, request):
        """
        The ID of the application. Default value: *app-1000000**. For more information, see [Overview](~~113600~~).
        

        @param request: ListTranscodeTemplateGroupRequest

        @return: ListTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_template_group_with_options(request, runtime)

    def list_vod_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVodTemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vod_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vod_template_with_options(request, runtime)

    def list_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWatermark',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ListWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def list_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_watermark_with_options(request, runtime)

    def move_app_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target_app_id):
            query['TargetAppId'] = request.target_app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAppResource',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.MoveAppResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def move_app_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_app_resource_with_options(request, runtime)

    def preload_vod_object_caches_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *PreloadVodObjectCaches**.
        

        @param request: PreloadVodObjectCachesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PreloadVodObjectCachesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='PreloadVodObjectCaches',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.PreloadVodObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def preload_vod_object_caches(self, request):
        """
        The operation that you want to perform. Set the value to *PreloadVodObjectCaches**.
        

        @param request: PreloadVodObjectCachesRequest

        @return: PreloadVodObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preload_vod_object_caches_with_options(request, runtime)

    def produce_editing_project_video_with_options(self, request, runtime):
        """
        The title of the online editing project.
        

        @param request: ProduceEditingProjectVideoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ProduceEditingProjectVideoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.media_metadata):
            query['MediaMetadata'] = request.media_metadata
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.produce_config):
            query['ProduceConfig'] = request.produce_config
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceEditingProjectVideo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.ProduceEditingProjectVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def produce_editing_project_video(self, request):
        """
        The title of the online editing project.
        

        @param request: ProduceEditingProjectVideoRequest

        @return: ProduceEditingProjectVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.produce_editing_project_video_with_options(request, runtime)

    def refresh_media_play_urls_with_options(self, request, runtime):
        """
        The formats of the media streams you want to refresh or prefetch. You can specify multiple formats. Separate multiple formats with commas (,). If you leave this parameter empty, media streams in all formats are refreshed or prefetched by default. Valid values:
        *   **mp4**\
        *   **m3u8**\
        *   **mp3**\
        *   **flv**\
        *   **webm**\
        *   **ts**\
        

        @param request: RefreshMediaPlayUrlsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RefreshMediaPlayUrlsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definitions):
            query['Definitions'] = request.definitions
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.slice_count):
            query['SliceCount'] = request.slice_count
        if not UtilClient.is_unset(request.slice_flag):
            query['SliceFlag'] = request.slice_flag
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshMediaPlayUrls',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshMediaPlayUrlsResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_media_play_urls(self, request):
        """
        The formats of the media streams you want to refresh or prefetch. You can specify multiple formats. Separate multiple formats with commas (,). If you leave this parameter empty, media streams in all formats are refreshed or prefetched by default. Valid values:
        *   **mp4**\
        *   **m3u8**\
        *   **mp3**\
        *   **flv**\
        *   **webm**\
        *   **ts**\
        

        @param request: RefreshMediaPlayUrlsRequest

        @return: RefreshMediaPlayUrlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_media_play_urls_with_options(request, runtime)

    def refresh_upload_video_with_options(self, request, runtime):
        """
        The upload credential.
        > The upload credential returned by this operation is Base64-encoded. Before you can use an SDK or an API operation to upload a media asset based on the upload credential, you must decode the upload credential by using the Base64 algorithm. You must parse the upload credential only if you use native OSS SDKs or OSS API for uploads.
        

        @param request: RefreshUploadVideoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RefreshUploadVideoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshUploadVideo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshUploadVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_upload_video(self, request):
        """
        The upload credential.
        > The upload credential returned by this operation is Base64-encoded. Before you can use an SDK or an API operation to upload a media asset based on the upload credential, you must decode the upload credential by using the Base64 algorithm. You must parse the upload credential only if you use native OSS SDKs or OSS API for uploads.
        

        @param request: RefreshUploadVideoRequest

        @return: RefreshUploadVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_video_with_options(request, runtime)

    def refresh_vod_object_caches_with_options(self, request, runtime):
        """
        The ID of the refresh task. Separate multiple task IDs with commas (,).
        

        @param request: RefreshVodObjectCachesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RefreshVodObjectCachesResponse
        """
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
            action='RefreshVodObjectCaches',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.RefreshVodObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_vod_object_caches(self, request):
        """
        The ID of the refresh task. Separate multiple task IDs with commas (,).
        

        @param request: RefreshVodObjectCachesRequest

        @return: RefreshVodObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_vod_object_caches_with_options(request, runtime)

    def register_media_with_options(self, request, runtime):
        """
        The media files that are registered, including newly registered and repeatedly registered media files.
        

        @param request: RegisterMediaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RegisterMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.register_metadatas):
            query['RegisterMetadatas'] = request.register_metadatas
        if not UtilClient.is_unset(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMedia',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.RegisterMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def register_media(self, request):
        """
        The media files that are registered, including newly registered and repeatedly registered media files.
        

        @param request: RegisterMediaRequest

        @return: RegisterMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_media_with_options(request, runtime)

    def restore_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.restore_days):
            query['RestoreDays'] = request.restore_days
        if not UtilClient.is_unset(request.restore_tier):
            query['RestoreTier'] = request.restore_tier
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreMedia',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.RestoreMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_media_with_options(request, runtime)

    def search_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEditingProject',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SearchEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def search_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    def search_media_with_options(self, request, runtime):
        """
        The ID of the parent category.
        

        @param request: SearchMediaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.match):
            query['Match'] = request.match
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scroll_token):
            query['ScrollToken'] = request.scroll_token
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMedia',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SearchMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def search_media(self, request):
        """
        The ID of the parent category.
        

        @param request: SearchMediaRequest

        @return: SearchMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    def set_audit_security_ip_with_options(self, request, runtime):
        """
        The name of the review security group. Default value: *Default**. You can specify a maximum of 10 review security groups.
        

        @param request: SetAuditSecurityIpRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetAuditSecurityIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ips):
            query['Ips'] = request.ips
        if not UtilClient.is_unset(request.operate_mode):
            query['OperateMode'] = request.operate_mode
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAuditSecurityIp',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetAuditSecurityIpResponse(),
            self.call_api(params, req, runtime)
        )

    def set_audit_security_ip(self, request):
        """
        The name of the review security group. Default value: *Default**. You can specify a maximum of 10 review security groups.
        

        @param request: SetAuditSecurityIpRequest

        @return: SetAuditSecurityIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_audit_security_ip_with_options(request, runtime)

    def set_crossdomain_content_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: SetCrossdomainContentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetCrossdomainContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_real_owner_id):
            query['ResourceRealOwnerId'] = request.resource_real_owner_id
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCrossdomainContent',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetCrossdomainContentResponse(),
            self.call_api(params, req, runtime)
        )

    def set_crossdomain_content(self, request):
        """
        The ID of the request.
        

        @param request: SetCrossdomainContentRequest

        @return: SetCrossdomainContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_crossdomain_content_with_options(request, runtime)

    def set_default_aitemplate_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: SetDefaultAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDefaultAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_aitemplate(self, request):
        """
        The ID of the request.
        

        @param request: SetDefaultAITemplateRequest

        @return: SetDefaultAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_aitemplate_with_options(request, runtime)

    def set_default_transcode_template_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultTranscodeTemplateGroup',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_transcode_template_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_transcode_template_group_with_options(request, runtime)

    def set_default_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultWatermark',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetDefaultWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_watermark_with_options(request, runtime)

    def set_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEditingProjectMaterials',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_editing_project_materials_with_options(request, runtime)

    def set_message_callback_with_options(self, request, runtime):
        """
        The ID of the application. If you do not set this parameter, the default value *app-1000000** is used.
        

        @param request: SetMessageCallbackRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetMessageCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_switch):
            query['AuthSwitch'] = request.auth_switch
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackURL'] = request.callback_url
        if not UtilClient.is_unset(request.event_type_list):
            query['EventTypeList'] = request.event_type_list
        if not UtilClient.is_unset(request.mns_endpoint):
            query['MnsEndpoint'] = request.mns_endpoint
        if not UtilClient.is_unset(request.mns_queue_name):
            query['MnsQueueName'] = request.mns_queue_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMessageCallback',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def set_message_callback(self, request):
        """
        The ID of the application. If you do not set this parameter, the default value *app-1000000** is used.
        

        @param request: SetMessageCallbackRequest

        @return: SetMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_message_callback_with_options(request, runtime)

    def set_vod_domain_certificate_with_options(self, request, runtime):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: SetVodDomainCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetVodDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='SetVodDomainCertificate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SetVodDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_vod_domain_certificate(self, request):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: SetVodDomainCertificateRequest

        @return: SetVodDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_vod_domain_certificate_with_options(request, runtime)

    def submit_aiimage_audit_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_audit_configuration):
            query['MediaAuditConfiguration'] = request.media_audit_configuration
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAIImageAuditJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIImageAuditJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_aiimage_audit_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_audit_job_with_options(request, runtime)

    def submit_aiimage_job_with_options(self, request, runtime):
        """
        The returned data.
        

        @param request: SubmitAIImageJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitAIImageJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aipipeline_id):
            query['AIPipelineId'] = request.aipipeline_id
        if not UtilClient.is_unset(request.aitemplate_id):
            query['AITemplateId'] = request.aitemplate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAIImageJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_aiimage_job(self, request):
        """
        The returned data.
        

        @param request: SubmitAIImageJobRequest

        @return: SubmitAIImageJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_job_with_options(request, runtime)

    def submit_aijob_with_options(self, request, runtime):
        """
        The returned data.
        

        @param request: SubmitAIJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitAIJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAIJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_aijob(self, request):
        """
        The returned data.
        

        @param request: SubmitAIJobRequest

        @return: SubmitAIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_aijob_with_options(request, runtime)

    def submit_aimedia_audit_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_audit_configuration):
            query['MediaAuditConfiguration'] = request.media_audit_configuration
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAIMediaAuditJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitAIMediaAuditJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_aimedia_audit_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_aimedia_audit_job_with_options(request, runtime)

    def submit_dynamic_image_job_with_options(self, request, runtime):
        """
        The ID of the video.
        

        @param request: SubmitDynamicImageJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitDynamicImageJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_image_template_id):
            query['DynamicImageTemplateId'] = request.dynamic_image_template_id
        if not UtilClient.is_unset(request.override_params):
            query['OverrideParams'] = request.override_params
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicImageJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitDynamicImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_dynamic_image_job(self, request):
        """
        The ID of the video.
        

        @param request: SubmitDynamicImageJobRequest

        @return: SubmitDynamicImageJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    def submit_media_dnadelete_job_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: SubmitMediaDNADeleteJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitMediaDNADeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaDNADeleteJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitMediaDNADeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_media_dnadelete_job(self, request):
        """
        The ID of the request.
        

        @param request: SubmitMediaDNADeleteJobRequest

        @return: SubmitMediaDNADeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_media_dnadelete_job_with_options(request, runtime)

    def submit_preprocess_jobs_with_options(self, request, runtime):
        """
        The ID of the job.
        

        @param request: SubmitPreprocessJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitPreprocessJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preprocess_type):
            query['PreprocessType'] = request.preprocess_type
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPreprocessJobs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitPreprocessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_preprocess_jobs(self, request):
        """
        The ID of the job.
        

        @param request: SubmitPreprocessJobsRequest

        @return: SubmitPreprocessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_preprocess_jobs_with_options(request, runtime)

    def submit_snapshot_job_with_options(self, request, runtime):
        """
        The ID of the snapshot template.
        *   We recommend that you create a snapshot template before you specify the ID of the snapshot template.
        *   If you set the SnapshotTemplateId parameter, all the other request parameters except the Action and VideoId parameters are ignored.
        *   For more information about how to create a snapshot template, see [AddVodTemplate](~~99406~~).
        

        @param request: SubmitSnapshotJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitSnapshotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.snapshot_template_id):
            query['SnapshotTemplateId'] = request.snapshot_template_id
        if not UtilClient.is_unset(request.specified_offset_time):
            query['SpecifiedOffsetTime'] = request.specified_offset_time
        if not UtilClient.is_unset(request.sprite_snapshot_config):
            query['SpriteSnapshotConfig'] = request.sprite_snapshot_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_snapshot_job(self, request):
        """
        The ID of the snapshot template.
        *   We recommend that you create a snapshot template before you specify the ID of the snapshot template.
        *   If you set the SnapshotTemplateId parameter, all the other request parameters except the Action and VideoId parameters are ignored.
        *   For more information about how to create a snapshot template, see [AddVodTemplate](~~99406~~).
        

        @param request: SubmitSnapshotJobRequest

        @return: SubmitSnapshotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    def submit_transcode_jobs_with_options(self, request, runtime):
        """
        The ID of the transcoding template group used when the video is transcoded. To specify a transcoding template group, you can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/?spm=a2c4g.11186623.2.18.2f1a2267jCybwh#/vod/settings/transcode/vod) and view the ID of the transcoding template group on the Transcode page.
        

        @param request: SubmitTranscodeJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitTranscodeJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_config):
            query['EncryptConfig'] = request.encrypt_config
        if not UtilClient.is_unset(request.override_params):
            query['OverrideParams'] = request.override_params
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTranscodeJobs',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitTranscodeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_transcode_jobs(self, request):
        """
        The ID of the transcoding template group used when the video is transcoded. To specify a transcoding template group, you can log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/?spm=a2c4g.11186623.2.18.2f1a2267jCybwh#/vod/settings/transcode/vod) and view the ID of the transcoding template group on the Transcode page.
        

        @param request: SubmitTranscodeJobsRequest

        @return: SubmitTranscodeJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_transcode_jobs_with_options(request, runtime)

    def submit_workflow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitWorkflowJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitWorkflowJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_workflow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_workflow_job_with_options(request, runtime)

    def update_aitemplate_with_options(self, request, runtime):
        """
        The returned result.
        

        @param request: UpdateAITemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAITemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAITemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aitemplate(self, request):
        """
        The returned result.
        

        @param request: UpdateAITemplateRequest

        @return: UpdateAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aitemplate_with_options(request, runtime)

    def update_app_info_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: UpdateAppInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_info(self, request):
        """
        The ID of the request.
        

        @param request: UpdateAppInfoRequest

        @return: UpdateAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_app_info_with_options(request, runtime)

    def update_attached_media_infos_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: UpdateAttachedMediaInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAttachedMediaInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAttachedMediaInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateAttachedMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def update_attached_media_infos(self, request):
        """
        The ID of the request.
        

        @param request: UpdateAttachedMediaInfosRequest

        @return: UpdateAttachedMediaInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_attached_media_infos_with_options(request, runtime)

    def update_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cate_name):
            query['CateName'] = request.cate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    def update_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEditingProject',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    def update_image_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImageInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def update_image_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_image_infos_with_options(request, runtime)

    def update_media_storage_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.restore_tier):
            query['RestoreTier'] = request.restore_tier
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaStorageClass',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateMediaStorageClassResponse(),
            self.call_api(params, req, runtime)
        )

    def update_media_storage_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_media_storage_class_with_options(request, runtime)

    def update_transcode_template_group_with_options(self, request, runtime):
        """
        The ID of the transcoding template group.
        

        @param request: UpdateTranscodeTemplateGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTranscodeTemplateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.locked):
            query['Locked'] = request.locked
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not UtilClient.is_unset(request.transcode_template_list):
            query['TranscodeTemplateList'] = request.transcode_template_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTranscodeTemplateGroup',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transcode_template_group(self, request):
        """
        The ID of the transcoding template group.
        

        @param request: UpdateTranscodeTemplateGroupRequest

        @return: UpdateTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_transcode_template_group_with_options(request, runtime)

    def update_video_info_with_options(self, request, runtime):
        """
        The ID of the video.
        

        @param request: UpdateVideoInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateVideoInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVideoInfo',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVideoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_video_info(self, request):
        """
        The ID of the video.
        

        @param request: UpdateVideoInfoRequest

        @return: UpdateVideoInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_video_info_with_options(request, runtime)

    def update_video_infos_with_options(self, request, runtime):
        """
        The IDs of the videos that do not exist.
        

        @param request: UpdateVideoInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateVideoInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVideoInfos',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVideoInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def update_video_infos(self, request):
        """
        The IDs of the videos that do not exist.
        

        @param request: UpdateVideoInfosRequest

        @return: UpdateVideoInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_video_infos_with_options(request, runtime)

    def update_vod_domain_with_options(self, request, runtime):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: UpdateVodDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateVodDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='UpdateVodDomain',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vod_domain(self, request):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: UpdateVodDomainRequest

        @return: UpdateVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_vod_domain_with_options(request, runtime)

    def update_vod_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVodTemplate',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vod_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vod_template_with_options(request, runtime)

    def update_watermark_with_options(self, request, runtime):
        """
        The configurations such as the position and effect of the text watermark or image watermark. The value is a JSON-formatted string.
        > The value of this parameter varies with the watermark type. For more information about the data structure, see the "WatermarkConfig" section of the [Media processing parameters](~~98618~~) topic.
        

        @param request: UpdateWatermarkRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.watermark_config):
            query['WatermarkConfig'] = request.watermark_config
        if not UtilClient.is_unset(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWatermark',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UpdateWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_watermark(self, request):
        """
        The configurations such as the position and effect of the text watermark or image watermark. The value is a JSON-formatted string.
        > The value of this parameter varies with the watermark type. For more information about the data structure, see the "WatermarkConfig" section of the [Media processing parameters](~~98618~~) topic.
        

        @param request: UpdateWatermarkRequest

        @return: UpdateWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    def upload_media_by_urlwith_options(self, request, runtime):
        """
        The ID of the workflow. To view the ID of the workflow, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose *Configuration Management** > **Media Processing** > **Workflows**.
        > If both the WorkflowId and TemplateGroupId parameters are set, the value of the WorkflowId parameter takes effect. For more information, see [Workflows](~~115347~~).
        

        @param request: UploadMediaByURLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadMediaByURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not UtilClient.is_unset(request.upload_metadatas):
            query['UploadMetadatas'] = request.upload_metadatas
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMediaByURL',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UploadMediaByURLResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_media_by_url(self, request):
        """
        The ID of the workflow. To view the ID of the workflow, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose *Configuration Management** > **Media Processing** > **Workflows**.
        > If both the WorkflowId and TemplateGroupId parameters are set, the value of the WorkflowId parameter takes effect. For more information, see [Workflows](~~115347~~).
        

        @param request: UploadMediaByURLRequest

        @return: UploadMediaByURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    def upload_stream_by_urlwith_options(self, request, runtime):
        """
        The URL of the transcoded stream.
        If URL authentication is required, you must pass authentication information in this parameter and make sure that the URL can be accessed over the Internet.
        

        @param request: UploadStreamByURLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadStreamByURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not UtilClient.is_unset(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadStreamByURL',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.UploadStreamByURLResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_stream_by_url(self, request):
        """
        The URL of the transcoded stream.
        If URL authentication is required, you must pass authentication information in this parameter and make sure that the URL can be accessed over the Internet.
        

        @param request: UploadStreamByURLRequest

        @return: UploadStreamByURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_stream_by_urlwith_options(request, runtime)

    def verify_vod_domain_owner_with_options(self, request, runtime):
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
            action='VerifyVodDomainOwner',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.VerifyVodDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_vod_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_vod_domain_owner_with_options(request, runtime)
