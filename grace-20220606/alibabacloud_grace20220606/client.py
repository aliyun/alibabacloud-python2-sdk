# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_grace20220606 import models as grace_20220606_models
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
        self._endpoint = self.get_endpoint('grace', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def analyze_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keep_unreachable_objects):
            query['keepUnreachableObjects'] = request.keep_unreachable_objects
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeFile',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/AnalyzeFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.AnalyzeFileResponse(),
            self.call_api(params, req, runtime)
        )

    def analyze_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.analyze_file_with_options(request, headers, runtime)

    def get_file_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/GetFile',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.GetFileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(request, headers, runtime)

    def upload_file_by_osswith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.display_name):
            query['displayName'] = request.display_name
        if not UtilClient.is_unset(request.endpoint):
            query['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFileByOSS',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/UploadFileByOSS',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.UploadFileByOSSResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_file_by_oss(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_file_by_osswith_options(request, headers, runtime)

    def upload_file_by_urlwith_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['displayName'] = request.display_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['url'] = request.url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFileByURL',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/UploadFileByURL',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            grace_20220606_models.UploadFileByURLResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_file_by_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_file_by_urlwith_options(request, headers, runtime)
