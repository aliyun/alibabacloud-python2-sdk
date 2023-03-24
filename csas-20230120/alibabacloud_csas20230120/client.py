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

    def create_private_access_application_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreatePrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        if not UtilClient.is_unset(tmp_req.port_ranges):
            request.port_ranges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.port_ranges, 'PortRanges', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges_shrink):
            body['PortRanges'] = request.port_ranges_shrink
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
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

    def create_private_access_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreatePrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        if not UtilClient.is_unset(tmp_req.custom_user_attributes):
            request.custom_user_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_user_attributes, 'CustomUserAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes_shrink):
            body['CustomUserAttributes'] = request.custom_user_attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.user_group_ids_shrink):
            body['UserGroupIds'] = request.user_group_ids_shrink
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
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

    def create_user_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
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

    def list_applications_for_private_access_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListApplicationsForPrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_ids):
            request.policy_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_ids, 'PolicyIds', 'json')
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

    def list_applications_for_private_access_tag_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListApplicationsForPrivateAccessTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
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

    def list_connectors_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListConnectorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.connector_ids):
            request.connector_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.connector_ids, 'ConnectorIds', 'json')
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

    def list_polices_for_private_access_application_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListPolicesForPrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
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

    def list_polices_for_private_access_tag_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListPolicesForPrivateAccessTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
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

    def list_polices_for_user_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListPolicesForUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
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

    def list_private_access_applications_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListPrivateAccessApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
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

    def list_private_access_polices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListPrivateAccessPolicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_ids):
            request.policy_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_ids, 'PolicyIds', 'json')
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

    def list_private_access_tags_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListPrivateAccessTagsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
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

    def list_tags_for_private_access_application_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListTagsForPrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
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

    def list_tags_for_private_access_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListTagsForPrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_ids):
            request.policy_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_ids, 'PolicyIds', 'json')
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

    def list_user_groups_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListUserGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
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

    def list_user_groups_for_private_access_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.ListUserGroupsForPrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_ids):
            request.policy_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_ids, 'PolicyIds', 'json')
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

    def update_private_access_application_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdatePrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        if not UtilClient.is_unset(tmp_req.port_ranges):
            request.port_ranges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.port_ranges, 'PortRanges', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.port_ranges_shrink):
            body['PortRanges'] = request.port_ranges_shrink
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
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

    def update_private_access_policy_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdatePrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        if not UtilClient.is_unset(tmp_req.custom_user_attributes):
            request.custom_user_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_user_attributes, 'CustomUserAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes_shrink):
            body['CustomUserAttributes'] = request.custom_user_attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
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
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.user_group_ids_shrink):
            body['UserGroupIds'] = request.user_group_ids_shrink
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
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

    def update_user_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdateUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
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
