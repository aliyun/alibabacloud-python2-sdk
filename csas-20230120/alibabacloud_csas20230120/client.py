# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_csas20230120 import models as csas_20230120_models
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
        self._endpoint = self.get_endpoint('csas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_application_2connector_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.AttachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.AttachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_application_2connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_application_2connector_with_options(request, runtime)

    def create_dynamic_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dynamic_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dynamic_route_with_options(request, runtime)

    def create_private_access_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_private_access_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_application_with_options(request, runtime)

    def create_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_policy_with_options(request, runtime)

    def create_private_access_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_private_access_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_tag_with_options(request, runtime)

    def create_registration_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateRegistrationPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.company_limit_count):
            request.company_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not UtilClient.is_unset(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not UtilClient.is_unset(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not UtilClient.is_unset(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not UtilClient.is_unset(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_registration_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_registration_policy_with_options(request, runtime)

    def create_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    def delete_dynamic_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dynamic_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_route_with_options(request, runtime)

    def delete_private_access_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_private_access_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_application_with_options(request, runtime)

    def delete_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_policy_with_options(request, runtime)

    def delete_private_access_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_private_access_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_tag_with_options(request, runtime)

    def delete_registration_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.policy_ids):
            body_flat['PolicyIds'] = request.policy_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRegistrationPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteRegistrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_registration_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_registration_policies_with_options(request, runtime)

    def delete_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    def detach_application_2connector_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.DetachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DetachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_application_2connector(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_application_2connector_with_options(request, runtime)

    def get_dynamic_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dynamic_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dynamic_route_with_options(request, runtime)

    def get_private_access_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_private_access_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_application_with_options(request, runtime)

    def get_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_policy_with_options(request, runtime)

    def get_registration_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_registration_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_registration_policy_with_options(request, runtime)

    def get_user_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserDevice',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_device_with_options(request, runtime)

    def get_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    def list_applications_for_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications_for_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_private_access_policy_with_options(request, runtime)

    def list_applications_for_private_access_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications_for_private_access_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_private_access_tag_with_options(request, runtime)

    def list_connectors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectors',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connectors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connectors_with_options(request, runtime)

    def list_dynamic_route_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDynamicRouteRegions',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRouteRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dynamic_route_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_route_regions_with_options(runtime)

    def list_dynamic_routes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicRoutes',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dynamic_routes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_routes_with_options(request, runtime)

    def list_excessive_device_registration_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExcessiveDeviceRegistrationApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_excessive_device_registration_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_excessive_device_registration_applications_with_options(request, runtime)

    def list_polices_for_private_access_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_polices_for_private_access_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_private_access_application_with_options(request, runtime)

    def list_polices_for_private_access_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    def list_polices_for_private_access_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_private_access_tag_with_options(request, runtime)

    def list_polices_for_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_polices_for_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_user_group_with_options(request, runtime)

    def list_pop_traffic_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPopTrafficStatistics',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPopTrafficStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pop_traffic_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pop_traffic_statistics_with_options(request, runtime)

    def list_private_access_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_access_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_applications_with_options(request, runtime)

    def list_private_access_applications_for_dynamic_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplicationsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_access_applications_for_dynamic_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_applications_for_dynamic_route_with_options(request, runtime)

    def list_private_access_polices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessPolices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessPolicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_access_polices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_polices_with_options(request, runtime)

    def list_private_access_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTags',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_access_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_tags_with_options(request, runtime)

    def list_private_access_tags_for_dynamic_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTagsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def list_private_access_tags_for_dynamic_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_tags_for_dynamic_route_with_options(request, runtime)

    def list_registration_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistrationPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListRegistrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_registration_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_registration_policies_with_options(request, runtime)

    def list_registration_policies_for_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistrationPoliciesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_registration_policies_for_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_registration_policies_for_user_group_with_options(request, runtime)

    def list_software_for_user_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwareForUserDevice',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListSoftwareForUserDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_software_for_user_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_software_for_user_device_with_options(request, runtime)

    def list_tags_for_private_access_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags_for_private_access_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tags_for_private_access_application_with_options(request, runtime)

    def list_tags_for_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags_for_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tags_for_private_access_policy_with_options(request, runtime)

    def list_user_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_devices_with_options(request, runtime)

    def list_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    def list_user_groups_for_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_groups_for_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_for_private_access_policy_with_options(request, runtime)

    def list_user_groups_for_registration_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_groups_for_registration_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_for_registration_policy_with_options(request, runtime)

    def update_dynamic_route_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dynamic_route(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dynamic_route_with_options(request, runtime)

    def update_excessive_device_registration_applications_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExcessiveDeviceRegistrationApplicationsStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_excessive_device_registration_applications_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_excessive_device_registration_applications_status_with_options(request, runtime)

    def update_private_access_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_private_access_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_private_access_application_with_options(request, runtime)

    def update_private_access_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_private_access_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_private_access_policy_with_options(request, runtime)

    def update_registration_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdateRegistrationPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.company_limit_count):
            request.company_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not UtilClient.is_unset(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not UtilClient.is_unset(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not UtilClient.is_unset(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not UtilClient.is_unset(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_registration_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_registration_policy_with_options(request, runtime)

    def update_user_devices_sharing_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not UtilClient.is_unset(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDevicesSharingStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserDevicesSharingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_devices_sharing_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_devices_sharing_status_with_options(request, runtime)

    def update_user_devices_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_action):
            body['DeviceAction'] = request.device_action
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDevicesStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserDevicesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_devices_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_devices_status_with_options(request, runtime)

    def update_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)
