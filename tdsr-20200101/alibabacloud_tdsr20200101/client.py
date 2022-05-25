# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tdsr20200101 import models as tdsr_20200101_models
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
            'cn-hangzhou': 'lyj.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('tdsr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_mosaics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mark_position):
            query['MarkPosition'] = request.mark_position
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMosaics',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddMosaicsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_mosaics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mosaics_with_options(request, runtime)

    def add_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def add_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_project_with_options(request, runtime)

    def add_relative_position_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relative_position):
            query['RelativePosition'] = request.relative_position
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRelativePosition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRelativePositionResponse(),
            self.call_api(params, req, runtime)
        )

    def add_relative_position(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_relative_position_with_options(request, runtime)

    def add_room_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRoomPlan',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRoomPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def add_room_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_room_plan_with_options(request, runtime)

    def add_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def add_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_scene_with_options(request, runtime)

    def add_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def add_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_sub_scene_with_options(request, runtime)

    def check_user_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserProperty',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CheckUserPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def check_user_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_user_property_with_options(request, runtime)

    def copy_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CopySceneResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_scene_with_options(request, runtime)

    def detail_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def detail_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detail_project_with_options(request, runtime)

    def detail_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def detail_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detail_scene_with_options(request, runtime)

    def detail_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def detail_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detail_sub_scene_with_options(request, runtime)

    def drop_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def drop_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_project_with_options(request, runtime)

    def drop_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def drop_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_scene_with_options(request, runtime)

    def drop_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DropSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def drop_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_sub_scene_with_options(request, runtime)

    def get_conn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_conn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conn_data_with_options(request, runtime)

    def get_copy_scene_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCopySceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetCopySceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_copy_scene_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_copy_scene_task_status_with_options(request, runtime)

    def get_hotspot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotspot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_config_with_options(request, runtime)

    def get_hotspot_scene_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotSceneData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotSceneDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotspot_scene_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_scene_data_with_options(request, runtime)

    def get_hotspot_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHotspotTag',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hotspot_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_tag_with_options(request, runtime)

    def get_layout_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_layout_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_layout_data_with_options(request, runtime)

    def get_origin_layout_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOriginLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOriginLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_origin_layout_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_origin_layout_data_with_options(request, runtime)

    def get_oss_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssPolicy',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oss_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    def get_pack_scene_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackSceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetPackSceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pack_scene_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pack_scene_task_status_with_options(request, runtime)

    def get_rectify_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRectifyImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetRectifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rectify_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rectify_image_with_options(request, runtime)

    def get_scene_build_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneBuildTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSceneBuildTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_build_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_build_task_status_with_options(request, runtime)

    def get_scene_pack_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePackUrl',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePackUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_pack_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_pack_url_with_options(request, runtime)

    def get_scene_preview_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        if not UtilClient.is_unset(request.show_tag):
            query['ShowTag'] = request.show_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_preview_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_data_with_options(request, runtime)

    def get_scene_preview_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_preview_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_info_with_options(request, runtime)

    def get_scene_preview_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenePreviewResource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_preview_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_resource_with_options(request, runtime)

    def get_single_conn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSingleConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSingleConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_single_conn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_single_conn_data_with_options(request, runtime)

    def get_source_pack_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSourcePackStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSourcePackStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_source_pack_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_source_pack_status_with_options(request, runtime)

    def get_sub_scene_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubSceneTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSubSceneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sub_scene_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sub_scene_task_status_with_options(request, runtime)

    def get_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    def get_window_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWindowConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetWindowConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_window_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_window_config_with_options(request, runtime)

    def label_build_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.model_style):
            query['ModelStyle'] = request.model_style
        if not UtilClient.is_unset(request.optimize_wall_width):
            query['OptimizeWallWidth'] = request.optimize_wall_width
        if not UtilClient.is_unset(request.plan_style):
            query['PlanStyle'] = request.plan_style
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.wall_height):
            query['WallHeight'] = request.wall_height
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LabelBuild',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LabelBuildResponse(),
            self.call_api(params, req, runtime)
        )

    def label_build(self, request):
        runtime = util_models.RuntimeOptions()
        return self.label_build_with_options(request, runtime)

    def link_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LinkImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LinkImageResponse(),
            self.call_api(params, req, runtime)
        )

    def link_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.link_image_with_options(request, runtime)

    def list_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    def list_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scene_with_options(request, runtime)

    def list_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.show_layout_data):
            query['ShowLayoutData'] = request.show_layout_data
        if not UtilClient.is_unset(request.sort_field):
            query['SortField'] = request.sort_field
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sub_scene_with_options(request, runtime)

    def optimize_right_angle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OptimizeRightAngle',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.OptimizeRightAngleResponse(),
            self.call_api(params, req, runtime)
        )

    def optimize_right_angle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.optimize_right_angle_with_options(request, runtime)

    def pack_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PackScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PackSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def pack_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pack_scene_with_options(request, runtime)

    def pack_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PackSource',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PackSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def pack_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pack_source_with_options(request, runtime)

    def pred_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.correct_vertical):
            query['CorrectVertical'] = request.correct_vertical
        if not UtilClient.is_unset(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not UtilClient.is_unset(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredImageResponse(),
            self.call_api(params, req, runtime)
        )

    def pred_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pred_image_with_options(request, runtime)

    def prediction_wall_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictionWallLine',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredictionWallLineResponse(),
            self.call_api(params, req, runtime)
        )

    def prediction_wall_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.prediction_wall_line_with_options(request, runtime)

    def publish_hotspot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishHotspot',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishHotspotResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_hotspot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_hotspot_with_options(request, runtime)

    def publish_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_scene_with_options(request, runtime)

    def publish_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_status_with_options(request, runtime)

    def recovery_origin_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryOriginImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RecoveryOriginImageResponse(),
            self.call_api(params, req, runtime)
        )

    def recovery_origin_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recovery_origin_image_with_options(request, runtime)

    def rect_vertical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count_detect_door):
            query['CountDetectDoor'] = request.count_detect_door
        if not UtilClient.is_unset(request.detect_door):
            query['DetectDoor'] = request.detect_door
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        if not UtilClient.is_unset(request.vertical_rect):
            query['VerticalRect'] = request.vertical_rect
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RectVertical',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectVerticalResponse(),
            self.call_api(params, req, runtime)
        )

    def rect_vertical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rect_vertical_with_options(request, runtime)

    def rectify_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.camera_height):
            query['CameraHeight'] = request.camera_height
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RectifyImage',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    def rectify_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rectify_image_with_options(request, runtime)

    def rollback_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RollbackSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_sub_scene_with_options(request, runtime)

    def save_hotspot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.preview_token):
            query['PreviewToken'] = request.preview_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveHotspotConfig',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_hotspot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_config_with_options(request, runtime)

    def save_hotspot_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_tag):
            query['ParamTag'] = request.param_tag
        if not UtilClient.is_unset(request.sub_scene_uuid):
            query['SubSceneUuid'] = request.sub_scene_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveHotspotTag',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotTagResponse(),
            self.call_api(params, req, runtime)
        )

    def save_hotspot_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_tag_with_options(request, runtime)

    def scene_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScenePublish',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ScenePublishResponse(),
            self.call_api(params, req, runtime)
        )

    def scene_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scene_publish_with_options(request, runtime)

    def temp_preview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempPreview',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    def temp_preview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_with_options(request, runtime)

    def temp_preview_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempPreviewStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def temp_preview_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_status_with_options(request, runtime)

    def update_conn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conn_data):
            query['ConnData'] = request.conn_data
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConnData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateConnDataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_conn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_conn_data_with_options(request, runtime)

    def update_layout_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.layout_data):
            query['LayoutData'] = request.layout_data
        if not UtilClient.is_unset(request.sub_scene_id):
            query['SubSceneId'] = request.sub_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLayoutData',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateLayoutDataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_layout_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_layout_data_with_options(request, runtime)

    def update_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def update_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    def update_sub_scene_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = tdsr_20200101_models.UpdateSubSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.view_point):
            request.view_point_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.view_point, 'ViewPoint', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.view_point_shrink):
            query['ViewPoint'] = request.view_point_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubScene',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sub_scene_with_options(request, runtime)

    def update_sub_scene_seq_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = tdsr_20200101_models.UpdateSubSceneSeqShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort_sub_scene_ids):
            request.sort_sub_scene_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_sub_scene_ids, 'SortSubSceneIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.sort_sub_scene_ids_shrink):
            query['SortSubSceneIds'] = request.sort_sub_scene_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubSceneSeq',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneSeqResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sub_scene_seq(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sub_scene_seq_with_options(request, runtime)
