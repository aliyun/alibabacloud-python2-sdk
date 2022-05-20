# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cgcs20211111 import models as cgcs20211111_models
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
        self._endpoint = self.get_endpoint('cgcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_app_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.enable_postpaid):
            query['EnablePostpaid'] = request.enable_postpaid
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_with_options(request, runtime)

    def get_app_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_session_with_options(request, runtime)

    def list_app_sessions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.custom_session_ids):
            query['CustomSessionIds'] = request.custom_session_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_session_ids):
            query['PlatformSessionIds'] = request.platform_session_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSessions',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_sessions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_sessions_with_options(request, runtime)

    def stop_app_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_app_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_app_session_with_options(request, runtime)
