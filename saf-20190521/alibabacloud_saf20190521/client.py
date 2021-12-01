# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_saf20190521 import models as saf_20190521_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'saf.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('saf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def execute_extend_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Region'] = request.region
        query['Service'] = request.service
        query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteExtendService',
            version='2019-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            saf_20190521_models.ExecuteExtendServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_extend_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_extend_service_with_options(request, runtime)

    def execute_request_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Service'] = request.service
        query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteRequest',
            version='2019-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            saf_20190521_models.ExecuteRequestResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_request(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_request_with_options(request, runtime)

    def execute_request_mlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Service'] = request.service
        query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteRequestML',
            version='2019-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            saf_20190521_models.ExecuteRequestMLResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_request_ml(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_request_mlwith_options(request, runtime)

    def execute_request_sgwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['Service'] = request.service
        query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecuteRequestSG',
            version='2019-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            saf_20190521_models.ExecuteRequestSGResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_request_sg(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_request_sgwith_options(request, runtime)

    def request_decision_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EventCode'] = request.event_code
        query['ServiceParameters'] = request.service_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RequestDecision',
            version='2019-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            saf_20190521_models.RequestDecisionResponse(),
            self.call_api(params, req, runtime)
        )

    def request_decision(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_decision_with_options(request, runtime)
