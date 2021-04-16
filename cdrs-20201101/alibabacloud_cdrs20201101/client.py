# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdrs20201101 import models as cdrs20201101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdrs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def search_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.SearchObjectResponse(),
            self.do_rpcrequest('SearchObject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_object_with_options(request, runtime)

    def list_area_hot_spot_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListAreaHotSpotMetricsResponse(),
            self.do_rpcrequest('ListAreaHotSpotMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_area_hot_spot_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_area_hot_spot_metrics_with_options(request, runtime)

    def bind_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.BindDeviceResponse(),
            self.do_rpcrequest('BindDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_device_with_options(request, runtime)

    def get_cdrs_monitor_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetCdrsMonitorResultResponse(),
            self.do_rpcrequest('GetCdrsMonitorResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cdrs_monitor_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cdrs_monitor_result_with_options(request, runtime)

    def list_vehicle_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleDetailsResponse(),
            self.do_rpcrequest('ListVehicleDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_details_with_options(request, runtime)

    def get_cdrs_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetCdrsMonitorListResponse(),
            self.do_rpcrequest('GetCdrsMonitorList', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cdrs_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cdrs_monitor_list_with_options(request, runtime)

    def update_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateMonitorResponse(),
            self.do_rpcrequest('UpdateMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_monitor_with_options(request, runtime)

    def list_data_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDataStatisticsResponse(),
            self.do_rpcrequest('ListDataStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_statistics_with_options(request, runtime)

    def unbind_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UnbindDeviceResponse(),
            self.do_rpcrequest('UnbindDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_device_with_options(request, runtime)

    def list_person_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonDetailsResponse(),
            self.do_rpcrequest('ListPersonDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_details_with_options(request, runtime)

    def list_vehicle_tag_distribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTagDistributeResponse(),
            self.do_rpcrequest('ListVehicleTagDistribute', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_tag_distribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_tag_distribute_with_options(request, runtime)

    def list_device_person_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDevicePersonStatisticsResponse(),
            self.do_rpcrequest('ListDevicePersonStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_person_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_person_statistics_with_options(request, runtime)

    def add_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.AddMonitorResponse(),
            self.do_rpcrequest('AddMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_monitor_with_options(request, runtime)

    def paginate_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PaginateDeviceResponse(),
            self.do_rpcrequest('PaginateDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def paginate_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.paginate_device_with_options(request, runtime)

    def stop_cdrs_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.StopCdrsMonitorResponse(),
            self.do_rpcrequest('StopCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_cdrs_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cdrs_monitor_with_options(request, runtime)

    def recall_trajectory_by_coordinate_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecallTrajectoryByCoordinateTimeResponse(),
            self.do_rpcrequest('RecallTrajectoryByCoordinateTime', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recall_trajectory_by_coordinate_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recall_trajectory_by_coordinate_time_with_options(request, runtime)

    def list_city_map_person_flow_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCityMapPersonFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.origin_data_source_id_list):
            request.origin_data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.origin_data_source_id_list, 'OriginDataSourceIdList', 'json')
        if not UtilClient.is_unset(tmp_req.target_data_source_id_list):
            request.target_data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_data_source_id_list, 'TargetDataSourceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapPersonFlowResponse(),
            self.do_rpcrequest('ListCityMapPersonFlow', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_person_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_person_flow_with_options(request, runtime)

    def add_cdrs_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.AddCdrsMonitorResponse(),
            self.do_rpcrequest('AddCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cdrs_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cdrs_monitor_with_options(request, runtime)

    def list_map_route_details_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListMapRouteDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.route_list):
            request.route_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.route_list, 'RouteList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListMapRouteDetailsResponse(),
            self.do_rpcrequest('ListMapRouteDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_map_route_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_map_route_details_with_options(request, runtime)

    def list_person_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTopResponse(),
            self.do_rpcrequest('ListPersonTop', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_top_with_options(request, runtime)

    def get_monitor_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetMonitorResultResponse(),
            self.do_rpcrequest('GetMonitorResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_monitor_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_result_with_options(request, runtime)

    def list_city_map_aois_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapAoisResponse(),
            self.do_rpcrequest('ListCityMapAois', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_aois(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_aois_with_options(request, runtime)

    def recognize_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.RecognizeImageResponse(),
            self.do_rpcrequest('RecognizeImage', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_with_options(request, runtime)

    def get_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.GetMonitorListResponse(),
            self.do_rpcrequest('GetMonitorList', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_list_with_options(request, runtime)

    def list_device_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceRelationResponse(),
            self.do_rpcrequest('ListDeviceRelation', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_relation_with_options(request, runtime)

    def list_person_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTrackResponse(),
            self.do_rpcrequest('ListPersonTrack', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_track_with_options(request, runtime)

    def list_city_map_camera_results_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCityMapCameraResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_id_list):
            request.data_source_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_id_list, 'DataSourceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapCameraResultsResponse(),
            self.do_rpcrequest('ListCityMapCameraResults', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_camera_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_camera_results_with_options(request, runtime)

    def query_trajectory_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.QueryTrajectoryByIdResponse(),
            self.do_rpcrequest('QueryTrajectoryById', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trajectory_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trajectory_by_id_with_options(request, runtime)

    def list_city_map_image_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapImageDetailsResponse(),
            self.do_rpcrequest('ListCityMapImageDetails', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_image_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_image_details_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def list_vehicle_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTopResponse(),
            self.do_rpcrequest('ListVehicleTop', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_top_with_options(request, runtime)

    def list_data_statistics_by_day_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDataStatisticsByDayResponse(),
            self.do_rpcrequest('ListDataStatisticsByDay', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_statistics_by_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_statistics_by_day_with_options(request, runtime)

    def list_vehicle_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleResultsResponse(),
            self.do_rpcrequest('ListVehicleResults', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_results_with_options(request, runtime)

    def search_aggregate_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.SearchAggregateObjectResponse(),
            self.do_rpcrequest('SearchAggregateObject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_aggregate_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_aggregate_object_with_options(request, runtime)

    def list_corp_metrics_statistic_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListCorpMetricsStatisticShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_group_list):
            request.user_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_list, 'UserGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_group_list):
            request.device_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_group_list, 'DeviceGroupList', 'json')
        if not UtilClient.is_unset(tmp_req.device_id_list):
            request.device_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_id_list, 'DeviceIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCorpMetricsStatisticResponse(),
            self.do_rpcrequest('ListCorpMetricsStatistic', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_metrics_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_metrics_statistic_with_options(request, runtime)

    def detect_trajectory_regular_pattern_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.DetectTrajectoryRegularPatternResponse(),
            self.do_rpcrequest('DetectTrajectoryRegularPattern', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_trajectory_regular_pattern(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_trajectory_regular_pattern_with_options(request, runtime)

    def list_vehicle_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListVehicleTrackResponse(),
            self.do_rpcrequest('ListVehicleTrack', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vehicle_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_track_with_options(request, runtime)

    def list_structure_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListStructureStatisticsResponse(),
            self.do_rpcrequest('ListStructureStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_structure_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_structure_statistics_with_options(request, runtime)

    def stop_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.StopMonitorResponse(),
            self.do_rpcrequest('StopMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_monitor_with_options(request, runtime)

    def predict_trajectory_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PredictTrajectoryDestinationResponse(),
            self.do_rpcrequest('PredictTrajectoryDestination', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def predict_trajectory_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_trajectory_destination_with_options(request, runtime)

    def list_range_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListRangeDeviceResponse(),
            self.do_rpcrequest('ListRangeDevice', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_range_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_range_device_with_options(request, runtime)

    def list_city_map_range_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapRangeStatisticResponse(),
            self.do_rpcrequest('ListCityMapRangeStatistic', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_range_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_range_statistic_with_options(request, runtime)

    def list_storage_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListStorageStatisticsResponse(),
            self.do_rpcrequest('ListStorageStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_storage_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_storage_statistics_with_options(request, runtime)

    def paginate_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.PaginateProjectResponse(),
            self.do_rpcrequest('PaginateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def paginate_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.paginate_project_with_options(request, runtime)

    def list_city_map_camera_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListCityMapCameraStatisticsResponse(),
            self.do_rpcrequest('ListCityMapCameraStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_city_map_camera_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_city_map_camera_statistics_with_options(request, runtime)

    def update_cdrs_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateCdrsMonitorResponse(),
            self.do_rpcrequest('UpdateCdrsMonitor', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cdrs_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cdrs_monitor_with_options(request, runtime)

    def list_person_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonResultResponse(),
            self.do_rpcrequest('ListPersonResult', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_result_with_options(request, runtime)

    def list_tag_metrics_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cdrs20201101_models.ListTagMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_code):
            request.tag_code_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_code, 'TagCode', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListTagMetricsResponse(),
            self.do_rpcrequest('ListTagMetrics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_metrics_with_options(request, runtime)

    def list_person_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListPersonTagResponse(),
            self.do_rpcrequest('ListPersonTag', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_tag_with_options(request, runtime)

    def update_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def list_device_person_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDevicePersonResponse(),
            self.do_rpcrequest('ListDevicePerson', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_person(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_person_with_options(request, runtime)

    def list_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceDetailResponse(),
            self.do_rpcrequest('ListDeviceDetail', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_detail_with_options(request, runtime)

    def list_device_gender_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cdrs20201101_models.ListDeviceGenderStatisticsResponse(),
            self.do_rpcrequest('ListDeviceGenderStatistics', '2020-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_gender_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_gender_statistics_with_options(request, runtime)
