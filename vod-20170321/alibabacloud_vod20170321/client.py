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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   Before you add an AI template for automated review and smart thumbnail tasks, make sure that [automated review](https://ai.aliyun.com/vi/censor) and [smart thumbnail](https://ai.aliyun.com/vi/cover) are enabled.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   Before you add an AI template for automated review and smart thumbnail tasks, make sure that [automated review](https://ai.aliyun.com/vi/censor) and [smart thumbnail](https://ai.aliyun.com/vi/cover) are enabled.
        

        @param request: AddAITemplateRequest

        @return: AddAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_aitemplate_with_options(request, runtime)

    def add_category_with_options(self, request, runtime):
        """
        A maximum of three category levels can be created. Each category can contain up to 100 subcategories.
        

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
        A maximum of three category levels can be created. Each category can contain up to 100 subcategories.
        

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

    def add_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_ids):
            query['MaterialIds'] = request.material_ids
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEditingProjectMaterials',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.AddEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_materials_with_options(request, runtime)

    def add_transcode_template_group_with_options(self, request, runtime):
        """
        You cannot perform custom operations on transcoding template groups that are **locked** in the ApsaraVideo VOD console. You can call the [GetTranscodeTemplateGroup](~~GetTranscodeTemplateGroup~~) operation to query the information about a transcoding template group and check whether the transcoding template group is locked based on the value of the Locked parameter. You can call the [UpdateTranscodeTemplateGroup](~~UpdateTranscodeTemplateGroup~~) operation to unlock a transcoding template group if it is locked. Then, you can perform custom operations on the transcoding template group.
        *   An Object Storage Service (OSS) bucket is required to store files that are used for transcoding. You cannot create a transcoding template group if no bucket is available. To activate a bucket, perform the following operations: Log on to the ApsaraVideo VOD console. In the left-side navigation pane, choose **Configuration Management > Media Management > Storage**. On the **Storage** page, activate the bucket that is allocated by ApsaraVideo VOD.
        *   You cannot add transcoding templates to the **No Transcoding** template group.
        *   You can create a maximum of 20 transcoding template groups.
        *   You can add a maximum of 20 transcoding templates to a transcoding template group.
        *   If you want to generate a URL for adaptive bitrate streaming, you can add video packaging templates to a transcoding template group. You can add a maximum of 10 video packaging templates to a transcoding template group. If you add more than 10 video packaging templates, URLs of the video transcoded based on the video packaging templates are generated but the URL for adaptive bitrate streaming is not generated.
        ### QPS limits
        You can call this operation up to five times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](~~342790~~).
        

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
        You cannot perform custom operations on transcoding template groups that are **locked** in the ApsaraVideo VOD console. You can call the [GetTranscodeTemplateGroup](~~GetTranscodeTemplateGroup~~) operation to query the information about a transcoding template group and check whether the transcoding template group is locked based on the value of the Locked parameter. You can call the [UpdateTranscodeTemplateGroup](~~UpdateTranscodeTemplateGroup~~) operation to unlock a transcoding template group if it is locked. Then, you can perform custom operations on the transcoding template group.
        *   An Object Storage Service (OSS) bucket is required to store files that are used for transcoding. You cannot create a transcoding template group if no bucket is available. To activate a bucket, perform the following operations: Log on to the ApsaraVideo VOD console. In the left-side navigation pane, choose **Configuration Management > Media Management > Storage**. On the **Storage** page, activate the bucket that is allocated by ApsaraVideo VOD.
        *   You cannot add transcoding templates to the **No Transcoding** template group.
        *   You can create a maximum of 20 transcoding template groups.
        *   You can add a maximum of 20 transcoding templates to a transcoding template group.
        *   If you want to generate a URL for adaptive bitrate streaming, you can add video packaging templates to a transcoding template group. You can add a maximum of 10 video packaging templates to a transcoding template group. If you add more than 10 video packaging templates, URLs of the video transcoded based on the video packaging templates are generated but the URL for adaptive bitrate streaming is not generated.
        ### QPS limits
        You can call this operation up to five times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](~~342790~~).
        

        @param request: AddTranscodeTemplateGroupRequest

        @return: AddTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_transcode_template_group_with_options(request, runtime)

    def add_vod_domain_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   Before you add a domain name to accelerate, you must activate ApsaraVideo VOD and apply for an Internet content provider (ICP) filing for the domain name. For more information about how to activate ApsaraVideo VOD, see [Activate ApsaraVideo VOD](~~51512~~).
        *   If the content on the origin server is not stored on Alibaba Cloud, the content must be reviewed by Alibaba Cloud. The review will be complete by the end of the next business day after you submit an application.
        *   You can add only one domain name to accelerate in a request. You can add a maximum of 20 accelerated domain names within an Alibaba Cloud account.
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   Before you add a domain name to accelerate, you must activate ApsaraVideo VOD and apply for an Internet content provider (ICP) filing for the domain name. For more information about how to activate ApsaraVideo VOD, see [Activate ApsaraVideo VOD](~~51512~~).
        *   If the content on the origin server is not stored on Alibaba Cloud, the content must be reviewed by Alibaba Cloud. The review will be complete by the end of the next business day after you submit an application.
        *   You can add only one domain name to accelerate in a request. You can add a maximum of 20 accelerated domain names within an Alibaba Cloud account.
        

        @param request: AddVodDomainRequest

        @return: AddVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vod_domain_with_options(request, runtime)

    def add_vod_template_with_options(self, request, runtime):
        """
        >    After you create a snapshot template, you can specify the ID of the snapshot template in the request of the [SubmitSnapshotJob](~~72213~~) operation to take snapshots.
        > *   You can receive the [SnapshotComplete](~~57337~~) event notification by using an HTTP or HTTPS URL or in Message Service (MNS). For more information, see [Overview](~~55627~~).
        

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
        >    After you create a snapshot template, you can specify the ID of the snapshot template in the request of the [SubmitSnapshotJob](~~72213~~) operation to take snapshots.
        > *   You can receive the [SnapshotComplete](~~57337~~) event notification by using an HTTP or HTTPS URL or in Message Service (MNS). For more information, see [Overview](~~55627~~).
        

        @param request: AddVodTemplateRequest

        @return: AddVodTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vod_template_with_options(request, runtime)

    def add_watermark_with_options(self, request, runtime):
        """
        > ApsaraVideo VOD supports static image watermarks such as PNG files and dynamic image watermarks such as GIF, APNG, and MOV files.
        

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
        > ApsaraVideo VOD supports static image watermarks such as PNG files and dynamic image watermarks such as GIF, APNG, and MOV files.
        

        @param request: AddWatermarkRequest

        @return: AddWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_watermark_with_options(request, runtime)

    def attach_app_policy_to_identity_with_options(self, request, runtime):
        """
        > You can grant a RAM user or RAM role permissions to access up to 10 applications.
        

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
        > You can grant a RAM user or RAM role permissions to access up to 10 applications.
        

        @param request: AttachAppPolicyToIdentityRequest

        @return: AttachAppPolicyToIdentityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_app_policy_to_identity_with_options(request, runtime)

    def batch_set_vod_domain_configs_with_options(self, request, runtime):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

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
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: BatchSetVodDomainConfigsRequest

        @return: BatchSetVodDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vod_domain_configs_with_options(request, runtime)

    def batch_start_vod_domain_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   If the domain name that you want to enable is invalid or your Alibaba Cloud account has overdue payments, you cannot call this operation to enable the domain name.
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   If the domain name that you want to enable is invalid or your Alibaba Cloud account has overdue payments, you cannot call this operation to enable the domain name.
        

        @param request: BatchStartVodDomainRequest

        @return: BatchStartVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_start_vod_domain_with_options(request, runtime)

    def batch_stop_vod_domain_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   After you disable an accelerated domain name, the information about the domain name is retained. The system automatically reroutes all the requests that are destined for the domain name to the origin server.
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   After you disable an accelerated domain name, the information about the domain name is retained. The system automatically reroutes all the requests that are destined for the domain name to the origin server.
        

        @param request: BatchStopVodDomainRequest

        @return: BatchStopVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_vod_domain_with_options(request, runtime)

    def cancel_url_upload_jobs_with_options(self, request, runtime):
        """
        You can cancel only a URL-based upload job in the **Pending** state. You can query the status of a URL-based upload job by calling the [GetURLUploadInfos](~~106830~~) operation.
        *   You cannot cancel an upload job that already starts.
        

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
        You can cancel only a URL-based upload job in the **Pending** state. You can query the status of a URL-based upload job by calling the [GetURLUploadInfos](~~106830~~) operation.
        *   You cannot cancel an upload job that already starts.
        

        @param request: CancelUrlUploadJobsRequest

        @return: CancelUrlUploadJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_url_upload_jobs_with_options(request, runtime)

    def create_app_info_with_options(self, request, runtime):
        """
        You can create up to 10 applications within an Alibaba Cloud account. For more information, see [Multi-application service](~~113600~~).
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

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
        You can create up to 10 applications within an Alibaba Cloud account. For more information, see [Multi-application service](~~113600~~).
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

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
        The process of obtaining upload URLs and credentials is a core process in ApsaraVideo VOD and is required for each upload operation. ApsaraVideo VOD provides multiple upload methods. You can upload auxiliary media assets by using server upload SDKs, client upload SDKs, URLs of auxiliary media assets, Object Storage Service (OSS) API, or native OSS SDKs. Each upload method has different requirements for obtaining upload URLs and credentials. For more information, see the "Usage notes" section of the [Upload URLs and credentials](~~55397~~) topic.
        *   If the upload credential expires, you can call this operation to obtain a new upload URL and credential. The default validity period of an upload credential is 3,000 seconds.
        *   You can configure a callback to receive an [AttachedMediaUploadComplete](~~103250~~) event notification to determine whether the upload is successful.
        

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
        The process of obtaining upload URLs and credentials is a core process in ApsaraVideo VOD and is required for each upload operation. ApsaraVideo VOD provides multiple upload methods. You can upload auxiliary media assets by using server upload SDKs, client upload SDKs, URLs of auxiliary media assets, Object Storage Service (OSS) API, or native OSS SDKs. Each upload method has different requirements for obtaining upload URLs and credentials. For more information, see the "Usage notes" section of the [Upload URLs and credentials](~~55397~~) topic.
        *   If the upload credential expires, you can call this operation to obtain a new upload URL and credential. The default validity period of an upload credential is 3,000 seconds.
        *   You can configure a callback to receive an [AttachedMediaUploadComplete](~~103250~~) event notification to determine whether the upload is successful.
        

        @param request: CreateUploadAttachedMediaRequest

        @return: CreateUploadAttachedMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_upload_attached_media_with_options(request, runtime)

    def create_upload_image_with_options(self, request, runtime):
        """
        You must obtain a URL and a credential before you upload an image to ApsaraVideo VOD. ApsaraVideo VOD provides multiple upload methods. You can upload files by using server upload SDKs, client upload SDKs, URLs, Object Storage Service (OSS) API, or OSS SDKs. Each upload method has different requirements for obtaining upload URLs and credentials. For more information, see the "Usage notes" section of the [Upload URLs and credentials](~~55397~~) topic.
        *   You cannot refresh the upload URL or credential when you upload images. If the image upload credential expires, you can call this operation to obtain a new upload URL and credential. By default, the validity period of an image upload credential is 3,000 seconds.
        *   You can call the [CreateUploadAttachedMedia](~~98467~~) operation to upload image watermarks.
        *   You can configure a callback for [ImageUploadComplete](~~91968~~) to receive notifications about the image upload status.
        

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
        You must obtain a URL and a credential before you upload an image to ApsaraVideo VOD. ApsaraVideo VOD provides multiple upload methods. You can upload files by using server upload SDKs, client upload SDKs, URLs, Object Storage Service (OSS) API, or OSS SDKs. Each upload method has different requirements for obtaining upload URLs and credentials. For more information, see the "Usage notes" section of the [Upload URLs and credentials](~~55397~~) topic.
        *   You cannot refresh the upload URL or credential when you upload images. If the image upload credential expires, you can call this operation to obtain a new upload URL and credential. By default, the validity period of an image upload credential is 3,000 seconds.
        *   You can call the [CreateUploadAttachedMedia](~~98467~~) operation to upload image watermarks.
        *   You can configure a callback for [ImageUploadComplete](~~91968~~) to receive notifications about the image upload status.
        

        @param request: CreateUploadImageRequest

        @return: CreateUploadImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_upload_image_with_options(request, runtime)

    def create_upload_video_with_options(self, request, runtime):
        """
        You can call this operation to obtain upload URLs and credentials for video and audio files. For more information, see [Upload URLs and credentials](~~55397~~).
        *   You can call this operation only to obtain the upload URLs and credentials for media files and create media assets in ApsaraVideo VOD. You cannot call this operation to upload media files. For more information about how to upload media files by calling API operations, see [Upload media files by calling API operations](~~476208~~).
        *   If the upload credential expires, call the [RefreshUploadVideo](~~55408~~) operation to obtain a new upload credential. The default validity period of an upload credential is 3,000 seconds.
        *   You can configure a callback to receive an [event notification](~~55396~~) when an audio or video file is uploaded. Alternatively, after you upload an audio or video file, you can call the [GetMezzanineInfo](~~59624~~) operation to determine whether the upload is successful based on the value of the Status response parameter.
        *   The VideoId parameter that is returned after you call this operation can be used for media processing or lifecycle management of media assets.
        *   You must obtain a URL and a credential before you upload a media file to ApsaraVideo VOD. ApsaraVideo VOD supports multiple upload methods. Each method has different requirements on upload URLs and credentials. For more information, see [Upload URLs and credentials](~~55397~~).
        

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
        You can call this operation to obtain upload URLs and credentials for video and audio files. For more information, see [Upload URLs and credentials](~~55397~~).
        *   You can call this operation only to obtain the upload URLs and credentials for media files and create media assets in ApsaraVideo VOD. You cannot call this operation to upload media files. For more information about how to upload media files by calling API operations, see [Upload media files by calling API operations](~~476208~~).
        *   If the upload credential expires, call the [RefreshUploadVideo](~~55408~~) operation to obtain a new upload credential. The default validity period of an upload credential is 3,000 seconds.
        *   You can configure a callback to receive an [event notification](~~55396~~) when an audio or video file is uploaded. Alternatively, after you upload an audio or video file, you can call the [GetMezzanineInfo](~~59624~~) operation to determine whether the upload is successful based on the value of the Status response parameter.
        *   The VideoId parameter that is returned after you call this operation can be used for media processing or lifecycle management of media assets.
        *   You must obtain a URL and a credential before you upload a media file to ApsaraVideo VOD. ApsaraVideo VOD supports multiple upload methods. Each method has different requirements on upload URLs and credentials. For more information, see [Upload URLs and credentials](~~55397~~).
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   This operation deletes only information about images that are submitted for AI processing. The image files are not deleted.
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   This operation deletes only information about images that are submitted for AI processing. The image files are not deleted.
        

        @param request: DeleteAIImageInfosRequest

        @return: DeleteAIImageInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aiimage_infos_with_options(request, runtime)

    def delete_aitemplate_with_options(self, request, runtime):
        """
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You cannot delete an AI template that is set as the default template.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You cannot delete an AI template that is set as the default template.
        

        @param request: DeleteAITemplateRequest

        @return: DeleteAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_aitemplate_with_options(request, runtime)

    def delete_app_info_with_options(self, request, runtime):
        """
        ## Usage note
        Application with resources can not be deleted.
        

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
        ## Usage note
        Application with resources can not be deleted.
        

        @param request: DeleteAppInfoRequest

        @return: DeleteAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_info_with_options(request, runtime)

    def delete_attached_media_with_options(self, request, runtime):
        """
        This operation physically deletes auxiliary media assets. Deleted auxiliary media assets cannot be recovered. Exercise caution when you call this operation.
        

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
        This operation physically deletes auxiliary media assets. Deleted auxiliary media assets cannot be recovered. Exercise caution when you call this operation.
        

        @param request: DeleteAttachedMediaRequest

        @return: DeleteAttachedMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_attached_media_with_options(request, runtime)

    def delete_category_with_options(self, request, runtime):
        """
        > If a video category is deleted, its subcategories, including level 2 and level 3 categories, are also deleted. Exercise caution when you call this operation.
        

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
        > If a video category is deleted, its subcategories, including level 2 and level 3 categories, are also deleted. Exercise caution when you call this operation.
        

        @param request: DeleteCategoryRequest

        @return: DeleteCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    def delete_dynamic_image_with_options(self, request, runtime):
        """
        > This operation deletes only the information about animated stickers, but not the animated stickers themselves.
        

        @param request: DeleteDynamicImageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDynamicImageResponse
        """
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
        """
        > This operation deletes only the information about animated stickers, but not the animated stickers themselves.
        

        @param request: DeleteDynamicImageRequest

        @return: DeleteDynamicImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_image_with_options(request, runtime)

    def delete_editing_project_with_options(self, request, runtime):
        """
        You can call this operation to delete multiple online editing projects at a time.
        ### QPS limits
        You can call this operation up to 20 times per second per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

        @param request: DeleteEditingProjectRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteEditingProjectResponse
        """
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
        """
        You can call this operation to delete multiple online editing projects at a time.
        ### QPS limits
        You can call this operation up to 20 times per second per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

        @param request: DeleteEditingProjectRequest

        @return: DeleteEditingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_with_options(request, runtime)

    def delete_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_ids):
            query['MaterialIds'] = request.material_ids
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjectMaterials',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.DeleteEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_materials_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        """
        After you call this operation to delete an image, the source file is permanently deleted and cannot be recovered. If some images are cached on Alibaba Cloud CDN points of presence (POPs), the image URLs do not immediately become invalid.
        *   You can call this operation to delete uploaded images and video snapshots.
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

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
        After you call this operation to delete an image, the source file is permanently deleted and cannot be recovered. If some images are cached on Alibaba Cloud CDN points of presence (POPs), the image URLs do not immediately become invalid.
        *   You can call this operation to delete uploaded images and video snapshots.
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

        @param request: DeleteImageRequest

        @return: DeleteImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_message_callback_with_options(self, request, runtime):
        """
        > For more information, see [Overview](~~55627~~).
        

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
        > For more information, see [Overview](~~55627~~).
        

        @param request: DeleteMessageCallbackRequest

        @return: DeleteMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    def delete_mezzanines_with_options(self, request, runtime):
        """
        All media processing operations in ApsaraVideo VOD, such as transcoding, snapshot capture, and content moderation, are performed on mezzanine files. If you delete the mezzanine files, you cannot perform follow-up media processing operations. Exercise caution when you call this operation.
        

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
        All media processing operations in ApsaraVideo VOD, such as transcoding, snapshot capture, and content moderation, are performed on mezzanine files. If you delete the mezzanine files, you cannot perform follow-up media processing operations. Exercise caution when you call this operation.
        

        @param request: DeleteMezzaninesRequest

        @return: DeleteMezzaninesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mezzanines_with_options(request, runtime)

    def delete_multipart_upload_with_options(self, request, runtime):
        """
        In a multipart upload, fragments may be generated if the upload fails. In most cases, the fragments are automatically deleted after seven days. You can call this operation to delete the generated fragments after the upload is successful or fails.
        * This operation does not delete the source file or transcoded file, but deletes only the fragments generated during the upload.
        * If you call the [DeleteVideo](~~52837~~) operation, the entire video file is deleted, including the generated fragments.
        

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
        In a multipart upload, fragments may be generated if the upload fails. In most cases, the fragments are automatically deleted after seven days. You can call this operation to delete the generated fragments after the upload is successful or fails.
        * This operation does not delete the source file or transcoded file, but deletes only the fragments generated during the upload.
        * If you call the [DeleteVideo](~~52837~~) operation, the entire video file is deleted, including the generated fragments.
        

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
        You cannot call this operation to delete the default transcoding template. You can delete the transcoding template when it is no longer specified as the default one.
        *   For security purposes, you cannot add, modify, or delete transcoding templates in a transcoding template group that is locked. To check whether a transcoding template group is locked, call the [GetTranscodeTemplateGroup](~~GetTranscodeTemplateGroup~~) operation and obtain the Locked parameter from the response. To modify transcoding templates within a locked transcoding template group, you must call the [UpdateTranscodeTemplateGroup](~~UpdateTranscodeTemplateGroup~~) operation to unlock the transcoding template group first.
        

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
        You cannot call this operation to delete the default transcoding template. You can delete the transcoding template when it is no longer specified as the default one.
        *   For security purposes, you cannot add, modify, or delete transcoding templates in a transcoding template group that is locked. To check whether a transcoding template group is locked, call the [GetTranscodeTemplateGroup](~~GetTranscodeTemplateGroup~~) operation and obtain the Locked parameter from the response. To modify transcoding templates within a locked transcoding template group, you must call the [UpdateTranscodeTemplateGroup](~~UpdateTranscodeTemplateGroup~~) operation to unlock the transcoding template group first.
        

        @param request: DeleteTranscodeTemplateGroupRequest

        @return: DeleteTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transcode_template_group_with_options(request, runtime)

    def delete_video_with_options(self, request, runtime):
        """
        This operation physically deletes videos. Deleted videos cannot be recovered. Exercise caution when you call this operation.
        *   You can call this operation to delete multiple videos at a time.
        *   When you delete a video, its source file, transcoded stream file, and thumbnail screenshot are also deleted. However, the Alibaba Cloud Content Delivery Network (CDN) cache is not refreshed simultaneously. You can use the refresh feature in the ApsaraVideo VOD console to clear garbage data on CDN nodes. For more information, see [Refresh and prefetch](~~86098~~).
        

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
        This operation physically deletes videos. Deleted videos cannot be recovered. Exercise caution when you call this operation.
        *   You can call this operation to delete multiple videos at a time.
        *   When you delete a video, its source file, transcoded stream file, and thumbnail screenshot are also deleted. However, the Alibaba Cloud Content Delivery Network (CDN) cache is not refreshed simultaneously. You can use the refresh feature in the ApsaraVideo VOD console to clear garbage data on CDN nodes. For more information, see [Refresh and prefetch](~~86098~~).
        

        @param request: DeleteVideoRequest

        @return: DeleteVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    def delete_vod_domain_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        > *   After a domain name for CDN is removed from ApsaraVideo VOD, the domain name becomes unavailable. Proceed with caution. We recommend that you restore the A record at your DNS service provider before you remove the domain name for CDN.
        > *   After you call this operation to remove a domain name for CDN from ApsaraVideo VOD, all records that are related to the domain name are deleted. If you only want to disable a domain name for CDN, call the [BatchStopVodDomain](~~120208~~) operation.
        

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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   After a domain name for CDN is removed from ApsaraVideo VOD, the domain name becomes unavailable. Proceed with caution. We recommend that you restore the A record at your DNS service provider before you remove the domain name for CDN.
        > *   After you call this operation to remove a domain name for CDN from ApsaraVideo VOD, all records that are related to the domain name are deleted. If you only want to disable a domain name for CDN, call the [BatchStopVodDomain](~~120208~~) operation.
        

        @param request: DeleteVodDomainRequest

        @return: DeleteVodDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_domain_with_options(request, runtime)

    def delete_vod_specific_config_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        > *   After the configurations of a domain name for CDN are deleted, the domain name becomes unavailable. We recommend that you restore the A record at your DNS service provider before you delete the configurations of the domain name for CDN.
        > *   After you call this operation to delete the configurations of a domain name for CDN, all records that are related to the domain name are deleted. If you only want to disable a domain name for CDN, call the [BatchStopVodDomain](~~120208~~) operation.
        

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
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   After the configurations of a domain name for CDN are deleted, the domain name becomes unavailable. We recommend that you restore the A record at your DNS service provider before you delete the configurations of the domain name for CDN.
        > *   After you call this operation to delete the configurations of a domain name for CDN, all records that are related to the domain name are deleted. If you only want to disable a domain name for CDN, call the [BatchStopVodDomain](~~120208~~) operation.
        

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
        >    The default watermark cannot be deleted.
        > *   If you delete a watermark, its mezzanine file is also physically deleted and cannot be recovered.
        

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
        >    The default watermark cannot be deleted.
        > *   If you delete a watermark, its mezzanine file is also physically deleted and cannot be recovered.
        

        @param request: DeleteWatermarkRequest

        @return: DeleteWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    def describe_play_top_videos_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can query playback statistics on top 1,000 videos at most on a specified day. By default, top videos are sorted in descending order based on video views.
        > *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        > *   Playback statistics for the previous day are generated at 09:00 on the current day, in UTC+8.
        > *   You can query data that is generated since January 1, 2018. The maximum time range to query is 180 days.
        

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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can query playback statistics on top 1,000 videos at most on a specified day. By default, top videos are sorted in descending order based on video views.
        > *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        > *   Playback statistics for the previous day are generated at 09:00 on the current day, in UTC+8.
        > *   You can query data that is generated since January 1, 2018. The maximum time range to query is 180 days.
        

        @param request: DescribePlayTopVideosRequest

        @return: DescribePlayTopVideosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_top_videos_with_options(request, runtime)

    def describe_play_user_avg_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        > *   Playback statistics for the previous day are generated at 09:00 on the current day, in UTC+8.
        > *   You can query data that is generated since January 1, 2018. The maximum time range to query is 180 days.
        

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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        > *   Playback statistics for the previous day are generated at 09:00 on the current day, in UTC+8.
        > *   You can query data that is generated since January 1, 2018. The maximum time range to query is 180 days.
        

        @param request: DescribePlayUserAvgRequest

        @return: DescribePlayUserAvgResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_avg_with_options(request, runtime)

    def describe_play_user_total_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        *   Playback statistics for the current day are generated at 09:00 (UTC+8) on the next day.
        *   You can query data that is generated since January 1, 2018. The maximum time range to query is 180 days.
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        *   Playback statistics for the current day are generated at 09:00 (UTC+8) on the next day.
        *   You can query data that is generated since January 1, 2018. The maximum time range to query is 180 days.
        

        @param request: DescribePlayUserTotalRequest

        @return: DescribePlayUserTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_total_with_options(request, runtime)

    def describe_play_video_statis_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        *   Playback statistics for the current day are generated at 09:00 (UTC+8) on the next day.
        *   You can query only data in the last 730 days. The maximum time range to query is 180 days.
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   You can call this operation to query only playback statistics collected on videos that are played by using ApsaraVideo Player SDKs.
        *   Playback statistics for the current day are generated at 09:00 (UTC+8) on the next day.
        *   You can query only data in the last 730 days. The maximum time range to query is 180 days.
        

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
        > This operation is available only in the *China (Shanghai)** region.
        

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
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: DescribeVodCertificateListRequest

        @return: DescribeVodCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_certificate_list_with_options(request, runtime)

    def describe_vod_domain_bps_data_with_options(self, request, runtime):
        """
        If you specify neither the StartTime parameter nor the EndTime parameter, the data in the last 24 hours is queried. Alternatively, you can specify both the StartTime and EndTime parameters to query data that is generated in the specified duration. You can query data for the last 90 days at most.
        

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
        If you specify neither the StartTime parameter nor the EndTime parameter, the data in the last 24 hours is queried. Alternatively, you can specify both the StartTime and EndTime parameters to query data that is generated in the specified duration. You can query data for the last 90 days at most.
        

        @param request: DescribeVodDomainBpsDataRequest

        @return: DescribeVodDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_bps_data_with_options(request, runtime)

    def describe_vod_domain_certificate_info_with_options(self, request, runtime):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: DescribeVodDomainCertificateInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainCertificateInfoResponse
        """
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
        """
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: DescribeVodDomainCertificateInfoRequest

        @return: DescribeVodDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_certificate_info_with_options(request, runtime)

    def describe_vod_domain_configs_with_options(self, request, runtime):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

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
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: DescribeVodDomainConfigsRequest

        @return: DescribeVodDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_configs_with_options(request, runtime)

    def describe_vod_domain_detail_with_options(self, request, runtime):
        """
        > This operation is available only in the *China (Shanghai)** region.
        

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
        > This operation is available only in the *China (Shanghai)** region.
        

        @param request: DescribeVodDomainDetailRequest

        @return: DescribeVodDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_detail_with_options(request, runtime)

    def describe_vod_domain_log_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   For more information about the log format and latency, see [Download logs](~~86099~~).
        *   If you specify neither StartTime nor EndTime, the log data in the previous 24 hours is queried.
        *   You can specify both StartTime and EndTime to query the log data that is generated in the specified time range.
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations](~~342790~~).
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   For more information about the log format and latency, see [Download logs](~~86099~~).
        *   If you specify neither StartTime nor EndTime, the log data in the previous 24 hours is queried.
        *   You can specify both StartTime and EndTime to query the log data that is generated in the specified time range.
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations](~~342790~~).
        

        @param request: DescribeVodDomainLogRequest

        @return: DescribeVodDomainLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_log_with_options(request, runtime)

    def describe_vod_domain_src_bps_data_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        * ApsaraVideo VOD stores the origin bandwidth data for 90 days before the data is deleted.
        * If you do not set the `StartTime` or `EndTime` parameter, the request returns the data collected in the last 24 hours. If you set both the `StartTime` and `EndTime` parameters, the request returns the data collected within the specified time range.
        * You can specify a maximum of 500 domain names in a request. Separate multiple domain names with commas (,). If you specify multiple domain names in a request, aggregation results are returned.
        ### Time granularity
        The time granularity supported by the Interval parameter varies based on the time range per query specified by using `StartTime` and `EndTime`. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Time range per query (days)|Historical data available (days)|Data delay|
        |---|---|---|---|
        |5 minutes|(0, 3\\]|93|15 minutes|
        |1 hour|(3, 31\\]|186|4 hours|
        |1 day|(31, 366\\]|366|04:00 on the next day|
        

        @param request: DescribeVodDomainSrcBpsDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainSrcBpsDataResponse
        """
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
        """
        This operation is available only in the **China (Shanghai)** region.
        * ApsaraVideo VOD stores the origin bandwidth data for 90 days before the data is deleted.
        * If you do not set the `StartTime` or `EndTime` parameter, the request returns the data collected in the last 24 hours. If you set both the `StartTime` and `EndTime` parameters, the request returns the data collected within the specified time range.
        * You can specify a maximum of 500 domain names in a request. Separate multiple domain names with commas (,). If you specify multiple domain names in a request, aggregation results are returned.
        ### Time granularity
        The time granularity supported by the Interval parameter varies based on the time range per query specified by using `StartTime` and `EndTime`. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Time range per query (days)|Historical data available (days)|Data delay|
        |---|---|---|---|
        |5 minutes|(0, 3\\]|93|15 minutes|
        |1 hour|(3, 31\\]|186|4 hours|
        |1 day|(31, 366\\]|366|04:00 on the next day|
        

        @param request: DescribeVodDomainSrcBpsDataRequest

        @return: DescribeVodDomainSrcBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_src_bps_data_with_options(request, runtime)

    def describe_vod_domain_src_traffic_data_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        * ApsaraVideo VOD stores the origin traffic data for 90 days before the data is deleted.
        * If you do not set the `StartTime` or `EndTime` parameter, the request returns the data collected in the last 24 hours. If you set both the `StartTime` and `EndTime` parameters, the request returns the data collected within the specified time range.
        * You can specify a maximum of 500 domain names in a request. Separate multiple domain names with commas (,). If you specify multiple domain names in a request, aggregation results are returned.
        ### Time granularity
        The time granularity supported by the Interval parameter varies based on the time range per query specified by using `StartTime` and `EndTime`. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Time range per query (days)|Historical data available (days)|Data delay|
        |---|---|---|---|
        |5 minutes|(0, 3\\]|93|15 minutes|
        |1 hour|(3, 31\\]|186|4 hours|
        |1 day|(31, 366\\]|366|04:00 on the next day|
        

        @param request: DescribeVodDomainSrcTrafficDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVodDomainSrcTrafficDataResponse
        """
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
        """
        This operation is available only in the **China (Shanghai)** region.
        * ApsaraVideo VOD stores the origin traffic data for 90 days before the data is deleted.
        * If you do not set the `StartTime` or `EndTime` parameter, the request returns the data collected in the last 24 hours. If you set both the `StartTime` and `EndTime` parameters, the request returns the data collected within the specified time range.
        * You can specify a maximum of 500 domain names in a request. Separate multiple domain names with commas (,). If you specify multiple domain names in a request, aggregation results are returned.
        ### Time granularity
        The time granularity supported by the Interval parameter varies based on the time range per query specified by using `StartTime` and `EndTime`. The following table describes the time period within which historical data is available and the data delay.
        |Time granularity|Time range per query (days)|Historical data available (days)|Data delay|
        |---|---|---|---|
        |5 minutes|(0, 3\\]|93|15 minutes|
        |1 hour|(3, 31\\]|186|4 hours|
        |1 day|(31, 366\\]|366|04:00 on the next day|
        

        @param request: DescribeVodDomainSrcTrafficDataRequest

        @return: DescribeVodDomainSrcTrafficDataResponse
        """
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
        This operation is available only in the **China (Shanghai)** region.
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
        This operation is available only in the **China (Shanghai)** region.
        *   You can specify up to 100 accelerated domain names in a request. Separate multiple domain names with commas (,). If you do not specify an accelerated domain name, the data of all accelerated domain names within your Alibaba Cloud account is returned.
        *   You can query data in the last year. The maximum time range that can be queried is three months. If you specify a time range of one to three days, the system returns data on an hourly basis. If you specify a time range of four days or more, the system returns data on a daily basis.
        

        @param request: DescribeVodDomainUsageDataRequest

        @return: DescribeVodDomainUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_usage_data_with_options(request, runtime)

    def describe_vod_refresh_quota_with_options(self, request, runtime):
        """
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh content and the [PreloadVodObjectCaches](~~69211~~) operation to prefetch content.
        

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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh content and the [PreloadVodObjectCaches](~~69211~~) operation to prefetch content.
        

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
        You can grant a maximum of 10 application permissions to a RAM user or RAM role.
        

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
        You can grant a maximum of 10 application permissions to a RAM user or RAM role.
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   Call the [SubmitAIImageJob](~~SubmitAIImageJob~~) operation to submit image AI processing jobs before you call this operation to query image AI processing jobs.
        *   You can query a maximum of 10 jobs of image AI processing in one request.
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   Call the [SubmitAIImageJob](~~SubmitAIImageJob~~) operation to submit image AI processing jobs before you call this operation to query image AI processing jobs.
        *   You can query a maximum of 10 jobs of image AI processing in one request.
        

        @param request: GetAIImageJobsRequest

        @return: GetAIImageJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aiimage_jobs_with_options(request, runtime)

    def get_aimedia_audit_job_with_options(self, request, runtime):
        """
        ApsaraVideo VOD stores the snapshots of the intelligent review results free of charge for two weeks. After this period, the snapshots are automatically deleted.
        

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
        ApsaraVideo VOD stores the snapshots of the intelligent review results free of charge for two weeks. After this period, the snapshots are automatically deleted.
        

        @param request: GetAIMediaAuditJobRequest

        @return: GetAIMediaAuditJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aimedia_audit_job_with_options(request, runtime)

    def get_aitemplate_with_options(self, request, runtime):
        """
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   Before you call this operation to query details of an AI template, you must obtain the ID of the AI template.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   Before you call this operation to query details of an AI template, you must obtain the ID of the AI template.
        

        @param request: GetAITemplateRequest

        @return: GetAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aitemplate_with_options(request, runtime)

    def get_aivideo_tag_result_with_options(self, request, runtime):
        """
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can obtain the smart tagging results by using the video ID.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can obtain the smart tagging results by using the video ID.
        

        @param request: GetAIVideoTagResultRequest

        @return: GetAIVideoTagResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aivideo_tag_result_with_options(request, runtime)

    def get_app_infos_with_options(self, request, runtime):
        """
        Supports batch query.
        

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
        Supports batch query.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can query information only about the default AI template for automated review.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can query information only about the default AI template for automated review.
        

        @param request: GetDefaultAITemplateRequest

        @return: GetDefaultAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_default_aitemplate_with_options(request, runtime)

    def get_digital_watermark_extract_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extract_type):
            query['ExtractType'] = request.extract_type
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
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
            action='GetDigitalWatermarkExtractResult',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.GetDigitalWatermarkExtractResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_digital_watermark_extract_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_digital_watermark_extract_result_with_options(request, runtime)

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
        During editing, you can add materials to the timeline, but some of them may not be used.
        

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
        During editing, you can add materials to the timeline, but some of them may not be used.
        

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
        If notifications for the [CreateAuditComplete](~~89576~~) event are configured, event notifications are sent to the callback URL after automated review is complete. You can call this operation to query the details of audio review results.
        

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
        If notifications for the [CreateAuditComplete](~~89576~~) event are configured, event notifications are sent to the callback URL after automated review is complete. You can call this operation to query the details of audio review results.
        

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
        - By default, only details of snapshots that violate content regulations and potentially violate content regulations are returned.
        - ApsaraVideo VOD stores the snapshots in the automated review results free of charge for two weeks. After this period, the snapshots are automatically deleted.
        

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
        - By default, only details of snapshots that violate content regulations and potentially violate content regulations are returned.
        - ApsaraVideo VOD stores the snapshots in the automated review results free of charge for two weeks. After this period, the snapshots are automatically deleted.
        

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
        Regions that support this operation: *China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        

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
        Regions that support this operation: *China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        

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
        > For more information, see [Event notification](~~55627~~).
        

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
        > For more information, see [Event notification](~~55627~~).
        

        @param request: GetMessageCallbackRequest

        @return: GetMessageCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_message_callback_with_options(request, runtime)

    def get_mezzanine_info_with_options(self, request, runtime):
        """
        > You can obtain the complete mezzanine file information only after a stream is transcoded.
        

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
        > You can obtain the complete mezzanine file information only after a stream is transcoded.
        

        @param request: GetMezzanineInfoRequest

        @return: GetMezzanineInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mezzanine_info_with_options(request, runtime)

    def get_play_info_with_options(self, request, runtime):
        """
        You can use the ID of a media file to query the playback URL of the file. After you integrate ApsaraVideo Player SDK for URL-based playback or a third-party player, you can use the obtained playback URLs to play audio and video files.
        *   Only videos whose Status is Normal can be played. The Status parameter in the response indicates the status of the video. For more information, see [Overview](~~57290~~).
        *   If video playback fails, you can call the [GetMezzanineInfo](~~GetMezzanineInfo~~) operation to check whether the video source information is correct.
        

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
        if not UtilClient.is_unset(request.digital_watermark_type):
            query['DigitalWatermarkType'] = request.digital_watermark_type
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
        if not UtilClient.is_unset(request.trace):
            query['Trace'] = request.trace
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
        You can use the ID of a media file to query the playback URL of the file. After you integrate ApsaraVideo Player SDK for URL-based playback or a third-party player, you can use the obtained playback URLs to play audio and video files.
        *   Only videos whose Status is Normal can be played. The Status parameter in the response indicates the status of the video. For more information, see [Overview](~~57290~~).
        *   If video playback fails, you can call the [GetMezzanineInfo](~~GetMezzanineInfo~~) operation to check whether the video source information is correct.
        

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
        You can call this operation to query only transcoding tasks created within the past year.
        

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
        You can call this operation to query only transcoding tasks created within the past year.
        

        @param request: GetTranscodeTaskRequest

        @return: GetTranscodeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_task_with_options(request, runtime)

    def get_transcode_template_group_with_options(self, request, runtime):
        """
        This operation returns the information about the specified transcoding template group and the configurations of all the transcoding templates in the group.
        

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
        This operation returns the information about the specified transcoding template group and the configurations of all the transcoding templates in the group.
        

        @param request: GetTranscodeTemplateGroupRequest

        @return: GetTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_template_group_with_options(request, runtime)

    def get_urlupload_infos_with_options(self, request, runtime):
        """
        You can query the information about a URL-based upload job by specifying the upload URL or using the job ID returned when you upload media files. The information includes the status of the upload job, custom configurations, the time when the job was created, and the time when the job was complete.
        If the upload fails, you can view the error code and error message. If the upload is successful, you can obtain the video ID.
        

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
        You can query the information about a URL-based upload job by specifying the upload URL or using the job ID returned when you upload media files. The information includes the status of the upload job, custom configurations, the time when the job was created, and the time when the job was complete.
        If the upload fails, you can view the error code and error message. If the upload is successful, you can obtain the video ID.
        

        @param request: GetURLUploadInfosRequest

        @return: GetURLUploadInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_urlupload_infos_with_options(request, runtime)

    def get_upload_details_with_options(self, request, runtime):
        """
        You can call this operation to obtain the upload details only about audio and video files.
        *   If you use the ApsaraVideo VOD console to upload audio and video files, you can call this operation to query information such as the upload ratio. If you use an upload SDK to upload audio and video files, make sure that the version of the [upload SDK](~~52200~~) meets one of the following requirements:
        *   The version of the upload SDK for Java is 1.4.4 or later.
        *   The version of the upload SDK for C++ is 1.0.0 or later.
        *   The version of the upload SDK for PHP is 1.0.2 or later.
        *   The version of the upload SDK for Python is 1.3.0 or later.
        *   The version of the upload SDK for JavaScript is 1.4.0 or later.
        *   The version of the upload SDK for Android is 1.5.0 or later.
        *   The version of the upload SDK for iOS is 1.5.0 or later.
        

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
        You can call this operation to obtain the upload details only about audio and video files.
        *   If you use the ApsaraVideo VOD console to upload audio and video files, you can call this operation to query information such as the upload ratio. If you use an upload SDK to upload audio and video files, make sure that the version of the [upload SDK](~~52200~~) meets one of the following requirements:
        *   The version of the upload SDK for Java is 1.4.4 or later.
        *   The version of the upload SDK for C++ is 1.0.0 or later.
        *   The version of the upload SDK for PHP is 1.0.2 or later.
        *   The version of the upload SDK for Python is 1.3.0 or later.
        *   The version of the upload SDK for JavaScript is 1.4.0 or later.
        *   The version of the upload SDK for Android is 1.5.0 or later.
        *   The version of the upload SDK for iOS is 1.5.0 or later.
        

        @param request: GetUploadDetailsRequest

        @return: GetUploadDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_details_with_options(request, runtime)

    def get_video_info_with_options(self, request, runtime):
        """
        The video snapshot URLs.
        > This operation returns only data about the snapshots that are captured when you upload a video. The snapshot data includes data of the thumbnail and snapshot data that is generated based on the workflow setting. To query the snapshot data that is generated after the video is uploaded, call the [ListSnapshots](~~ListSnapshots~~) operation. For more information, see [Video snapshots](~~99368~~).
        

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
        > This operation returns only data about the snapshots that are captured when you upload a video. The snapshot data includes data of the thumbnail and snapshot data that is generated based on the workflow setting. To query the snapshot data that is generated after the video is uploaded, call the [ListSnapshots](~~ListSnapshots~~) operation. For more information, see [Video snapshots](~~99368~~).
        

        @param request: GetVideoInfoRequest

        @return: GetVideoInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_info_with_options(request, runtime)

    def get_video_infos_with_options(self, request, runtime):
        """
        You can call this operation to obtain the basic information about multiple videos at a time based on video IDs. The basic information includes the title, description, duration, thumbnail URL, status, creation time, size, snapshots, category, and tags of each video.
        

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
        You can call this operation to obtain the basic information about multiple videos at a time based on video IDs. The basic information includes the title, description, duration, thumbnail URL, status, creation time, size, snapshots, category, and tags of each video.
        

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
        ###
        *   You can call this operation to obtain a playback credential when you use ApsaraVideo Player SDK to play a media file based on PlayAuth. The credential is used to obtain the playback URL.
        *   You cannot obtain the playback URL of a video by using a credential that has expired. A new credential is required.
        ### QPS limit
        You can call this operation up to 360 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on API operations](~~342790~~).
        

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
        ###
        *   You can call this operation to obtain a playback credential when you use ApsaraVideo Player SDK to play a media file based on PlayAuth. The credential is used to obtain the playback URL.
        *   You cannot obtain the playback URL of a video by using a credential that has expired. A new credential is required.
        ### QPS limit
        You can call this operation up to 360 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on API operations](~~342790~~).
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   You can call this operation to query AI processing results about images of a specified video. Images of different videos cannot be queried in one request.
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   You can call this operation to query AI processing results about images of a specified video. Images of different videos cannot be queried in one request.
        

        @param request: ListAIImageInfoRequest

        @return: ListAIImageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aiimage_info_with_options(request, runtime)

    def list_aijob_with_options(self, request, runtime):
        """
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can call this operation to query video fingerprinting jobs and smart tagging jobs.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can call this operation to query video fingerprinting jobs and smart tagging jobs.
        

        @param request: ListAIJobRequest

        @return: ListAIJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aijob_with_options(request, runtime)

    def list_aitemplate_with_options(self, request, runtime):
        """
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can call this operation to query AI templates of a specified type.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   You can call this operation to query AI templates of a specified type.
        

        @param request: ListAITemplateRequest

        @return: ListAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_aitemplate_with_options(request, runtime)

    def list_app_info_with_options(self, request, runtime):
        """
        Supports filtering queries by application status.
        

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
        Supports filtering queries by application status.
        

        @param request: ListAppInfoRequest

        @return: ListAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_info_with_options(request, runtime)

    def list_app_policies_for_identity_with_options(self, request, runtime):
        """
        > The IdentityType and IdentityName parameters take effect only when an identity assumes the application administrator role to call this operation. Otherwise, only application policies that are attached to the current identity are returned.
        

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
        > The IdentityType and IdentityName parameters take effect only when an identity assumes the application administrator role to call this operation. Otherwise, only application policies that are attached to the current identity are returned.
        

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
        You can query a maximum of 5,000 videos based on the specified filter condition.
        

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
        You can query a maximum of 5,000 videos based on the specified filter condition.
        

        @param request: ListLiveRecordVideoRequest

        @return: ListLiveRecordVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_video_with_options(request, runtime)

    def list_snapshots_with_options(self, request, runtime):
        """
        If multiple snapshots of a video exist, the data of the latest snapshot is returned.
        

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
        If multiple snapshots of a video exist, the data of the latest snapshot is returned.
        

        @param request: ListSnapshotsRequest

        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    def list_transcode_task_with_options(self, request, runtime):
        """
        You can call the [GetTranscodeTask](~~109121~~) operation to query details about transcoding jobs.
        *   **You can call this operation to query only transcoding tasks created within the past year.**\
        

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
        You can call the [GetTranscodeTask](~~109121~~) operation to query details about transcoding jobs.
        *   **You can call this operation to query only transcoding tasks created within the past year.**\
        

        @param request: ListTranscodeTaskRequest

        @return: ListTranscodeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_task_with_options(request, runtime)

    def list_transcode_template_group_with_options(self, request, runtime):
        """
        > This operation does not return the configurations of transcoding templates in each transcoding template group. To query the configurations of transcoding templates in a specific transcoding template group, call the [GetTranscodeTemplateGroup](~~102670~~) operation.
        

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
        > This operation does not return the configurations of transcoding templates in each transcoding template group. To query the configurations of transcoding templates in a specific transcoding template group, call the [GetTranscodeTemplateGroup](~~102670~~) operation.
        

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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can submit a maximum of 500 requests to prefetch resources based on URLs each day by using an Alibaba Cloud account. You cannot prefetch resources based on directories.
        > *   You can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh content and the [PreloadVodObjectCaches](~~69211~~l) operation to prefetch content.
        

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
        >    This operation is available only in the **China (Shanghai)** region.
        > *   You can submit a maximum of 500 requests to prefetch resources based on URLs each day by using an Alibaba Cloud account. You cannot prefetch resources based on directories.
        > *   You can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh content and the [PreloadVodObjectCaches](~~69211~~l) operation to prefetch content.
        

        @param request: PreloadVodObjectCachesRequest

        @return: PreloadVodObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preload_vod_object_caches_with_options(request, runtime)

    def produce_editing_project_video_with_options(self, request, runtime):
        """
        This operation returns only the submission result of a video production task. When the submission result is returned, video production may still be in progress. After a video production task is submitted, the task is queued in the background for asynchronous processing.
        *   The source files that are used in the timeline of an online editing project can be materials directly uploaded to the online project or selected from the media asset library.
        *   Videos are produced based on ProjectId and Timeline. The following rules apply when you specify the parameters:
        *   You must specify at least one of the ProjectId and Timeline parameters. Otherwise, video production fails.
        *   If you specify only the Timeline parameter, the system automatically creates an online editing project based on the specified timeline. Then, the system uses the source files specified in the timeline to produce videos.
        *   If you specify only the ProjectId parameter, the system obtains the latest timeline data of the specified project to produce videos.
        *   If you specify both the ProjectId and Timeline parameters, the system produces videos based on the specified timeline and updates the timeline data for the specified online editing project. You can also specify other parameters to update the corresponding information about the online editing project.
        *   After a video is produced, the video is automatically uploaded to ApsaraVideo VOD. Then, the **ProduceMediaComplete** and **FileUploadComplete** event notifications are sent to you. After the produced video is transcoded, the **StreamTranscodeComplete** and **TranscodeComplete** event notifications are sent to you.
        *   You can add special effects to the video. For more information, see [Special effects](~~69082~~).
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

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
        This operation returns only the submission result of a video production task. When the submission result is returned, video production may still be in progress. After a video production task is submitted, the task is queued in the background for asynchronous processing.
        *   The source files that are used in the timeline of an online editing project can be materials directly uploaded to the online project or selected from the media asset library.
        *   Videos are produced based on ProjectId and Timeline. The following rules apply when you specify the parameters:
        *   You must specify at least one of the ProjectId and Timeline parameters. Otherwise, video production fails.
        *   If you specify only the Timeline parameter, the system automatically creates an online editing project based on the specified timeline. Then, the system uses the source files specified in the timeline to produce videos.
        *   If you specify only the ProjectId parameter, the system obtains the latest timeline data of the specified project to produce videos.
        *   If you specify both the ProjectId and Timeline parameters, the system produces videos based on the specified timeline and updates the timeline data for the specified online editing project. You can also specify other parameters to update the corresponding information about the online editing project.
        *   After a video is produced, the video is automatically uploaded to ApsaraVideo VOD. Then, the **ProduceMediaComplete** and **FileUploadComplete** event notifications are sent to you. After the produced video is transcoded, the **StreamTranscodeComplete** and **TranscodeComplete** event notifications are sent to you.
        *   You can add special effects to the video. For more information, see [Special effects](~~69082~~).
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VOD](~~342790~~).
        

        @param request: ProduceEditingProjectVideoRequest

        @return: ProduceEditingProjectVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.produce_editing_project_video_with_options(request, runtime)

    def refresh_media_play_urls_with_options(self, request, runtime):
        """
        - ApsaraVideo VOD allows you to refresh and prefetch resources. The refresh feature forces the point of presence (POP) to clear cached resources and retrieve the latest resources from origin servers. The prefetch feature allows the POP to retrieve frequently accessed resources from origin servers during off-peak hours. This increases the cache hit ratio.
        - You can call this operation to submit refresh or prefetch tasks based on the media ID. You can also specify the format and resolution of the media streams to refresh or prefetch based on your business requirements.
        - You can submit a maximum of 20 refresh or prefetch tasks at a time.
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

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
        - ApsaraVideo VOD allows you to refresh and prefetch resources. The refresh feature forces the point of presence (POP) to clear cached resources and retrieve the latest resources from origin servers. The prefetch feature allows the POP to retrieve frequently accessed resources from origin servers during off-peak hours. This increases the cache hit ratio.
        - You can call this operation to submit refresh or prefetch tasks based on the media ID. You can also specify the format and resolution of the media streams to refresh or prefetch based on your business requirements.
        - You can submit a maximum of 20 refresh or prefetch tasks at a time.
        ### QPS limits
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits on API operations in ApsaraVideo VoD](~~342790~~).
        

        @param request: RefreshMediaPlayUrlsRequest

        @return: RefreshMediaPlayUrlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_media_play_urls_with_options(request, runtime)

    def refresh_upload_video_with_options(self, request, runtime):
        """
        If you want to overwrite a video or audio source file, you can obtain the upload URL of the source file by calling this operation. Then, you can upload a new source file without changing the video or audio ID. However, the file overwriting may automatically trigger transcoding and snapshot jobs if these jobs are configured. For more information, see [Upload URLs and credentials](~~55397~~).
        

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
        If you want to overwrite a video or audio source file, you can obtain the upload URL of the source file by calling this operation. Then, you can upload a new source file without changing the video or audio ID. However, the file overwriting may automatically trigger transcoding and snapshot jobs if these jobs are configured. For more information, see [Upload URLs and credentials](~~55397~~).
        

        @param request: RefreshUploadVideoRequest

        @return: RefreshUploadVideoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_video_with_options(request, runtime)

    def refresh_vod_object_caches_with_options(self, request, runtime):
        """
        This operation is available only in the **China (Shanghai)** region.
        *   You can submit a maximum of 2,000 requests to refresh resources based on URLs and 100 requests to refresh resources based on directories each day by using an Alibaba Cloud account.
        *   You can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh content and the [PreloadVodObjectCaches](~~69211~~) operation to prefetch content.
        

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
        This operation is available only in the **China (Shanghai)** region.
        *   You can submit a maximum of 2,000 requests to refresh resources based on URLs and 100 requests to refresh resources based on directories each day by using an Alibaba Cloud account.
        *   You can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh content and the [PreloadVodObjectCaches](~~69211~~) operation to prefetch content.
        

        @param request: RefreshVodObjectCachesRequest

        @return: RefreshVodObjectCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_vod_object_caches_with_options(request, runtime)

    def register_media_with_options(self, request, runtime):
        """
        After you store an audio or video file in an Object Storage Service (OSS) bucket that is used for ApsaraVideo VOD, you can call the RegisterMedia operation to register the media file. After the media file is registered, you can use the media ID associated with the media file to submit transcoding jobs and snapshot jobs in ApsaraVideo VOD. For more information, see [SubmitTranscodeJobs](~~68570~~) and [SubmitSnapshotJob](~~72213~~).
        > *   You can register up to 10 OSS media files that have the same storage location at a time.
        > *   If you use the ApsaraVideo VOD console to upload a media file and do not specify a transcoding template group ID, ApsaraVideo VOD uses the default transcoding template group to transcode the media file. However, if you do not specify a transcoding template group ID when you call the RegisterMedia operation, ApsaraVideo VOD does not automatically transcode the media file after the media file is registered. If you specify a transcoding template group ID, ApsaraVideo VOD uses the specified transcoding template group to transcode the media file.
        > *   If the media file that you want to register is registered before, this operation returns only the unique media ID that is associated with the media file. No further processing is performed.
        

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
        After you store an audio or video file in an Object Storage Service (OSS) bucket that is used for ApsaraVideo VOD, you can call the RegisterMedia operation to register the media file. After the media file is registered, you can use the media ID associated with the media file to submit transcoding jobs and snapshot jobs in ApsaraVideo VOD. For more information, see [SubmitTranscodeJobs](~~68570~~) and [SubmitSnapshotJob](~~72213~~).
        > *   You can register up to 10 OSS media files that have the same storage location at a time.
        > *   If you use the ApsaraVideo VOD console to upload a media file and do not specify a transcoding template group ID, ApsaraVideo VOD uses the default transcoding template group to transcode the media file. However, if you do not specify a transcoding template group ID when you call the RegisterMedia operation, ApsaraVideo VOD does not automatically transcode the media file after the media file is registered. If you specify a transcoding template group ID, ApsaraVideo VOD uses the specified transcoding template group to transcode the media file.
        > *   If the media file that you want to register is registered before, this operation returns only the unique media ID that is associated with the media file. No further processing is performed.
        

        @param request: RegisterMediaRequest

        @return: RegisterMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_media_with_options(request, runtime)

    def restore_media_with_options(self, request, runtime):
        """
        You can call this operation to restore only Archive and Cold Archive audio and video files. You can access the audio and video files after the files are restored. You cannot change the storage class of an audio or video file that is being restored. You are charged for the retrieval traffic generated during restoration. After a Cold Archive audio or video file is restored, a Standard replica of the file is generated for access. You are charged for the storage of the replica before the file returns to the frozen state.
        

        @param request: RestoreMediaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestoreMediaResponse
        """
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
        """
        You can call this operation to restore only Archive and Cold Archive audio and video files. You can access the audio and video files after the files are restored. You cannot change the storage class of an audio or video file that is being restored. You are charged for the retrieval traffic generated during restoration. After a Cold Archive audio or video file is restored, a Standard replica of the file is generated for access. You are charged for the storage of the replica before the file returns to the frozen state.
        

        @param request: RestoreMediaRequest

        @return: RestoreMediaResponse
        """
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
        The maximum number of data records that you can query is limited based on the method used to query the data. You can use the following methods to query data:
        *   Method 1: You must use the PageNo and PageSize parameters for the first 5,000 data records that meet the specified filter criteria. This allows you to traverse data page by page. If the number of data records that meet the specified filter criteria exceeds 5,000, use Method 2.
        *   Method 2: This method applies only to the data of video and audio files. To traverse all the data records that meet the specified filter criteria, you must set the PageNo, PageSize, and ScrollToken parameters to traverse data page by page. The total number of data records from the current page to the desired page cannot exceed 1,200. Assume that the PageSize parameter is set to **20**:
        *   When the PageNo parameter is set to **1**, you can scroll forward to traverse data records from page 1 to page **60** at most.
        *   When the PageNo parameter is set to **2**, you can scroll forward to traverse data records from page 2 to page **61** at most.
        *   When the PageNo parameter is set to **61**, you can scroll backward to traverse data records from page 61 to page **2** at most or scroll forward to traverse data records from page 61 to page **120** at most.
        

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
        The maximum number of data records that you can query is limited based on the method used to query the data. You can use the following methods to query data:
        *   Method 1: You must use the PageNo and PageSize parameters for the first 5,000 data records that meet the specified filter criteria. This allows you to traverse data page by page. If the number of data records that meet the specified filter criteria exceeds 5,000, use Method 2.
        *   Method 2: This method applies only to the data of video and audio files. To traverse all the data records that meet the specified filter criteria, you must set the PageNo, PageSize, and ScrollToken parameters to traverse data page by page. The total number of data records from the current page to the desired page cannot exceed 1,200. Assume that the PageSize parameter is set to **20**:
        *   When the PageNo parameter is set to **1**, you can scroll forward to traverse data records from page 1 to page **60** at most.
        *   When the PageNo parameter is set to **2**, you can scroll forward to traverse data records from page 2 to page **61** at most.
        *   When the PageNo parameter is set to **61**, you can scroll backward to traverse data records from page 61 to page **2** at most or scroll forward to traverse data records from page 61 to page **120** at most.
        

        @param request: SearchMediaRequest

        @return: SearchMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    def set_audit_security_ip_with_options(self, request, runtime):
        """
        > You can play videos in the Checking or Blocked state only from the IP addresses that are added to review security groups.
        

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
        > You can play videos in the Checking or Blocked state only from the IP addresses that are added to review security groups.
        

        @param request: SetAuditSecurityIpRequest

        @return: SetAuditSecurityIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_audit_security_ip_with_options(request, runtime)

    def set_crossdomain_content_with_options(self, request, runtime):
        """
        > After you use the cross-domain policy file to update the resources on the origin server, you must refresh the resources that are cached on Alibaba Cloud CDN nodes. You can use the ApsaraVideo VOD console to refresh resources. For more information, see [Refresh and prefetch](~~86098~~). Alternatively, you can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh resources.
        

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
        > After you use the cross-domain policy file to update the resources on the origin server, you must refresh the resources that are cached on Alibaba Cloud CDN nodes. You can use the ApsaraVideo VOD console to refresh resources. For more information, see [Refresh and prefetch](~~86098~~). Alternatively, you can call the [RefreshVodObjectCaches](~~69215~~) operation to refresh resources.
        

        @param request: SetCrossdomainContentRequest

        @return: SetCrossdomainContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_crossdomain_content_with_options(request, runtime)

    def set_default_aitemplate_with_options(self, request, runtime):
        """
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   Before you can call this operation to specify an AI template as the default template, you must obtain the ID of the AI template. You cannot delete an AI template that is set as the default template.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   Before you can call this operation to specify an AI template as the default template, you must obtain the ID of the AI template. You cannot delete an AI template that is set as the default template.
        

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
        ## Usage note
        ApsaraVideo VOD supports the HTTP and MNS callback methods. For more information, see [Event notification](~~55627~~).
        

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
        ## Usage note
        ApsaraVideo VOD supports the HTTP and MNS callback methods. For more information, see [Event notification](~~55627~~).
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   After you call this operation, you can call the [GetAIImageJobs](~~186923~~) operation to query the job execution result.
        

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
        Regions that support this operation: **China (Beijing)** and **China (Shanghai)**.
        *   After you call this operation, you can call the [GetAIImageJobs](~~186923~~) operation to query the job execution result.
        

        @param request: SubmitAIImageJobRequest

        @return: SubmitAIImageJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_job_with_options(request, runtime)

    def submit_aijob_with_options(self, request, runtime):
        """
        Regions that support the video fingerprinting feature: **China (Beijing)**, **China (Shanghai)**, and **Singapore**. Regions that support the smart tagging feature: **China (Beijing)** and **China (Shanghai)**.
        *   You need to enable the video fingerprinting feature or the smart tagging feature before you can call this operation to submit jobs. For more information, see [Video AI](~~101148~~).
        *   If this is the first time you use the video fingerprinting feature, you must [submit a ticket](https://yida.alibaba-inc.com/o/ticketapply) to apply for using the media fingerprint library for free. Otherwise, the video fingerprinting feature will be affected.
        *   After you submit an AI job, ApsaraVideo VOD asynchronously processes the job. The operation may return a response before the job is complete. You can configure the [Event Notification](~~55627~~) feature and set the callback event to **AI Processing Completed**. After you receive the event notification, you can query the execution result of the AI job.
        

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
        Regions that support the video fingerprinting feature: **China (Beijing)**, **China (Shanghai)**, and **Singapore**. Regions that support the smart tagging feature: **China (Beijing)** and **China (Shanghai)**.
        *   You need to enable the video fingerprinting feature or the smart tagging feature before you can call this operation to submit jobs. For more information, see [Video AI](~~101148~~).
        *   If this is the first time you use the video fingerprinting feature, you must [submit a ticket](https://yida.alibaba-inc.com/o/ticketapply) to apply for using the media fingerprint library for free. Otherwise, the video fingerprinting feature will be affected.
        *   After you submit an AI job, ApsaraVideo VOD asynchronously processes the job. The operation may return a response before the job is complete. You can configure the [Event Notification](~~55627~~) feature and set the callback event to **AI Processing Completed**. After you receive the event notification, you can query the execution result of the AI job.
        

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

    def submit_digital_watermark_extract_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extract_type):
            query['ExtractType'] = request.extract_type
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
            action='SubmitDigitalWatermarkExtractJob',
            version='2017-03-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vod_20170321_models.SubmitDigitalWatermarkExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_digital_watermark_extract_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_digital_watermark_extract_job_with_options(request, runtime)

    def submit_dynamic_image_job_with_options(self, request, runtime):
        """
        You can capture a part of a video and generate animated images only when the video is in the **Uploaded**, **Transcoding**, **Normal**, **Reviewing**, or **Flagged** state.
        *   The fees for frame animation are included in your video transcoding bill. You are charged based on the output resolution and the duration. For more information, see [Billing of basic services](~~188308~~).
        ### QPS limits
        You can call this operation up to 30 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on API operations](~~342790~~).
        

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
        You can capture a part of a video and generate animated images only when the video is in the **Uploaded**, **Transcoding**, **Normal**, **Reviewing**, or **Flagged** state.
        *   The fees for frame animation are included in your video transcoding bill. You are charged based on the output resolution and the duration. For more information, see [Billing of basic services](~~188308~~).
        ### QPS limits
        You can call this operation up to 30 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit on API operations](~~342790~~).
        

        @param request: SubmitDynamicImageJobRequest

        @return: SubmitDynamicImageJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    def submit_media_dnadelete_job_with_options(self, request, runtime):
        """
        Regions that support this operation: *China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        

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
        Regions that support this operation: *China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        

        @param request: SubmitMediaDNADeleteJobRequest

        @return: SubmitMediaDNADeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_media_dnadelete_job_with_options(request, runtime)

    def submit_preprocess_jobs_with_options(self, request, runtime):
        """
        During video preprocessing, videos are transcoded to meet the playback requirements of the production studio. Therefore, you are **charged** for video preprocessing. You can submit a ticket for information about the **production studio** service.
        *   You can obtain the preprocessing result in the [TranscodeComplete](~~55638~~) event notification. If the value of the **Preprocess** parameter is true in the event notification, the video is preprocessed.
        

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
        During video preprocessing, videos are transcoded to meet the playback requirements of the production studio. Therefore, you are **charged** for video preprocessing. You can submit a ticket for information about the **production studio** service.
        *   You can obtain the preprocessing result in the [TranscodeComplete](~~55638~~) event notification. If the value of the **Preprocess** parameter is true in the event notification, the video is preprocessed.
        

        @param request: SubmitPreprocessJobsRequest

        @return: SubmitPreprocessJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_preprocess_jobs_with_options(request, runtime)

    def submit_snapshot_job_with_options(self, request, runtime):
        """
        >    Only snapshots in the JPG format are generated.
        > *   After a snapshot job is complete, ApsaraVideo VOD sends a [SnapshotComplete](~~57337~~) event notification that contains EventType=SnapshotComplete and SubType=SpecifiedTime.
        

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
        >    Only snapshots in the JPG format are generated.
        > *   After a snapshot job is complete, ApsaraVideo VOD sends a [SnapshotComplete](~~57337~~) event notification that contains EventType=SnapshotComplete and SubType=SpecifiedTime.
        

        @param request: SubmitSnapshotJobRequest

        @return: SubmitSnapshotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    def submit_transcode_jobs_with_options(self, request, runtime):
        """
        You can transcode a video only in the UploadSucc, Normal, or Checking state.
        *   You can obtain the transcoding result in the [StreamTranscodeComplete](~~55636~~) or [TranscodeComplete](~~55638~~) event notification.
        *   If you initiate an HTTP Live Streaming (HLS) packaging task, you can call this operation to dynamically override the subtitle. If the packaging task does not contain subtitles, we recommend that you do not call this operation to initiate the packaging task. Instead, you can specify the ID of the specific template group when you upload the video. The packaging process is automatically initiated.
        

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
        You can transcode a video only in the UploadSucc, Normal, or Checking state.
        *   You can obtain the transcoding result in the [StreamTranscodeComplete](~~55636~~) or [TranscodeComplete](~~55638~~) event notification.
        *   If you initiate an HTTP Live Streaming (HLS) packaging task, you can call this operation to dynamically override the subtitle. If the packaging task does not contain subtitles, we recommend that you do not call this operation to initiate the packaging task. Instead, you can specify the ID of the specific template group when you upload the video. The packaging process is automatically initiated.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   After you call the [AddAITemplate](~~102930~~) operation to add an AI template, you can call this operation to modify the AI template.
        

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
        Regions that support this operation: **China (Beijing)**, **China (Shanghai)**, and **Singapore**.
        *   After you call the [AddAITemplate](~~102930~~) operation to add an AI template, you can call this operation to modify the AI template.
        

        @param request: UpdateAITemplateRequest

        @return: UpdateAITemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_aitemplate_with_options(request, runtime)

    def update_app_info_with_options(self, request, runtime):
        """
        ## QPS limit
        A single user can perform a maximum of 30 queries per second (QPS). Throttling is triggered when the number of calls per second exceeds the QPS limit. The throttling may affect your business. Thus, we recommend that you observe the QPS limit on this operation.
        

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
        ## QPS limit
        A single user can perform a maximum of 30 queries per second (QPS). Throttling is triggered when the number of calls per second exceeds the QPS limit. The throttling may affect your business. Thus, we recommend that you observe the QPS limit on this operation.
        

        @param request: UpdateAppInfoRequest

        @return: UpdateAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_app_info_with_options(request, runtime)

    def update_attached_media_infos_with_options(self, request, runtime):
        """
        The specific parameter of an auxiliary media asset is updated only when a new value is passed in the parameter.
        

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
        The specific parameter of an auxiliary media asset is updated only when a new value is passed in the parameter.
        

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
        """
        UpdateMediaStorageClass is an asynchronous operation. You can call this operation to modify the storage classes of media assets. After the storage class is modified, a callback notification is sent.
        If the storage class of a media asset is Archive or Cold Archive, the media asset is automatically restored when you call this operation. After the media asset is restored, the storage class is modified. To restore the media asset, you do not need to call the RestoreMedia operation. To modify the storage class of a Cold Archive media asset, you must specify the restoration priority. By default, the restoration priority is set to Standard.
        Media assets whose storage classes are being modified cannot be used or processed.
        The media assets that are not of the Standard storage class have a limit on storage duration. If the storage duration does not meet the following requirements, you cannot change the storage classes: Infrequent Access (IA) media assets or source files are stored for at least 30 days, Archive media assets or source files are stored for at least 60 days, and Cold Archive media assets or source files are stored for at least 180 days.
        

        @param request: UpdateMediaStorageClassRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateMediaStorageClassResponse
        """
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
        """
        UpdateMediaStorageClass is an asynchronous operation. You can call this operation to modify the storage classes of media assets. After the storage class is modified, a callback notification is sent.
        If the storage class of a media asset is Archive or Cold Archive, the media asset is automatically restored when you call this operation. After the media asset is restored, the storage class is modified. To restore the media asset, you do not need to call the RestoreMedia operation. To modify the storage class of a Cold Archive media asset, you must specify the restoration priority. By default, the restoration priority is set to Standard.
        Media assets whose storage classes are being modified cannot be used or processed.
        The media assets that are not of the Standard storage class have a limit on storage duration. If the storage duration does not meet the following requirements, you cannot change the storage classes: Infrequent Access (IA) media assets or source files are stored for at least 30 days, Archive media assets or source files are stored for at least 60 days, and Cold Archive media assets or source files are stored for at least 180 days.
        

        @param request: UpdateMediaStorageClassRequest

        @return: UpdateMediaStorageClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_storage_class_with_options(request, runtime)

    def update_transcode_template_group_with_options(self, request, runtime):
        """
        >    You cannot add, modify, or remove transcoding templates in a transcoding template group that is locked in the ApsaraVideo VOD console. To manage such transcoding template groups, contact the ApsaraVideo VOD technical support.
        > *   You can call the GetTranscodeTemplateGroup operation to query the configurations of a transcoding template group and check whether the transcoding template group is locked by using the response parameter Locked.
        

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
        >    You cannot add, modify, or remove transcoding templates in a transcoding template group that is locked in the ApsaraVideo VOD console. To manage such transcoding template groups, contact the ApsaraVideo VOD technical support.
        > *   You can call the GetTranscodeTemplateGroup operation to query the configurations of a transcoding template group and check whether the transcoding template group is locked by using the response parameter Locked.
        

        @param request: UpdateTranscodeTemplateGroupRequest

        @return: UpdateTranscodeTemplateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_transcode_template_group_with_options(request, runtime)

    def update_video_info_with_options(self, request, runtime):
        """
        The specific parameter of a video is updated only when a new value is passed in the parameter.
        

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
        The specific parameter of a video is updated only when a new value is passed in the parameter.
        

        @param request: UpdateVideoInfoRequest

        @return: UpdateVideoInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_video_info_with_options(request, runtime)

    def update_video_infos_with_options(self, request, runtime):
        """
        The specific parameter of a video is updated only when a new value is passed in the parameter.
        

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
        The specific parameter of a video is updated only when a new value is passed in the parameter.
        

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
        You can modify only the name and configurations of a watermark.
        

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
        You can modify only the name and configurations of a watermark.
        

        @param request: UpdateWatermarkRequest

        @return: UpdateWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    def upload_media_by_urlwith_options(self, request, runtime):
        """
        You can call this operation to upload media files that are not stored on a local server or device and must be uploaded based on URLs over the Internet.
        *   The URL-based upload jobs are asynchronous. After you submit a URL-based upload job by calling this operation, it may take hours, even days to complete. If you require high timeliness, we recommend that you use the upload SDK.
        *   If you configure callbacks, you can receive an [UploadByURLComplete](~~86326~~) event notification after the media file is uploaded. You can query the upload status by calling the [GetURLUploadInfos](~~106830~~) operation.
        *   After you submit an upload job, the job is asynchronously processed on the cloud. All URL-based upload jobs that are submitted in each region are queued. The waiting time for the upload job depends on the number of queued jobs. After the upload job is complete, you can associate the playback URL included in the callback with the media ID.
        *   You can call this operation only in the **China (Shanghai)** and **Singapore** regions.
        *   Every time you submit a URL-based upload job, a new media ID is generated in ApsaraVideo VOD.
        

        @param request: UploadMediaByURLRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadMediaByURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
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
        You can call this operation to upload media files that are not stored on a local server or device and must be uploaded based on URLs over the Internet.
        *   The URL-based upload jobs are asynchronous. After you submit a URL-based upload job by calling this operation, it may take hours, even days to complete. If you require high timeliness, we recommend that you use the upload SDK.
        *   If you configure callbacks, you can receive an [UploadByURLComplete](~~86326~~) event notification after the media file is uploaded. You can query the upload status by calling the [GetURLUploadInfos](~~106830~~) operation.
        *   After you submit an upload job, the job is asynchronously processed on the cloud. All URL-based upload jobs that are submitted in each region are queued. The waiting time for the upload job depends on the number of queued jobs. After the upload job is complete, you can associate the playback URL included in the callback with the media ID.
        *   You can call this operation only in the **China (Shanghai)** and **Singapore** regions.
        *   Every time you submit a URL-based upload job, a new media ID is generated in ApsaraVideo VOD.
        

        @param request: UploadMediaByURLRequest

        @return: UploadMediaByURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    def upload_stream_by_urlwith_options(self, request, runtime):
        """
        You can call this operation to upload transcoded streams to ApsaraVideo VOD from external storage. The following HDR types of transcoded streams are supported: HDR, HDR 10, HLG, Dolby Vision, HDR Vivid, and SDR+. You can call the [GetURLUploadInfos](~~106830~~) operation to query the upload status. After the upload is complete, the callback of the UploadByURLComplete event is returned.
        >  This operation is available only in the Singapore (Singapore) region.
        

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
        You can call this operation to upload transcoded streams to ApsaraVideo VOD from external storage. The following HDR types of transcoded streams are supported: HDR, HDR 10, HLG, Dolby Vision, HDR Vivid, and SDR+. You can call the [GetURLUploadInfos](~~106830~~) operation to query the upload status. After the upload is complete, the callback of the UploadByURLComplete event is returned.
        >  This operation is available only in the Singapore (Singapore) region.
        

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
