# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dop20221130 import models as dop_20221130_models
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
        self._endpoint = self.get_endpoint('dop', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_oss_meta_download_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ds):
            query['ds'] = request.ds
        if not UtilClient.is_unset(request.expire):
            query['expire'] = request.expire
        if not UtilClient.is_unset(request.table_name):
            query['tableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssMetaDownload',
            version='2022-11-30',
            protocol='HTTPS',
            pathname='/dop/getOssMetaDownload',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dop_20221130_models.GetOssMetaDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oss_meta_download(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_oss_meta_download_with_options(request, headers, runtime)

    def get_oss_meta_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        if not UtilClient.is_unset(request.table_name):
            query['tableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssMetaList',
            version='2022-11-30',
            protocol='HTTPS',
            pathname='/dop/getOssMetaList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dop_20221130_models.GetOssMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oss_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_oss_meta_list_with_options(request, headers, runtime)

    def submit_backfill_4api_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.package_id):
            query['packageId'] = request.package_id
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBackfill4Api',
            version='2022-11-30',
            protocol='HTTPS',
            pathname='/dop/submitBackfill4Api',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            dop_20221130_models.SubmitBackfill4ApiResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_backfill_4api(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_backfill_4api_with_options(request, headers, runtime)
