# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_pts20190522 import models as pts20190522_models
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

    def get_aliware_report_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetAliwareReportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAliwareReportResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAliwareReport',
            version='2019-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20190522_models.GetAliwareReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aliware_report(self, request):
        """
        @deprecated
        

        @param request: GetAliwareReportRequest

        @return: GetAliwareReportResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_aliware_report_with_options(request, runtime)

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
            version='2019-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20190522_models.GetReportResponse(),
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
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.team_id):
            query['TeamId'] = request.team_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartScene',
            version='2019-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pts20190522_models.StartSceneResponse(),
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
