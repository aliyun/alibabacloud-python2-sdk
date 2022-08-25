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
        runtime = util_models.RuntimeOptions()
        return self.add_aitemplate_with_options(request, runtime)

    def add_category_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.add_transcode_template_group_with_options(request, runtime)

    def add_vod_domain_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.add_vod_domain_with_options(request, runtime)

    def add_vod_template_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.add_vod_template_with_options(request, runtime)

    def add_watermark_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.add_watermark_with_options(request, runtime)

    def attach_app_policy_to_identity_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.attach_app_policy_to_identity_with_options(request, runtime)

    def batch_set_vod_domain_configs_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vod_domain_configs_with_options(request, runtime)

    def batch_start_vod_domain_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.batch_start_vod_domain_with_options(request, runtime)

    def batch_stop_vod_domain_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_vod_domain_with_options(request, runtime)

    def cancel_url_upload_jobs_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.cancel_url_upload_jobs_with_options(request, runtime)

    def create_app_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_upload_attached_media_with_options(request, runtime)

    def create_upload_image_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_upload_image_with_options(request, runtime)

    def create_upload_video_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_aiimage_infos_with_options(request, runtime)

    def delete_aitemplate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_aitemplate_with_options(request, runtime)

    def delete_app_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_app_info_with_options(request, runtime)

    def delete_attached_media_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_attached_media_with_options(request, runtime)

    def delete_category_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_message_callback_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    def delete_mezzanines_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_mezzanines_with_options(request, runtime)

    def delete_multipart_upload_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_transcode_template_group_with_options(request, runtime)

    def delete_video_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    def delete_vod_domain_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_domain_with_options(request, runtime)

    def delete_vod_specific_config_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    def describe_play_top_videos_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_play_top_videos_with_options(request, runtime)

    def describe_play_user_avg_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_avg_with_options(request, runtime)

    def describe_play_user_total_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_total_with_options(request, runtime)

    def describe_play_video_statis_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_play_video_statis_with_options(request, runtime)

    def describe_vod_aidata_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_aidata_with_options(request, runtime)

    def describe_vod_certificate_list_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_certificate_list_with_options(request, runtime)

    def describe_vod_domain_bps_data_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_configs_with_options(request, runtime)

    def describe_vod_domain_detail_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_detail_with_options(request, runtime)

    def describe_vod_domain_log_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_log_with_options(request, runtime)

    def describe_vod_domain_traffic_data_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_traffic_data_with_options(request, runtime)

    def describe_vod_domain_usage_data_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_usage_data_with_options(request, runtime)

    def describe_vod_refresh_quota_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_quota_with_options(request, runtime)

    def describe_vod_refresh_tasks_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_tasks_with_options(request, runtime)

    def describe_vod_storage_data_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_storage_data_with_options(request, runtime)

    def describe_vod_transcode_data_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_aiimage_jobs_with_options(request, runtime)

    def get_aimedia_audit_job_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_aimedia_audit_job_with_options(request, runtime)

    def get_aitemplate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_aitemplate_with_options(request, runtime)

    def get_aivideo_tag_result_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_aivideo_tag_result_with_options(request, runtime)

    def get_app_infos_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_image_infos_with_options(request, runtime)

    def get_media_audit_audio_result_detail_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_media_dnaresult_with_options(request, runtime)

    def get_media_refresh_jobs_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_media_refresh_jobs_with_options(request, runtime)

    def get_message_callback_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_message_callback_with_options(request, runtime)

    def get_mezzanine_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_mezzanine_info_with_options(request, runtime)

    def get_play_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    def get_transcode_summary_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_summary_with_options(request, runtime)

    def get_transcode_task_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_task_with_options(request, runtime)

    def get_transcode_template_group_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_template_group_with_options(request, runtime)

    def get_urlupload_infos_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_urlupload_infos_with_options(request, runtime)

    def get_upload_details_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_upload_details_with_options(request, runtime)

    def get_video_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_video_info_with_options(request, runtime)

    def get_video_infos_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_video_infos_with_options(request, runtime)

    def get_video_list_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.get_video_list_with_options(request, runtime)

    def get_video_play_auth_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_aiimage_info_with_options(request, runtime)

    def list_aijob_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_aijob_with_options(request, runtime)

    def list_aitemplate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_aitemplate_with_options(request, runtime)

    def list_app_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_app_info_with_options(request, runtime)

    def list_app_policies_for_identity_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_video_with_options(request, runtime)

    def list_snapshots_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    def list_transcode_task_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_task_with_options(request, runtime)

    def list_transcode_template_group_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.preload_vod_object_caches_with_options(request, runtime)

    def produce_editing_project_video_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.produce_editing_project_video_with_options(request, runtime)

    def refresh_media_play_urls_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.refresh_media_play_urls_with_options(request, runtime)

    def refresh_upload_video_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_video_with_options(request, runtime)

    def refresh_vod_object_caches_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.refresh_vod_object_caches_with_options(request, runtime)

    def register_media_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.register_media_with_options(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    def set_audit_security_ip_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.set_audit_security_ip_with_options(request, runtime)

    def set_crossdomain_content_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.set_crossdomain_content_with_options(request, runtime)

    def set_default_aitemplate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.set_message_callback_with_options(request, runtime)

    def set_vod_domain_certificate_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_job_with_options(request, runtime)

    def submit_aijob_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    def submit_media_dnadelete_job_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.submit_media_dnadelete_job_with_options(request, runtime)

    def submit_preprocess_jobs_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.submit_preprocess_jobs_with_options(request, runtime)

    def submit_snapshot_job_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    def submit_transcode_jobs_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_aitemplate_with_options(request, runtime)

    def update_app_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_app_info_with_options(request, runtime)

    def update_attached_media_infos_with_options(self, request, runtime):
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

    def update_transcode_template_group_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_transcode_template_group_with_options(request, runtime)

    def update_video_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_video_info_with_options(request, runtime)

    def update_video_infos_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_video_infos_with_options(request, runtime)

    def update_vod_domain_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    def upload_media_by_urlwith_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    def upload_stream_by_urlwith_options(self, request, runtime):
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
