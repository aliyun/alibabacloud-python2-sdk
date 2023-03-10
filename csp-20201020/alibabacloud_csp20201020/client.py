# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_csp20201020 import models as csp_20201020_models
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
        self._endpoint = self.get_endpoint('csp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_acl_authorization_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation):
            query['AclOperation'] = request.acl_operation
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.pattern_type):
            query['PatternType'] = request.pattern_type
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAclAuthorization',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/add_acl_authorization',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.AddAclAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_acl_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_acl_authorization_with_options(request, headers, runtime)

    def add_authenticated_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAuthenticatedUser',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/add_user',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.AddAuthenticatedUserResponse(),
            self.call_api(params, req, runtime)
        )

    def add_authenticated_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_authenticated_user_with_options(request, headers, runtime)

    def check_cluster_name_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckClusterName',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/cluster_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    def check_cluster_name(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_cluster_name_with_options(request, headers, runtime)

    def check_inventory_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckInventory',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/inventory',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    def check_inventory(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_inventory_with_options(request, headers, runtime)

    def check_left_cu_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cu_num):
            query['CuNum'] = request.cu_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLeftCu',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/cu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckLeftCuResponse(),
            self.call_api(params, req, runtime)
        )

    def check_left_cu(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_left_cu_with_options(request, headers, runtime)

    def check_user_account_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckUserAccount',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/user_account',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckUserAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def check_user_account(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_user_account_with_options(headers, runtime)

    def check_user_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserResource',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/user_resource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckUserResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_user_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_user_resource_with_options(request, headers, runtime)

    def check_vpc_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckVpc',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/vpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def check_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_vpc_with_options(request, headers, runtime)

    def check_vswitch_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckVswitch',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/check/vswitch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CheckVswitchResponse(),
            self.call_api(params, req, runtime)
        )

    def check_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_vswitch_with_options(request, headers, runtime)

    def create_cluster_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    def create_default_role_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDefaultRole',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CreateDefaultRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_default_role(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_default_role_with_options(request, headers, runtime)

    def create_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.order_info):
            query['OrderInfo'] = request.order_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/order/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_order_with_options(request, headers, runtime)

    def delete_acl_authorization_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation):
            query['AclOperation'] = request.acl_operation
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pattern_type):
            query['PatternType'] = request.pattern_type
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAclAuthorization',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/delete_acl_authorization',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.DeleteAclAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_acl_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_acl_authorization_with_options(request, headers, runtime)

    def delete_authenticated_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthenticatedUser',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/delete_user',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.DeleteAuthenticatedUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_authenticated_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_authenticated_user_with_options(request, headers, runtime)

    def get_cluster_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDetail',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_detail_with_options(request, headers, runtime)

    def get_config_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConfigInfo',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/config_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetConfigInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_config_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_config_info_with_options(headers, runtime)

    def get_csp_connector_deployed_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCspConnectorDeployedList',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/connectors_deployed',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetCspConnectorDeployedListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_csp_connector_deployed_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_csp_connector_deployed_list_with_options(request, headers, runtime)

    def get_csp_specification_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCspSpecificationInfo',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/specification_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetCspSpecificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_csp_specification_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_csp_specification_info_with_options(headers, runtime)

    def get_csp_upgrade_limit_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCspUpgradeLimitInfo',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/upgrade_limit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetCspUpgradeLimitInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_csp_upgrade_limit_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_csp_upgrade_limit_info_with_options(headers, runtime)

    def get_renew_spec_version_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenewSpecVersionInfo',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/renew_spec_version_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetRenewSpecVersionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_renew_spec_version_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_renew_spec_version_info_with_options(request, headers, runtime)

    def get_spec_version_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSpecVersionInfo',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/spec_version_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetSpecVersionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_spec_version_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_spec_version_info_with_options(headers, runtime)

    def get_user_acl_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pattern_type):
            query['PatternType'] = request.pattern_type
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserAclDetail',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/user_acl_detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetUserAclDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_acl_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_acl_detail_with_options(request, headers, runtime)

    def get_version_infos_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVersionInfos',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/version_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.GetVersionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def get_version_infos(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_version_infos_with_options(headers, runtime)

    def has_default_role_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='HasDefaultRole',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/has_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.HasDefaultRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def has_default_role(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.has_default_role_with_options(headers, runtime)

    def list_acl_authorization_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pattern_type):
            query['PatternType'] = request.pattern_type
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclAuthorization',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/acls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListAclAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_acl_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_acl_authorization_with_options(request, headers, runtime)

    def list_authenticated_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticatedUser',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListAuthenticatedUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authenticated_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_authenticated_user_with_options(request, headers, runtime)

    def list_component_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponentInfo',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/component_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListComponentInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def list_component_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_info_with_options(request, headers, runtime)

    def list_csp_connector_detail_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = csp_20201020_models.ListCspConnectorDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'simple')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCspConnectorDetail',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/connectors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListCspConnectorDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def list_csp_connector_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_csp_connector_detail_with_options(request, headers, runtime)

    def list_ossinfos_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name_prefix):
            query['BucketNamePrefix'] = request.bucket_name_prefix
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssinfos',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/ossinfos',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListOssinfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ossinfos(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ossinfos_with_options(request, headers, runtime)

    def list_regions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/region/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    def list_security_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityGroups',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/security_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_security_groups_with_options(request, headers, runtime)

    def list_vpcs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcs',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/vpcs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpcs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpcs_with_options(request, headers, runtime)

    def list_vswitches_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVswitches',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/vswitches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vswitches_with_options(request, headers, runtime)

    def list_zones_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/user/zones',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_zones(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_zones_with_options(request, headers, runtime)

    def modify_acl_authorization_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operations):
            query['AclOperations'] = request.acl_operations
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pattern_type):
            query['PatternType'] = request.pattern_type
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAclAuthorization',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/modify_acl_authorization',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ModifyAclAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_acl_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_acl_authorization_with_options(request, headers, runtime)

    def modify_user_password_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPassword',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/ldap/modify_user_password',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ModifyUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_user_password_with_options(request, headers, runtime)

    def query_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrice',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/buy/query_abm_asi_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.QueryPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_price_with_options(request, headers, runtime)

    def query_renew_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewPrice',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/buy/query_abm_asi_renew_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.QueryRenewPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_renew_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_renew_price_with_options(request, headers, runtime)

    def query_scale_up_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.broker_number):
            query['BrokerNumber'] = request.broker_number
        if not UtilClient.is_unset(request.connector_cpu):
            query['ConnectorCpu'] = request.connector_cpu
        if not UtilClient.is_unset(request.connector_num):
            query['ConnectorNum'] = request.connector_num
        if not UtilClient.is_unset(request.control_center_cpu):
            query['ControlCenterCpu'] = request.control_center_cpu
        if not UtilClient.is_unset(request.control_center_num):
            query['ControlCenterNum'] = request.control_center_num
        if not UtilClient.is_unset(request.control_center_storage):
            query['ControlCenterStorage'] = request.control_center_storage
        if not UtilClient.is_unset(request.cu_number):
            query['CuNumber'] = request.cu_number
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ksql_cpu):
            query['KsqlCpu'] = request.ksql_cpu
        if not UtilClient.is_unset(request.ksql_num):
            query['KsqlNum'] = request.ksql_num
        if not UtilClient.is_unset(request.ksql_storage):
            query['KsqlStorage'] = request.ksql_storage
        if not UtilClient.is_unset(request.rest_proxy_cpu):
            query['RestProxyCpu'] = request.rest_proxy_cpu
        if not UtilClient.is_unset(request.rest_proxy_num):
            query['RestProxyNum'] = request.rest_proxy_num
        if not UtilClient.is_unset(request.schemaregistry_cpu):
            query['SchemaregistryCpu'] = request.schemaregistry_cpu
        if not UtilClient.is_unset(request.schemaregistry_num):
            query['SchemaregistryNum'] = request.schemaregistry_num
        if not UtilClient.is_unset(request.zookeeper_cpu):
            query['ZookeeperCpu'] = request.zookeeper_cpu
        if not UtilClient.is_unset(request.zookeeper_num):
            query['ZookeeperNum'] = request.zookeeper_num
        if not UtilClient.is_unset(request.zookeeper_storage):
            query['ZookeeperStorage'] = request.zookeeper_storage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpPrice',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/buy/query_abm_asi_scale_up_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.QueryScaleUpPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_scale_up_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_scale_up_price_with_options(request, headers, runtime)

    def query_unpaid_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnpaidOrder',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/order/query_abm_asi_unpaid_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.QueryUnpaidOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def query_unpaid_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_unpaid_order_with_options(request, headers, runtime)

    def renew_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/order/renew_instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(request, headers, runtime)

    def scale_up_cluster_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.broker_number):
            query['BrokerNumber'] = request.broker_number
        if not UtilClient.is_unset(request.connector_cpu):
            query['ConnectorCpu'] = request.connector_cpu
        if not UtilClient.is_unset(request.connector_num):
            query['ConnectorNum'] = request.connector_num
        if not UtilClient.is_unset(request.control_center_cpu):
            query['ControlCenterCpu'] = request.control_center_cpu
        if not UtilClient.is_unset(request.control_center_num):
            query['ControlCenterNum'] = request.control_center_num
        if not UtilClient.is_unset(request.control_center_storage):
            query['ControlCenterStorage'] = request.control_center_storage
        if not UtilClient.is_unset(request.cu_number):
            query['CuNumber'] = request.cu_number
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ksql_cpu):
            query['KsqlCpu'] = request.ksql_cpu
        if not UtilClient.is_unset(request.ksql_num):
            query['KsqlNum'] = request.ksql_num
        if not UtilClient.is_unset(request.ksql_storage):
            query['KsqlStorage'] = request.ksql_storage
        if not UtilClient.is_unset(request.rest_proxy_cpu):
            query['RestProxyCpu'] = request.rest_proxy_cpu
        if not UtilClient.is_unset(request.rest_proxy_num):
            query['RestProxyNum'] = request.rest_proxy_num
        if not UtilClient.is_unset(request.schemaregistry_cpu):
            query['SchemaregistryCpu'] = request.schemaregistry_cpu
        if not UtilClient.is_unset(request.schemaregistry_num):
            query['SchemaregistryNum'] = request.schemaregistry_num
        if not UtilClient.is_unset(request.zookeeper_cpu):
            query['ZookeeperCpu'] = request.zookeeper_cpu
        if not UtilClient.is_unset(request.zookeeper_num):
            query['ZookeeperNum'] = request.zookeeper_num
        if not UtilClient.is_unset(request.zookeeper_storage):
            query['ZookeeperStorage'] = request.zookeeper_storage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleUpCluster',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/scale_up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.ScaleUpClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_up_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_up_cluster_with_options(request, headers, runtime)

    def search_cluster_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchClusterInstances',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.SearchClusterInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_cluster_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_cluster_instances_with_options(request, headers, runtime)

    def single_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleOrder',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/order/single',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.SingleOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def single_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.single_order_with_options(request, headers, runtime)

    def update_cluster_name_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterName',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.UpdateClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster_name(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_cluster_name_with_options(request, headers, runtime)

    def update_csp_connector_detail_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = csp_20201020_models.UpdateCspConnectorDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.connector_details):
            request.connector_details_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.connector_details, 'ConnectorDetails', 'json')
        query = {}
        if not UtilClient.is_unset(request.connector_details_shrink):
            query['ConnectorDetails'] = request.connector_details_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCspConnectorDetail',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/connectors_update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.UpdateCspConnectorDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def update_csp_connector_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_csp_connector_detail_with_options(request, headers, runtime)

    def update_public_network_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicNetworkStatus',
            version='2020-10-20',
            protocol='HTTPS',
            pathname='/webapi/csp/public_network_switch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            csp_20201020_models.UpdatePublicNetworkStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_public_network_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_network_status_with_options(request, headers, runtime)
