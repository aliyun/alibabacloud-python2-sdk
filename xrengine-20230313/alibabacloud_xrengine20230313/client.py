# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xrengine20230313 import models as xr_engine_20230313_models
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
            'ap-northeast-1': 'xrengine-daily.aliyuncs.com',
            'ap-northeast-2-pop': 'xrengine-daily.aliyuncs.com',
            'ap-south-1': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-1': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-2': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-3': 'xrengine-daily.aliyuncs.com',
            'ap-southeast-5': 'xrengine-daily.aliyuncs.com',
            'cn-beijing': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-finance-1': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-finance-pop': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-gov-1': 'xrengine-daily.aliyuncs.com',
            'cn-beijing-nu16-b01': 'xrengine-daily.aliyuncs.com',
            'cn-chengdu': 'xrengine-daily.aliyuncs.com',
            'cn-edge-1': 'xrengine-daily.aliyuncs.com',
            'cn-fujian': 'xrengine-daily.aliyuncs.com',
            'cn-haidian-cm12-c01': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-finance': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'xrengine-daily.aliyuncs.com',
            'cn-hangzhou-test-306': 'xrengine-daily.aliyuncs.com',
            'cn-hongkong': 'xrengine-daily.aliyuncs.com',
            'cn-hongkong-finance-pop': 'xrengine-daily.aliyuncs.com',
            'cn-huhehaote': 'xrengine-daily.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'xrengine-daily.aliyuncs.com',
            'cn-north-2-gov-1': 'xrengine-daily.aliyuncs.com',
            'cn-qingdao': 'xrengine-daily.aliyuncs.com',
            'cn-qingdao-nebula': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-et15-b01': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-et2-b01': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-finance-1': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-inner': 'xrengine-daily.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-finance-1': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-inner': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'xrengine-daily.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'xrengine-daily.aliyuncs.com',
            'cn-wuhan': 'xrengine-daily.aliyuncs.com',
            'cn-wulanchabu': 'xrengine-daily.aliyuncs.com',
            'cn-yushanfang': 'xrengine-daily.aliyuncs.com',
            'cn-zhangbei': 'xrengine-daily.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'xrengine-daily.aliyuncs.com',
            'cn-zhangjiakou': 'xrengine-daily.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'xrengine-daily.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'xrengine-daily.aliyuncs.com',
            'eu-central-1': 'xrengine-daily.aliyuncs.com',
            'eu-west-1': 'xrengine-daily.aliyuncs.com',
            'eu-west-1-oxs': 'xrengine-daily.aliyuncs.com',
            'me-east-1': 'xrengine-daily.aliyuncs.com',
            'rus-west-1-pop': 'xrengine-daily.aliyuncs.com',
            'us-east-1': 'xrengine-daily.aliyuncs.com',
            'us-west-1': 'xrengine-daily.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('xrengine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def auth_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthUser',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.AuthUserResponse(),
            self.call_api(params, req, runtime)
        )

    def auth_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.auth_user_with_options(request, runtime)

    def create_digital_human_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.audio_id):
            body['AudioId'] = request.audio_id
        if not UtilClient.is_unset(request.audio_url):
            body['AudioUrl'] = request.audio_url
        if not UtilClient.is_unset(request.background_id):
            body['BackgroundId'] = request.background_id
        if not UtilClient.is_unset(request.background_url):
            body['BackgroundUrl'] = request.background_url
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.foreground_id):
            body['ForegroundId'] = request.foreground_id
        if not UtilClient.is_unset(request.foreground_url):
            body['ForegroundUrl'] = request.foreground_url
        if not UtilClient.is_unset(request.human_layer_style):
            body['HumanLayerStyle'] = request.human_layer_style
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.output_config):
            body['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.tts_voice_id):
            body['TtsVoiceId'] = request.tts_voice_id
        if not UtilClient.is_unset(request.watermark_image_url):
            body['WatermarkImageUrl'] = request.watermark_image_url
        if not UtilClient.is_unset(request.watermark_style):
            body['WatermarkStyle'] = request.watermark_style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDigitalHumanProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.CreateDigitalHumanProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_digital_human_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_digital_human_project_with_options(request, runtime)

    def create_live_portrait_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.audio_id):
            body['AudioId'] = request.audio_id
        if not UtilClient.is_unset(request.audio_url):
            body['AudioUrl'] = request.audio_url
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.light_model):
            body['LightModel'] = request.light_model
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.output_config):
            body['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.tts_voice_id):
            body['TtsVoiceId'] = request.tts_voice_id
        if not UtilClient.is_unset(request.watermark_image_url):
            body['WatermarkImageUrl'] = request.watermark_image_url
        if not UtilClient.is_unset(request.watermark_style):
            body['WatermarkStyle'] = request.watermark_style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLivePortraitProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.CreateLivePortraitProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_portrait_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_portrait_project_with_options(request, runtime)

    def get_map_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMapData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.GetMapDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_map_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_map_data_with_options(request, runtime)

    def get_map_publish_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMapPublishData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.GetMapPublishDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_map_publish_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_map_publish_data_with_options(request, runtime)

    def init_locate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitLocate',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.InitLocateResponse(),
            self.call_api(params, req, runtime)
        )

    def init_locate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_locate_with_options(request, runtime)

    def list_digital_human_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.only_personal_materials):
            body['OnlyPersonalMaterials'] = request.only_personal_materials
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.types):
            body['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDigitalHumanMaterials',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.ListDigitalHumanMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_digital_human_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_digital_human_materials_with_options(request, runtime)

    def list_location_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLocationService',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.ListLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_location_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_location_service_with_options(request, runtime)

    def live_portrait_face_detect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LivePortraitFaceDetect',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.LivePortraitFaceDetectResponse(),
            self.call_api(params, req, runtime)
        )

    def live_portrait_face_detect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.live_portrait_face_detect_with_options(request, runtime)

    def locate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image):
            body['Image'] = request.image
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Locate',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.LocateResponse(),
            self.call_api(params, req, runtime)
        )

    def locate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.locate_with_options(request, runtime)

    def login_model_scope_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.emp_id):
            body['EmpId'] = request.emp_id
        if not UtilClient.is_unset(request.emp_name):
            body['EmpName'] = request.emp_name
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LoginModelScope',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.LoginModelScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def login_model_scope(self, request):
        runtime = util_models.RuntimeOptions()
        return self.login_model_scope_with_options(request, runtime)

    def pop_batch_query_object_generation_project_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.project_ids):
            body['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBatchQueryObjectGenerationProjectStatus',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBatchQueryObjectGenerationProjectStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_batch_query_object_generation_project_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_batch_query_object_generation_project_status_with_options(request, runtime)

    def pop_batch_query_object_project_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_ids):
            body['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBatchQueryObjectProjectStatus',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBatchQueryObjectProjectStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_batch_query_object_project_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_batch_query_object_project_status_with_options(request, runtime)

    def pop_build_feature_to_avatar_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildFeatureToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_build_feature_to_avatar_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_build_feature_to_avatar_project_with_options(request, runtime)

    def pop_build_live_portrait_model_scope_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildLivePortraitModelScopeProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildLivePortraitModelScopeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_build_live_portrait_model_scope_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_build_live_portrait_model_scope_project_with_options(request, runtime)

    def pop_build_object_generation_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildObjectGenerationProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildObjectGenerationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_build_object_generation_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_build_object_generation_project_with_options(request, runtime)

    def pop_build_object_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildObjectProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_build_object_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_build_object_project_with_options(request, runtime)

    def pop_build_pak_render_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildPakRenderProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildPakRenderProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_build_pak_render_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_build_pak_render_project_with_options(request, runtime)

    def pop_build_text_to_avatar_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopBuildTextToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopBuildTextToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_build_text_to_avatar_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_build_text_to_avatar_project_with_options(request, runtime)

    def pop_create_feature_to_avatar_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateFeatureToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_feature_to_avatar_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_feature_to_avatar_project_with_options(request, runtime)

    def pop_create_live_portrait_model_scope_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateLivePortraitModelScopeProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateLivePortraitModelScopeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_live_portrait_model_scope_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_live_portrait_model_scope_project_with_options(request, runtime)

    def pop_create_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.check_status):
            body['CheckStatus'] = request.check_status
        if not UtilClient.is_unset(request.ext):
            body['Ext'] = request.ext
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.list_status):
            body['ListStatus'] = request.list_status
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            body['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateMaterial',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_material_with_options(request, runtime)

    def pop_create_object_generation_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.biz_usage):
            body['BizUsage'] = request.biz_usage
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateObjectGenerationProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateObjectGenerationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_object_generation_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_object_generation_project_with_options(request, runtime)

    def pop_create_object_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_build):
            body['AutoBuild'] = request.auto_build
        if not UtilClient.is_unset(request.biz_usage):
            body['BizUsage'] = request.biz_usage
        if not UtilClient.is_unset(request.custom_source):
            body['CustomSource'] = request.custom_source
        if not UtilClient.is_unset(request.dependencies):
            body['Dependencies'] = request.dependencies
        if not UtilClient.is_unset(request.foreign_uid):
            body['ForeignUid'] = request.foreign_uid
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.recommend_status):
            body['RecommendStatus'] = request.recommend_status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateObjectProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_object_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_object_project_with_options(request, runtime)

    def pop_create_pak_render_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreatePakRenderProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreatePakRenderProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_pak_render_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_pak_render_project_with_options(request, runtime)

    def pop_create_text_to_avatar_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.intro):
            body['Intro'] = request.intro
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopCreateTextToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopCreateTextToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_create_text_to_avatar_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_create_text_to_avatar_project_with_options(request, runtime)

    def pop_delete_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopDeleteMaterial',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopDeleteMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_delete_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_delete_material_with_options(request, runtime)

    def pop_get_aitry_on_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.with_material):
            query['WithMaterial'] = request.with_material
        if not UtilClient.is_unset(request.with_result):
            query['WithResult'] = request.with_result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopGetAITryOnJob',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopGetAITryOnJobResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_get_aitry_on_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_get_aitry_on_job_with_options(request, runtime)

    def pop_list_aitry_on_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListAITryOnJobs',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListAITryOnJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_aitry_on_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_aitry_on_jobs_with_options(request, runtime)

    def pop_list_common_materials_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.list_status):
            query['ListStatus'] = request.list_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListCommonMaterialsAll',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListCommonMaterialsAllResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_common_materials_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_common_materials_all_with_options(request, runtime)

    def pop_list_feature_to_avatar_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.list_status):
            body['ListStatus'] = request.list_status
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListFeatureToAvatarMaterials',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListFeatureToAvatarMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_feature_to_avatar_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_feature_to_avatar_materials_with_options(request, runtime)

    def pop_list_feature_to_avatar_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListFeatureToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListFeatureToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_feature_to_avatar_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_feature_to_avatar_project_with_options(request, runtime)

    def pop_list_live_portrait_model_scope_materials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.types):
            body['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListLivePortraitModelScopeMaterials',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListLivePortraitModelScopeMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_live_portrait_model_scope_materials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_live_portrait_model_scope_materials_with_options(request, runtime)

    def pop_list_object_case_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListObjectCase',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListObjectCaseResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_object_case(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_object_case_with_options(request, runtime)

    def pop_list_object_generation_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListObjectGenerationProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListObjectGenerationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_object_generation_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_object_generation_project_with_options(request, runtime)

    def pop_list_object_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audit_status):
            body['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.custom_source):
            body['CustomSource'] = request.custom_source
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.with_source):
            body['WithSource'] = request.with_source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListObjectProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListObjectProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_object_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_object_project_with_options(request, runtime)

    def pop_list_pak_render_expression_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_status):
            query['ListStatus'] = request.list_status
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListPakRenderExpression',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListPakRenderExpressionResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_pak_render_expression(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_pak_render_expression_with_options(request, runtime)

    def pop_list_text_to_avatar_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopListTextToAvatarProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopListTextToAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_list_text_to_avatar_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_list_text_to_avatar_project_with_options(request, runtime)

    def pop_object_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopObjectProjectDetail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopObjectProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_object_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_object_project_detail_with_options(request, runtime)

    def pop_object_retrieval_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopObjectRetrieval',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopObjectRetrievalResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_object_retrieval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_object_retrieval_with_options(request, runtime)

    def pop_object_retrieval_upload_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopObjectRetrievalUploadData',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopObjectRetrievalUploadDataResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_object_retrieval_upload_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_object_retrieval_upload_data_with_options(request, runtime)

    def pop_query_avatar_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopQueryAvatarProjectDetail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopQueryAvatarProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_query_avatar_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_query_avatar_project_detail_with_options(request, runtime)

    def pop_query_latest_avatar_project_detail_by_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopQueryLatestAvatarProjectDetailByUser',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopQueryLatestAvatarProjectDetailByUserResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_query_latest_avatar_project_detail_by_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_query_latest_avatar_project_detail_by_user_with_options(request, runtime)

    def pop_query_live_portrait_model_scope_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopQueryLivePortraitModelScopeProjectDetail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopQueryLivePortraitModelScopeProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_query_live_portrait_model_scope_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_query_live_portrait_model_scope_project_detail_with_options(request, runtime)

    def pop_query_object_generation_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopQueryObjectGenerationProjectDetail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopQueryObjectGenerationProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_query_object_generation_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_query_object_generation_project_detail_with_options(request, runtime)

    def pop_retry_aitry_on_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopRetryAITryOnTask',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopRetryAITryOnTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_retry_aitry_on_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_retry_aitry_on_task_with_options(request, runtime)

    def pop_submit_aitry_on_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bottoms_id):
            query['BottomsId'] = request.bottoms_id
        if not UtilClient.is_unset(request.clothing_type):
            query['ClothingType'] = request.clothing_type
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.shoe_type):
            query['ShoeType'] = request.shoe_type
        if not UtilClient.is_unset(request.suit_id):
            query['SuitId'] = request.suit_id
        if not UtilClient.is_unset(request.tops_id):
            query['TopsId'] = request.tops_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopSubmitAITryOnJob',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopSubmitAITryOnJobResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_submit_aitry_on_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_submit_aitry_on_job_with_options(request, runtime)

    def pop_upload_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PopUploadMaterial',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopUploadMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_upload_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_upload_material_with_options(request, runtime)

    def pop_video_save_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PopVideoSaveSource',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.PopVideoSaveSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def pop_video_save_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pop_video_save_source_with_options(request, runtime)

    def query_digital_human_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDigitalHumanProject',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.QueryDigitalHumanProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def query_digital_human_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_digital_human_project_with_options(request, runtime)

    def query_long_tts_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLongTtsResult',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.QueryLongTtsResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_long_tts_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_long_tts_result_with_options(request, runtime)

    def submit_long_tts_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.jwt_token):
            query['JwtToken'] = request.jwt_token
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.tts_voice_id):
            body['TtsVoiceId'] = request.tts_voice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLongTtsTask',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.SubmitLongTtsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_long_tts_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_long_tts_task_with_options(request, runtime)

    def update_user_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.jwt_token):
            body['JwtToken'] = request.jwt_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserEmail',
            version='2023-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xr_engine_20230313_models.UpdateUserEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_email_with_options(request, runtime)
