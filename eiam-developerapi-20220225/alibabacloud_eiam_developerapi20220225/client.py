# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eiam_developerapi20220225 import models as eiam_developerapi_20220225_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eiam-developerapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_organizational_unit(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateOrganizationalUnitHeaders()
        return self.create_organizational_unit_with_options(instance_id, application_id, request, headers, runtime)

    def create_organizational_unit_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateUserHeaders()
        return self.create_user_with_options(instance_id, application_id, request, headers, runtime)

    def create_user_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.password_initialization_config):
            body['passwordInitializationConfig'] = request.password_initialization_config
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.primary_organizational_unit_id):
            body['primaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not UtilClient.is_unset(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_organizational_unit(self, instance_id, application_id, organizational_unit_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteOrganizationalUnitHeaders()
        return self.delete_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    def delete_organizational_unit_with_options(self, instance_id, application_id, organizational_unit_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organizational_unit_id))),
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, instance_id, application_id, user_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteUserHeaders()
        return self.delete_user_with_options(instance_id, application_id, user_id, headers, runtime)

    def delete_user_with_options(self, instance_id, application_id, user_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_user(self, instance_id, application_id, user_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DisableUserHeaders()
        return self.disable_user_with_options(instance_id, application_id, user_id, headers, runtime)

    def disable_user_with_options(self, instance_id, application_id, user_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/%s/actions/disable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DisableUserResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_user(self, instance_id, application_id, user_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.EnableUserHeaders()
        return self.enable_user_with_options(instance_id, application_id, user_id, headers, runtime)

    def enable_user_with_options(self, instance_id, application_id, user_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/%s/actions/enable' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.EnableUserResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_device_code(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_device_code_with_options(instance_id, application_id, request, headers, runtime)

    def generate_device_code_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceCode',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/oauth2/device/code' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GenerateDeviceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_token(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_token_with_options(instance_id, application_id, request, headers, runtime)

    def generate_token_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            query['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        if not UtilClient.is_unset(request.code_verifier):
            query['code_verifier'] = request.code_verifier
        if not UtilClient.is_unset(request.device_code):
            query['device_code'] = request.device_code
        if not UtilClient.is_unset(request.exclusive_tag):
            query['exclusive_tag'] = request.exclusive_tag
        if not UtilClient.is_unset(request.grant_type):
            query['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            query['refresh_token'] = request.refresh_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateToken',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/oauth2/token' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GenerateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application_provisioning_scope(self, instance_id, application_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetApplicationProvisioningScopeHeaders()
        return self.get_application_provisioning_scope_with_options(instance_id, application_id, headers, runtime)

    def get_application_provisioning_scope_with_options(self, instance_id, application_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningScope',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/provisioningScope' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organizational_unit(self, instance_id, application_id, organizational_unit_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetOrganizationalUnitHeaders()
        return self.get_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    def get_organizational_unit_with_options(self, instance_id, application_id, organizational_unit_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organizational_unit_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organizational_unit_id_by_external_id(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdHeaders()
        return self.get_organizational_unit_id_by_external_id_with_options(instance_id, application_id, request, headers, runtime)

    def get_organizational_unit_id_by_external_id_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_source_id):
            body['organizationalUnitSourceId'] = request.organizational_unit_source_id
        if not UtilClient.is_unset(request.organizational_unit_source_type):
            body['organizationalUnitSourceType'] = request.organizational_unit_source_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnitIdByExternalId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits/_/actions/getOrganizationalUnitIdByExternalId' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, instance_id, application_id, user_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserHeaders()
        return self.get_user_with_options(instance_id, application_id, user_id, headers, runtime)

    def get_user_with_options(self, instance_id, application_id, user_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_id_by_email(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByEmailHeaders()
        return self.get_user_id_by_email_with_options(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_email_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByEmail',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/_/actions/getUserIdByEmail' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_id_by_phone_number(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByPhoneNumberHeaders()
        return self.get_user_id_by_phone_number_with_options(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_phone_number_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByPhoneNumber',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/_/actions/getUserIdByPhoneNumber' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_id_by_user_external_id(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByUserExternalIdHeaders()
        return self.get_user_id_by_user_external_id_with_options(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_user_external_id_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_source_id):
            body['userSourceId'] = request.user_source_id
        if not UtilClient.is_unset(request.user_source_type):
            body['userSourceType'] = request.user_source_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByUserExternalId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/_/actions/getUserIdByExternalId' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_id_by_username(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByUsernameHeaders()
        return self.get_user_id_by_username_with_options(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_username_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByUsername',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/_/actions/getUserIdByUsername' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByUsernameResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_info(self, instance_id, application_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserInfoHeaders()
        return self.get_user_info_with_options(instance_id, application_id, headers, runtime)

    def get_user_info_with_options(self, instance_id, application_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/oauth2/userinfo' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizational_unit_parent_ids(self, instance_id, application_id, organizational_unit_id):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsHeaders()
        return self.list_organizational_unit_parent_ids_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    def list_organizational_unit_parent_ids_with_options(self, instance_id, application_id, organizational_unit_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitParentIds',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits/%s/parentIds' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organizational_unit_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organizational_units(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListOrganizationalUnitsHeaders()
        return self.list_organizational_units_with_options(instance_id, application_id, request, headers, runtime)

    def list_organizational_units_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListUsersHeaders()
        return self.list_users_with_options(instance_id, application_id, request, headers, runtime)

    def list_users_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['organizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def patch_organizational_unit(self, instance_id, application_id, organizational_unit_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchOrganizationalUnitHeaders()
        return self.patch_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, request, headers, runtime)

    def patch_organizational_unit_with_options(self, instance_id, application_id, organizational_unit_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/organizationalUnits/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(organizational_unit_id))),
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def patch_user(self, instance_id, application_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchUserHeaders()
        return self.patch_user_with_options(instance_id, application_id, user_id, request, headers, runtime)

    def patch_user_with_options(self, instance_id, application_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/users/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(user_id))),
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchUserResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_token(self, instance_id, application_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_token_with_options(instance_id, application_id, request, headers, runtime)

    def revoke_token_with_options(self, instance_id, application_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            query['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        if not UtilClient.is_unset(request.token_type_hint):
            query['token_type_hint'] = request.token_type_hint
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeToken',
            version='2022-02-25',
            protocol='HTTPS',
            pathname='/v2/%s/%s/oauth2/revoke' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(application_id))),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RevokeTokenResponse(),
            self.call_api(params, req, runtime)
        )
