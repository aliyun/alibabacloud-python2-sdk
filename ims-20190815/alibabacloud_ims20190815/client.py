# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ims20190815 import models as ims_20190815_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ims', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.AddUserToGroupResponse().from_map(
            self.do_rpcrequest('AddUserToGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_user_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    def bind_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.BindMFADeviceResponse().from_map(
            self.do_rpcrequest('BindMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    def change_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ChangePasswordResponse().from_map(
            self.do_rpcrequest('ChangePassword', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    def create_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateAccessKeyResponse().from_map(
            self.do_rpcrequest('CreateAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateApplicationResponse().from_map(
            self.do_rpcrequest('CreateApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def create_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateAppSecretResponse().from_map(
            self.do_rpcrequest('CreateAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateGroupResponse().from_map(
            self.do_rpcrequest('CreateGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateLoginProfileResponse().from_map(
            self.do_rpcrequest('CreateLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    def create_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateSAMLProviderResponse().from_map(
            self.do_rpcrequest('CreateSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.CreateVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('CreateVirtualMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    def delete_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteAccessKeyResponse().from_map(
            self.do_rpcrequest('DeleteAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    def delete_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteApplicationResponse().from_map(
            self.do_rpcrequest('DeleteApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    def delete_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteAppSecretResponse().from_map(
            self.do_rpcrequest('DeleteAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteGroupResponse().from_map(
            self.do_rpcrequest('DeleteGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteLoginProfileResponse().from_map(
            self.do_rpcrequest('DeleteLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    def delete_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteSAMLProviderResponse().from_map(
            self.do_rpcrequest('DeleteSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DeleteVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('DeleteVirtualMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    def disable_virtual_mfawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.DisableVirtualMFAResponse().from_map(
            self.do_rpcrequest('DisableVirtualMFA', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_virtual_mfa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    def generate_credential_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GenerateCredentialReportResponse().from_map(
            self.do_rpcrequest('GenerateCredentialReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_credential_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_credential_report_with_options(request, runtime)

    def get_access_key_last_used_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetAccessKeyLastUsedResponse().from_map(
            self.do_rpcrequest('GetAccessKeyLastUsed', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_access_key_last_used(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    def get_account_mfainfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetAccountMFAInfoResponse().from_map(
            self.do_rpcrequest('GetAccountMFAInfo', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_mfainfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_mfainfo_with_options(request, runtime)

    def get_account_security_practice_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetAccountSecurityPracticeReportResponse().from_map(
            self.do_rpcrequest('GetAccountSecurityPracticeReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_security_practice_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_security_practice_report_with_options(request, runtime)

    def get_account_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetAccountSummaryResponse().from_map(
            self.do_rpcrequest('GetAccountSummary', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(request, runtime)

    def get_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetApplicationResponse().from_map(
            self.do_rpcrequest('GetApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    def get_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetAppSecretResponse().from_map(
            self.do_rpcrequest('GetAppSecret', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    def get_credential_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetCredentialReportResponse().from_map(
            self.do_rpcrequest('GetCredentialReport', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_credential_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_credential_report_with_options(request, runtime)

    def get_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetDefaultDomainResponse().from_map(
            self.do_rpcrequest('GetDefaultDomain', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_default_domain_with_options(request, runtime)

    def get_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetGroupResponse().from_map(
            self.do_rpcrequest('GetGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    def get_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetLoginProfileResponse().from_map(
            self.do_rpcrequest('GetLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    def get_password_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetPasswordPolicyResponse().from_map(
            self.do_rpcrequest('GetPasswordPolicy', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_password_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(request, runtime)

    def get_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetSAMLProviderResponse().from_map(
            self.do_rpcrequest('GetSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    def get_security_preference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetSecurityPreferenceResponse().from_map(
            self.do_rpcrequest('GetSecurityPreference', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_security_preference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetUserResponse().from_map(
            self.do_rpcrequest('GetUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def get_user_mfainfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetUserMFAInfoResponse().from_map(
            self.do_rpcrequest('GetUserMFAInfo', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_mfainfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    def get_user_sso_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.GetUserSsoSettingsResponse().from_map(
            self.do_rpcrequest('GetUserSsoSettings', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_sso_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_sso_settings_with_options(request, runtime)

    def list_access_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListAccessKeysResponse().from_map(
            self.do_rpcrequest('ListAccessKeys', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_access_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    def list_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListApplicationsResponse().from_map(
            self.do_rpcrequest('ListApplications', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    def list_app_secret_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListAppSecretIdsResponse().from_map(
            self.do_rpcrequest('ListAppSecretIds', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_secret_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    def list_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListGroupsResponse().from_map(
            self.do_rpcrequest('ListGroups', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    def list_groups_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListGroupsForUserResponse().from_map(
            self.do_rpcrequest('ListGroupsForUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_groups_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    def list_predefined_scopes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListPredefinedScopesResponse().from_map(
            self.do_rpcrequest('ListPredefinedScopes', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_predefined_scopes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    def list_samlproviders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListSAMLProvidersResponse().from_map(
            self.do_rpcrequest('ListSAMLProviders', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_samlproviders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    def list_user_basic_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListUserBasicInfosResponse().from_map(
            self.do_rpcrequest('ListUserBasicInfos', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_basic_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_users_for_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListUsersForGroupResponse().from_map(
            self.do_rpcrequest('ListUsersForGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users_for_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    def list_virtual_mfadevices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.ListVirtualMFADevicesResponse().from_map(
            self.do_rpcrequest('ListVirtualMFADevices', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_virtual_mfadevices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    def remove_user_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.RemoveUserFromGroupResponse().from_map(
            self.do_rpcrequest('RemoveUserFromGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_user_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    def set_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.SetDefaultDomainResponse().from_map(
            self.do_rpcrequest('SetDefaultDomain', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    def set_password_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.SetPasswordPolicyResponse().from_map(
            self.do_rpcrequest('SetPasswordPolicy', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_password_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    def set_security_preference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.SetSecurityPreferenceResponse().from_map(
            self.do_rpcrequest('SetSecurityPreference', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_security_preference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    def set_user_sso_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.SetUserSsoSettingsResponse().from_map(
            self.do_rpcrequest('SetUserSsoSettings', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_user_sso_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    def unbind_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UnbindMFADeviceResponse().from_map(
            self.do_rpcrequest('UnbindMFADevice', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    def update_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UpdateAccessKeyResponse().from_map(
            self.do_rpcrequest('UpdateAccessKey', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    def update_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UpdateApplicationResponse().from_map(
            self.do_rpcrequest('UpdateApplication', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    def update_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UpdateGroupResponse().from_map(
            self.do_rpcrequest('UpdateGroup', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    def update_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UpdateLoginProfileResponse().from_map(
            self.do_rpcrequest('UpdateLoginProfile', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    def update_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UpdateSAMLProviderResponse().from_map(
            self.do_rpcrequest('UpdateSAMLProvider', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ims_20190815_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2019-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)
