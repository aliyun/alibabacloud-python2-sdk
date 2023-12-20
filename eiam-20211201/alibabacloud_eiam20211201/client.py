# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eiam20211201 import models as eiam_20211201_models
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
        self._endpoint = self.get_endpoint('eiam', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_organizational_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddUserToOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_to_organizational_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_organizational_units_with_options(request, runtime)

    def add_users_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddUsersToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_users_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_group_with_options(request, runtime)

    def authorize_application_to_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_application_to_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_application_to_groups_with_options(request, runtime)

    def authorize_application_to_organizational_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_application_to_organizational_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_application_to_organizational_units_with_options(request, runtime)

    def authorize_application_to_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_application_to_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_application_to_users_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        """
        IDaaS EIAM supports the following two standard single sign-on (SSO) protocols for adding applications: SAML 2.0 and OIDC. You can select an SSO protocol based on your business requirements when you add an application. You cannot change the SSO protocol that you selected after the application is added.
        

        @param request: CreateApplicationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_source_type):
            query['ApplicationSourceType'] = request.application_source_type
        if not UtilClient.is_unset(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.sso_type):
            query['SsoType'] = request.sso_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application(self, request):
        """
        IDaaS EIAM supports the following two standard single sign-on (SSO) protocols for adding applications: SAML 2.0 and OIDC. You can select an SSO protocol based on your business requirements when you add an application. You cannot change the SSO protocol that you selected after the application is added.
        

        @param request: CreateApplicationRequest

        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def create_application_client_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application_client_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_client_secret_with_options(request, runtime)

    def create_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.filing):
            query['Filing'] = request.filing
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_domain_proxy_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain_proxy_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_proxy_token_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_network_access_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def create_network_access_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_access_endpoint_with_options(request, runtime)

    def create_organizational_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            query['OrganizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def create_organizational_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_organizational_unit_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_initialization_config):
            query['PasswordInitializationConfig'] = request.password_initialization_config
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.primary_organizational_unit_id):
            query['PrimaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def delete_application_with_options(self, request, runtime):
        """
        Make sure that the EIAM application that you want to delete is not used before you delete the EIAM application. After you delete the EIAM application, all configurations are deleted and cannot be restored.
        

        @param request: DeleteApplicationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application(self, request):
        """
        Make sure that the EIAM application that you want to delete is not used before you delete the EIAM application. After you delete the EIAM application, all configurations are deleted and cannot be restored.
        

        @param request: DeleteApplicationRequest

        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    def delete_application_client_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application_client_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_application_client_secret_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_domain_proxy_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_proxy_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_proxy_token_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        """
        Make sure that the instance to be deleted is no longer used. If the instance is deleted, all data related to the instance will be deleted.
        

        @param request: DeleteInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        """
        Make sure that the instance to be deleted is no longer used. If the instance is deleted, all data related to the instance will be deleted.
        

        @param request: DeleteInstanceRequest

        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_network_access_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_network_access_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_access_endpoint_with_options(request, runtime)

    def delete_organizational_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_organizational_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_organizational_unit_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def disable_application_with_options(self, request, runtime):
        """
        All features of the EIAM application cannot be used if you disable the EIAM application, such as single sign-on (SSO) and account synchronization. Make sure that you acknowledge the risks of the delete operation.
        

        @param request: DisableApplicationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application(self, request):
        """
        All features of the EIAM application cannot be used if you disable the EIAM application, such as single sign-on (SSO) and account synchronization. Make sure that you acknowledge the risks of the delete operation.
        

        @param request: DisableApplicationRequest

        @return: DisableApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_with_options(request, runtime)

    def disable_application_api_invoke_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationApiInvoke',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application_api_invoke(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_application_api_invoke_with_options(request, runtime)

    def disable_application_client_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application_client_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_application_client_secret_with_options(request, runtime)

    def disable_application_provisioning_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationProvisioning',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application_provisioning(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_application_provisioning_with_options(request, runtime)

    def disable_application_sso_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationSso',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationSsoResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application_sso(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_application_sso_with_options(request, runtime)

    def disable_domain_proxy_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_domain_proxy_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_domain_proxy_token_with_options(request, runtime)

    def disable_init_domain_auto_redirect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInitDomainAutoRedirect',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableInitDomainAutoRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_init_domain_auto_redirect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_init_domain_auto_redirect_with_options(request, runtime)

    def disable_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableUserResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_user_with_options(request, runtime)

    def enable_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_application_with_options(request, runtime)

    def enable_application_api_invoke_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationApiInvoke',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application_api_invoke(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_application_api_invoke_with_options(request, runtime)

    def enable_application_client_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application_client_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_application_client_secret_with_options(request, runtime)

    def enable_application_provisioning_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationProvisioning',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application_provisioning(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_application_provisioning_with_options(request, runtime)

    def enable_application_sso_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationSso',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationSsoResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application_sso(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_application_sso_with_options(request, runtime)

    def enable_domain_proxy_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_domain_proxy_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_domain_proxy_token_with_options(request, runtime)

    def enable_init_domain_auto_redirect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInitDomainAutoRedirect',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableInitDomainAutoRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_init_domain_auto_redirect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_init_domain_auto_redirect_with_options(request, runtime)

    def enable_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableUserResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_user_with_options(request, runtime)

    def get_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    def get_application_grant_scope_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationGrantScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationGrantScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_grant_scope(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_grant_scope_with_options(request, runtime)

    def get_application_provisioning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationProvisioningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_provisioning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_provisioning_config_with_options(request, runtime)

    def get_application_provisioning_scope_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_provisioning_scope(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_provisioning_scope_with_options(request, runtime)

    def get_application_sso_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationSsoConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationSsoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_sso_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_application_sso_config_with_options(request, runtime)

    def get_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_with_options(request, runtime)

    def get_domain_dns_challenge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainDnsChallenge',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetDomainDnsChallengeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain_dns_challenge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_dns_challenge_with_options(request, runtime)

    def get_forget_password_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetForgetPasswordConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetForgetPasswordConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_forget_password_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_forget_password_configuration_with_options(request, runtime)

    def get_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_network_access_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def get_network_access_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_network_access_endpoint_with_options(request, runtime)

    def get_organizational_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organizational_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_organizational_unit_with_options(request, runtime)

    def get_password_complexity_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordComplexityConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordComplexityConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_password_complexity_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_password_complexity_configuration_with_options(request, runtime)

    def get_password_expiration_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordExpirationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordExpirationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_password_expiration_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_password_expiration_configuration_with_options(request, runtime)

    def get_password_history_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordHistoryConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordHistoryConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_password_history_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_password_history_configuration_with_options(request, runtime)

    def get_password_initialization_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordInitializationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordInitializationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_password_initialization_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_password_initialization_configuration_with_options(request, runtime)

    def get_root_organizational_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRootOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetRootOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_root_organizational_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_root_organizational_unit_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def list_application_client_secrets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationClientSecrets',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationClientSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_application_client_secrets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_application_client_secrets_with_options(request, runtime)

    def list_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    def list_applications_for_organizational_unit_with_options(self, request, runtime):
        """
        You can only query the permissions that are directly granted to the EIAM organization by calling the ListApplicationsForOrganizationalUnit operation. You can filter applications by configuring the *ApplicationIds** parameter when you call this operation.
        

        @param request: ListApplicationsForOrganizationalUnitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListApplicationsForOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications_for_organizational_unit(self, request):
        """
        You can only query the permissions that are directly granted to the EIAM organization by calling the ListApplicationsForOrganizationalUnit operation. You can filter applications by configuring the *ApplicationIds** parameter when you call this operation.
        

        @param request: ListApplicationsForOrganizationalUnitRequest

        @return: ListApplicationsForOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_organizational_unit_with_options(request, runtime)

    def list_applications_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_user_with_options(request, runtime)

    def list_domain_proxy_tokens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomainProxyTokens',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListDomainProxyTokensResponse(),
            self.call_api(params, req, runtime)
        )

    def list_domain_proxy_tokens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_domain_proxy_tokens_with_options(request, runtime)

    def list_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    def list_eiam_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEiamInstances',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListEiamInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_eiam_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_eiam_instances_with_options(request, runtime)

    def list_eiam_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEiamRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListEiamRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_eiam_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_eiam_regions_with_options(runtime)

    def list_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_name_starts_with):
            query['GroupNameStartsWith'] = request.group_name_starts_with
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    def list_groups_for_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups_for_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_application_with_options(request, runtime)

    def list_groups_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ListGroupsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_network_access_endpoint_available_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListNetworkAccessEndpointAvailableRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_network_access_endpoint_available_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_endpoint_available_regions_with_options(runtime)

    def list_network_access_endpoint_available_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nae_region_id):
            query['NaeRegionId'] = request.nae_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessEndpointAvailableZones',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_network_access_endpoint_available_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_endpoint_available_zones_with_options(request, runtime)

    def list_network_access_endpoints_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_status):
            query['NetworkAccessEndpointStatus'] = request.network_access_endpoint_status
        if not UtilClient.is_unset(request.network_access_endpoint_type):
            query['NetworkAccessEndpointType'] = request.network_access_endpoint_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessEndpoints',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_network_access_endpoints(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_endpoints_with_options(request, runtime)

    def list_network_access_paths_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessPaths',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessPathsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_network_access_paths(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_paths_with_options(request, runtime)

    def list_organizational_unit_parents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitParents',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitParentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizational_unit_parents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_organizational_unit_parents_with_options(request, runtime)

    def list_organizational_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.organizational_unit_name_starts_with):
            query['OrganizationalUnitNameStartsWith'] = request.organizational_unit_name_starts_with
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizational_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_organizational_units_with_options(request, runtime)

    def list_organizational_units_for_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitsForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizational_units_for_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_organizational_units_for_application_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name_starts_with):
            query['DisplayNameStartsWith'] = request.display_name_starts_with
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.user_source_id):
            query['UserSourceId'] = request.user_source_id
        if not UtilClient.is_unset(request.user_source_type):
            query['UserSourceType'] = request.user_source_type
        if not UtilClient.is_unset(request.username_starts_with):
            query['UsernameStartsWith'] = request.username_starts_with
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_users_for_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users_for_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_application_with_options(request, runtime)

    def list_users_for_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users_for_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    def obtain_application_client_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def obtain_application_client_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.obtain_application_client_secret_with_options(request, runtime)

    def obtain_domain_proxy_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def obtain_domain_proxy_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.obtain_domain_proxy_token_with_options(request, runtime)

    def remove_user_from_organizational_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_user_from_organizational_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_organizational_units_with_options(request, runtime)

    def remove_users_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveUsersFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_users_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_group_with_options(request, runtime)

    def revoke_application_from_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_application_from_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_application_from_groups_with_options(request, runtime)

    def revoke_application_from_organizational_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_application_from_organizational_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_application_from_organizational_units_with_options(request, runtime)

    def revoke_application_from_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_application_from_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_application_from_users_with_options(request, runtime)

    def set_application_grant_scope_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.grant_scopes):
            query['GrantScopes'] = request.grant_scopes
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationGrantScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationGrantScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_application_grant_scope(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_application_grant_scope_with_options(request, runtime)

    def set_application_provisioning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.callback_provisioning_config):
            query['CallbackProvisioningConfig'] = request.callback_provisioning_config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.provision_password):
            query['ProvisionPassword'] = request.provision_password
        if not UtilClient.is_unset(request.provision_protocol_type):
            query['ProvisionProtocolType'] = request.provision_protocol_type
        if not UtilClient.is_unset(request.scim_provisioning_config):
            query['ScimProvisioningConfig'] = request.scim_provisioning_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationProvisioningConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationProvisioningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_application_provisioning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_application_provisioning_config_with_options(request, runtime)

    def set_application_provisioning_scope_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationProvisioningScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_application_provisioning_scope(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_application_provisioning_scope_with_options(request, runtime)

    def set_application_sso_config_with_options(self, request, runtime):
        """
        In IDaaS EIAM, the application management feature supports multiple SSO protocols for applications, including SAML 2.0 and OIDC protocols. Each application supports only one protocol, and the protocol cannot be changed after the application is created. You can specify the SSO configuration attributes of an application based on the supported SSO protocol.
        

        @param request: SetApplicationSsoConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetApplicationSsoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.init_login_type):
            query['InitLoginType'] = request.init_login_type
        if not UtilClient.is_unset(request.init_login_url):
            query['InitLoginUrl'] = request.init_login_url
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oidc_sso_config):
            query['OidcSsoConfig'] = request.oidc_sso_config
        if not UtilClient.is_unset(request.saml_sso_config):
            query['SamlSsoConfig'] = request.saml_sso_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationSsoConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationSsoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_application_sso_config(self, request):
        """
        In IDaaS EIAM, the application management feature supports multiple SSO protocols for applications, including SAML 2.0 and OIDC protocols. Each application supports only one protocol, and the protocol cannot be changed after the application is created. You can specify the SSO configuration attributes of an application based on the supported SSO protocol.
        

        @param request: SetApplicationSsoConfigRequest

        @return: SetApplicationSsoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_application_sso_config_with_options(request, runtime)

    def set_default_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    def set_forget_password_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_channels):
            query['AuthenticationChannels'] = request.authentication_channels
        if not UtilClient.is_unset(request.forget_password_status):
            query['ForgetPasswordStatus'] = request.forget_password_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForgetPasswordConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetForgetPasswordConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_forget_password_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_forget_password_configuration_with_options(request, runtime)

    def set_password_complexity_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_complexity_rules):
            query['PasswordComplexityRules'] = request.password_complexity_rules
        if not UtilClient.is_unset(request.password_min_length):
            query['PasswordMinLength'] = request.password_min_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordComplexityConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordComplexityConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_password_complexity_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_complexity_configuration_with_options(request, runtime)

    def set_password_expiration_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_expiration_action):
            query['PasswordExpirationAction'] = request.password_expiration_action
        if not UtilClient.is_unset(request.password_expiration_notification_channels):
            query['PasswordExpirationNotificationChannels'] = request.password_expiration_notification_channels
        if not UtilClient.is_unset(request.password_expiration_notification_duration):
            query['PasswordExpirationNotificationDuration'] = request.password_expiration_notification_duration
        if not UtilClient.is_unset(request.password_expiration_notification_status):
            query['PasswordExpirationNotificationStatus'] = request.password_expiration_notification_status
        if not UtilClient.is_unset(request.password_expiration_status):
            query['PasswordExpirationStatus'] = request.password_expiration_status
        if not UtilClient.is_unset(request.password_forced_update_duration):
            query['PasswordForcedUpdateDuration'] = request.password_forced_update_duration
        if not UtilClient.is_unset(request.password_valid_max_day):
            query['PasswordValidMaxDay'] = request.password_valid_max_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordExpirationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordExpirationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_password_expiration_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_expiration_configuration_with_options(request, runtime)

    def set_password_history_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_history_max_retention):
            query['PasswordHistoryMaxRetention'] = request.password_history_max_retention
        if not UtilClient.is_unset(request.password_history_status):
            query['PasswordHistoryStatus'] = request.password_history_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordHistoryConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordHistoryConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_password_history_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_history_configuration_with_options(request, runtime)

    def set_password_initialization_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not UtilClient.is_unset(request.password_initialization_notification_channels):
            query['PasswordInitializationNotificationChannels'] = request.password_initialization_notification_channels
        if not UtilClient.is_unset(request.password_initialization_status):
            query['PasswordInitializationStatus'] = request.password_initialization_status
        if not UtilClient.is_unset(request.password_initialization_type):
            query['PasswordInitializationType'] = request.password_initialization_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordInitializationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordInitializationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_password_initialization_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_password_initialization_configuration_with_options(request, runtime)

    def set_user_primary_organizational_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserPrimaryOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def set_user_primary_organizational_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_primary_organizational_unit_with_options(request, runtime)

    def unlock_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UnlockUserResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_user_with_options(request, runtime)

    def update_application_authorization_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationAuthorizationType',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_authorization_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_application_authorization_type_with_options(request, runtime)

    def update_application_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_application_description_with_options(request, runtime)

    def update_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    def update_group_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateGroupDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_description_with_options(request, runtime)

    def update_instance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_description_with_options(request, runtime)

    def update_network_access_endpoint_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkAccessEndpointName',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_network_access_endpoint_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_network_access_endpoint_name_with_options(request, runtime)

    def update_organizational_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def update_organizational_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_organizational_unit_with_options(request, runtime)

    def update_organizational_unit_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnitDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_organizational_unit_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_organizational_unit_description_with_options(request, runtime)

    def update_organizational_unit_parent_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnitParentId',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse(),
            self.call_api(params, req, runtime)
        )

    def update_organizational_unit_parent_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_organizational_unit_parent_id_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_user_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_description_with_options(request, runtime)

    def update_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_notification_channels):
            query['UserNotificationChannels'] = request.user_notification_channels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_password_with_options(request, runtime)
