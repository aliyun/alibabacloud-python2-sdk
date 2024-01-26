# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pts20181111 import models as pts20181111_models
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

    def get_report_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetReportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetReportResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReport',
            version='2018-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20181111_models.GetReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_report(self, request):
        """
        @deprecated
        

        @param request: GetReportRequest

        @return: GetReportResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_report_with_options(request, runtime)

    def list_runnable_scenes_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListRunnableScenesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRunnableScenesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRunnableScenes',
            version='2018-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20181111_models.ListRunnableScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_runnable_scenes(self, request):
        """
        @deprecated
        

        @param request: ListRunnableScenesRequest

        @return: ListRunnableScenesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_runnable_scenes_with_options(request, runtime)

    def query_plan_status_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: QueryPlanStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryPlanStatusResponse
        Deprecated
        """
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
            action='QueryPlanStatus',
            version='2018-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20181111_models.QueryPlanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_plan_status(self, request):
        """
        @deprecated
        

        @param request: QueryPlanStatusRequest

        @return: QueryPlanStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.query_plan_status_with_options(request, runtime)

    def start_scene_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: StartSceneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartSceneResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartScene',
            version='2018-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20181111_models.StartSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def start_scene(self, request):
        """
        @deprecated
        

        @param request: StartSceneRequest

        @return: StartSceneResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.start_scene_with_options(request, runtime)

    def stop_scene_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: StopSceneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopSceneResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopScene',
            version='2018-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20181111_models.StopSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_scene(self, request):
        """
        @deprecated
        

        @param request: StopSceneRequest

        @return: StopSceneResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_scene_with_options(request, runtime)
