# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_expressconnectrouter20230901 import models as express_connect_router_20230901_models
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
        self._endpoint = self.get_endpoint('expressconnectrouter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_express_connect_router_child_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            body['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            body['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachExpressConnectRouterChildInstance',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.AttachExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_express_connect_router_child_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_express_connect_router_child_instance_with_options(request, runtime)

    def check_add_region_to_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.fresh_region_id):
            body['FreshRegionId'] = request.fresh_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckAddRegionToExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.CheckAddRegionToExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def check_add_region_to_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_add_region_to_express_connect_router_with_options(request, runtime)

    def create_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alibaba_side_asn):
            body['AlibabaSideAsn'] = request.alibaba_side_asn
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.CreateExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_express_connect_router_with_options(request, runtime)

    def create_express_connect_router_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allowed_prefixes):
            body['AllowedPrefixes'] = request.allowed_prefixes
        if not UtilClient.is_unset(request.association_region_id):
            body['AssociationRegionId'] = request.association_region_id
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_attachment):
            body['CreateAttachment'] = request.create_attachment
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.transit_router_id):
            body['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_owner_id):
            body['TransitRouterOwnerId'] = request.transit_router_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            body['VpcOwnerId'] = request.vpc_owner_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExpressConnectRouterAssociation',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.CreateExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_express_connect_router_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_express_connect_router_association_with_options(request, runtime)

    def delete_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DeleteExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_express_connect_router_with_options(request, runtime)

    def delete_express_connect_router_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.association_id):
            body['AssociationId'] = request.association_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_attachment):
            body['DeleteAttachment'] = request.delete_attachment
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteExpressConnectRouterAssociation',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DeleteExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_express_connect_router_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_express_connect_router_association_with_options(request, runtime)

    def describe_disabled_express_connect_router_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisabledExpressConnectRouterRouteEntries',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeDisabledExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_disabled_express_connect_router_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disabled_express_connect_router_route_entries_with_options(request, runtime)

    def describe_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_models):
            body['TagModels'] = request.tag_models
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_with_options(request, runtime)

    def describe_express_connect_router_allowed_prefix_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.associaton_id):
            body['AssociatonId'] = request.associaton_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouterAllowedPrefixHistory',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router_allowed_prefix_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_allowed_prefix_history_with_options(request, runtime)

    def describe_express_connect_router_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.association_id):
            body['AssociationId'] = request.association_id
        if not UtilClient.is_unset(request.association_node_type):
            body['AssociationNodeType'] = request.association_node_type
        if not UtilClient.is_unset(request.association_region_id):
            body['AssociationRegionId'] = request.association_region_id
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.transit_router_id):
            body['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouterAssociation',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_association_with_options(request, runtime)

    def describe_express_connect_router_child_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.association_id):
            body['AssociationId'] = request.association_id
        if not UtilClient.is_unset(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            body['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouterChildInstance',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router_child_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_child_instance_with_options(request, runtime)

    def describe_express_connect_router_inter_region_transit_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouterInterRegionTransitMode',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterInterRegionTransitModeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router_inter_region_transit_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_inter_region_transit_mode_with_options(request, runtime)

    def describe_express_connect_router_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouterRegion',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_region_with_options(request, runtime)

    def describe_express_connect_router_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.as_path):
            body['AsPath'] = request.as_path
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.community):
            body['Community'] = request.community
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        if not UtilClient.is_unset(request.query_region_id):
            body['QueryRegionId'] = request.query_region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeExpressConnectRouterRouteEntries',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_express_connect_router_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_express_connect_router_route_entries_with_options(request, runtime)

    def describe_instance_granted_to_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            body['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_models):
            body['TagModels'] = request.tag_models
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceGrantedToExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DescribeInstanceGrantedToExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_granted_to_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_granted_to_express_connect_router_with_options(request, runtime)

    def detach_express_connect_router_child_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.child_instance_id):
            body['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_type):
            body['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachExpressConnectRouterChildInstance',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DetachExpressConnectRouterChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_express_connect_router_child_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_express_connect_router_child_instance_with_options(request, runtime)

    def disable_express_connect_router_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableExpressConnectRouterRouteEntries',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.DisableExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_express_connect_router_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_express_connect_router_route_entries_with_options(request, runtime)

    def enable_express_connect_router_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.nexthop_instance_id):
            body['NexthopInstanceId'] = request.nexthop_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableExpressConnectRouterRouteEntries',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.EnableExpressConnectRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_express_connect_router_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_express_connect_router_route_entries_with_options(request, runtime)

    def force_delete_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ForceDeleteExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.ForceDeleteExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def force_delete_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.force_delete_express_connect_router_with_options(request, runtime)

    def get_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.GetExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_express_connect_router_with_options(request, runtime)

    def grant_instance_to_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.ecr_owner_ali_uid):
            body['EcrOwnerAliUid'] = request.ecr_owner_ali_uid
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantInstanceToExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.GrantInstanceToExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_instance_to_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_instance_to_express_connect_router_with_options(request, runtime)

    def list_express_connect_router_supported_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListExpressConnectRouterSupportedRegion',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.ListExpressConnectRouterSupportedRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_express_connect_router_supported_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_express_connect_router_supported_region_with_options(request, runtime)

    def modify_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.ModifyExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_express_connect_router_with_options(request, runtime)

    def modify_express_connect_router_association_allowed_prefix_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.allowed_prefixes):
            body['AllowedPrefixes'] = request.allowed_prefixes
        if not UtilClient.is_unset(request.association_id):
            body['AssociationId'] = request.association_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.owner_account):
            body['OwnerAccount'] = request.owner_account
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyExpressConnectRouterAssociationAllowedPrefix',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.ModifyExpressConnectRouterAssociationAllowedPrefixResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_express_connect_router_association_allowed_prefix(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_express_connect_router_association_allowed_prefix_with_options(request, runtime)

    def modify_express_connect_router_inter_region_transit_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.transit_mode_list):
            body['TransitModeList'] = request.transit_mode_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyExpressConnectRouterInterRegionTransitMode',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.ModifyExpressConnectRouterInterRegionTransitModeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_express_connect_router_inter_region_transit_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_express_connect_router_inter_region_transit_mode_with_options(request, runtime)

    def revoke_instance_from_express_connect_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        if not UtilClient.is_unset(request.ecr_owner_ali_uid):
            body['EcrOwnerAliUid'] = request.ecr_owner_ali_uid
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_region_id):
            body['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromExpressConnectRouter',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.RevokeInstanceFromExpressConnectRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_instance_from_express_connect_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_express_connect_router_with_options(request, runtime)

    def synchronize_express_connect_router_inter_region_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ecr_id):
            body['EcrId'] = request.ecr_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SynchronizeExpressConnectRouterInterRegionBandwidth',
            version='2023-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            express_connect_router_20230901_models.SynchronizeExpressConnectRouterInterRegionBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    def synchronize_express_connect_router_inter_region_bandwidth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.synchronize_express_connect_router_inter_region_bandwidth_with_options(request, runtime)
