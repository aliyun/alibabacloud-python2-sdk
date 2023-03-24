# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ims20190815 import models as ims_20190815_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def add_client_id_to_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to add the client ID `598469743454717***` to the OIDC IdP named `TestOIDCProvider`.
        

        @param request: AddClientIdToOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddClientIdToOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientIdToOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddClientIdToOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def add_client_id_to_oidcprovider(self, request):
        """
        This topic provides an example on how to add the client ID `598469743454717***` to the OIDC IdP named `TestOIDCProvider`.
        

        @param request: AddClientIdToOIDCProviderRequest

        @return: AddClientIdToOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_client_id_to_oidcprovider_with_options(request, runtime)

    def add_fingerprint_to_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to add the fingerprint `902ef2deeb3c5b13ea4c3d5193629309e231***` to the OIDC IdP named `TestOIDCProvider`.
        

        @param request: AddFingerprintToOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddFingerprintToOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFingerprintToOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddFingerprintToOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def add_fingerprint_to_oidcprovider(self, request):
        """
        This topic provides an example on how to add the fingerprint `902ef2deeb3c5b13ea4c3d5193629309e231***` to the OIDC IdP named `TestOIDCProvider`.
        

        @param request: AddFingerprintToOIDCProviderRequest

        @return: AddFingerprintToOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_fingerprint_to_oidcprovider_with_options(request, runtime)

    def add_user_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    def bind_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_code_1):
            query['AuthenticationCode1'] = request.authentication_code_1
        if not UtilClient.is_unset(request.authentication_code_2):
            query['AuthenticationCode2'] = request.authentication_code_2
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.BindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_mfadevice_with_options(request, runtime)

    def change_password_with_options(self, request, runtime):
        """
        >  This operation is available only for RAM users. Before you call this operation, make sure that `AllowUserToChangePassword` in [SetSecurityPreference](~~43765~~) is set to `True`. The value True indicates that RAM users can change their passwords.
        

        @param request: ChangePasswordRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChangePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
        if not UtilClient.is_unset(request.old_password):
            query['OldPassword'] = request.old_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangePassword',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ChangePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def change_password(self, request):
        """
        >  This operation is available only for RAM users. Before you call this operation, make sure that `AllowUserToChangePassword` in [SetSecurityPreference](~~43765~~) is set to `True`. The value True indicates that RAM users can change their passwords.
        

        @param request: ChangePasswordRequest

        @return: ChangePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_password_with_options(request, runtime)

    def create_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_key_with_options(request, runtime)

    def create_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_secret_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_validity):
            query['AccessTokenValidity'] = request.access_token_validity
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.is_multi_tenant):
            query['IsMultiTenant'] = request.is_multi_tenant
        if not UtilClient.is_unset(request.predefined_scopes):
            query['PredefinedScopes'] = request.predefined_scopes
        if not UtilClient.is_unset(request.redirect_uris):
            query['RedirectUris'] = request.redirect_uris
        if not UtilClient.is_unset(request.refresh_token_validity):
            query['RefreshTokenValidity'] = request.refresh_token_validity
        if not UtilClient.is_unset(request.secret_required):
            query['SecretRequired'] = request.secret_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_login_profile_with_options(request, runtime)

    def create_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to create an IdP named `TestOIDCProvider` to configure a trust relationship between the external IdP Okta and Alibaba Cloud.
        ## Prerequisites
        Before you call this operation, make sure that the information such as the URL of the issuer, the fingerprints of HTTPS certificates, and the client IDs are obtained from an external IdP, such as Google G Suite or Okta.
        ## Limits
        - You can create a maximum of 100 OIDC IdPs in an Alibaba Cloud account.
        - You can add a maximum of 20 client IDs to an OIDC IdP.
        - You can add a maximum of five fingerprints to an OIDC IdP.
        

        @param request: CreateOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.fingerprints):
            query['Fingerprints'] = request.fingerprints
        if not UtilClient.is_unset(request.issuer_url):
            query['IssuerUrl'] = request.issuer_url
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_oidcprovider(self, request):
        """
        This topic provides an example on how to create an IdP named `TestOIDCProvider` to configure a trust relationship between the external IdP Okta and Alibaba Cloud.
        ## Prerequisites
        Before you call this operation, make sure that the information such as the URL of the issuer, the fingerprints of HTTPS certificates, and the client IDs are obtained from an external IdP, such as Google G Suite or Okta.
        ## Limits
        - You can create a maximum of 100 OIDC IdPs in an Alibaba Cloud account.
        - You can add a maximum of 20 client IDs to an OIDC IdP.
        - You can add a maximum of five fingerprints to an OIDC IdP.
        

        @param request: CreateOIDCProviderRequest

        @return: CreateOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oidcprovider_with_options(request, runtime)

    def create_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encoded_samlmetadata_document):
            query['EncodedSAMLMetadataDocument'] = request.encoded_samlmetadata_document
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_samlprovider_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        """
        This topic provides an example on how to create a RAM user named `test`.
        

        @param request: CreateUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.mobile_phone):
            query['MobilePhone'] = request.mobile_phone
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        """
        This topic provides an example on how to create a RAM user named `test`.
        

        @param request: CreateUserRequest

        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.virtual_mfadevice_name):
            query['VirtualMFADeviceName'] = request.virtual_mfadevice_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.CreateVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_mfadevice_with_options(request, runtime)

    def delete_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_key_with_options(request, runtime)

    def delete_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_secret_with_options(request, runtime)

    def delete_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        """
        Before you delete a RAM user group, make sure that no policies are attached to the group and no RAM users are included in the group.
        

        @param request: DeleteGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, request):
        """
        Before you delete a RAM user group, make sure that no policies are attached to the group and no RAM users are included in the group.
        

        @param request: DeleteGroupRequest

        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_login_profile_with_options(request, runtime)

    def delete_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to remove the OIDC IdP named `TestOIDCProvider`.
        

        @param request: DeleteOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_oidcprovider(self, request):
        """
        This topic provides an example on how to remove the OIDC IdP named `TestOIDCProvider`.
        

        @param request: DeleteOIDCProviderRequest

        @return: DeleteOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_oidcprovider_with_options(request, runtime)

    def delete_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_samlprovider_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DeleteVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    def disable_virtual_mfawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableVirtualMFA',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.DisableVirtualMFAResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_virtual_mfa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_virtual_mfawith_options(request, runtime)

    def generate_credential_report_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GenerateCredentialReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GenerateCredentialReportResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_credential_report(self):
        runtime = util_models.RuntimeOptions()
        return self.generate_credential_report_with_options(runtime)

    def get_access_key_last_used_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsed',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccessKeyLastUsedResponse(),
            self.call_api(params, req, runtime)
        )

    def get_access_key_last_used(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_with_options(request, runtime)

    def get_account_mfainfo_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountMFAInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_mfainfo(self):
        runtime = util_models.RuntimeOptions()
        return self.get_account_mfainfo_with_options(runtime)

    def get_account_security_practice_report_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountSecurityPracticeReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSecurityPracticeReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_security_practice_report(self):
        runtime = util_models.RuntimeOptions()
        return self.get_account_security_practice_report_with_options(runtime)

    def get_account_summary_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAccountSummary',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_summary(self):
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(runtime)

    def get_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_secret_id):
            query['AppSecretId'] = request.app_secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSecret',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_secret_with_options(request, runtime)

    def get_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    def get_credential_report_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCredentialReport',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetCredentialReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_credential_report(self):
        runtime = util_models.RuntimeOptions()
        return self.get_credential_report_with_options(runtime)

    def get_default_domain_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultDomain',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def get_default_domain(self):
        runtime = util_models.RuntimeOptions()
        return self.get_default_domain_with_options(runtime)

    def get_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    def get_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_profile_with_options(request, runtime)

    def get_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to query the information about an OIDC IdP named `TestOIDCProvider`.
        

        @param request: GetOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oidcprovider(self, request):
        """
        This topic provides an example on how to query the information about an OIDC IdP named `TestOIDCProvider`.
        

        @param request: GetOIDCProviderRequest

        @return: GetOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oidcprovider_with_options(request, runtime)

    def get_password_policy_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetPasswordPolicy',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_password_policy(self):
        runtime = util_models.RuntimeOptions()
        return self.get_password_policy_with_options(runtime)

    def get_samlprovider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_samlprovider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_samlprovider_with_options(request, runtime)

    def get_security_preference_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSecurityPreference',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_security_preference(self):
        runtime = util_models.RuntimeOptions()
        return self.get_security_preference_with_options(runtime)

    def get_user_with_options(self, request, runtime):
        """
        This topic provides an example to show how to query the information about a RAM user named `test@example.onaliyun.com`.
        

        @param request: GetUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        """
        This topic provides an example to show how to query the information about a RAM user named `test@example.onaliyun.com`.
        

        @param request: GetUserRequest

        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def get_user_mfainfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserMFAInfo',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserMFAInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_mfainfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfainfo_with_options(request, runtime)

    def get_user_sso_settings_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUserSsoSettings',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.GetUserSsoSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_sso_settings(self):
        runtime = util_models.RuntimeOptions()
        return self.get_user_sso_settings_with_options(runtime)

    def list_access_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessKeys',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAccessKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_keys_with_options(request, runtime)

    def list_app_secret_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSecretIds',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListAppSecretIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_secret_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_secret_ids_with_options(request, runtime)

    def list_applications_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications(self):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(runtime)

    def list_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    def list_groups_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    def list_oidcproviders_with_options(self, request, runtime):
        """
        This topic provides an example on how to query all OIDC IdPs within your Alibaba Cloud account. The response shows that your Alibaba Cloud account has only one OIDC IdP named `TestOIDCProvider`.
        

        @param request: ListOIDCProvidersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListOIDCProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOIDCProviders',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListOIDCProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_oidcproviders(self, request):
        """
        This topic provides an example on how to query all OIDC IdPs within your Alibaba Cloud account. The response shows that your Alibaba Cloud account has only one OIDC IdP named `TestOIDCProvider`.
        

        @param request: ListOIDCProvidersRequest

        @return: ListOIDCProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_oidcproviders_with_options(request, runtime)

    def list_predefined_scopes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPredefinedScopes',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListPredefinedScopesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_predefined_scopes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_predefined_scopes_with_options(request, runtime)

    def list_samlproviders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSAMLProviders',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListSAMLProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_samlproviders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_samlproviders_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        You must specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        *   `ResourceId.N`
        *   `Tag.N.Key`
        *   `Tag.N.Key` and `Tag.N.Value`
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        You must specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        *   `ResourceId.N`
        *   `Tag.N.Key`
        *   `Tag.N.Key` and `Tag.N.Value`
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_basic_infos_with_options(self, request, runtime):
        """
        You can call the following API operations to query the information about all RAM users:
        *   ListUsers: queries the details of all RAM users.
        *   ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        

        @param request: ListUserBasicInfosRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListUserBasicInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserBasicInfos',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUserBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_basic_infos(self, request):
        """
        You can call the following API operations to query the information about all RAM users:
        *   ListUsers: queries the details of all RAM users.
        *   ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        

        @param request: ListUserBasicInfosRequest

        @return: ListUserBasicInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_basic_infos_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        """
        You can call the following API operations to query the information about all RAM users:
        *   ListUsers: queries the details of all RAM users.
        *   ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        

        @param request: ListUsersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        """
        You can call the following API operations to query the information about all RAM users:
        *   ListUsers: queries the details of all RAM users.
        *   ListUserBasicInfos: queries the basic information about all RAM users. The basic information includes only the logon names (`UserPrincipalName`), display names (`DisplayName`), and user IDs (`UserId`).
        

        @param request: ListUsersRequest

        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_users_for_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users_for_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    def list_virtual_mfadevices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVirtualMFADevices',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.ListVirtualMFADevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_virtual_mfadevices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_mfadevices_with_options(request, runtime)

    def remove_client_id_from_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to remove the client ID `498469743454717***` from the OIDC IdP named `TestOIDCProvider`.
        

        @param request: RemoveClientIdFromOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveClientIdFromOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClientIdFromOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveClientIdFromOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_client_id_from_oidcprovider(self, request):
        """
        This topic provides an example on how to remove the client ID `498469743454717***` from the OIDC IdP named `TestOIDCProvider`.
        

        @param request: RemoveClientIdFromOIDCProviderRequest

        @return: RemoveClientIdFromOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_client_id_from_oidcprovider_with_options(request, runtime)

    def remove_fingerprint_from_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to remove the fingerprint `6938fd4d98bab03faadb97b34396831e3780***` from the OIDC IdP named `TestOIDCProvider`.
        

        @param request: RemoveFingerprintFromOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveFingerprintFromOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fingerprint):
            query['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFingerprintFromOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveFingerprintFromOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_fingerprint_from_oidcprovider(self, request):
        """
        This topic provides an example on how to remove the fingerprint `6938fd4d98bab03faadb97b34396831e3780***` from the OIDC IdP named `TestOIDCProvider`.
        

        @param request: RemoveFingerprintFromOIDCProviderRequest

        @return: RemoveFingerprintFromOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_fingerprint_from_oidcprovider_with_options(request, runtime)

    def remove_user_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_user_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    def set_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_domain_name):
            query['DefaultDomainName'] = request.default_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultDomain',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    def set_password_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hard_expire):
            query['HardExpire'] = request.hard_expire
        if not UtilClient.is_unset(request.max_login_attemps):
            query['MaxLoginAttemps'] = request.max_login_attemps
        if not UtilClient.is_unset(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not UtilClient.is_unset(request.minimum_password_different_character):
            query['MinimumPasswordDifferentCharacter'] = request.minimum_password_different_character
        if not UtilClient.is_unset(request.minimum_password_length):
            query['MinimumPasswordLength'] = request.minimum_password_length
        if not UtilClient.is_unset(request.password_not_contain_user_name):
            query['PasswordNotContainUserName'] = request.password_not_contain_user_name
        if not UtilClient.is_unset(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        if not UtilClient.is_unset(request.require_lowercase_characters):
            query['RequireLowercaseCharacters'] = request.require_lowercase_characters
        if not UtilClient.is_unset(request.require_numbers):
            query['RequireNumbers'] = request.require_numbers
        if not UtilClient.is_unset(request.require_symbols):
            query['RequireSymbols'] = request.require_symbols
        if not UtilClient.is_unset(request.require_uppercase_characters):
            query['RequireUppercaseCharacters'] = request.require_uppercase_characters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordPolicy',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_password_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    def set_security_preference_with_options(self, tmp_req, runtime):
        """
        This topic provides an example on how to enable multi-factor authentication (MFA) only for RAM users who initiated unusual logons.
        

        @param tmp_req: SetSecurityPreferenceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetSecurityPreferenceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ims_20190815_models.SetSecurityPreferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.verification_types):
            request.verification_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.verification_types, 'VerificationTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.allow_user_to_change_password):
            query['AllowUserToChangePassword'] = request.allow_user_to_change_password
        if not UtilClient.is_unset(request.allow_user_to_manage_access_keys):
            query['AllowUserToManageAccessKeys'] = request.allow_user_to_manage_access_keys
        if not UtilClient.is_unset(request.allow_user_to_manage_mfadevices):
            query['AllowUserToManageMFADevices'] = request.allow_user_to_manage_mfadevices
        if not UtilClient.is_unset(request.allow_user_to_manage_personal_ding_talk):
            query['AllowUserToManagePersonalDingTalk'] = request.allow_user_to_manage_personal_ding_talk
        if not UtilClient.is_unset(request.enable_save_mfaticket):
            query['EnableSaveMFATicket'] = request.enable_save_mfaticket
        if not UtilClient.is_unset(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        if not UtilClient.is_unset(request.login_session_duration):
            query['LoginSessionDuration'] = request.login_session_duration
        if not UtilClient.is_unset(request.mfaoperation_for_login):
            query['MFAOperationForLogin'] = request.mfaoperation_for_login
        if not UtilClient.is_unset(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        if not UtilClient.is_unset(request.verification_types_shrink):
            query['VerificationTypes'] = request.verification_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSecurityPreference',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetSecurityPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def set_security_preference(self, request):
        """
        This topic provides an example on how to enable multi-factor authentication (MFA) only for RAM users who initiated unusual logons.
        

        @param request: SetSecurityPreferenceRequest

        @return: SetSecurityPreferenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_security_preference_with_options(request, runtime)

    def set_user_sso_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auxiliary_domain):
            query['AuxiliaryDomain'] = request.auxiliary_domain
        if not UtilClient.is_unset(request.metadata_document):
            query['MetadataDocument'] = request.metadata_document
        if not UtilClient.is_unset(request.sso_enabled):
            query['SsoEnabled'] = request.sso_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserSsoSettings',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.SetUserSsoSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_user_sso_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_sso_settings_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unbind_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindMFADevice',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UnbindMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_mfadevice_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_principal_name):
            query['ResourcePrincipalName'] = request.resource_principal_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_access_key_id):
            query['UserAccessKeyId'] = request.user_access_key_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessKey',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_access_key_with_options(request, runtime)

    def update_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.new_access_token_validity):
            query['NewAccessTokenValidity'] = request.new_access_token_validity
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_is_multi_tenant):
            query['NewIsMultiTenant'] = request.new_is_multi_tenant
        if not UtilClient.is_unset(request.new_predefined_scopes):
            query['NewPredefinedScopes'] = request.new_predefined_scopes
        if not UtilClient.is_unset(request.new_redirect_uris):
            query['NewRedirectUris'] = request.new_redirect_uris
        if not UtilClient.is_unset(request.new_refresh_token_validity):
            query['NewRefreshTokenValidity'] = request.new_refresh_token_validity
        if not UtilClient.is_unset(request.new_secret_required):
            query['NewSecretRequired'] = request.new_secret_required
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    def update_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.new_comments):
            query['NewComments'] = request.new_comments
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    def update_login_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfabind_required):
            query['MFABindRequired'] = request.mfabind_required
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_reset_required):
            query['PasswordResetRequired'] = request.password_reset_required
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoginProfile',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateLoginProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_login_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_login_profile_with_options(request, runtime)

    def update_oidcprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to change the description of the OIDC IdP named `TestOIDCProvider` to `This is a new OIDC Provider.`
        

        @param request: UpdateOIDCProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateOIDCProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ids):
            query['ClientIds'] = request.client_ids
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.oidcprovider_name):
            query['OIDCProviderName'] = request.oidcprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOIDCProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateOIDCProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_oidcprovider(self, request):
        """
        This topic provides an example on how to change the description of the OIDC IdP named `TestOIDCProvider` to `This is a new OIDC Provider.`
        

        @param request: UpdateOIDCProviderRequest

        @return: UpdateOIDCProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_oidcprovider_with_options(request, runtime)

    def update_samlprovider_with_options(self, request, runtime):
        """
        This topic provides an example on how to change the description of an IdP named `test-provider` to `This is a new provider.`
        

        @param request: UpdateSAMLProviderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSAMLProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_encoded_samlmetadata_document):
            query['NewEncodedSAMLMetadataDocument'] = request.new_encoded_samlmetadata_document
        if not UtilClient.is_unset(request.samlprovider_name):
            query['SAMLProviderName'] = request.samlprovider_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSAMLProvider',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateSAMLProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_samlprovider(self, request):
        """
        This topic provides an example on how to change the description of an IdP named `test-provider` to `This is a new provider.`
        

        @param request: UpdateSAMLProviderRequest

        @return: UpdateSAMLProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_samlprovider_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        """
        This topic provides an example to show how to modify the name of a RAM user from `test@example.onaliyun.com` to `new@example.onaliyun.com`.
        

        @param request: UpdateUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_comments):
            query['NewComments'] = request.new_comments
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_email):
            query['NewEmail'] = request.new_email
        if not UtilClient.is_unset(request.new_mobile_phone):
            query['NewMobilePhone'] = request.new_mobile_phone
        if not UtilClient.is_unset(request.new_user_principal_name):
            query['NewUserPrincipalName'] = request.new_user_principal_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_principal_name):
            query['UserPrincipalName'] = request.user_principal_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2019-08-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ims_20190815_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        """
        This topic provides an example to show how to modify the name of a RAM user from `test@example.onaliyun.com` to `new@example.onaliyun.com`.
        

        @param request: UpdateUserRequest

        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)
