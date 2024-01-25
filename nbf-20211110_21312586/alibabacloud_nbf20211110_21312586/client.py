# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nbf20211110_21312586 import models as nbf20211110__21312586_models
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
        self._endpoint = self.get_endpoint('nbf', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def api_test_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.test_cmd):
            query['testCmd'] = request.test_cmd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApiTest',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/apiTest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.ApiTestResponse(),
            self.call_api(params, req, runtime)
        )

    def api_test(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.api_test_with_options(request, headers, runtime)

    def build_sdk_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.build_cmd):
            query['buildCmd'] = request.build_cmd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BuildSdk',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/buildSdk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.BuildSdkResponse(),
            self.call_api(params, req, runtime)
        )

    def build_sdk(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.build_sdk_with_options(request, headers, runtime)

    def create_and_release_api_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creat_api_cmd):
            query['creatApiCmd'] = request.creat_api_cmd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndReleaseApi',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/createAndReleaseApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.CreateAndReleaseApiResponse(),
            self.call_api(params, req, runtime)
        )

    def create_and_release_api(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_and_release_api_with_options(request, headers, runtime)

    def create_sdk_version_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_sdk_cmd):
            query['createSdkCmd'] = request.create_sdk_cmd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSdkVersion',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/createSdkVersion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.CreateSdkVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sdk_version(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sdk_version_with_options(request, headers, runtime)

    def delete_api_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_external_id):
            query['apiExternalId'] = request.api_external_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/deleteApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_api_with_options(request, headers, runtime)

    def get_result_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResult',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/getResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.GetResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_result(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_result_with_options(request, headers, runtime)

    def open_api_generic_proxy_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenApiGenericProxy',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/openApiGenericProxy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.OpenApiGenericProxyResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_generic_proxy(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_api_generic_proxy_with_options(headers, runtime)

    def pre_check_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_schema_dto):
            query['apiSchemaDTO'] = request.api_schema_dto
        if not UtilClient.is_unset(request.group_version_extra_info):
            query['groupVersionExtraInfo'] = request.group_version_extra_info
        if not UtilClient.is_unset(request.namespace_external_id):
            query['namespaceExternalId'] = request.namespace_external_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreCheck',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/preCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.PreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def pre_check(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pre_check_with_options(request, headers, runtime)

    def publish_sdk_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishSdk',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/publishSdk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.PublishSdkResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_sdk(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_sdk_with_options(request, headers, runtime)

    def serialize_api_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_schema_dto):
            query['apiSchemaDTO'] = request.api_schema_dto
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SerializeApi',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/serializeApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.SerializeApiResponse(),
            self.call_api(params, req, runtime)
        )

    def serialize_api(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.serialize_api_with_options(request, headers, runtime)

    def update_and_release_api_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.update_api_cmd):
            query['updateApiCmd'] = request.update_api_cmd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAndReleaseApi',
            version='2021-11-10_21-31-25-86',
            protocol='HTTPS',
            pathname='/nbf_gateway_inner/1_0_0/updateAndReleaseApi',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            nbf20211110__21312586_models.UpdateAndReleaseApiResponse(),
            self.call_api(params, req, runtime)
        )

    def update_and_release_api(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_and_release_api_with_options(request, headers, runtime)
