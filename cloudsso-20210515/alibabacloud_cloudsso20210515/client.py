# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudsso20210515 import models as cloudsso_20210515_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudsso', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_external_samlid_pcertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_external_samlid_pcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_external_samlid_pcertificate_with_options(request, runtime)

    def add_permission_policy_to_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.inline_policy_document):
            query['InlinePolicyDocument'] = request.inline_policy_document
        if not UtilClient.is_unset(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPermissionPolicyToAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_permission_policy_to_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_permission_policy_to_access_configuration_with_options(request, runtime)

    def add_user_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    def clear_external_samlidentity_provider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_external_samlidentity_provider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_external_samlidentity_provider_with_options(request, runtime)

    def create_access_assignment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateAccessAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_assignment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_assignment_with_options(request, runtime)

    def create_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_name):
            query['AccessConfigurationName'] = request.access_configuration_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.relay_state):
            query['RelayState'] = request.relay_state
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_configuration_with_options(request, runtime)

    def create_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_scimserver_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateSCIMServerCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scimserver_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scimserver_credential_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.first_name):
            query['FirstName'] = request.first_name
        if not UtilClient.is_unset(request.last_name):
            query['LastName'] = request.last_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def delete_access_assignment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.deprovision_strategy):
            query['DeprovisionStrategy'] = request.deprovision_strategy
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteAccessAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_assignment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_assignment_with_options(request, runtime)

    def delete_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.force_remove_permission_policies):
            query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_configuration_with_options(request, runtime)

    def delete_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_mfadevice_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfadevice_id):
            query['MFADeviceId'] = request.mfadevice_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMFADeviceForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteMFADeviceForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mfadevice_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mfadevice_for_user_with_options(request, runtime)

    def delete_scimserver_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteSCIMServerCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scimserver_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scimserver_credential_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def deprovision_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeprovisionAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def deprovision_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deprovision_access_configuration_with_options(request, runtime)

    def disable_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DisableServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_service(self):
        runtime = util_models.RuntimeOptions()
        return self.disable_service_with_options(runtime)

    def enable_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.EnableServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_service(self):
        runtime = util_models.RuntimeOptions()
        return self.enable_service_with_options(runtime)

    def get_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_access_configuration_with_options(request, runtime)

    def get_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_directory_with_options(request, runtime)

    def get_directory_samlservice_provider_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectorySAMLServiceProviderInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_directory_samlservice_provider_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_directory_samlservice_provider_info_with_options(request, runtime)

    def get_directory_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectoryStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_directory_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_directory_statistics_with_options(request, runtime)

    def get_external_samlidentity_provider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_external_samlidentity_provider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_external_samlidentity_provider_with_options(request, runtime)

    def get_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    def get_mfaauthentication_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mfaauthentication_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mfaauthentication_settings_with_options(request, runtime)

    def get_mfaauthentication_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mfaauthentication_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mfaauthentication_status_with_options(request, runtime)

    def get_scimsynchronization_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scimsynchronization_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scimsynchronization_status_with_options(request, runtime)

    def get_service_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetServiceStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_status(self):
        runtime = util_models.RuntimeOptions()
        return self.get_service_status_with_options(runtime)

    def get_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    def get_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def get_user_mfaauthentication_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_mfaauthentication_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfaauthentication_settings_with_options(request, runtime)

    def list_access_assignments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessAssignments',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessAssignmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_assignments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_assignments_with_options(request, runtime)

    def list_access_configuration_provisionings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provisioning_status):
            query['ProvisioningStatus'] = request.provisioning_status
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurationProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_configuration_provisionings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_configuration_provisionings_with_options(request, runtime)

    def list_access_configurations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_notifications):
            query['StatusNotifications'] = request.status_notifications
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurations',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_configurations_with_options(request, runtime)

    def list_directories_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDirectories',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_directories(self):
        runtime = util_models.RuntimeOptions()
        return self.list_directories_with_options(runtime)

    def list_external_samlid_pcertificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalSAMLIdPCertificates',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_external_samlid_pcertificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_external_samlid_pcertificates_with_options(request, runtime)

    def list_group_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMembers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_members_with_options(request, runtime)

    def list_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provision_type):
            query['ProvisionType'] = request.provision_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    def list_joined_groups_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJoinedGroupsForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListJoinedGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_joined_groups_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_joined_groups_for_user_with_options(request, runtime)

    def list_mfadevices_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMFADevicesForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListMFADevicesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mfadevices_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mfadevices_for_user_with_options(request, runtime)

    def list_permission_policies_in_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionPoliciesInAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_permission_policies_in_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_permission_policies_in_access_configuration_with_options(request, runtime)

    def list_scimserver_credentials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSCIMServerCredentials',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListSCIMServerCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scimserver_credentials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scimserver_credentials_with_options(request, runtime)

    def list_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provision_type):
            query['ProvisionType'] = request.provision_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def provision_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ProvisionAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def provision_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.provision_access_configuration_with_options(request, runtime)

    def remove_external_samlid_pcertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_external_samlid_pcertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_external_samlid_pcertificate_with_options(request, runtime)

    def remove_permission_policy_from_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePermissionPolicyFromAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_permission_policy_from_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_permission_policy_from_access_configuration_with_options(request, runtime)

    def remove_user_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_user_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    def reset_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.generate_random_password):
            query['GenerateRandomPassword'] = request.generate_random_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.require_password_reset_for_next_login):
            query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    def set_external_samlidentity_provider_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.encoded_metadata_document):
            query['EncodedMetadataDocument'] = request.encoded_metadata_document
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.login_url):
            query['LoginUrl'] = request.login_url
        if not UtilClient.is_unset(request.ssostatus):
            query['SSOStatus'] = request.ssostatus
        if not UtilClient.is_unset(request.want_request_signed):
            query['WantRequestSigned'] = request.want_request_signed
        if not UtilClient.is_unset(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    def set_external_samlidentity_provider(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_external_samlidentity_provider_with_options(request, runtime)

    def set_mfaauthentication_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfaauthentication_status):
            query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetMFAAuthenticationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_mfaauthentication_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_mfaauthentication_status_with_options(request, runtime)

    def set_scimsynchronization_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.scimsynchronization_status):
            query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scimsynchronization_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scimsynchronization_status_with_options(request, runtime)

    def update_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_relay_state):
            query['NewRelayState'] = request.new_relay_state
        if not UtilClient.is_unset(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_access_configuration_with_options(request, runtime)

    def update_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_directory_name):
            query['NewDirectoryName'] = request.new_directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_directory_with_options(request, runtime)

    def update_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    def update_inline_policy_for_access_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.inline_policy_name):
            query['InlinePolicyName'] = request.inline_policy_name
        if not UtilClient.is_unset(request.new_inline_policy_document):
            query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInlinePolicyForAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_inline_policy_for_access_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_inline_policy_for_access_configuration_with_options(request, runtime)

    def update_mfaauthentication_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfaauthentication_settings):
            query['MFAAuthenticationSettings'] = request.mfaauthentication_settings
        if not UtilClient.is_unset(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mfaauthentication_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mfaauthentication_settings_with_options(request, runtime)

    def update_scimserver_credential_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_status):
            query['NewStatus'] = request.new_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSCIMServerCredentialStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scimserver_credential_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scimserver_credential_status_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_email):
            query['NewEmail'] = request.new_email
        if not UtilClient.is_unset(request.new_first_name):
            query['NewFirstName'] = request.new_first_name
        if not UtilClient.is_unset(request.new_last_name):
            query['NewLastName'] = request.new_last_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_user_mfaauthentication_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_mfaauthentication_settings):
            query['UserMFAAuthenticationSettings'] = request.user_mfaauthentication_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_mfaauthentication_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_mfaauthentication_settings_with_options(request, runtime)

    def update_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_status):
            query['NewStatus'] = request.new_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_status_with_options(request, runtime)
