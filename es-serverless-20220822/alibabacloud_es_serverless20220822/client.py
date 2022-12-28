# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_es_serverless20220822 import models as es_serverless_20220822_models
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
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(request, headers, runtime)

    def create_data_stream_with_options(self, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_stream_name):
            body['dataStreamName'] = request.data_stream_name
        if not UtilClient.is_unset(request.delete_phase):
            body['deletePhase'] = request.delete_phase
        if not UtilClient.is_unset(request.dynamic):
            body['dynamic'] = request.dynamic
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.time_stamp_key):
            body['timeStampKey'] = request.time_stamp_key
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataStream',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s/data-streams' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.CreateDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_stream(self, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_stream_with_options(app_name, request, headers, runtime)

    def delete_access_token_with_options(self, token_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAccessToken',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/tokens/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.DeleteAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_token(self, token_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_access_token_with_options(token_id, headers, runtime)

    def delete_app_with_options(self, app_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, app_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_with_options(app_name, headers, runtime)

    def delete_data_stream_with_options(self, app_name, data_stream_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataStream',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s/data-streams/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_stream_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.DeleteDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_stream(self, app_name, data_stream_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_stream_with_options(app_name, data_stream_name, headers, runtime)

    def descibe_regions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescibeRegions',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.DescibeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def descibe_regions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.descibe_regions_with_options(headers, runtime)

    def disable_access_token_with_options(self, token_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DisableAccessToken',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/tokens/%s/actions/disable' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.DisableAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_access_token(self, token_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_access_token_with_options(token_id, headers, runtime)

    def enable_access_token_with_options(self, token_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableAccessToken',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/tokens/%s/actions/enable' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(token_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.EnableAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_access_token(self, token_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_access_token_with_options(token_id, headers, runtime)

    def generate_acccess_token_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GenerateAcccessToken',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/tokens',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.GenerateAcccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_acccess_token(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_acccess_token_with_options(headers, runtime)

    def get_app_with_options(self, app_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app(self, app_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_with_options(app_name, headers, runtime)

    def get_data_stream_with_options(self, app_name, data_stream_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataStream',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s/data-streams/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_stream_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.GetDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_stream(self, app_name, data_stream_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_stream_with_options(app_name, data_stream_name, headers, runtime)

    def get_region_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegionInfo',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/regions/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.GetRegionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_region_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_info_with_options(headers, runtime)

    def list_access_tokens_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token_id):
            query['tokenId'] = request.token_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessTokens',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.ListAccessTokensResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_tokens(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_access_tokens_with_options(request, headers, runtime)

    def list_apps_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['appName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(request, headers, runtime)

    def list_data_streams_with_options(self, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_stream_name):
            query['dataStreamName'] = request.data_stream_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataStreams',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s/data-streams' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.ListDataStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_streams(self, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_streams_with_options(app_name, request, headers, runtime)

    def update_app_with_options(self, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app(self, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_with_options(app_name, request, headers, runtime)

    def update_data_stream_with_options(self, data_stream_name, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.delete_phase):
            body['deletePhase'] = request.delete_phase
        if not UtilClient.is_unset(request.dynamic):
            body['dynamic'] = request.dynamic
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.time_stamp_key):
            body['timeStampKey'] = request.time_stamp_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataStream',
            version='2022-08-22',
            protocol='HTTPS',
            pathname='/openapi/xops/instances/%s/data-streams/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_stream_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20220822_models.UpdateDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_stream(self, data_stream_name, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_data_stream_with_options(data_stream_name, app_name, request, headers, runtime)
