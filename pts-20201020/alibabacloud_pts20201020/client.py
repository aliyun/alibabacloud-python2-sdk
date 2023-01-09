# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pts20201020 import models as pts20201020_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('pts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def adjust_jmeter_scene_speed_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AdjustJMeterSceneSpeed',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.AdjustJMeterSceneSpeedResponse(),
            self.call_api(params, req, runtime)
        )

    def adjust_jmeter_scene_speed(self, request):
        runtime = util_models.RuntimeOptions()
        return self.adjust_jmeter_scene_speed_with_options(request, runtime)

    def create_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pts_scene_with_options(request, runtime)

    def create_pts_scene_base_line_from_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePtsSceneBaseLineFromReport',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneBaseLineFromReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pts_scene_base_line_from_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pts_scene_base_line_from_report_with_options(request, runtime)

    def delete_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scene_with_options(request, runtime)

    def delete_pts_scene_base_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePtsSceneBaseLine',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneBaseLineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pts_scene_base_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scene_base_line_with_options(request, runtime)

    def delete_pts_scenes_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.DeletePtsScenesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene_ids):
            request.scene_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_ids, 'SceneIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.scene_ids_shrink):
            query['SceneIds'] = request.scene_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePtsScenes',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pts_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scenes_with_options(request, runtime)

    def get_all_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAllRegions',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetAllRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.get_all_regions_with_options(runtime)

    def get_jmeter_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_index):
            query['AgentIndex'] = request.agent_index
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.thread):
            query['Thread'] = request.thread
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJMeterLogs',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_jmeter_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_logs_with_options(request, runtime)

    def get_jmeter_sample_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.sampler_id):
            query['SamplerId'] = request.sampler_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJMeterSampleMetrics',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSampleMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_jmeter_sample_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_sample_metrics_with_options(request, runtime)

    def get_jmeter_sampling_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_rt):
            query['MaxRT'] = request.max_rt
        if not UtilClient.is_unset(request.min_rt):
            query['MinRT'] = request.min_rt
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.response_code):
            query['ResponseCode'] = request.response_code
        if not UtilClient.is_unset(request.sampler_id):
            query['SamplerId'] = request.sampler_id
        if not UtilClient.is_unset(request.success):
            query['Success'] = request.success
        if not UtilClient.is_unset(request.thread):
            query['Thread'] = request.thread
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJMeterSamplingLogs',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSamplingLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_jmeter_sampling_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_sampling_logs_with_options(request, runtime)

    def get_jmeter_scene_running_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJMeterSceneRunningData',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSceneRunningDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_jmeter_scene_running_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_scene_running_data_with_options(request, runtime)

    def get_open_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpenJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetOpenJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def get_open_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_open_jmeter_scene_with_options(request, runtime)

    def get_pts_report_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPtsReportDetails',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pts_report_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_report_details_with_options(request, runtime)

    def get_pts_reports_by_scene_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPtsReportsBySceneId',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportsBySceneIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pts_reports_by_scene_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_reports_by_scene_id_with_options(request, runtime)

    def get_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_with_options(request, runtime)

    def get_pts_scene_base_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPtsSceneBaseLine',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneBaseLineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pts_scene_base_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_base_line_with_options(request, runtime)

    def get_pts_scene_running_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPtsSceneRunningData',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pts_scene_running_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_running_data_with_options(request, runtime)

    def get_pts_scene_running_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPtsSceneRunningStatus',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pts_scene_running_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_running_status_with_options(request, runtime)

    def get_user_vpc_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserVpcSecurityGroup',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetUserVpcSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_vpc_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_vpc_security_group_with_options(request, runtime)

    def get_user_vpc_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserVpcVSwitch',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetUserVpcVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_vpc_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_vpc_vswitch_with_options(request, runtime)

    def get_user_vpcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserVpcs',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.GetUserVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_vpcs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_vpcs_with_options(request, runtime)

    def list_envs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.env_name):
            query['EnvName'] = request.env_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvs',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.ListEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_envs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_envs_with_options(request, runtime)

    def list_jmeter_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJMeterReports',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.ListJMeterReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jmeter_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jmeter_reports_with_options(request, runtime)

    def list_open_jmeter_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOpenJMeterScenes',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.ListOpenJMeterScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_open_jmeter_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_open_jmeter_scenes_with_options(request, runtime)

    def list_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.ListPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pts_scene_with_options(request, runtime)

    def modify_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.ModifyPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_pts_scene_with_options(request, runtime)

    def remove_env_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEnv',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveEnvResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_env(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_env_with_options(request, runtime)

    def remove_open_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveOpenJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveOpenJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_open_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_open_jmeter_scene_with_options(request, runtime)

    def save_env_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveEnvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env):
            request.env_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.env, 'Env', 'json')
        query = {}
        if not UtilClient.is_unset(request.env_shrink):
            query['Env'] = request.env_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveEnv',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.SaveEnvResponse(),
            self.call_api(params, req, runtime)
        )

    def save_env(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_env_with_options(request, runtime)

    def save_open_jmeter_scene_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveOpenJMeterSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.open_jmeter_scene):
            request.open_jmeter_scene_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_jmeter_scene, 'OpenJMeterScene', 'json')
        query = {}
        if not UtilClient.is_unset(request.open_jmeter_scene_shrink):
            query['OpenJMeterScene'] = request.open_jmeter_scene_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveOpenJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.SaveOpenJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def save_open_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_open_jmeter_scene_with_options(request, runtime)

    def save_pts_scene_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SavePtsSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scene):
            request.scene_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene, 'Scene', 'json')
        query = {}
        if not UtilClient.is_unset(request.scene_shrink):
            query['Scene'] = request.scene_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SavePtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.SavePtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def save_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_pts_scene_with_options(request, runtime)

    def start_debug_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDebugPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebugPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def start_debug_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_debug_pts_scene_with_options(request, runtime)

    def start_debugging_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDebuggingJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebuggingJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def start_debugging_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_debugging_jmeter_scene_with_options(request, runtime)

    def start_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StartPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def start_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_pts_scene_with_options(request, runtime)

    def start_testing_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTestingJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StartTestingJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def start_testing_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_testing_jmeter_scene_with_options(request, runtime)

    def stop_debug_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDebugPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebugPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_debug_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_debug_pts_scene_with_options(request, runtime)

    def stop_debugging_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDebuggingJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebuggingJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_debugging_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_debugging_jmeter_scene_with_options(request, runtime)

    def stop_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPtsScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StopPtsSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_pts_scene_with_options(request, runtime)

    def stop_testing_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTestingJMeterScene',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.StopTestingJMeterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_testing_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_testing_jmeter_scene_with_options(request, runtime)

    def update_pts_scene_base_line_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.UpdatePtsSceneBaseLineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_baselines):
            request.api_baselines_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_baselines, 'ApiBaselines', 'json')
        if not UtilClient.is_unset(tmp_req.scene_baseline):
            request.scene_baseline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scene_baseline, 'SceneBaseline', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_baselines_shrink):
            query['ApiBaselines'] = request.api_baselines_shrink
        if not UtilClient.is_unset(request.scene_baseline_shrink):
            query['SceneBaseline'] = request.scene_baseline_shrink
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePtsSceneBaseLine',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20201020_models.UpdatePtsSceneBaseLineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pts_scene_base_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_pts_scene_base_line_with_options(request, runtime)
