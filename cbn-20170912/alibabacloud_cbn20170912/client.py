# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cbn20170912 import models as cbn_20170912_models
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
        self._endpoint = self.get_endpoint('cbn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def active_flow_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActiveFlowLog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ActiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    def active_flow_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    def add_traffic_match_rule_to_traffic_marking_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficMatchRuleToTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AddTrafficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def add_traffic_match_rule_to_traffic_marking_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    def add_trafic_match_rule_to_traffic_marking_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTraficMatchRuleToTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AddTraficMatchRuleToTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def add_trafic_match_rule_to_traffic_marking_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_trafic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    def associate_cen_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_cen_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_cen_bandwidth_package_with_options(request, runtime)

    def associate_transit_router_attachment_with_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateTransitRouterAttachmentWithRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateTransitRouterAttachmentWithRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_transit_router_attachment_with_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_transit_router_attachment_with_route_table_with_options(request, runtime)

    def associate_transit_router_multicast_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_transit_router_multicast_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_transit_router_multicast_domain_with_options(request, runtime)

    def attach_cen_child_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCenChildInstance',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.AttachCenChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_cen_child_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_child_instance_with_options(request, runtime)

    def check_transit_router_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTransitRouterService',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CheckTransitRouterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_transit_router_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_transit_router_service_with_options(request, runtime)

    def create_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_with_options(request, runtime)

    def create_cen_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_package_charge_type):
            query['BandwidthPackageChargeType'] = request.bandwidth_package_charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not UtilClient.is_unset(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_bandwidth_package_with_options(request, runtime)

    def create_cen_child_instance_route_entry_to_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenChildInstanceRouteEntryToAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen_child_instance_route_entry_to_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    def create_cen_child_instance_route_entry_to_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenChildInstanceRouteEntryToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen_child_instance_route_entry_to_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    def create_cen_inter_region_traffic_qos_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not UtilClient.is_unset(request.traffic_qos_queues):
            query['TrafficQosQueues'] = request.traffic_qos_queues
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenInterRegionTrafficQosPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenInterRegionTrafficQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen_inter_region_traffic_qos_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    def create_cen_inter_region_traffic_qos_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dscps):
            query['Dscps'] = request.dscps
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not UtilClient.is_unset(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not UtilClient.is_unset(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenInterRegionTrafficQosQueue',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenInterRegionTrafficQosQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen_inter_region_traffic_qos_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    def create_cen_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not UtilClient.is_unset(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not UtilClient.is_unset(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not UtilClient.is_unset(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not UtilClient.is_unset(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not UtilClient.is_unset(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not UtilClient.is_unset(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not UtilClient.is_unset(request.map_result):
            query['MapResult'] = request.map_result
        if not UtilClient.is_unset(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not UtilClient.is_unset(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not UtilClient.is_unset(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not UtilClient.is_unset(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not UtilClient.is_unset(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preference):
            query['Preference'] = request.preference
        if not UtilClient.is_unset(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_types):
            query['RouteTypes'] = request.route_types
        if not UtilClient.is_unset(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not UtilClient.is_unset(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not UtilClient.is_unset(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not UtilClient.is_unset(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not UtilClient.is_unset(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cen_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cen_route_map_with_options(request, runtime)

    def create_flowlog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowlog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    def create_flowlog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flowlog_with_options(request, runtime)

    def create_traffic_marking_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.marking_dscp):
            query['MarkingDscp'] = request.marking_dscp
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not UtilClient.is_unset(request.traffic_match_rules):
            query['TrafficMatchRules'] = request.traffic_match_rules
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_traffic_marking_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_marking_policy_with_options(request, runtime)

    def create_transit_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        if not UtilClient.is_unset(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_with_options(request, runtime)

    def create_transit_router_multicast_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not UtilClient.is_unset(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_multicast_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_multicast_domain_with_options(request, runtime)

    def create_transit_router_peer_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_id):
            query['PeerTransitRouterId'] = request.peer_transit_router_id
        if not UtilClient.is_unset(request.peer_transit_router_region_id):
            query['PeerTransitRouterRegionId'] = request.peer_transit_router_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterPeerAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterPeerAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_peer_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_peer_attachment_with_options(request, runtime)

    def create_transit_router_prefix_list_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_prefix_list_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_prefix_list_association_with_options(request, runtime)

    def create_transit_router_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_route_entry_with_options(request, runtime)

    def create_transit_router_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not UtilClient.is_unset(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_route_table_with_options(request, runtime)

    def create_transit_router_vbr_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vbr_owner_id):
            query['VbrOwnerId'] = request.vbr_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVbrAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVbrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_vbr_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vbr_attachment_with_options(request, runtime)

    def create_transit_router_vpc_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_owner_id):
            query['VpcOwnerId'] = request.vpc_owner_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVpcAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVpcAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_vpc_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vpc_attachment_with_options(request, runtime)

    def create_transit_router_vpn_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpn_id):
            query['VpnId'] = request.vpn_id
        if not UtilClient.is_unset(request.vpn_owner_id):
            query['VpnOwnerId'] = request.vpn_owner_id
        if not UtilClient.is_unset(request.zone):
            query['Zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouterVpnAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateTransitRouterVpnAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_vpn_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vpn_attachment_with_options(request, runtime)

    def deactive_flow_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactiveFlowLog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeactiveFlowLogResponse(),
            self.call_api(params, req, runtime)
        )

    def deactive_flow_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    def delete_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_with_options(request, runtime)

    def delete_cen_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_bandwidth_package_with_options(request, runtime)

    def delete_cen_child_instance_route_entry_to_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenChildInstanceRouteEntryToAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    def delete_cen_child_instance_route_entry_to_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_ali_uid):
            query['ChildInstanceAliUid'] = request.child_instance_ali_uid
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenChildInstanceRouteEntryToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    def delete_cen_inter_region_traffic_qos_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenInterRegionTrafficQosPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenInterRegionTrafficQosPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen_inter_region_traffic_qos_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    def delete_cen_inter_region_traffic_qos_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenInterRegionTrafficQosQueue',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenInterRegionTrafficQosQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen_inter_region_traffic_qos_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    def delete_cen_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cen_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_route_map_with_options(request, runtime)

    def delete_flowlog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowlog',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteFlowlogResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_flowlog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flowlog_with_options(request, runtime)

    def delete_route_service_in_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteServiceInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteRouteServiceInCenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_route_service_in_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_route_service_in_cen_with_options(request, runtime)

    def delete_traffic_marking_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_traffic_marking_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_marking_policy_with_options(request, runtime)

    def delete_transit_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_with_options(request, runtime)

    def delete_transit_router_multicast_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_multicast_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_multicast_domain_with_options(request, runtime)

    def delete_transit_router_peer_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterPeerAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterPeerAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_peer_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_peer_attachment_with_options(request, runtime)

    def delete_transit_router_prefix_list_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_prefix_list_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_prefix_list_association_with_options(request, runtime)

    def delete_transit_router_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_id):
            query['TransitRouterRouteEntryNextHopId'] = request.transit_router_route_entry_next_hop_id
        if not UtilClient.is_unset(request.transit_router_route_entry_next_hop_type):
            query['TransitRouterRouteEntryNextHopType'] = request.transit_router_route_entry_next_hop_type
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_route_entry_with_options(request, runtime)

    def delete_transit_router_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_route_table_with_options(request, runtime)

    def delete_transit_router_vbr_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVbrAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVbrAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_vbr_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vbr_attachment_with_options(request, runtime)

    def delete_transit_router_vpc_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVpcAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVpcAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_vpc_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vpc_attachment_with_options(request, runtime)

    def delete_transit_router_vpn_attachment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterVpnAttachment',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteTransitRouterVpnAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_vpn_attachment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vpn_attachment_with_options(request, runtime)

    def deregister_transit_router_multicast_group_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterTransitRouterMulticastGroupMembers',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeregisterTransitRouterMulticastGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_transit_router_multicast_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_transit_router_multicast_group_members_with_options(request, runtime)

    def deregister_transit_router_multicast_group_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterTransitRouterMulticastGroupSources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeregisterTransitRouterMulticastGroupSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_transit_router_multicast_group_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_transit_router_multicast_group_sources_with_options(request, runtime)

    def describe_cen_attached_child_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenAttachedChildInstanceAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_attached_child_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_attached_child_instance_attribute_with_options(request, runtime)

    def describe_cen_attached_child_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenAttachedChildInstances',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_attached_child_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_attached_child_instances_with_options(request, runtime)

    def describe_cen_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_reservation_data):
            query['IncludeReservationData'] = request.include_reservation_data
        if not UtilClient.is_unset(request.is_or_key):
            query['IsOrKey'] = request.is_or_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenBandwidthPackages',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_bandwidth_packages_with_options(request, runtime)

    def describe_cen_child_instance_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenChildInstanceRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_child_instance_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_child_instance_route_entries_with_options(request, runtime)

    def describe_cen_geographic_span_remaining_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.geographic_region_aid):
            query['GeographicRegionAId'] = request.geographic_region_aid
        if not UtilClient.is_unset(request.geographic_region_bid):
            query['GeographicRegionBId'] = request.geographic_region_bid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenGeographicSpanRemainingBandwidth',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_geographic_span_remaining_bandwidth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_geographic_span_remaining_bandwidth_with_options(request, runtime)

    def describe_cen_geographic_spans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.geographic_span_id):
            query['GeographicSpanId'] = request.geographic_span_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenGeographicSpans',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_geographic_spans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_geographic_spans_with_options(request, runtime)

    def describe_cen_inter_region_bandwidth_limits_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenInterRegionBandwidthLimits',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_inter_region_bandwidth_limits(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_inter_region_bandwidth_limits_with_options(request, runtime)

    def describe_cen_private_zone_routes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenPrivateZoneRoutes',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_private_zone_routes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_private_zone_routes_with_options(request, runtime)

    def describe_cen_region_domain_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenRegionDomainRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_region_domain_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_region_domain_route_entries_with_options(request, runtime)

    def describe_cen_route_maps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transmit_direction):
            query['TransmitDirection'] = request.transmit_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenRouteMaps',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_route_maps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_route_maps_with_options(request, runtime)

    def describe_cen_vbr_health_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_vbr_health_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_vbr_health_check_with_options(request, runtime)

    def describe_cen_vpc_flow_statistic_switch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCenVpcFlowStatisticSwitch',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenVpcFlowStatisticSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cen_vpc_flow_statistic_switch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_vpc_flow_statistic_switch_with_options(request, runtime)

    def describe_cens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    def describe_child_instance_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChildInstanceRegions',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeChildInstanceRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_child_instance_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_child_instance_regions_with_options(request, runtime)

    def describe_flowlogs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.log_store_name):
            query['LogStoreName'] = request.log_store_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowlogs',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeFlowlogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flowlogs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flowlogs_with_options(request, runtime)

    def describe_geographic_region_membership_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.geographic_region_id):
            query['GeographicRegionId'] = request.geographic_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGeographicRegionMembership',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGeographicRegionMembershipResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_geographic_region_membership(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_geographic_region_membership_with_options(request, runtime)

    def describe_grant_rules_to_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRulesToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToCenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grant_rules_to_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_to_cen_with_options(request, runtime)

    def describe_grant_rules_to_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGrantRulesToResource',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grant_rules_to_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_to_resource_with_options(request, runtime)

    def describe_published_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePublishedRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribePublishedRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_published_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_published_route_entries_with_options(request, runtime)

    def describe_route_conflict_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteConflict',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteConflictResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_route_conflict(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_route_conflict_with_options(request, runtime)

    def describe_route_services_in_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteServicesInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteServicesInCenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_route_services_in_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_route_services_in_cen_with_options(request, runtime)

    def detach_cen_child_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_owner_id):
            query['ChildInstanceOwnerId'] = request.child_instance_owner_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCenChildInstance',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DetachCenChildInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_cen_child_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_child_instance_with_options(request, runtime)

    def disable_cen_vbr_health_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_cen_vbr_health_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_cen_vbr_health_check_with_options(request, runtime)

    def disable_cen_vpc_flow_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCenVpcFlowStatistic',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableCenVpcFlowStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_cen_vpc_flow_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_cen_vpc_flow_statistic_with_options(request, runtime)

    def disable_transit_router_route_table_propagation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableTransitRouterRouteTablePropagation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableTransitRouterRouteTablePropagationResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_transit_router_route_table_propagation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_transit_router_route_table_propagation_with_options(request, runtime)

    def disassociate_transit_router_multicast_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisassociateTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def disassociate_transit_router_multicast_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disassociate_transit_router_multicast_domain_with_options(request, runtime)

    def dissociate_transit_router_attachment_from_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateTransitRouterAttachmentFromRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.DissociateTransitRouterAttachmentFromRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_transit_router_attachment_from_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_transit_router_attachment_from_route_table_with_options(request, runtime)

    def enable_cen_vbr_health_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_only):
            query['HealthCheckOnly'] = request.health_check_only
        if not UtilClient.is_unset(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not UtilClient.is_unset(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vbr_instance_id):
            query['VbrInstanceId'] = request.vbr_instance_id
        if not UtilClient.is_unset(request.vbr_instance_owner_id):
            query['VbrInstanceOwnerId'] = request.vbr_instance_owner_id
        if not UtilClient.is_unset(request.vbr_instance_region_id):
            query['VbrInstanceRegionId'] = request.vbr_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCenVbrHealthCheck',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableCenVbrHealthCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_cen_vbr_health_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_cen_vbr_health_check_with_options(request, runtime)

    def enable_cen_vpc_flow_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCenVpcFlowStatistic',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableCenVpcFlowStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_cen_vpc_flow_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_cen_vpc_flow_statistic_with_options(request, runtime)

    def enable_transit_router_route_table_propagation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableTransitRouterRouteTablePropagation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableTransitRouterRouteTablePropagationResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_transit_router_route_table_propagation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_transit_router_route_table_propagation_with_options(request, runtime)

    def grant_instance_to_transit_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantInstanceToTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.GrantInstanceToTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_instance_to_transit_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_instance_to_transit_router_with_options(request, runtime)

    def list_cen_inter_region_traffic_qos_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCenInterRegionTrafficQosPolicies',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListCenInterRegionTrafficQosPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cen_inter_region_traffic_qos_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cen_inter_region_traffic_qos_policies_with_options(request, runtime)

    def list_grant_vswitch_enis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrantVSwitchEnis',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListGrantVSwitchEnisResponse(),
            self.call_api(params, req, runtime)
        )

    def list_grant_vswitch_enis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_grant_vswitch_enis_with_options(request, runtime)

    def list_grant_vswitches_to_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrantVSwitchesToCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListGrantVSwitchesToCenResponse(),
            self.call_api(params, req, runtime)
        )

    def list_grant_vswitches_to_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_grant_vswitches_to_cen_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_traffic_marking_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrafficMarkingPolicies',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTrafficMarkingPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_traffic_marking_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_traffic_marking_policies_with_options(request, runtime)

    def list_transit_router_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.support_multicast):
            query['SupportMulticast'] = request.support_multicast
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterAvailableResource',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_available_resource_with_options(request, runtime)

    def list_transit_router_multicast_domain_associations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomainAssociations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_multicast_domain_associations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domain_associations_with_options(request, runtime)

    def list_transit_router_multicast_domain_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomainVSwitches',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_multicast_domain_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domain_vswitches_with_options(request, runtime)

    def list_transit_router_multicast_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastDomains',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_multicast_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domains_with_options(request, runtime)

    def list_transit_router_multicast_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connect_peer_ids):
            query['ConnectPeerIds'] = request.connect_peer_ids
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterMulticastGroups',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterMulticastGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_multicast_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_groups_with_options(request, runtime)

    def list_transit_router_peer_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterPeerAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterPeerAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_peer_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_peer_attachments_with_options(request, runtime)

    def list_transit_router_prefix_list_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_hop):
            query['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_table_id):
            query['TransitRouterTableId'] = request.transit_router_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterPrefixListAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterPrefixListAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_prefix_list_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_prefix_list_association_with_options(request, runtime)

    def list_transit_router_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_destination_cidr_block):
            query['TransitRouterRouteEntryDestinationCidrBlock'] = request.transit_router_route_entry_destination_cidr_block
        if not UtilClient.is_unset(request.transit_router_route_entry_ids):
            query['TransitRouterRouteEntryIds'] = request.transit_router_route_entry_ids
        if not UtilClient.is_unset(request.transit_router_route_entry_names):
            query['TransitRouterRouteEntryNames'] = request.transit_router_route_entry_names
        if not UtilClient.is_unset(request.transit_router_route_entry_status):
            query['TransitRouterRouteEntryStatus'] = request.transit_router_route_entry_status
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_entries_with_options(request, runtime)

    def list_transit_router_route_table_associations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTableAssociations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTableAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_route_table_associations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_table_associations_with_options(request, runtime)

    def list_transit_router_route_table_propagations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTablePropagations',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTablePropagationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_route_table_propagations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_table_propagations_with_options(request, runtime)

    def list_transit_router_route_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_route_table_ids):
            query['TransitRouterRouteTableIds'] = request.transit_router_route_table_ids
        if not UtilClient.is_unset(request.transit_router_route_table_names):
            query['TransitRouterRouteTableNames'] = request.transit_router_route_table_names
        if not UtilClient.is_unset(request.transit_router_route_table_status):
            query['TransitRouterRouteTableStatus'] = request.transit_router_route_table_status
        if not UtilClient.is_unset(request.transit_router_route_table_type):
            query['TransitRouterRouteTableType'] = request.transit_router_route_table_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterRouteTables',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterRouteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_route_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_route_tables_with_options(request, runtime)

    def list_transit_router_vbr_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVbrAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVbrAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_vbr_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vbr_attachments_with_options(request, runtime)

    def list_transit_router_vpc_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVpcAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVpcAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_vpc_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vpc_attachments_with_options(request, runtime)

    def list_transit_router_vpn_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterVpnAttachments',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRouterVpnAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_vpn_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vpn_attachments_with_options(request, runtime)

    def list_transit_routers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouters',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTransitRoutersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_routers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_routers_with_options(request, runtime)

    def modify_cen_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cen_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_attribute_with_options(request, runtime)

    def modify_cen_bandwidth_package_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenBandwidthPackageAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cen_bandwidth_package_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_bandwidth_package_attribute_with_options(request, runtime)

    def modify_cen_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenBandwidthPackageSpec',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cen_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_bandwidth_package_spec_with_options(request, runtime)

    def modify_cen_route_map_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.as_path_match_mode):
            query['AsPathMatchMode'] = request.as_path_match_mode
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_region_id):
            query['CenRegionId'] = request.cen_region_id
        if not UtilClient.is_unset(request.cidr_match_mode):
            query['CidrMatchMode'] = request.cidr_match_mode
        if not UtilClient.is_unset(request.community_match_mode):
            query['CommunityMatchMode'] = request.community_match_mode
        if not UtilClient.is_unset(request.community_operate_mode):
            query['CommunityOperateMode'] = request.community_operate_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_child_instance_types):
            query['DestinationChildInstanceTypes'] = request.destination_child_instance_types
        if not UtilClient.is_unset(request.destination_cidr_blocks):
            query['DestinationCidrBlocks'] = request.destination_cidr_blocks
        if not UtilClient.is_unset(request.destination_instance_ids):
            query['DestinationInstanceIds'] = request.destination_instance_ids
        if not UtilClient.is_unset(request.destination_instance_ids_reverse_match):
            query['DestinationInstanceIdsReverseMatch'] = request.destination_instance_ids_reverse_match
        if not UtilClient.is_unset(request.destination_route_table_ids):
            query['DestinationRouteTableIds'] = request.destination_route_table_ids
        if not UtilClient.is_unset(request.map_result):
            query['MapResult'] = request.map_result
        if not UtilClient.is_unset(request.match_address_type):
            query['MatchAddressType'] = request.match_address_type
        if not UtilClient.is_unset(request.match_asns):
            query['MatchAsns'] = request.match_asns
        if not UtilClient.is_unset(request.match_community_set):
            query['MatchCommunitySet'] = request.match_community_set
        if not UtilClient.is_unset(request.next_priority):
            query['NextPriority'] = request.next_priority
        if not UtilClient.is_unset(request.operate_community_set):
            query['OperateCommunitySet'] = request.operate_community_set
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preference):
            query['Preference'] = request.preference
        if not UtilClient.is_unset(request.prepend_as_path):
            query['PrependAsPath'] = request.prepend_as_path
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.route_map_id):
            query['RouteMapId'] = request.route_map_id
        if not UtilClient.is_unset(request.route_types):
            query['RouteTypes'] = request.route_types
        if not UtilClient.is_unset(request.source_child_instance_types):
            query['SourceChildInstanceTypes'] = request.source_child_instance_types
        if not UtilClient.is_unset(request.source_instance_ids):
            query['SourceInstanceIds'] = request.source_instance_ids
        if not UtilClient.is_unset(request.source_instance_ids_reverse_match):
            query['SourceInstanceIdsReverseMatch'] = request.source_instance_ids_reverse_match
        if not UtilClient.is_unset(request.source_region_ids):
            query['SourceRegionIds'] = request.source_region_ids
        if not UtilClient.is_unset(request.source_route_table_ids):
            query['SourceRouteTableIds'] = request.source_route_table_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCenRouteMap',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cen_route_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_route_map_with_options(request, runtime)

    def modify_flow_log_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.flow_log_id):
            query['FlowLogId'] = request.flow_log_id
        if not UtilClient.is_unset(request.flow_log_name):
            query['FlowLogName'] = request.flow_log_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowLogAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyFlowLogAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_flow_log_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    def modify_transit_router_multicast_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_description):
            query['TransitRouterMulticastDomainDescription'] = request.transit_router_multicast_domain_description
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_name):
            query['TransitRouterMulticastDomainName'] = request.transit_router_multicast_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTransitRouterMulticastDomain',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyTransitRouterMulticastDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_transit_router_multicast_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_transit_router_multicast_domain_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def open_transit_router_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenTransitRouterService',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.OpenTransitRouterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_transit_router_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_transit_router_service_with_options(request, runtime)

    def publish_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.PublishRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_route_entries_with_options(request, runtime)

    def register_transit_router_multicast_group_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_transit_router_multicast_domains):
            query['PeerTransitRouterMulticastDomains'] = request.peer_transit_router_multicast_domains
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterTransitRouterMulticastGroupMembers',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RegisterTransitRouterMulticastGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def register_transit_router_multicast_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_transit_router_multicast_group_members_with_options(request, runtime)

    def register_transit_router_multicast_group_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_multicast_domain_id):
            query['TransitRouterMulticastDomainId'] = request.transit_router_multicast_domain_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterTransitRouterMulticastGroupSources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RegisterTransitRouterMulticastGroupSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def register_transit_router_multicast_group_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_transit_router_multicast_group_sources_with_options(request, runtime)

    def remove_traffic_match_rule_from_traffic_marking_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTrafficMatchRuleFromTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_traffic_match_rule_from_traffic_marking_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    def remove_trafic_match_rule_from_traffic_marking_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_mark_rule_ids):
            query['TrafficMarkRuleIds'] = request.traffic_mark_rule_ids
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTraficMatchRuleFromTrafficMarkingPolicy',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_trafic_match_rule_from_traffic_marking_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_trafic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    def replace_transit_router_route_table_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceTransitRouterRouteTableAssociation',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ReplaceTransitRouterRouteTableAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_transit_router_route_table_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_transit_router_route_table_association_with_options(request, runtime)

    def resolve_and_route_service_in_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_ids):
            query['AccessRegionIds'] = request.access_region_ids
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResolveAndRouteServiceInCen',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.ResolveAndRouteServiceInCenResponse(),
            self.call_api(params, req, runtime)
        )

    def resolve_and_route_service_in_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resolve_and_route_service_in_cen_with_options(request, runtime)

    def revoke_instance_from_transit_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeInstanceFromTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RevokeInstanceFromTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_instance_from_transit_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_transit_router_with_options(request, runtime)

    def route_private_zone_in_cen_to_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.host_region_id):
            query['HostRegionId'] = request.host_region_id
        if not UtilClient.is_unset(request.host_vpc_id):
            query['HostVpcId'] = request.host_vpc_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RoutePrivateZoneInCenToVpc',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def route_private_zone_in_cen_to_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.route_private_zone_in_cen_to_vpc_with_options(request, runtime)

    def set_cen_inter_region_bandwidth_limit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_limit):
            query['BandwidthLimit'] = request.bandwidth_limit
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.local_region_id):
            query['LocalRegionId'] = request.local_region_id
        if not UtilClient.is_unset(request.opposite_region_id):
            query['OppositeRegionId'] = request.opposite_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCenInterRegionBandwidthLimit',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cen_inter_region_bandwidth_limit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cen_inter_region_bandwidth_limit_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def temp_upgrade_cen_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempUpgradeCenBandwidthPackageSpec',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def temp_upgrade_cen_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.temp_upgrade_cen_bandwidth_package_spec_with_options(request, runtime)

    def unassociate_cen_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateCenBandwidthPackage',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnassociateCenBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def unassociate_cen_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_cen_bandwidth_package_with_options(request, runtime)

    def unroute_private_zone_in_cen_to_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_region_id):
            query['AccessRegionId'] = request.access_region_id
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnroutePrivateZoneInCenToVpc',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def unroute_private_zone_in_cen_to_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unroute_private_zone_in_cen_to_vpc_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_cen_inter_region_traffic_qos_policy_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_qos_policy_description):
            query['TrafficQosPolicyDescription'] = request.traffic_qos_policy_description
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_policy_name):
            query['TrafficQosPolicyName'] = request.traffic_qos_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCenInterRegionTrafficQosPolicyAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateCenInterRegionTrafficQosPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cen_inter_region_traffic_qos_policy_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cen_inter_region_traffic_qos_policy_attribute_with_options(request, runtime)

    def update_cen_inter_region_traffic_qos_queue_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dscps):
            query['Dscps'] = request.dscps
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.qos_queue_description):
            query['QosQueueDescription'] = request.qos_queue_description
        if not UtilClient.is_unset(request.qos_queue_id):
            query['QosQueueId'] = request.qos_queue_id
        if not UtilClient.is_unset(request.qos_queue_name):
            query['QosQueueName'] = request.qos_queue_name
        if not UtilClient.is_unset(request.remain_bandwidth_percent):
            query['RemainBandwidthPercent'] = request.remain_bandwidth_percent
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCenInterRegionTrafficQosQueueAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateCenInterRegionTrafficQosQueueAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cen_inter_region_traffic_qos_queue_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cen_inter_region_traffic_qos_queue_attribute_with_options(request, runtime)

    def update_traffic_marking_policy_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.traffic_marking_policy_description):
            query['TrafficMarkingPolicyDescription'] = request.traffic_marking_policy_description
        if not UtilClient.is_unset(request.traffic_marking_policy_id):
            query['TrafficMarkingPolicyId'] = request.traffic_marking_policy_id
        if not UtilClient.is_unset(request.traffic_marking_policy_name):
            query['TrafficMarkingPolicyName'] = request.traffic_marking_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrafficMarkingPolicyAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTrafficMarkingPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_traffic_marking_policy_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_traffic_marking_policy_attribute_with_options(request, runtime)

    def update_transit_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_description):
            query['TransitRouterDescription'] = request.transit_router_description
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouter',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_with_options(request, runtime)

    def update_transit_router_peer_attachment_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.cen_bandwidth_package_id):
            query['CenBandwidthPackageId'] = request.cen_bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterPeerAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterPeerAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_peer_attachment_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_peer_attachment_attribute_with_options(request, runtime)

    def update_transit_router_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_entry_description):
            query['TransitRouterRouteEntryDescription'] = request.transit_router_route_entry_description
        if not UtilClient.is_unset(request.transit_router_route_entry_id):
            query['TransitRouterRouteEntryId'] = request.transit_router_route_entry_id
        if not UtilClient.is_unset(request.transit_router_route_entry_name):
            query['TransitRouterRouteEntryName'] = request.transit_router_route_entry_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterRouteEntry',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_route_entry_with_options(request, runtime)

    def update_transit_router_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_route_table_description):
            query['TransitRouterRouteTableDescription'] = request.transit_router_route_table_description
        if not UtilClient.is_unset(request.transit_router_route_table_id):
            query['TransitRouterRouteTableId'] = request.transit_router_route_table_id
        if not UtilClient.is_unset(request.transit_router_route_table_name):
            query['TransitRouterRouteTableName'] = request.transit_router_route_table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterRouteTable',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_route_table_with_options(request, runtime)

    def update_transit_router_vbr_attachment_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVbrAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVbrAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_vbr_attachment_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vbr_attachment_attribute_with_options(request, runtime)

    def update_transit_router_vpc_attachment_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpcAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpcAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_vpc_attachment_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpc_attachment_attribute_with_options(request, runtime)

    def update_transit_router_vpc_attachment_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_zone_mappings):
            query['AddZoneMappings'] = request.add_zone_mappings
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remove_zone_mappings):
            query['RemoveZoneMappings'] = request.remove_zone_mappings
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpcAttachmentZones',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpcAttachmentZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_vpc_attachment_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpc_attachment_zones_with_options(request, runtime)

    def update_transit_router_vpn_attachment_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_publish_route_enabled):
            query['AutoPublishRouteEnabled'] = request.auto_publish_route_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_attachment_description):
            query['TransitRouterAttachmentDescription'] = request.transit_router_attachment_description
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_name):
            query['TransitRouterAttachmentName'] = request.transit_router_attachment_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTransitRouterVpnAttachmentAttribute',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.UpdateTransitRouterVpnAttachmentAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transit_router_vpn_attachment_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpn_attachment_attribute_with_options(request, runtime)

    def withdraw_published_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not UtilClient.is_unset(request.child_instance_region_id):
            query['ChildInstanceRegionId'] = request.child_instance_region_id
        if not UtilClient.is_unset(request.child_instance_route_table_id):
            query['ChildInstanceRouteTableId'] = request.child_instance_route_table_id
        if not UtilClient.is_unset(request.child_instance_type):
            query['ChildInstanceType'] = request.child_instance_type
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawPublishedRouteEntries',
            version='2017-09-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cbn_20170912_models.WithdrawPublishedRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def withdraw_published_route_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.withdraw_published_route_entries_with_options(request, runtime)
