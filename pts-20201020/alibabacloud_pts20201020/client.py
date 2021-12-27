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

    def create_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneResponse(),
            self.do_rpcrequest('CreatePtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pts_scene_with_options(request, runtime)

    def create_pts_scene_base_line_from_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.CreatePtsSceneBaseLineFromReportResponse(),
            self.do_rpcrequest('CreatePtsSceneBaseLineFromReport', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pts_scene_base_line_from_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pts_scene_base_line_from_report_with_options(request, runtime)

    def delete_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneResponse(),
            self.do_rpcrequest('DeletePtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scene_with_options(request, runtime)

    def delete_pts_scene_base_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsSceneBaseLineResponse(),
            self.do_rpcrequest('DeletePtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.DeletePtsScenesResponse(),
            self.do_rpcrequest('DeletePtsScenes', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pts_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pts_scenes_with_options(request, runtime)

    def get_jmeter_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterLogsResponse(),
            self.do_rpcrequest('GetJMeterLogs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_logs_with_options(request, runtime)

    def get_jmeter_sample_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSampleMetricsResponse(),
            self.do_rpcrequest('GetJMeterSampleMetrics', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_sample_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_sample_metrics_with_options(request, runtime)

    def get_jmeter_sampling_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSamplingLogsResponse(),
            self.do_rpcrequest('GetJMeterSamplingLogs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_sampling_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_sampling_logs_with_options(request, runtime)

    def get_jmeter_scene_running_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetJMeterSceneRunningDataResponse(),
            self.do_rpcrequest('GetJMeterSceneRunningData', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_jmeter_scene_running_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_jmeter_scene_running_data_with_options(request, runtime)

    def get_open_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetOpenJMeterSceneResponse(),
            self.do_rpcrequest('GetOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_open_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_open_jmeter_scene_with_options(request, runtime)

    def get_pts_report_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportDetailsResponse(),
            self.do_rpcrequest('GetPtsReportDetails', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_report_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_report_details_with_options(request, runtime)

    def get_pts_reports_by_scene_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsReportsBySceneIdResponse(),
            self.do_rpcrequest('GetPtsReportsBySceneId', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_reports_by_scene_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_reports_by_scene_id_with_options(request, runtime)

    def get_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneResponse(),
            self.do_rpcrequest('GetPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_with_options(request, runtime)

    def get_pts_scene_base_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneBaseLineResponse(),
            self.do_rpcrequest('GetPtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene_base_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_base_line_with_options(request, runtime)

    def get_pts_scene_running_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningDataResponse(),
            self.do_rpcrequest('GetPtsSceneRunningData', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene_running_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_running_data_with_options(request, runtime)

    def get_pts_scene_running_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.GetPtsSceneRunningStatusResponse(),
            self.do_rpcrequest('GetPtsSceneRunningStatus', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pts_scene_running_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pts_scene_running_status_with_options(request, runtime)

    def list_envs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListEnvsResponse(),
            self.do_rpcrequest('ListEnvs', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_envs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_envs_with_options(request, runtime)

    def list_jmeter_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListJMeterReportsResponse(),
            self.do_rpcrequest('ListJMeterReports', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jmeter_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jmeter_reports_with_options(request, runtime)

    def list_open_jmeter_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListOpenJMeterScenesResponse(),
            self.do_rpcrequest('ListOpenJMeterScenes', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_open_jmeter_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_open_jmeter_scenes_with_options(request, runtime)

    def list_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ListPtsSceneResponse(),
            self.do_rpcrequest('ListPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pts_scene_with_options(request, runtime)

    def modify_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.ModifyPtsSceneResponse(),
            self.do_rpcrequest('ModifyPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_pts_scene_with_options(request, runtime)

    def remove_env_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveEnvResponse(),
            self.do_rpcrequest('RemoveEnv', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_env(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_env_with_options(request, runtime)

    def remove_open_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.RemoveOpenJMeterSceneResponse(),
            self.do_rpcrequest('RemoveOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_open_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_open_jmeter_scene_with_options(request, runtime)

    def save_env_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveEnvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.env):
            request.env_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.env), 'Env', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.SaveEnvResponse(),
            self.do_rpcrequest('SaveEnv', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_env(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_env_with_options(request, runtime)

    def save_open_jmeter_scene_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = pts20201020_models.SaveOpenJMeterSceneShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.open_jmeter_scene):
            request.open_jmeter_scene_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.open_jmeter_scene), 'OpenJMeterScene', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.SaveOpenJMeterSceneResponse(),
            self.do_rpcrequest('SaveOpenJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_open_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_open_jmeter_scene_with_options(request, runtime)

    def start_debug_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebugPtsSceneResponse(),
            self.do_rpcrequest('StartDebugPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_debug_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_debug_pts_scene_with_options(request, runtime)

    def start_debugging_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartDebuggingJMeterSceneResponse(),
            self.do_rpcrequest('StartDebuggingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_debugging_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_debugging_jmeter_scene_with_options(request, runtime)

    def start_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartPtsSceneResponse(),
            self.do_rpcrequest('StartPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_pts_scene_with_options(request, runtime)

    def start_testing_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StartTestingJMeterSceneResponse(),
            self.do_rpcrequest('StartTestingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_testing_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_testing_jmeter_scene_with_options(request, runtime)

    def stop_debug_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebugPtsSceneResponse(),
            self.do_rpcrequest('StopDebugPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_debug_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_debug_pts_scene_with_options(request, runtime)

    def stop_debugging_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopDebuggingJMeterSceneResponse(),
            self.do_rpcrequest('StopDebuggingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_debugging_jmeter_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_debugging_jmeter_scene_with_options(request, runtime)

    def stop_pts_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopPtsSceneResponse(),
            self.do_rpcrequest('StopPtsScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_pts_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_pts_scene_with_options(request, runtime)

    def stop_testing_jmeter_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.StopTestingJMeterSceneResponse(),
            self.do_rpcrequest('StopTestingJMeterScene', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            pts20201020_models.UpdatePtsSceneBaseLineResponse(),
            self.do_rpcrequest('UpdatePtsSceneBaseLine', '2020-10-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_pts_scene_base_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_pts_scene_base_line_with_options(request, runtime)
