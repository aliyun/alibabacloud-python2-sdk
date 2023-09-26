# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ettrafficisp20230830 import models as ettraffic_isp_20230830_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('ettrafficisp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def ak_disable_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_name):
            body['accessKeyName'] = request.access_key_name
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AkDisable',
            version='2023-08-30',
            protocol='HTTPS',
            pathname='/console/ak/disable',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ettraffic_isp_20230830_models.AkDisableResponse(),
            self.call_api(params, req, runtime)
        )

    def ak_disable(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.ak_disable_with_options(request, headers, runtime)

    def ak_enable_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_name):
            body['accessKeyName'] = request.access_key_name
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AkEnable',
            version='2023-08-30',
            protocol='HTTPS',
            pathname='/console/ak/enable',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ettraffic_isp_20230830_models.AkEnableResponse(),
            self.call_api(params, req, runtime)
        )

    def ak_enable(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.ak_enable_with_options(request, headers, runtime)

    def ak_generate_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_name):
            body['accessKeyName'] = request.access_key_name
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AkGenerate',
            version='2023-08-30',
            protocol='HTTPS',
            pathname='/console/ak/generate',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ettraffic_isp_20230830_models.AkGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    def ak_generate(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.ak_generate_with_options(request, headers, runtime)

    def ak_list_page_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AkListPage',
            version='2023-08-30',
            protocol='HTTPS',
            pathname='/console/ak/listPage',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ettraffic_isp_20230830_models.AkListPageResponse(),
            self.call_api(params, req, runtime)
        )

    def ak_list_page(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.ak_list_page_with_options(request, headers, runtime)

    def ak_update_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key_id):
            body['accessKeyId'] = request.access_key_id
        if not UtilClient.is_unset(request.access_key_name):
            body['accessKeyName'] = request.access_key_name
        if not UtilClient.is_unset(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AkUpdate',
            version='2023-08-30',
            protocol='HTTPS',
            pathname='/console/ak/update',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ettraffic_isp_20230830_models.AkUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    def ak_update(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.ak_update_with_options(request, headers, runtime)

    def dim_group_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DimGroup',
            version='2023-08-30',
            protocol='HTTPS',
            pathname='/console/dim/group',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ettraffic_isp_20230830_models.DimGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def dim_group(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dim_group_with_options(headers, runtime)
