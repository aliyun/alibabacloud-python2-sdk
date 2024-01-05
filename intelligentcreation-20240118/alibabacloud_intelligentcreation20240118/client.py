# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_intelligentcreation20240118 import models as intelligent_creation_20240118_models
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
        self._endpoint = self.get_endpoint('intelligentcreation', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def actual_deduct_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ActualDeductResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/digital-human/commands/actual-deduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.ActualDeductResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def actual_deduct_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.actual_deduct_resource_with_options(request, headers, runtime)

    def direct_deduct_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DirectDeductResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/digital-human/commands/direct-deduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.DirectDeductResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def direct_deduct_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.direct_deduct_resource_with_options(request, headers, runtime)

    def expect_deduct_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ExpectDeductResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/digital-human/commands/expect-deduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.ExpectDeductResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def expect_deduct_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.expect_deduct_resource_with_options(request, headers, runtime)
