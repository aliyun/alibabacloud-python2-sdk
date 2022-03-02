# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tunnel_service20210509 import models as tunnel__service_20210509_models
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
        self._endpoint = self.get_endpoint('tunnel-service', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_session(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_session_with_options(request, headers, runtime)

    def create_session_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_name):
            body['sessionName'] = request.session_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSession',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/sessions/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.CreateSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_session(self, session_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_session_with_options(session_id, headers, runtime)

    def delete_session_with_options(self, session_id, headers, runtime):
        session_id = OpenApiUtilClient.get_encode_param(session_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSession',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/sessions/%s' % TeaConverter.to_unicode(session_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.DeleteSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_session(self, session_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_session_with_options(session_id, headers, runtime)

    def get_session_with_options(self, session_id, headers, runtime):
        session_id = OpenApiUtilClient.get_encode_param(session_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSession',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/sessions/%s' % TeaConverter.to_unicode(session_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.GetSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def heart_beat(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.heart_beat_with_options(request, headers, runtime)

    def heart_beat_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.session_status):
            body['sessionStatus'] = request.session_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HeartBeat',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/sessions/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.HeartBeatResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sessions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sessions_with_options(request, headers, runtime)

    def list_sessions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessions',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/sessions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.ListSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    def register_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.register_instance_with_options(request, headers, runtime)

    def register_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterInstance',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/instances/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.RegisterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def un_register_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_register_instance_with_options(instance_id, headers, runtime)

    def un_register_instance_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnRegisterInstance',
            version='2021-05-09',
            protocol='HTTPS',
            pathname='/v1/instances/%s' % TeaConverter.to_unicode(instance_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.UnRegisterInstanceResponse(),
            self.call_api(params, req, runtime)
        )
