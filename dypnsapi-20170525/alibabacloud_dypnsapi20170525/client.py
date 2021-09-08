# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dypnsapi20170525 import models as dypnsapi_20170525_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dypnsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_verify_scheme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.CreateVerifySchemeResponse(),
            self.do_rpcrequest('CreateVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_verify_scheme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_verify_scheme_with_options(request, runtime)

    def delete_verify_scheme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.DeleteVerifySchemeResponse(),
            self.do_rpcrequest('DeleteVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_verify_scheme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_verify_scheme_with_options(request, runtime)

    def describe_verify_scheme_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.DescribeVerifySchemeResponse(),
            self.do_rpcrequest('DescribeVerifyScheme', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_verify_scheme(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_scheme_with_options(request, runtime)

    def get_authorization_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetAuthorizationUrlResponse(),
            self.do_rpcrequest('GetAuthorizationUrl', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authorization_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_url_with_options(request, runtime)

    def get_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetAuthTokenResponse(),
            self.do_rpcrequest('GetAuthToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    def get_certify_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetCertifyResultResponse(),
            self.do_rpcrequest('GetCertifyResult', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_certify_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_certify_result_with_options(request, runtime)

    def get_mobile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.GetMobileResponse(),
            self.do_rpcrequest('GetMobile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mobile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mobile_with_options(request, runtime)

    def twice_tel_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.TwiceTelVerifyResponse(),
            self.do_rpcrequest('TwiceTelVerify', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def twice_tel_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.twice_tel_verify_with_options(request, runtime)

    def verify_mobile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.VerifyMobileResponse(),
            self.do_rpcrequest('VerifyMobile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_mobile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_mobile_with_options(request, runtime)

    def verify_phone_with_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dypnsapi_20170525_models.VerifyPhoneWithTokenResponse(),
            self.do_rpcrequest('VerifyPhoneWithToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_phone_with_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_phone_with_token_with_options(request, runtime)
