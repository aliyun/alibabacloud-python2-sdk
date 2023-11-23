# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ice20201109 import models as ice20201109_models
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
            'ap-northeast-1': 'ice.aliyuncs.com',
            'ap-northeast-2-pop': 'ice.aliyuncs.com',
            'ap-south-1': 'ice.aliyuncs.com',
            'ap-southeast-1': 'ice.aliyuncs.com',
            'ap-southeast-2': 'ice.aliyuncs.com',
            'ap-southeast-3': 'ice.aliyuncs.com',
            'ap-southeast-5': 'ice.aliyuncs.com',
            'cn-beijing': 'ice.aliyuncs.com',
            'cn-beijing-finance-1': 'ice.aliyuncs.com',
            'cn-beijing-finance-pop': 'ice.aliyuncs.com',
            'cn-beijing-gov-1': 'ice.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ice.aliyuncs.com',
            'cn-chengdu': 'ice.aliyuncs.com',
            'cn-edge-1': 'ice.aliyuncs.com',
            'cn-fujian': 'ice.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ice.aliyuncs.com',
            'cn-hangzhou': 'ice.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ice.aliyuncs.com',
            'cn-hangzhou-finance': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ice.aliyuncs.com',
            'cn-hangzhou-test-306': 'ice.aliyuncs.com',
            'cn-hongkong': 'ice.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ice.aliyuncs.com',
            'cn-huhehaote': 'ice.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ice.aliyuncs.com',
            'cn-north-2-gov-1': 'ice.aliyuncs.com',
            'cn-qingdao': 'ice.aliyuncs.com',
            'cn-qingdao-nebula': 'ice.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ice.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ice.aliyuncs.com',
            'cn-shanghai-finance-1': 'ice.aliyuncs.com',
            'cn-shanghai-inner': 'ice.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ice.aliyuncs.com',
            'cn-shenzhen': 'ice.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ice.aliyuncs.com',
            'cn-shenzhen-inner': 'ice.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ice.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ice.aliyuncs.com',
            'cn-wuhan': 'ice.aliyuncs.com',
            'cn-wulanchabu': 'ice.aliyuncs.com',
            'cn-yushanfang': 'ice.aliyuncs.com',
            'cn-zhangbei': 'ice.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ice.aliyuncs.com',
            'cn-zhangjiakou': 'ice.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ice.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ice.aliyuncs.com',
            'eu-central-1': 'ice.aliyuncs.com',
            'eu-west-1': 'ice.aliyuncs.com',
            'eu-west-1-oxs': 'ice.aliyuncs.com',
            'me-east-1': 'ice.aliyuncs.com',
            'rus-west-1-pop': 'ice.aliyuncs.com',
            'us-east-1': 'ice.aliyuncs.com',
            'us-west-1': 'ice.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

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
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    def add_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_maps):
            query['MaterialMaps'] = request.material_maps
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_materials_with_options(request, runtime)

    def add_favorite_public_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFavoritePublicMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddFavoritePublicMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def add_favorite_public_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_favorite_public_media_with_options(request, runtime)

    def add_media_marks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_marks):
            query['MediaMarks'] = request.media_marks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaMarks',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddMediaMarksResponse(),
            self.call_api(params, req, runtime)
        )

    def add_media_marks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_media_marks_with_options(request, runtime)

    def add_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.preview_media):
            query['PreviewMedia'] = request.preview_media
        if not UtilClient.is_unset(request.related_mediaids):
            query['RelatedMediaids'] = request.related_mediaids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    def alter_search_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_config):
            query['IndexConfig'] = request.index_config
        if not UtilClient.is_unset(request.index_status):
            query['IndexStatus'] = request.index_status
        if not UtilClient.is_unset(request.index_type):
            query['IndexType'] = request.index_type
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AlterSearchIndex',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AlterSearchIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def alter_search_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.alter_search_index_with_options(request, runtime)

    def batch_get_media_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetMediaInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.BatchGetMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_media_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_media_infos_with_options(request, runtime)

    def cancel_dnajob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
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
            action='CancelDNAJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CancelDNAJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_dnajob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_dnajob_with_options(request, runtime)

    def cancel_favorite_public_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelFavoritePublicMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CancelFavoritePublicMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_favorite_public_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_favorite_public_media_with_options(request, runtime)

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
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    def create_audit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_audit_with_options(request, runtime)

    def create_avatar_training_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_description):
            query['AvatarDescription'] = request.avatar_description
        if not UtilClient.is_unset(request.avatar_name):
            query['AvatarName'] = request.avatar_name
        if not UtilClient.is_unset(request.avatar_type):
            query['AvatarType'] = request.avatar_type
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.thumbnail):
            query['Thumbnail'] = request.thumbnail
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAvatarTrainingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateAvatarTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_avatar_training_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_avatar_training_job_with_options(request, runtime)

    def create_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_template_with_options(request, runtime)

    def create_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gender):
            query['Gender'] = request.gender
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.voice_desc):
            query['VoiceDesc'] = request.voice_desc
        if not UtilClient.is_unset(request.voice_id):
            query['VoiceId'] = request.voice_id
        if not UtilClient.is_unset(request.voice_name):
            query['VoiceName'] = request.voice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_customized_voice_job_with_options(request, runtime)

    def create_dnadbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='CreateDNADB',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateDNADBResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dnadb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dnadbwith_options(request, runtime)

    def create_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_config):
            query['BusinessConfig'] = request.business_config
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.material_maps):
            query['MaterialMaps'] = request.material_maps
        if not UtilClient.is_unset(request.project_type):
            query['ProjectType'] = request.project_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.timeline):
            body['Timeline'] = request.timeline
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_editing_project_with_options(request, runtime)

    def create_live_record_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.CreateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_format):
            request.record_format_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_format, 'RecordFormat', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_format_shrink):
            body['RecordFormat'] = request.record_format_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRecordTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_record_template_with_options(request, runtime)

    def create_live_snapshot_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overwrite_format):
            body['OverwriteFormat'] = request.overwrite_format
        if not UtilClient.is_unset(request.sequence_format):
            body['SequenceFormat'] = request.sequence_format
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.time_interval):
            body['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveSnapshotTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_snapshot_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_snapshot_template_with_options(request, runtime)

    def create_live_transcode_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.CreateLiveTranscodeTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveTranscodeTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_transcode_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_transcode_template_with_options(request, runtime)

    def create_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_with_options(request, runtime)

    def create_search_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_config):
            query['IndexConfig'] = request.index_config
        if not UtilClient.is_unset(request.index_status):
            query['IndexStatus'] = request.index_status
        if not UtilClient.is_unset(request.index_type):
            query['IndexType'] = request.index_type
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSearchIndex',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateSearchIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def create_search_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_search_index_with_options(request, runtime)

    def create_search_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSearchLib',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateSearchLibResponse(),
            self.call_api(params, req, runtime)
        )

    def create_search_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_search_lib_with_options(request, runtime)

    def create_upload_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.file_info):
            query['FileInfo'] = request.file_info
        if not UtilClient.is_unset(request.media_meta_data):
            query['MediaMetaData'] = request.media_meta_data
        if not UtilClient.is_unset(request.post_process_config):
            query['PostProcessConfig'] = request.post_process_config
        if not UtilClient.is_unset(request.upload_target_config):
            query['UploadTargetConfig'] = request.upload_target_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateUploadMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def create_upload_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upload_media_with_options(request, runtime)

    def create_upload_stream_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadStream',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateUploadStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def create_upload_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upload_stream_with_options(request, runtime)

    def decrypt_kmsdata_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecryptKMSDataKey',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DecryptKMSDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def decrypt_kmsdata_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decrypt_kmsdata_key_with_options(request, runtime)

    def delete_avatar_training_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAvatarTrainingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteAvatarTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_avatar_training_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_avatar_training_job_with_options(request, runtime)

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
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    def delete_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_template_with_options(request, runtime)

    def delete_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_customized_voice_job_with_options(request, runtime)

    def delete_dnadbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbid):
            query['DBId'] = request.dbid
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
            action='DeleteDNADB',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteDNADBResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dnadb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dnadbwith_options(request, runtime)

    def delete_dnafiles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbid):
            query['DBId'] = request.dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.primary_keys):
            query['PrimaryKeys'] = request.primary_keys
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDNAFiles',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteDNAFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dnafiles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dnafiles_with_options(request, runtime)

    def delete_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_materials_with_options(request, runtime)

    def delete_editing_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_ids):
            query['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjects',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_editing_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_projects_with_options(request, runtime)

    def delete_live_record_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_ids):
            query['RecordIds'] = request.record_ids
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordFiles',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteLiveRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_record_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_files_with_options(request, runtime)

    def delete_live_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_template_with_options(request, runtime)

    def delete_live_snapshot_files_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DeleteLiveSnapshotFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_timestamp_list):
            request.create_timestamp_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_timestamp_list, 'CreateTimestampList', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_timestamp_list_shrink):
            query['CreateTimestampList'] = request.create_timestamp_list_shrink
        if not UtilClient.is_unset(request.delete_original_file):
            query['DeleteOriginalFile'] = request.delete_original_file
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotFiles',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteLiveSnapshotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_snapshot_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_files_with_options(request, runtime)

    def delete_live_snapshot_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_snapshot_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_template_with_options(request, runtime)

    def delete_live_transcode_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveTranscodeJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_transcode_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_transcode_job_with_options(request, runtime)

    def delete_live_transcode_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveTranscodeTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_transcode_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_transcode_template_with_options(request, runtime)

    def delete_media_from_search_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.msg_body):
            query['MsgBody'] = request.msg_body
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaFromSearchLib',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaFromSearchLibResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_media_from_search_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_media_from_search_lib_with_options(request, runtime)

    def delete_media_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not UtilClient.is_unset(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_media_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_media_infos_with_options(request, runtime)

    def delete_media_marks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_mark_ids):
            query['MediaMarkIds'] = request.media_mark_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaMarks',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaMarksResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_media_marks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_media_marks_with_options(request, runtime)

    def delete_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pipeline_with_options(request, runtime)

    def delete_play_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlayInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeletePlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_play_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_play_info_with_options(request, runtime)

    def delete_smart_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteSmartJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_smart_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_job_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def describe_meter_ims_edit_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsEditUsage',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMeterImsEditUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_ims_edit_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_edit_usage_with_options(request, runtime)

    def describe_meter_ims_media_convert_uhdusage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMediaConvertUHDUsage',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_ims_media_convert_uhdusage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_media_convert_uhdusage_with_options(request, runtime)

    def describe_meter_ims_media_convert_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMediaConvertUsage',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMeterImsMediaConvertUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_ims_media_convert_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_media_convert_usage_with_options(request, runtime)

    def describe_meter_ims_mps_ai_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMpsAiUsage',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMeterImsMpsAiUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_ims_mps_ai_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_mps_ai_usage_with_options(request, runtime)

    def describe_meter_ims_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsSummary',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMeterImsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_ims_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_summary_with_options(request, runtime)

    def describe_play_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayList',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribePlayListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_play_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_play_list_with_options(request, runtime)

    def detect_audio_for_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_record_id):
            query['AudioRecordId'] = request.audio_record_id
        if not UtilClient.is_unset(request.record_url):
            query['RecordUrl'] = request.record_url
        if not UtilClient.is_unset(request.voice_id):
            query['VoiceId'] = request.voice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectAudioForCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DetectAudioForCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_audio_for_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_audio_for_customized_voice_job_with_options(request, runtime)

    def drop_search_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_type):
            query['IndexType'] = request.index_type
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropSearchIndex',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DropSearchIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def drop_search_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_search_index_with_options(request, runtime)

    def drop_search_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropSearchLib',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DropSearchLibResponse(),
            self.call_api(params, req, runtime)
        )

    def drop_search_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_search_lib_with_options(request, runtime)

    def generate_kmsdata_key_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GenerateKMSDataKey',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GenerateKMSDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_kmsdata_key(self):
        runtime = util_models.RuntimeOptions()
        return self.generate_kmsdata_key_with_options(runtime)

    def get_avatar_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_id):
            query['AvatarId'] = request.avatar_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvatar',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def get_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_avatar_with_options(request, runtime)

    def get_avatar_training_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvatarTrainingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetAvatarTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_avatar_training_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_avatar_training_job_with_options(request, runtime)

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
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_categories_with_options(request, runtime)

    def get_content_analyze_config_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetContentAnalyzeConfig',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetContentAnalyzeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_content_analyze_config(self):
        runtime = util_models.RuntimeOptions()
        return self.get_content_analyze_config_with_options(runtime)

    def get_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_custom_template_with_options(request, runtime)

    def get_customized_voice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.voice_id):
            query['VoiceId'] = request.voice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizedVoice',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetCustomizedVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_customized_voice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customized_voice_with_options(request, runtime)

    def get_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customized_voice_job_with_options(request, runtime)

    def get_default_storage_location_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultStorageLocation',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetDefaultStorageLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_default_storage_location(self):
        runtime = util_models.RuntimeOptions()
        return self.get_default_storage_location_with_options(runtime)

    def get_demonstration_for_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDemonstrationForCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetDemonstrationForCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_demonstration_for_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_demonstration_for_customized_voice_job_with_options(request, runtime)

    def get_dynamic_image_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicImageJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetDynamicImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dynamic_image_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dynamic_image_job_with_options(request, runtime)

    def get_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.request_source):
            query['RequestSource'] = request.request_source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    def get_editing_project_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_editing_project_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    def get_event_callback_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetEventCallback',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEventCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_callback(self):
        runtime = util_models.RuntimeOptions()
        return self.get_event_callback_with_options(runtime)

    def get_live_editing_index_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveEditingIndexFile',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveEditingIndexFileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_editing_index_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_editing_index_file_with_options(request, runtime)

    def get_live_editing_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveEditingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveEditingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_editing_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_editing_job_with_options(request, runtime)

    def get_live_record_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveRecordJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveRecordJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_record_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_job_with_options(request, runtime)

    def get_live_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveRecordTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_template_with_options(request, runtime)

    def get_live_snapshot_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveSnapshotJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_snapshot_job_with_options(request, runtime)

    def get_live_snapshot_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveSnapshotTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_snapshot_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_snapshot_template_with_options(request, runtime)

    def get_live_transcode_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveTranscodeJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_transcode_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_transcode_job_with_options(request, runtime)

    def get_live_transcode_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveTranscodeTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_transcode_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_transcode_template_with_options(request, runtime)

    def get_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_info_with_options(request, runtime)

    def get_media_info_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaInfoJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_info_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_info_job_with_options(request, runtime)

    def get_media_marks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_mark_ids):
            query['MediaMarkIds'] = request.media_mark_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaMarks',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaMarksResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_marks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_marks_with_options(request, runtime)

    def get_media_producing_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaProducingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaProducingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_media_producing_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_producing_job_with_options(request, runtime)

    def get_package_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackageJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetPackageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_package_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_package_job_with_options(request, runtime)

    def get_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_with_options(request, runtime)

    def get_play_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPlayInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_play_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    def get_public_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetPublicMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_public_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_public_media_info_with_options(request, runtime)

    def get_smart_handle_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartHandleJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetSmartHandleJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_smart_handle_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_smart_handle_job_with_options(request, runtime)

    def get_snapshot_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_snapshot_job_with_options(request, runtime)

    def get_snapshot_urls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotUrls',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetSnapshotUrlsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_snapshot_urls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_snapshot_urls_with_options(request, runtime)

    def get_system_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSystemTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetSystemTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_system_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_system_template_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.related_mediaid_flag):
            query['RelatedMediaidFlag'] = request.related_mediaid_flag
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def get_template_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_list):
            query['FileList'] = request.file_list
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_materials_with_options(request, runtime)

    def get_template_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateParams',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateParamsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_params_with_options(request, runtime)

    def get_transcode_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranscodeJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_transcode_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_job_with_options(request, runtime)

    def get_url_upload_infos_with_options(self, request, runtime):
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
            action='GetUrlUploadInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetUrlUploadInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def get_url_upload_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_url_upload_infos_with_options(request, runtime)

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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoList',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetVideoListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_list_with_options(request, runtime)

    def get_workflow_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowTask',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetWorkflowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workflow_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_task_with_options(request, runtime)

    def insert_media_to_search_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.msg_body):
            query['MsgBody'] = request.msg_body
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertMediaToSearchLib',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.InsertMediaToSearchLibResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_media_to_search_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_media_to_search_lib_with_options(request, runtime)

    def list_all_public_media_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPublicMediaTags',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListAllPublicMediaTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_all_public_media_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_all_public_media_tags_with_options(request, runtime)

    def list_avatar_training_jobs_with_options(self, request, runtime):
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
            action='ListAvatarTrainingJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListAvatarTrainingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_avatar_training_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_avatar_training_jobs_with_options(request, runtime)

    def list_avatars_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_type):
            query['AvatarType'] = request.avatar_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvatars',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListAvatarsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_avatars(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_avatars_with_options(request, runtime)

    def list_custom_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListCustomTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_templates_with_options(request, runtime)

    def list_customized_voice_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomizedVoiceJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListCustomizedVoiceJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_customized_voice_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_customized_voice_jobs_with_options(request, runtime)

    def list_customized_voices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomizedVoices',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListCustomizedVoicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_customized_voices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_customized_voices_with_options(request, runtime)

    def list_dnadbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbids):
            query['DBIds'] = request.dbids
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
            action='ListDNADB',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListDNADBResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dnadb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dnadbwith_options(request, runtime)

    def list_dnafiles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbid):
            query['DBId'] = request.dbid
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDNAFiles',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListDNAFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dnafiles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dnafiles_with_options(request, runtime)

    def list_dynamic_image_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicImageJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListDynamicImageJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dynamic_image_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_image_jobs_with_options(request, runtime)

    def list_live_record_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordFiles',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_record_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_files_with_options(request, runtime)

    def list_live_record_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveRecordJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_record_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_jobs_with_options(request, runtime)

    def list_live_record_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_record_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_templates_with_options(request, runtime)

    def list_live_snapshot_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotFiles',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveSnapshotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_snapshot_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_snapshot_files_with_options(request, runtime)

    def list_live_snapshot_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveSnapshotJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_snapshot_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_snapshot_jobs_with_options(request, runtime)

    def list_live_snapshot_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveSnapshotTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_snapshot_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_snapshot_templates_with_options(request, runtime)

    def list_live_transcode_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_mode):
            query['StartMode'] = request.start_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveTranscodeJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveTranscodeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_transcode_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_transcode_jobs_with_options(request, runtime)

    def list_live_transcode_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.video_codec):
            query['VideoCodec'] = request.video_codec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveTranscodeTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListLiveTranscodeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_transcode_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_transcode_templates_with_options(request, runtime)

    def list_media_basic_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.include_file_basic_info):
            query['IncludeFileBasicInfo'] = request.include_file_basic_info
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_media_basic_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_media_basic_infos_with_options(request, runtime)

    def list_media_info_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaInfoJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaInfoJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_media_info_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_media_info_jobs_with_options(request, runtime)

    def list_media_marks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_mark_ids):
            query['MediaMarkIds'] = request.media_mark_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaMarks',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaMarksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_media_marks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_media_marks_with_options(request, runtime)

    def list_package_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPackageJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListPackageJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_package_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_package_jobs_with_options(request, runtime)

    def list_pipelines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipelines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pipelines_with_options(request, runtime)

    def list_public_media_basic_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_file_basic_info):
            query['IncludeFileBasicInfo'] = request.include_file_basic_info
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_tag_id):
            query['MediaTagId'] = request.media_tag_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListPublicMediaBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_public_media_basic_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_public_media_basic_infos_with_options(request, runtime)

    def list_smart_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_smart_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_smart_jobs_with_options(request, runtime)

    def list_smart_sys_avatar_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartSysAvatarModels',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartSysAvatarModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_smart_sys_avatar_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_smart_sys_avatar_models_with_options(request, runtime)

    def list_smart_voice_groups_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSmartVoiceGroups',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartVoiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_smart_voice_groups(self):
        runtime = util_models.RuntimeOptions()
        return self.list_smart_voice_groups_with_options(runtime)

    def list_snapshot_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshotJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSnapshotJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_snapshot_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_jobs_with_options(request, runtime)

    def list_system_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSystemTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_templates_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_source):
            query['CreateSource'] = request.create_source
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def list_transcode_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTranscodeJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListTranscodeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transcode_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_jobs_with_options(request, runtime)

    def query_dnajob_list_with_options(self, request, runtime):
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
            action='QueryDNAJobList',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QueryDNAJobListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dnajob_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dnajob_list_with_options(request, runtime)

    def query_iproduction_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QueryIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_iproduction_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_iproduction_job_with_options(request, runtime)

    def query_media_censor_job_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
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
            action='QueryMediaCensorJobDetail',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QueryMediaCensorJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_media_censor_job_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_detail_with_options(request, runtime)

    def query_media_censor_job_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QueryMediaCensorJobListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_media_censor_job_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_list_with_options(request, runtime)

    def query_media_index_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaIndexJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QueryMediaIndexJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_media_index_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_media_index_job_with_options(request, runtime)

    def query_search_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_type):
            query['IndexType'] = request.index_type
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySearchIndex',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QuerySearchIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def query_search_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_search_index_with_options(request, runtime)

    def query_search_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySearchLib',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QuerySearchLibResponse(),
            self.call_api(params, req, runtime)
        )

    def query_search_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_search_lib_with_options(request, runtime)

    def query_smarttag_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.QuerySmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_smarttag_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_job_with_options(request, runtime)

    def refresh_upload_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshUploadMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.RefreshUploadMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_upload_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_media_with_options(request, runtime)

    def register_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not UtilClient.is_unset(request.register_config):
            query['RegisterConfig'] = request.register_config
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
            action='RegisterMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def register_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_media_info_with_options(request, runtime)

    def register_media_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMediaStream',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def register_media_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_media_stream_with_options(request, runtime)

    def search_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_source):
            query['CreateSource'] = request.create_source
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_type):
            query['ProjectType'] = request.project_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def search_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    def search_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.match):
            query['Match'] = request.match
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scroll_token):
            query['ScrollToken'] = request.scroll_token
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def search_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    def search_media_by_ailabel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.multimodal_search_type):
            query['MultimodalSearchType'] = request.multimodal_search_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.specific_search):
            query['SpecificSearch'] = request.specific_search
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaByAILabel',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchMediaByAILabelResponse(),
            self.call_api(params, req, runtime)
        )

    def search_media_by_ailabel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_media_by_ailabel_with_options(request, runtime)

    def search_media_by_face_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.face_search_token):
            query['FaceSearchToken'] = request.face_search_token
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_image_url):
            query['PersonImageUrl'] = request.person_image_url
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaByFace',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchMediaByFaceResponse(),
            self.call_api(params, req, runtime)
        )

    def search_media_by_face(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_media_by_face_with_options(request, runtime)

    def search_media_by_multimodal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaByMultimodal',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchMediaByMultimodalResponse(),
            self.call_api(params, req, runtime)
        )

    def search_media_by_multimodal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_media_by_multimodal_with_options(request, runtime)

    def search_media_clip_by_face_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.face_search_token):
            query['FaceSearchToken'] = request.face_search_token
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaClipByFace',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchMediaClipByFaceResponse(),
            self.call_api(params, req, runtime)
        )

    def search_media_clip_by_face(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_media_clip_by_face_with_options(request, runtime)

    def search_public_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized):
            query['Authorized'] = request.authorized
        if not UtilClient.is_unset(request.dynamic_meta_data_match_fields):
            query['DynamicMetaDataMatchFields'] = request.dynamic_meta_data_match_fields
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.favorite):
            query['Favorite'] = request.favorite
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPublicMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchPublicMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def search_public_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_public_media_info_with_options(request, runtime)

    def send_live_snapshot_job_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.command):
            body['Command'] = request.command
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendLiveSnapshotJobCommand',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SendLiveSnapshotJobCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def send_live_snapshot_job_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_live_snapshot_job_command_with_options(request, runtime)

    def send_live_transcode_job_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendLiveTranscodeJobCommand',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SendLiveTranscodeJobCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def send_live_transcode_job_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_live_transcode_job_command_with_options(request, runtime)

    def set_content_analyze_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto):
            query['Auto'] = request.auto
        if not UtilClient.is_unset(request.save_type):
            query['SaveType'] = request.save_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetContentAnalyzeConfig',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetContentAnalyzeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_content_analyze_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_content_analyze_config_with_options(request, runtime)

    def set_default_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultCustomTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_custom_template_with_options(request, runtime)

    def set_default_storage_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultStorageLocation',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultStorageLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_storage_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_storage_location_with_options(request, runtime)

    def set_event_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_switch):
            query['AuthSwitch'] = request.auth_switch
        if not UtilClient.is_unset(request.callback_queue_name):
            query['CallbackQueueName'] = request.callback_queue_name
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackURL'] = request.callback_url
        if not UtilClient.is_unset(request.event_type_list):
            query['EventTypeList'] = request.event_type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEventCallback',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetEventCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def set_event_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_event_callback_with_options(request, runtime)

    def start_workflow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_input):
            query['TaskInput'] = request.task_input
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartWorkflow',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.StartWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def start_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_workflow_with_options(request, runtime)

    def submit_asrjob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.input_file):
            query['InputFile'] = request.input_file
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitASRJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitASRJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_asrjob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_asrjob_with_options(request, runtime)

    def submit_audio_produce_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioProduceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAudioProduceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_audio_produce_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_produce_job_with_options(request, runtime)

    def submit_avatar_training_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAvatarTrainingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAvatarTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_avatar_training_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_avatar_training_job_with_options(request, runtime)

    def submit_avatar_video_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAvatarVideoJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAvatarVideoJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_avatar_video_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_avatar_video_job_with_options(request, runtime)

    def submit_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demo_audio_media_url):
            query['DemoAudioMediaURL'] = request.demo_audio_media_url
        if not UtilClient.is_unset(request.voice_id):
            query['VoiceId'] = request.voice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_customized_voice_job_with_options(request, runtime)

    def submit_dnajob_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitDNAJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.dbid):
            query['DBId'] = request.dbid
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.primary_key):
            query['PrimaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDNAJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDNAJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_dnajob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_dnajob_with_options(request, runtime)

    def submit_dynamic_chart_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.axis_params):
            query['AxisParams'] = request.axis_params
        if not UtilClient.is_unset(request.background):
            query['Background'] = request.background
        if not UtilClient.is_unset(request.chart_config):
            query['ChartConfig'] = request.chart_config
        if not UtilClient.is_unset(request.chart_title):
            query['ChartTitle'] = request.chart_title
        if not UtilClient.is_unset(request.chart_type):
            query['ChartType'] = request.chart_type
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.subtitle):
            query['Subtitle'] = request.subtitle
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.unit):
            query['Unit'] = request.unit
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicChartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDynamicChartJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_dynamic_chart_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_chart_job_with_options(request, runtime)

    def submit_dynamic_image_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitDynamicImageJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicImageJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDynamicImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_dynamic_image_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    def submit_iproduction_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitIProductionJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_iproduction_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_iproduction_job_with_options(request, runtime)

    def submit_live_editing_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clips):
            query['Clips'] = request.clips
        if not UtilClient.is_unset(request.live_stream_config):
            query['LiveStreamConfig'] = request.live_stream_config
        if not UtilClient.is_unset(request.media_produce_config):
            query['MediaProduceConfig'] = request.media_produce_config
        if not UtilClient.is_unset(request.output_media_config):
            query['OutputMediaConfig'] = request.output_media_config
        if not UtilClient.is_unset(request.output_media_target):
            query['OutputMediaTarget'] = request.output_media_target
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitLiveEditingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitLiveEditingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_live_editing_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_live_editing_job_with_options(request, runtime)

    def submit_live_record_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveRecordJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_output):
            request.record_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_output, 'RecordOutput', 'json')
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notify_url):
            body['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.record_output_shrink):
            body['RecordOutput'] = request.record_output_shrink
        if not UtilClient.is_unset(request.stream_input_shrink):
            body['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLiveRecordJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitLiveRecordJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_live_record_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_live_record_job_with_options(request, runtime)

    def submit_live_snapshot_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveSnapshotJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.snapshot_output):
            request.snapshot_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.snapshot_output, 'SnapshotOutput', 'json')
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.snapshot_output_shrink):
            body['SnapshotOutput'] = request.snapshot_output_shrink
        if not UtilClient.is_unset(request.stream_input_shrink):
            body['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLiveSnapshotJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitLiveSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_live_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_live_snapshot_job_with_options(request, runtime)

    def submit_live_transcode_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        if not UtilClient.is_unset(tmp_req.timed_config):
            request.timed_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timed_config, 'TimedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transcode_output):
            request.transcode_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcode_output, 'TranscodeOutput', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_mode):
            query['StartMode'] = request.start_mode
        if not UtilClient.is_unset(request.stream_input_shrink):
            query['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timed_config_shrink):
            query['TimedConfig'] = request.timed_config_shrink
        if not UtilClient.is_unset(request.transcode_output_shrink):
            query['TranscodeOutput'] = request.transcode_output_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitLiveTranscodeJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_live_transcode_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_live_transcode_job_with_options(request, runtime)

    def submit_media_censor_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitMediaCensorJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaCensorJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_media_censor_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_media_censor_job_with_options(request, runtime)

    def submit_media_info_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitMediaInfoJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_media_info_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_media_info_job_with_options(request, runtime)

    def submit_media_producing_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.editing_produce_config):
            query['EditingProduceConfig'] = request.editing_produce_config
        if not UtilClient.is_unset(request.media_metadata):
            query['MediaMetadata'] = request.media_metadata
        if not UtilClient.is_unset(request.output_media_config):
            query['OutputMediaConfig'] = request.output_media_config
        if not UtilClient.is_unset(request.output_media_target):
            query['OutputMediaTarget'] = request.output_media_target
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_metadata):
            query['ProjectMetadata'] = request.project_metadata
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.timeline):
            body['Timeline'] = request.timeline
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitMediaProducingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaProducingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_media_producing_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_media_producing_job_with_options(request, runtime)

    def submit_package_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitPackageJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPackageJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitPackageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_package_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_package_job_with_options(request, runtime)

    def submit_smarttag_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSmarttagJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_smarttag_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_smarttag_job_with_options(request, runtime)

    def submit_snapshot_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSnapshotJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    def submit_standard_customized_voice_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audios):
            query['Audios'] = request.audios
        if not UtilClient.is_unset(request.authentication):
            query['Authentication'] = request.authentication
        if not UtilClient.is_unset(request.demo_audio_media_url):
            query['DemoAudioMediaURL'] = request.demo_audio_media_url
        if not UtilClient.is_unset(request.gender):
            query['Gender'] = request.gender
        if not UtilClient.is_unset(request.voice_name):
            query['VoiceName'] = request.voice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitStandardCustomizedVoiceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitStandardCustomizedVoiceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_standard_customized_voice_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_standard_customized_voice_job_with_options(request, runtime)

    def submit_subtitle_produce_job_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: SubmitSubtitleProduceJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitSubtitleProduceJobResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSubtitleProduceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSubtitleProduceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_subtitle_produce_job(self, request):
        """
        @deprecated
        

        @param request: SubmitSubtitleProduceJobRequest

        @return: SubmitSubtitleProduceJobResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_subtitle_produce_job_with_options(request, runtime)

    def submit_sync_media_info_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSyncMediaInfoJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSyncMediaInfoJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSyncMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_sync_media_info_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_sync_media_info_job_with_options(request, runtime)

    def submit_transcode_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_group):
            request.input_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_group, 'InputGroup', 'json')
        if not UtilClient.is_unset(tmp_req.output_group):
            request.output_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output_group, 'OutputGroup', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.input_group_shrink):
            query['InputGroup'] = request.input_group_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_group_shrink):
            query['OutputGroup'] = request.output_group_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTranscodeJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_transcode_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_transcode_job_with_options(request, runtime)

    def update_avatar_training_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avatar_description):
            query['AvatarDescription'] = request.avatar_description
        if not UtilClient.is_unset(request.avatar_name):
            query['AvatarName'] = request.avatar_name
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.thumbnail):
            query['Thumbnail'] = request.thumbnail
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAvatarTrainingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateAvatarTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_avatar_training_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_avatar_training_job_with_options(request, runtime)

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
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    def update_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_custom_template_with_options(request, runtime)

    def update_customized_voice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demo_audio_media_id):
            query['DemoAudioMediaId'] = request.demo_audio_media_id
        if not UtilClient.is_unset(request.voice_id):
            query['VoiceId'] = request.voice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomizedVoice',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateCustomizedVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_customized_voice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_customized_voice_with_options(request, runtime)

    def update_editing_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_status):
            query['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.timeline):
            body['Timeline'] = request.timeline
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_editing_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    def update_live_record_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_format):
            request.record_format_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_format, 'RecordFormat', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_format_shrink):
            body['RecordFormat'] = request.record_format_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveRecordTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_template_with_options(request, runtime)

    def update_live_snapshot_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overwrite_format):
            body['OverwriteFormat'] = request.overwrite_format
        if not UtilClient.is_unset(request.sequence_format):
            body['SequenceFormat'] = request.sequence_format
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.time_interval):
            body['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveSnapshotTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_snapshot_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_snapshot_template_with_options(request, runtime)

    def update_live_transcode_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        if not UtilClient.is_unset(tmp_req.timed_config):
            request.timed_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timed_config, 'TimedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transcode_output):
            request.transcode_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcode_output, 'TranscodeOutput', 'json')
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.stream_input_shrink):
            query['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.timed_config_shrink):
            query['TimedConfig'] = request.timed_config_shrink
        if not UtilClient.is_unset(request.transcode_output_shrink):
            query['TranscodeOutput'] = request.transcode_output_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTranscodeJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_transcode_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_transcode_job_with_options(request, runtime)

    def update_live_transcode_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveTranscodeTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTranscodeTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_transcode_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_transcode_template_with_options(request, runtime)

    def update_media_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not UtilClient.is_unset(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_media_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_media_info_with_options(request, runtime)

    def update_media_marks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_marks):
            query['MediaMarks'] = request.media_marks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaMarks',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaMarksResponse(),
            self.call_api(params, req, runtime)
        )

    def update_media_marks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_media_marks_with_options(request, runtime)

    def update_media_to_search_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.msg_body):
            query['MsgBody'] = request.msg_body
        if not UtilClient.is_unset(request.search_lib_name):
            query['SearchLibName'] = request.search_lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaToSearchLib',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaToSearchLibResponse(),
            self.call_api(params, req, runtime)
        )

    def update_media_to_search_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_media_to_search_lib_with_options(request, runtime)

    def update_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_with_options(request, runtime)

    def update_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.preview_media):
            query['PreviewMedia'] = request.preview_media
        if not UtilClient.is_unset(request.related_mediaids):
            query['RelatedMediaids'] = request.related_mediaids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    def upload_media_by_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.media_meta_data):
            query['MediaMetaData'] = request.media_meta_data
        if not UtilClient.is_unset(request.post_process_config):
            query['PostProcessConfig'] = request.post_process_config
        if not UtilClient.is_unset(request.upload_target_config):
            query['UploadTargetConfig'] = request.upload_target_config
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMediaByURL',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UploadMediaByURLResponse(),
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
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UploadStreamByURLResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_stream_by_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_stream_by_urlwith_options(request, runtime)
