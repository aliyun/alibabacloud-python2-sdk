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

    def get_single_conn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSingleConnDataResponse(),
            self.do_rpcrequest('GetSingleConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_single_conn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_single_conn_data_with_options(request, runtime)

    def get_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetTaskStatusResponse(),
            self.do_rpcrequest('GetTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    def link_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LinkImageResponse(),
            self.do_rpcrequest('LinkImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def link_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.link_image_with_options(request, runtime)

    def add_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSceneResponse(),
            self.do_rpcrequest('AddScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_scene_with_options(request, runtime)

    def update_conn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateConnDataResponse(),
            self.do_rpcrequest('UpdateConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_conn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_conn_data_with_options(request, runtime)

    def rectify_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectifyImageResponse(),
            self.do_rpcrequest('RectifyImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rectify_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rectify_image_with_options(request, runtime)

    def label_build_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.LabelBuildResponse(),
            self.do_rpcrequest('LabelBuild', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def label_build(self, request):
        runtime = util_models.RuntimeOptions()
        return self.label_build_with_options(request, runtime)

    def drop_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSceneResponse(),
            self.do_rpcrequest('DropScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_scene_with_options(request, runtime)

    def optimize_right_angle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.OptimizeRightAngleResponse(),
            self.do_rpcrequest('OptimizeRightAngle', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def optimize_right_angle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.optimize_right_angle_with_options(request, runtime)

    def add_relative_position_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddRelativePositionResponse(),
            self.do_rpcrequest('AddRelativePosition', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_relative_position(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_relative_position_with_options(request, runtime)

    def detail_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSceneResponse(),
            self.do_rpcrequest('DetailScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detail_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detail_scene_with_options(request, runtime)

    def create_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CreateSceneResponse(),
            self.do_rpcrequest('CreateScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_with_options(request, runtime)

    def delete_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DeleteFileResponse(),
            self.do_rpcrequest('DeleteFile', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    def check_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CheckResourceResponse(),
            self.do_rpcrequest('CheckResource', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_resource_with_options(request, runtime)

    def list_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSceneResponse(),
            self.do_rpcrequest('ListScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scene_with_options(request, runtime)

    def publish_hotspot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PublishHotspotResponse(),
            self.do_rpcrequest('PublishHotspot', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_hotspot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_hotspot_with_options(request, runtime)

    def update_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSceneResponse(),
            self.do_rpcrequest('UpdateScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    def update_layout_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateLayoutDataResponse(),
            self.do_rpcrequest('UpdateLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_layout_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_layout_data_with_options(request, runtime)

    def save_hotspot_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotTagResponse(),
            self.do_rpcrequest('SaveHotspotTag', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_hotspot_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_tag_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DeleteProjectResponse(),
            self.do_rpcrequest('DeleteProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def rect_vertical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.RectVerticalResponse(),
            self.do_rpcrequest('RectVertical', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rect_vertical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rect_vertical_with_options(request, runtime)

    def pred_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredImageResponse(),
            self.do_rpcrequest('PredImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pred_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pred_image_with_options(request, runtime)

    def get_oss_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOssPolicyResponse(),
            self.do_rpcrequest('GetOssPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_oss_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    def get_conn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetConnDataResponse(),
            self.do_rpcrequest('GetConnData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conn_data_with_options(request, runtime)

    def temp_preview_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewStatusResponse(),
            self.do_rpcrequest('TempPreviewStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def temp_preview_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_status_with_options(request, runtime)

    def add_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddProjectResponse(),
            self.do_rpcrequest('AddProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_project_with_options(request, runtime)

    def detail_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailSubSceneResponse(),
            self.do_rpcrequest('DetailSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detail_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detail_sub_scene_with_options(request, runtime)

    def list_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListSubSceneResponse(),
            self.do_rpcrequest('ListSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sub_scene_with_options(request, runtime)

    def update_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateSubSceneResponse(),
            self.do_rpcrequest('UpdateSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sub_scene_with_options(request, runtime)

    def get_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetJobResponse(),
            self.do_rpcrequest('GetJob', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def save_hotspot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.SaveHotspotConfigResponse(),
            self.do_rpcrequest('SaveHotspotConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_hotspot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_hotspot_config_with_options(request, runtime)

    def get_window_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetWindowConfigResponse(),
            self.do_rpcrequest('GetWindowConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_window_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_window_config_with_options(request, runtime)

    def get_hotspot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotConfigResponse(),
            self.do_rpcrequest('GetHotspotConfig', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotspot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_config_with_options(request, runtime)

    def get_scene_build_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSceneBuildTaskStatusResponse(),
            self.do_rpcrequest('GetSceneBuildTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_scene_build_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_build_task_status_with_options(request, runtime)

    def temp_preview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.TempPreviewResponse(),
            self.do_rpcrequest('TempPreview', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def temp_preview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.temp_preview_with_options(request, runtime)

    def detail_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DetailProjectResponse(),
            self.do_rpcrequest('DetailProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detail_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detail_project_with_options(request, runtime)

    def list_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListScenesResponse(),
            self.do_rpcrequest('ListScenes', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scenes_with_options(request, runtime)

    def drop_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropSubSceneResponse(),
            self.do_rpcrequest('DropSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_sub_scene_with_options(request, runtime)

    def get_hotspot_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotTagResponse(),
            self.do_rpcrequest('GetHotspotTag', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotspot_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_tag_with_options(request, runtime)

    def drop_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.DropProjectResponse(),
            self.do_rpcrequest('DropProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_project_with_options(request, runtime)

    def list_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ListProjectResponse(),
            self.do_rpcrequest('ListProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_with_options(request, runtime)

    def get_origin_layout_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetOriginLayoutDataResponse(),
            self.do_rpcrequest('GetOriginLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_origin_layout_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_origin_layout_data_with_options(request, runtime)

    def get_hotspot_scene_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetHotspotSceneDataResponse(),
            self.do_rpcrequest('GetHotspotSceneData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotspot_scene_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotspot_scene_data_with_options(request, runtime)

    def scene_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.ScenePublishResponse(),
            self.do_rpcrequest('ScenePublish', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def scene_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scene_publish_with_options(request, runtime)

    def get_rectify_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetRectifyImageResponse(),
            self.do_rpcrequest('GetRectifyImage', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rectify_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rectify_image_with_options(request, runtime)

    def update_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def get_sub_scene_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetSubSceneTaskStatusResponse(),
            self.do_rpcrequest('GetSubSceneTaskStatus', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sub_scene_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sub_scene_task_status_with_options(request, runtime)

    def prediction_wall_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.PredictionWallLineResponse(),
            self.do_rpcrequest('PredictionWallLine', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def prediction_wall_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.prediction_wall_line_with_options(request, runtime)

    def get_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetPolicyResponse(),
            self.do_rpcrequest('GetPolicy', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    def get_scene_preview_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetScenePreviewInfoResponse(),
            self.do_rpcrequest('GetScenePreviewInfo', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_scene_preview_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_preview_info_with_options(request, runtime)

    def add_sub_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.AddSubSceneResponse(),
            self.do_rpcrequest('AddSubScene', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sub_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_sub_scene_with_options(request, runtime)

    def get_layout_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            tdsr_20200101_models.GetLayoutDataResponse(),
            self.do_rpcrequest('GetLayoutData', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_layout_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_layout_data_with_options(request, runtime)
