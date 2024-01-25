# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdp20210402 import models as cdp_20210402_models
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
        self._endpoint = self.get_endpoint('cdp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_order_with_options(request, headers, runtime)

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
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/check/cluster_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CheckClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    def check_cluster_name(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_cluster_name_with_options(request, headers, runtime)

    def confirm_notice_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmNotice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/confirm_notice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ConfirmNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_notice(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_notice_with_options(request, headers, runtime)

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
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    def get_cluster_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDetail',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.GetClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_detail_with_options(request, headers, runtime)

    def has_default_role_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='HasDefaultRole',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/user/has_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.HasDefaultRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def has_default_role(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.has_default_role_with_options(headers, runtime)

    def initialize_cloudera_data_platform_with_options(self, client_token, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='InitializeClouderaDataPlatform',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.InitializeClouderaDataPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def initialize_cloudera_data_platform(self, client_token):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initialize_cloudera_data_platform_with_options(client_token, headers, runtime)

    def list_default_components_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.security_mode):
            query['SecurityMode'] = request.security_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDefaultComponents',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cdp/defaultComponents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListDefaultComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_default_components(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_default_components_with_options(request, headers, runtime)

    def list_node_group_constraints_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeGroupConstraints',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cdp/nodeGroupConstraints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListNodeGroupConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_node_group_constraints(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_group_constraints_with_options(request, headers, runtime)

    def list_nodes_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(request, headers, runtime)

    def list_operations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.parent_operation_node_id):
            query['ParentOperationNodeId'] = request.parent_operation_node_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperations',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_operations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_operations_with_options(request, headers, runtime)

    def list_regions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/region/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

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
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/user/zones',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_zones(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_zones_with_options(request, headers, runtime)

    def query_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def query_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_order_with_options(request, headers, runtime)

    def query_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_specs):
            query['NodeGroupSpecs'] = request.node_group_specs
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/buy/query_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_price_with_options(request, headers, runtime)

    def query_renew_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/query_renew_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryRenewOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def query_renew_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_renew_order_with_options(request, headers, runtime)

    def query_renew_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/buy/query_renew_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryRenewPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_renew_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_renew_price_with_options(request, headers, runtime)

    def query_scale_up_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/query_scale_up_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryScaleUpOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def query_scale_up_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_scale_up_order_with_options(request, headers, runtime)

    def query_scale_up_price_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.core_number):
            query['CoreNumber'] = request.core_number
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/buy/query_scale_up_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryScaleUpPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_scale_up_price(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_scale_up_price_with_options(request, headers, runtime)

    def release_cluster_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ReleaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def release_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_cluster_with_options(request, headers, runtime)

    def renew_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/renew_instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(request, headers, runtime)

    def scale_up_cluster_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.core_number):
            query['CoreNumber'] = request.core_number
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleUpCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/scale_up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ScaleUpClusterResponse(),
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
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.SearchClusterInstancesResponse(),
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
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/order/single',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.SingleOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def single_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.single_order_with_options(request, headers, runtime)

    def update_cluster_name_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterName',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.UpdateClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster_name(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_cluster_name_with_options(request, headers, runtime)

    def upload_license_with_options(self, region_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UploadLicense',
            version='2021-04-02',
            protocol='HTTPS',
            pathname='/webapi/user/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.UploadLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_license(self, region_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_license_with_options(region_id, headers, runtime)
