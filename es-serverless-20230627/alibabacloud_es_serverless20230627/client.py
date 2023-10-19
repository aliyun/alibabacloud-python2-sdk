# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_es_serverless20230627 import models as es_serverless_20230627_models
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
        self._endpoint = self.get_endpoint('es-serverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_app_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.quota_info):
            body['quotaInfo'] = request.quota_info
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(request, headers, runtime)

    def delete_app_with_options(self, app_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, app_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_with_options(app_name, headers, runtime)

    def get_app_with_options(self, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detailed):
            query['detailed'] = request.detailed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app(self, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_with_options(app_name, request, headers, runtime)

    def get_app_quota_with_options(self, app_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppQuota',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/instances/%s/quota' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetAppQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_quota(self, app_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_quota_with_options(app_name, headers, runtime)

    def get_monitor_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetMonitorData',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/emon/metrics/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_monitor_data_with_options(request, headers, runtime)

    def list_apps_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['appName'] = request.app_name
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(request, headers, runtime)

    def update_app_with_options(self, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname='/openapi/es-serverless/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app(self, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_with_options(app_name, request, headers, runtime)
