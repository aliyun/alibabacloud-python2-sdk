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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.registration_context):
            query['RegistrationContext'] = request.registration_context
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_display_name):
            query['UserDisplayName'] = request.user_display_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthenticatorRegistration',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_authenticator_registration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_authenticator_registration_with_options(request, runtime)

    def create_user_authenticate_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.bind_hash_base_64):
            query['BindHashBase64'] = request.bind_hash_base_64
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserAuthenticateOptions',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_authenticate_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_authenticate_options_with_options(request, runtime)

    def deregister_authenticator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_authenticator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_authenticator_with_options(request, runtime)

    def fetch_access_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.mobile_extend_params_json):
            query['MobileExtendParamsJson'] = request.mobile_extend_params_json
        if not UtilClient.is_unset(request.mobile_extend_params_json_sign):
            query['MobileExtendParamsJsonSign'] = request.mobile_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.xclient_ip):
            query['XClientIp'] = request.xclient_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchAccessToken',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.FetchAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def fetch_access_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fetch_access_token_with_options(request, runtime)

    def get_authenticator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.GetAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authenticator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_authenticator_with_options(request, runtime)

    def list_authentication_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.from_time):
            query['FromTime'] = request.from_time
        if not UtilClient.is_unset(request.log_tag):
            query['LogTag'] = request.log_tag
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_time):
            query['ToTime'] = request.to_time
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticationLogs',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authentication_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authentication_logs_with_options(request, runtime)

    def list_authenticator_ops_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.from_time):
            query['FromTime'] = request.from_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_time):
            query['ToTime'] = request.to_time
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticatorOpsLogs',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authenticator_ops_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authenticator_ops_logs_with_options(request, runtime)

    def list_authenticators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticators',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authenticators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authenticators_with_options(request, runtime)

    def list_cost_unit_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not UtilClient.is_unset(request.final_date):
            query['FinalDate'] = request.final_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCostUnitOrders',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListCostUnitOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cost_unit_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cost_unit_orders_with_options(request, runtime)

    def list_order_consume_statistic_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_order_code):
            query['AliOrderCode'] = request.ali_order_code
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.statistic_time_max):
            query['StatisticTimeMax'] = request.statistic_time_max
        if not UtilClient.is_unset(request.statistic_time_min):
            query['StatisticTimeMin'] = request.statistic_time_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrderConsumeStatisticRecords',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_order_consume_statistic_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_order_consume_statistic_records_with_options(request, runtime)

    def list_pwned_passwords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.prefix_hex_password_sha_1hash):
            query['PrefixHexPasswordSha1Hash'] = request.prefix_hex_password_sha_1hash
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPwnedPasswords',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListPwnedPasswordsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pwned_passwords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pwned_passwords_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def query_sms_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsReports',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.QuerySmsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sms_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sms_reports_with_options(request, runtime)

    def query_sms_ups_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySmsUps',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.QuerySmsUpsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sms_ups(self):
        runtime = util_models.RuntimeOptions()
        return self.query_sms_ups_with_options(runtime)

    def register_authenticator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_name):
            query['AuthenticatorName'] = request.authenticator_name
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.log_params):
            query['LogParams'] = request.log_params
        if not UtilClient.is_unset(request.registration_context):
            query['RegistrationContext'] = request.registration_context
        if not UtilClient.is_unset(request.require_challenge_base_64):
            query['RequireChallengeBase64'] = request.require_challenge_base_64
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source_ip):
            query['UserSourceIp'] = request.user_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.RegisterAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    def register_authenticator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_authenticator_with_options(request, runtime)

    def service_invoke_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.doraemon_action):
            query['DoraemonAction'] = request.doraemon_action
        if not UtilClient.is_unset(request.mobile_extend_params_json):
            query['MobileExtendParamsJson'] = request.mobile_extend_params_json
        if not UtilClient.is_unset(request.mobile_extend_params_json_sign):
            query['MobileExtendParamsJsonSign'] = request.mobile_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.test_model):
            query['TestModel'] = request.test_model
        if not UtilClient.is_unset(request.xclient_ip):
            query['XClientIp'] = request.xclient_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ServiceInvoke',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ServiceInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    def service_invoke(self, request):
        runtime = util_models.RuntimeOptions()
        return self.service_invoke_with_options(request, runtime)

    def update_authenticator_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_name):
            query['AuthenticatorName'] = request.authenticator_name
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthenticatorAttribute',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_authenticator_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_authenticator_attribute_with_options(request, runtime)

    def verify_id_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.jwt_id_token):
            query['JwtIdToken'] = request.jwt_id_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyIdToken',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyIdTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_id_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_id_token_with_options(request, runtime)

    def verify_user_authentication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authentication_context):
            query['AuthenticationContext'] = request.authentication_context
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.log_params):
            query['LogParams'] = request.log_params
        if not UtilClient.is_unset(request.log_tag):
            query['LogTag'] = request.log_tag
        if not UtilClient.is_unset(request.require_bind_hash_base_64):
            query['RequireBindHashBase64'] = request.require_bind_hash_base_64
        if not UtilClient.is_unset(request.require_challenge_base_64):
            query['RequireChallengeBase64'] = request.require_challenge_base_64
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source_ip):
            query['UserSourceIp'] = request.user_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUserAuthentication',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_user_authentication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_user_authentication_with_options(request, runtime)
