# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_idaas_doraemon20210520 import models as idaas_doraemon_20210520_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-hangzhou': 'idaas-doraemon.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('idaas-doraemon', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_authenticator_registration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse(),
            self.do_rpcrequest('CreateAuthenticatorRegistration', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_authenticator_registration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_authenticator_registration_with_options(request, runtime)

    def create_user_authenticate_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse(),
            self.do_rpcrequest('CreateUserAuthenticateOptions', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_authenticate_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_authenticate_options_with_options(request, runtime)

    def deregister_authenticator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse(),
            self.do_rpcrequest('DeregisterAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_authenticator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_authenticator_with_options(request, runtime)

    def fetch_access_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.FetchAccessTokenResponse(),
            self.do_rpcrequest('FetchAccessToken', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_access_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fetch_access_token_with_options(request, runtime)

    def get_authenticator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.GetAuthenticatorResponse(),
            self.do_rpcrequest('GetAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authenticator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_authenticator_with_options(request, runtime)

    def list_authentication_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticationLogsResponse(),
            self.do_rpcrequest('ListAuthenticationLogs', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authentication_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authentication_logs_with_options(request, runtime)

    def list_authenticator_ops_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse(),
            self.do_rpcrequest('ListAuthenticatorOpsLogs', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authenticator_ops_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authenticator_ops_logs_with_options(request, runtime)

    def list_authenticators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorsResponse(),
            self.do_rpcrequest('ListAuthenticators', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authenticators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authenticators_with_options(request, runtime)

    def list_pwned_passwords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListPwnedPasswordsResponse(),
            self.do_rpcrequest('ListPwnedPasswords', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pwned_passwords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pwned_passwords_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def register_authenticator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.RegisterAuthenticatorResponse(),
            self.do_rpcrequest('RegisterAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_authenticator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_authenticator_with_options(request, runtime)

    def service_invoke_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ServiceInvokeResponse(),
            self.do_rpcrequest('ServiceInvoke', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def service_invoke(self, request):
        runtime = util_models.RuntimeOptions()
        return self.service_invoke_with_options(request, runtime)

    def update_authenticator_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse(),
            self.do_rpcrequest('UpdateAuthenticatorAttribute', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_authenticator_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_authenticator_attribute_with_options(request, runtime)

    def verify_user_authentication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse(),
            self.do_rpcrequest('VerifyUserAuthentication', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_user_authentication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_user_authentication_with_options(request, runtime)
