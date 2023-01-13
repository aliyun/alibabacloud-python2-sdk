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
        """
        ## Usage notes
        *   After you create a flow log, it is enabled by default. You can call this operation to enable a disabled flow log.
        *   `ActiveFlowLog` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Modifying** state, the flow log is being enabled. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Active** state, the flow log is enabled.
        

        @param request: ActiveFlowLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ActiveFlowLogResponse
        """
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
        """
        ## Usage notes
        *   After you create a flow log, it is enabled by default. You can call this operation to enable a disabled flow log.
        *   `ActiveFlowLog` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Modifying** state, the flow log is being enabled. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Active** state, the flow log is enabled.
        

        @param request: ActiveFlowLogRequest

        @return: ActiveFlowLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    def add_traffic_match_rule_to_traffic_marking_policy_with_options(self, request, runtime):
        """
        *AddTrafficMatchRuleToTrafficMarkingPolicy** is an asynchronous operation. After you send a request, a **request ID** is returned but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic classification rule.
        *   If a traffic classification rule is in the **Creating** state, the traffic classification rule is being created. In this case, you can query the traffic classification rule but cannot perform other operations.
        *   If a traffic classification rule is in the **Active** state, the traffic classification rule is added to the traffic marking policy.
        

        @param request: AddTrafficMatchRuleToTrafficMarkingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTrafficMatchRuleToTrafficMarkingPolicyResponse
        """
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
        """
        *AddTrafficMatchRuleToTrafficMarkingPolicy** is an asynchronous operation. After you send a request, a **request ID** is returned but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic classification rule.
        *   If a traffic classification rule is in the **Creating** state, the traffic classification rule is being created. In this case, you can query the traffic classification rule but cannot perform other operations.
        *   If a traffic classification rule is in the **Active** state, the traffic classification rule is added to the traffic marking policy.
        

        @param request: AddTrafficMatchRuleToTrafficMarkingPolicyRequest

        @return: AddTrafficMatchRuleToTrafficMarkingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    def add_trafic_match_rule_to_traffic_marking_policy_with_options(self, request, runtime):
        """
        @deprecated : AddTraficMatchRuleToTrafficMarkingPolicy is deprecated, please use Cbn::2017-09-12::AddTrafficMatchRuleToTrafficMarkingPolicy instead.
        ## Usage notes
        The **AddTraficMatchRuleToTrafficMarkingPolicy** operation is deprecated and will be discontinued soon. If you need to add a traffic classification rule to a traffic marking policy, call the [AddTrafficMatchRuleToTrafficMarkingPolicy](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/addtrafficmatchruletotrafficmarkingpolicy) operation.
        

        @param request: AddTraficMatchRuleToTrafficMarkingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTraficMatchRuleToTrafficMarkingPolicyResponse
        Deprecated
        """
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
        """
        @deprecated : AddTraficMatchRuleToTrafficMarkingPolicy is deprecated, please use Cbn::2017-09-12::AddTrafficMatchRuleToTrafficMarkingPolicy instead.
        ## Usage notes
        The **AddTraficMatchRuleToTrafficMarkingPolicy** operation is deprecated and will be discontinued soon. If you need to add a traffic classification rule to a traffic marking policy, call the [AddTrafficMatchRuleToTrafficMarkingPolicy](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/addtrafficmatchruletotrafficmarkingpolicy) operation.
        

        @param request: AddTraficMatchRuleToTrafficMarkingPolicyRequest

        @return: AddTraficMatchRuleToTrafficMarkingPolicyResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.add_trafic_match_rule_to_traffic_marking_policy_with_options(request, runtime)

    def associate_cen_bandwidth_package_with_options(self, request, runtime):
        """
        ## Limits
        You can associate multiple bandwidth plans with a CEN instance, but the combination of areas connected by each bandwidth plan must be unique.
        For example, if the CEN instance is associated with a bandwidth plan that connects the Chinese mainland to the Chinese mainland, you cannot associate the CEN instance with another bandwidth plan that connects the Chinese mainland to the Chinese mainland. However, you can associate the CEN instance with a bandwidth plan that connects the Chinese mainland to North America.
        

        @param request: AssociateCenBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateCenBandwidthPackageResponse
        """
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
        """
        ## Limits
        You can associate multiple bandwidth plans with a CEN instance, but the combination of areas connected by each bandwidth plan must be unique.
        For example, if the CEN instance is associated with a bandwidth plan that connects the Chinese mainland to the Chinese mainland, you cannot associate the CEN instance with another bandwidth plan that connects the Chinese mainland to the Chinese mainland. However, you can associate the CEN instance with a bandwidth plan that connects the Chinese mainland to North America.
        

        @param request: AssociateCenBandwidthPackageRequest

        @return: AssociateCenBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_cen_bandwidth_package_with_options(request, runtime)

    def associate_transit_router_attachment_with_route_table_with_options(self, request, runtime):
        """
        ## Usage notes
        After you create a network instance connection on a transit router, you can configure an associated forwarding correlation to associate the network instance connection with a route table. Then, the network instance connection can forward network traffic based on the associated route table. Before you begin, we recommend that you read and understand the following rules:
        *   Only Enterprise Edition transit routers support associated forwarding correlations. For more information about the regions and zones that support Enterprise Edition transit routers, see [Transit routers](~~181681~~).
        *   **AssociateTransitRouterAttachmentWithRouteTable** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTableAssociations** to query the status of an associated forwarding correlation.
        *   If an associated forwarding correlation is in the **Associating** state, the associated forwarding correlation is being created. You can query the associated forwarding correlation but cannot perform other operations.
        *   If an associated forwarding correlation is in the **Active** state, the associated forwarding correlation is created.
        

        @param request: AssociateTransitRouterAttachmentWithRouteTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateTransitRouterAttachmentWithRouteTableResponse
        """
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
        """
        ## Usage notes
        After you create a network instance connection on a transit router, you can configure an associated forwarding correlation to associate the network instance connection with a route table. Then, the network instance connection can forward network traffic based on the associated route table. Before you begin, we recommend that you read and understand the following rules:
        *   Only Enterprise Edition transit routers support associated forwarding correlations. For more information about the regions and zones that support Enterprise Edition transit routers, see [Transit routers](~~181681~~).
        *   **AssociateTransitRouterAttachmentWithRouteTable** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTableAssociations** to query the status of an associated forwarding correlation.
        *   If an associated forwarding correlation is in the **Associating** state, the associated forwarding correlation is being created. You can query the associated forwarding correlation but cannot perform other operations.
        *   If an associated forwarding correlation is in the **Active** state, the associated forwarding correlation is created.
        

        @param request: AssociateTransitRouterAttachmentWithRouteTableRequest

        @return: AssociateTransitRouterAttachmentWithRouteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_transit_router_attachment_with_route_table_with_options(request, runtime)

    def associate_transit_router_multicast_domain_with_options(self, request, runtime):
        """
        ## Usage notes
        *   A vSwitch can be associated with only one multicast domain. Make sure that the vSwitch is not associated with other multicast domains. For more information about how to disassociate a vSwitch from a multicast domain, see [DisassociateTransitRouterMulticastDomain](~~429774~~).
        *   **AssociateTransitRouterMulticastDomain** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouterMulticastDomainAssociations** to query the association status between a vSwitch and a multicast domain.
        *   **Associating**: The vSwitch is being associated with the multicast domain. In this case, you can query the vSwitch but cannot perform other operations.
        *   **Associated**: The vSwitch is associated with the multicast domain.
        

        @param request: AssociateTransitRouterMulticastDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateTransitRouterMulticastDomainResponse
        """
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
        """
        ## Usage notes
        *   A vSwitch can be associated with only one multicast domain. Make sure that the vSwitch is not associated with other multicast domains. For more information about how to disassociate a vSwitch from a multicast domain, see [DisassociateTransitRouterMulticastDomain](~~429774~~).
        *   **AssociateTransitRouterMulticastDomain** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouterMulticastDomainAssociations** to query the association status between a vSwitch and a multicast domain.
        *   **Associating**: The vSwitch is being associated with the multicast domain. In this case, you can query the vSwitch but cannot perform other operations.
        *   **Associated**: The vSwitch is associated with the multicast domain.
        

        @param request: AssociateTransitRouterMulticastDomainRequest

        @return: AssociateTransitRouterMulticastDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_transit_router_multicast_domain_with_options(request, runtime)

    def attach_cen_child_instance_with_options(self, request, runtime):
        """
        ## Description
        CEN allows you to attach a network instance that belongs to another Alibaba Cloud account. Before you attach the network instance, CEN must acquire permissions to access the network instance that belongs to another Alibaba Cloud account.
        *   For more information about how to grant CEN permissions on accessing virtual private clouds (VPCs) that belong to another Alibaba Cloud account, see [GrantInstanceToCen](~~126224~~).
        *   For more information about how to grant CEN permissions on accessing Cloud Connect Network (CCN) instances that belong to another Alibaba Cloud account, see [GrantInstanceToCbn](~~126141~~).
        *   By default, you cannot grant CEN permissions on accessing virtual border routers (VBRs) that belong to another Alibaba Cloud account. To grant the permissions, you must [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        

        @param request: AttachCenChildInstanceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachCenChildInstanceResponse
        """
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
        """
        ## Description
        CEN allows you to attach a network instance that belongs to another Alibaba Cloud account. Before you attach the network instance, CEN must acquire permissions to access the network instance that belongs to another Alibaba Cloud account.
        *   For more information about how to grant CEN permissions on accessing virtual private clouds (VPCs) that belong to another Alibaba Cloud account, see [GrantInstanceToCen](~~126224~~).
        *   For more information about how to grant CEN permissions on accessing Cloud Connect Network (CCN) instances that belong to another Alibaba Cloud account, see [GrantInstanceToCbn](~~126141~~).
        *   By default, you cannot grant CEN permissions on accessing virtual border routers (VBRs) that belong to another Alibaba Cloud account. To grant the permissions, you must [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        

        @param request: AttachCenChildInstanceRequest

        @return: AttachCenChildInstanceResponse
        """
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
        """
        *CreateCen** is an asynchronous operation. After you send a request, the system returns the CEN instance ID but the operation is still being performed in the system background. You can call **DescribeCens** to query the status of a CEN instance.
        * If a CEN instance is in the **Creating** state, the CEN instance is being created. You can query the CEN instance but cannot perform other operations.
        * If a CEN instance is in the **Active** state, the CEN instance is created.
        

        @param request: CreateCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        *CreateCen** is an asynchronous operation. After you send a request, the system returns the CEN instance ID but the operation is still being performed in the system background. You can call **DescribeCens** to query the status of a CEN instance.
        * If a CEN instance is in the **Creating** state, the CEN instance is being created. You can query the CEN instance but cannot perform other operations.
        * If a CEN instance is in the **Active** state, the CEN instance is created.
        

        @param request: CreateCenRequest

        @return: CreateCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_with_options(request, runtime)

    def create_cen_bandwidth_package_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You must specify the areas to be connected when you create a bandwidth plan. An area contains one or more Alibaba Cloud regions. When you select areas for a bandwidth plan, make sure that the areas contain the regions that you want to connect. For more information about the supported areas and regions, see [Purchase a bandwidth plan](~~181560~~).
        *   For more information about the billing rules, see [Billing](~~189836~~).
        *   **CreateCenBandwidthPackage** is an asynchronous operation. After you send a request, the system returns the bandwidth plan ID but the operation is still being performed in the system background. You can call **DescribeCenBandwidthPackages** to query the status of a bandwidth plan. If a bandwidth plan is in the **Idle** or **InUse** state, the bandwidth plan is created.
        

        @param request: CreateCenBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenBandwidthPackageResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Usage notes
        *   You must specify the areas to be connected when you create a bandwidth plan. An area contains one or more Alibaba Cloud regions. When you select areas for a bandwidth plan, make sure that the areas contain the regions that you want to connect. For more information about the supported areas and regions, see [Purchase a bandwidth plan](~~181560~~).
        *   For more information about the billing rules, see [Billing](~~189836~~).
        *   **CreateCenBandwidthPackage** is an asynchronous operation. After you send a request, the system returns the bandwidth plan ID but the operation is still being performed in the system background. You can call **DescribeCenBandwidthPackages** to query the status of a bandwidth plan. If a bandwidth plan is in the **Idle** or **InUse** state, the bandwidth plan is created.
        

        @param request: CreateCenBandwidthPackageRequest

        @return: CreateCenBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_bandwidth_package_with_options(request, runtime)

    def create_cen_child_instance_route_entry_to_attachment_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You can add routes only to virtual private clouds (VPCs) or virtual border routers (VBRs) that are connected to an Enterprise Edition transit router.
        *   By default, the next hop of the routes is the **transit router connection**, which is the connection between the VBR and the Enterprise Edition transit router. You cannot modify the next hop.
        *   **CreateCenChildInstanceRouteEntryToAttachment** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeRouteEntryList** to query the status of a route.
        *   If a route is in the **Pending** state, the route is being created. You can query the route but cannot perform other operations.
        *   If a route is in the **Available** state, the route is created.
        

        @param request: CreateCenChildInstanceRouteEntryToAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenChildInstanceRouteEntryToAttachmentResponse
        """
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
        """
        ## Usage notes
        *   You can add routes only to virtual private clouds (VPCs) or virtual border routers (VBRs) that are connected to an Enterprise Edition transit router.
        *   By default, the next hop of the routes is the **transit router connection**, which is the connection between the VBR and the Enterprise Edition transit router. You cannot modify the next hop.
        *   **CreateCenChildInstanceRouteEntryToAttachment** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeRouteEntryList** to query the status of a route.
        *   If a route is in the **Pending** state, the route is being created. You can query the route but cannot perform other operations.
        *   If a route is in the **Available** state, the route is created.
        

        @param request: CreateCenChildInstanceRouteEntryToAttachmentRequest

        @return: CreateCenChildInstanceRouteEntryToAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    def create_cen_child_instance_route_entry_to_cen_with_options(self, request, runtime):
        """
        ## Limits
        *   By default, the CreateCenChildInstanceRouteEntryToCen operation is unavailable. To call this operation, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   You cannot add a route entry to an Enterprise Edition transit router by calling the CreateCenChildInstanceRouteEntryToCen operation.
        *   By default, the next hop of the route entry is the regional gateway of the CEN instance. You cannot modify the next hop.
        

        @param request: CreateCenChildInstanceRouteEntryToCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenChildInstanceRouteEntryToCenResponse
        """
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
        """
        ## Limits
        *   By default, the CreateCenChildInstanceRouteEntryToCen operation is unavailable. To call this operation, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   You cannot add a route entry to an Enterprise Edition transit router by calling the CreateCenChildInstanceRouteEntryToCen operation.
        *   By default, the next hop of the route entry is the regional gateway of the CEN instance. You cannot modify the next hop.
        

        @param request: CreateCenChildInstanceRouteEntryToCenRequest

        @return: CreateCenChildInstanceRouteEntryToCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    def create_cen_inter_region_traffic_qos_policy_with_options(self, request, runtime):
        """
        Only inter-region connections created on Enterprise Edition transit routers support QoS policies.
        If your inter-region connection uses test bandwidth, you cannot create QoS policies for the inter-region connection.
        *   QoS policies apply only to outbound traffic on Enterprise Edition transit routers.
        If you create an inter-region connection between the China (Hangzhou) region and the China (Qingdao) region, and create QoS policies for the transit router in the China (Hangzhou) region and the transit router in the China (Qingdao) region, the QoS policies apply only to the network traffic that flows from China (Hangzhou) to China (Qingdao). QoS policies allocate bandwidth resources to different services.
        *   **CreateCenInterRegionTrafficQosPolicy** is an asynchronous operation. After you send a request, the system returns a QoS policy ID and runs the task in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of a QoS policy.
        *   If a QoS policy is in the **Creating** state, the QoS policy is being created. You can query the QoS policy but cannot perform other operations.
        *   If a QoS policy is in the **Active** state, the QoS policy is created.
        ### Prerequisites
        Make sure that the following requirements are met before you call the **CreateCenInterRegionTrafficQosPolicy** operation:
        *   An inter-region connection is created. For more information, see [CreateTransitRouterPeerAttachment](~~261363~~).
        *   A traffic marking policy is created. For more information, see [CreateTrafficMarkingPolicy](~~419025~~).
        

        @param request: CreateCenInterRegionTrafficQosPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenInterRegionTrafficQosPolicyResponse
        """
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
        """
        Only inter-region connections created on Enterprise Edition transit routers support QoS policies.
        If your inter-region connection uses test bandwidth, you cannot create QoS policies for the inter-region connection.
        *   QoS policies apply only to outbound traffic on Enterprise Edition transit routers.
        If you create an inter-region connection between the China (Hangzhou) region and the China (Qingdao) region, and create QoS policies for the transit router in the China (Hangzhou) region and the transit router in the China (Qingdao) region, the QoS policies apply only to the network traffic that flows from China (Hangzhou) to China (Qingdao). QoS policies allocate bandwidth resources to different services.
        *   **CreateCenInterRegionTrafficQosPolicy** is an asynchronous operation. After you send a request, the system returns a QoS policy ID and runs the task in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of a QoS policy.
        *   If a QoS policy is in the **Creating** state, the QoS policy is being created. You can query the QoS policy but cannot perform other operations.
        *   If a QoS policy is in the **Active** state, the QoS policy is created.
        ### Prerequisites
        Make sure that the following requirements are met before you call the **CreateCenInterRegionTrafficQosPolicy** operation:
        *   An inter-region connection is created. For more information, see [CreateTransitRouterPeerAttachment](~~261363~~).
        *   A traffic marking policy is created. For more information, see [CreateTrafficMarkingPolicy](~~419025~~).
        

        @param request: CreateCenInterRegionTrafficQosPolicyRequest

        @return: CreateCenInterRegionTrafficQosPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    def create_cen_inter_region_traffic_qos_queue_with_options(self, request, runtime):
        """
        ## Usage note
        **CreateCenInterRegionTrafficQosQueue** is an asynchronous operation. After you send a request, the queue ID is returned but the operation is still being performed in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of the QoS policy to determine the status of the queue. When you call this operation, you must set the **TrafficQosPolicyId** parameter.
        *   If a QoS policy is in the **Modifying** state, the queue is being created. In this case, you can query the QoS policy and queue but cannot perform other operations.
        *   If a QoS policy is in the **Active** state, the queue is created.
        

        @param request: CreateCenInterRegionTrafficQosQueueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenInterRegionTrafficQosQueueResponse
        """
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
        """
        ## Usage note
        **CreateCenInterRegionTrafficQosQueue** is an asynchronous operation. After you send a request, the queue ID is returned but the operation is still being performed in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of the QoS policy to determine the status of the queue. When you call this operation, you must set the **TrafficQosPolicyId** parameter.
        *   If a QoS policy is in the **Modifying** state, the queue is being created. In this case, you can query the QoS policy and queue but cannot perform other operations.
        *   If a QoS policy is in the **Active** state, the queue is created.
        

        @param request: CreateCenInterRegionTrafficQosQueueRequest

        @return: CreateCenInterRegionTrafficQosQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    def create_cen_route_map_with_options(self, request, runtime):
        """
        Routing policies are sorted by priority. A smaller value indicates a higher priority. Each routing policy is a collection of conditional statements and execution statements. Starting from the routing policy with the highest priority, the system matches routes against the match conditions specified by routing policies. If a route meets all the match conditions of a routing policy, the system permits or denies the route based on the action specified in the routing policy. You can also modify the attributes of permitted routes. By default, the system permits routes that meet none of the match conditions. For more information, see [Routing policy overview](~~124157~~).
        `CreateCenRouteMap` is an asynchronous operation. After you send a request, the routing policy ID is returned but the operation is still being performed in the system background. You can call `DescribeCenRouteMaps` to query the status of a routing policy.
        *   If a routing policy is in the **Creating** state, the routing policy is being created. In this case, you can query the routing policy but cannot perform other operations.
        *   If a routing policy is in the **Active** state, the routing policy is created.
        

        @param request: CreateCenRouteMapRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCenRouteMapResponse
        """
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
        """
        Routing policies are sorted by priority. A smaller value indicates a higher priority. Each routing policy is a collection of conditional statements and execution statements. Starting from the routing policy with the highest priority, the system matches routes against the match conditions specified by routing policies. If a route meets all the match conditions of a routing policy, the system permits or denies the route based on the action specified in the routing policy. You can also modify the attributes of permitted routes. By default, the system permits routes that meet none of the match conditions. For more information, see [Routing policy overview](~~124157~~).
        `CreateCenRouteMap` is an asynchronous operation. After you send a request, the routing policy ID is returned but the operation is still being performed in the system background. You can call `DescribeCenRouteMaps` to query the status of a routing policy.
        *   If a routing policy is in the **Creating** state, the routing policy is being created. In this case, you can query the routing policy but cannot perform other operations.
        *   If a routing policy is in the **Active** state, the routing policy is created.
        

        @param request: CreateCenRouteMapRequest

        @return: CreateCenRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cen_route_map_with_options(request, runtime)

    def create_flowlog_with_options(self, request, runtime):
        """
        ## Usage notes
        Flow logs are used to capture the information about network traffic between transit routers and between virtual border routers (VBRs). Before you create a flow log, take note of the following items:
        *   Flow logs are supported only by Enterprise Edition transit routers.
        *   Only flow logs in some regions can capture the information about network traffic over VBR connections. For more information, see [Limits](~~339822~~).
        *   Flow logs are used to capture the information about outbound traffic on transit routers. Information about inbound traffic on transit routers is not captured.
        For example, an Elastic Compute Service (ECS) instance in the US (Silicon Valley) region accesses an ECS instance in the US (Virginia) region through CEN. After you enable the flow log feature for the transit router in the US (Virginia) region, you can check the log entries about packets sent from the ECS instance in the US (Virginia) region to the ECS instance in the US (Silicon Valley) region. However, packets sent from the ECS instance in the US (Silicon Valley) region to the ECS instance in the US (Virginia) region are not recorded. If you want to record the packets sent from the ECS instance in the US (Silicon Valley) region to the ECS instance in the US (Virginia) region, you must also enable the flow log feature on the transit router that is in the US (Silicon Valley) region.
        *   `CreateFlowLog` is an asynchronous operation. After you send a request, the system returns the request ID but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Creating** state, the flow log is being created. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Active** state, the flow log is created.
        ## Prerequisites
        An inter-region connection or a VBR connection is created. For more information, see [CreateTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createtransitrouterpeerattachment) or [CreateTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createtransitroutervbrattachment)
        

        @param request: CreateFlowlogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFlowlogResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Usage notes
        Flow logs are used to capture the information about network traffic between transit routers and between virtual border routers (VBRs). Before you create a flow log, take note of the following items:
        *   Flow logs are supported only by Enterprise Edition transit routers.
        *   Only flow logs in some regions can capture the information about network traffic over VBR connections. For more information, see [Limits](~~339822~~).
        *   Flow logs are used to capture the information about outbound traffic on transit routers. Information about inbound traffic on transit routers is not captured.
        For example, an Elastic Compute Service (ECS) instance in the US (Silicon Valley) region accesses an ECS instance in the US (Virginia) region through CEN. After you enable the flow log feature for the transit router in the US (Virginia) region, you can check the log entries about packets sent from the ECS instance in the US (Virginia) region to the ECS instance in the US (Silicon Valley) region. However, packets sent from the ECS instance in the US (Silicon Valley) region to the ECS instance in the US (Virginia) region are not recorded. If you want to record the packets sent from the ECS instance in the US (Silicon Valley) region to the ECS instance in the US (Virginia) region, you must also enable the flow log feature on the transit router that is in the US (Silicon Valley) region.
        *   `CreateFlowLog` is an asynchronous operation. After you send a request, the system returns the request ID but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Creating** state, the flow log is being created. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Active** state, the flow log is created.
        ## Prerequisites
        An inter-region connection or a VBR connection is created. For more information, see [CreateTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createtransitrouterpeerattachment) or [CreateTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createtransitroutervbrattachment)
        

        @param request: CreateFlowlogRequest

        @return: CreateFlowlogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_flowlog_with_options(request, runtime)

    def create_traffic_marking_policy_with_options(self, request, runtime):
        """
        ## Usage notes
        *   Only Enterprise Edition transit routers support traffic marking policies.
        *   **CreateTrafficMarkingPolicy** is an asynchronous operation. After you send a request, the system returns the traffic marking policy ID but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic marking policy.
        *   If a traffic marking policy is in the **Creating** state, the traffic marking policy is being created. You can query the traffic marking policy but cannot perform other operations.
        *   If a traffic marking policy is in the **Active** state, the traffic marking policy is created.
        

        @param request: CreateTrafficMarkingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTrafficMarkingPolicyResponse
        """
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
        """
        ## Usage notes
        *   Only Enterprise Edition transit routers support traffic marking policies.
        *   **CreateTrafficMarkingPolicy** is an asynchronous operation. After you send a request, the system returns the traffic marking policy ID but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic marking policy.
        *   If a traffic marking policy is in the **Creating** state, the traffic marking policy is being created. You can query the traffic marking policy but cannot perform other operations.
        *   If a traffic marking policy is in the **Active** state, the traffic marking policy is created.
        

        @param request: CreateTrafficMarkingPolicyRequest

        @return: CreateTrafficMarkingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_marking_policy_with_options(request, runtime)

    def create_transit_route_table_aggregation_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not UtilClient.is_unset(request.transit_route_table_aggregation_description):
            query['TransitRouteTableAggregationDescription'] = request.transit_route_table_aggregation_description
        if not UtilClient.is_unset(request.transit_route_table_aggregation_name):
            query['TransitRouteTableAggregationName'] = request.transit_route_table_aggregation_name
        if not UtilClient.is_unset(request.transit_route_table_aggregation_scop):
            query['TransitRouteTableAggregationScop'] = request.transit_route_table_aggregation_scop
        if not UtilClient.is_unset(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTransitRouteTableAggregation',
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
            cbn_20170912_models.CreateTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_route_table_aggregation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_transit_route_table_aggregation_with_options(request, runtime)

    def create_transit_router_with_options(self, tmp_req, runtime):
        """
        You can call **CreateTransitRouter** to create an Enterprise Edition transit router. For more information about the regions that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   **CreateTransitRouter** is an asynchronous operation. After you send a request, the transit router ID is returned but the operation is still being performed in the system background. You can call **ListTransitRouters** to query the status of an Enterprise Edition transit router transit router.
        *   If an Enterprise Edition transit router is in the **Creating** state, the Enterprise Edition transit router is being created. In this case, you can query the Enterprise Edition transit router but cannot perform other operations.
        *   If an Enterprise Edition transit router is in the **Active** state, the Enterprise Edition transit router is created.
        

        @param tmp_req: CreateTransitRouterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cbn_20170912_models.CreateTransitRouterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.transit_router_cidr_list):
            request.transit_router_cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transit_router_cidr_list, 'TransitRouterCidrList', 'json')
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_cidr_list_shrink):
            query['TransitRouterCidrList'] = request.transit_router_cidr_list_shrink
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
        """
        You can call **CreateTransitRouter** to create an Enterprise Edition transit router. For more information about the regions that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   **CreateTransitRouter** is an asynchronous operation. After you send a request, the transit router ID is returned but the operation is still being performed in the system background. You can call **ListTransitRouters** to query the status of an Enterprise Edition transit router transit router.
        *   If an Enterprise Edition transit router is in the **Creating** state, the Enterprise Edition transit router is being created. In this case, you can query the Enterprise Edition transit router but cannot perform other operations.
        *   If an Enterprise Edition transit router is in the **Active** state, the Enterprise Edition transit router is created.
        

        @param request: CreateTransitRouterRequest

        @return: CreateTransitRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_with_options(request, runtime)

    def create_transit_router_cidr_with_options(self, request, runtime):
        """
        You can specify a CIDR block for a transit router. The CIDR block works in a similar way as the CIDR block of the loopback interface on a router. IP addresses within the CIDR block can be assigned to IPsec-VPN connections. For more information, see [Transit router CIDR blocks](~~462635~~).
        The **CreateTransitRouterCidr** operation can be used to create a CIDR block only after you create a transit router.
        The CIDR block must meet the following requirements:
        *   Only Enterprise Edition transit routers support custom CIDR blocks.
        *   This feature is in pubic preview and is available only in some regions. For more information about the supported regions, see [Limits on transit router CIDR blocks](~~462635~~).
        *   Each transit router supports at most five CIDR blocks. The subnet mask of a CIDR block must be 16 bits to 24 bits in length.
        *   The following CIDR blocks and their subnets are not supported: 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, and 169.254.0.0/16.
        *   The CIDR block cannot overlap with CIDR blocks that network instances attached to the CEN instance use to communicate with each other.
        *   On the same CEN instance, each transit router CIDR block must be unique.
        *   When you create the first VPN connection after you add a CIDR block for a transit router, three CIDR blocks within the CIDR block are reserved. An IP address is allocated from the remaining CIDR blocks to the IPsec-VPN connection.
        You can call [ListTransitRouterCidrAllocation](~~464173~~) to query reserved CIDR blocks and IP addresses allocated to network connections.
        

        @param request: CreateTransitRouterCidrRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
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
            action='CreateTransitRouterCidr',
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
            cbn_20170912_models.CreateTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transit_router_cidr(self, request):
        """
        You can specify a CIDR block for a transit router. The CIDR block works in a similar way as the CIDR block of the loopback interface on a router. IP addresses within the CIDR block can be assigned to IPsec-VPN connections. For more information, see [Transit router CIDR blocks](~~462635~~).
        The **CreateTransitRouterCidr** operation can be used to create a CIDR block only after you create a transit router.
        The CIDR block must meet the following requirements:
        *   Only Enterprise Edition transit routers support custom CIDR blocks.
        *   This feature is in pubic preview and is available only in some regions. For more information about the supported regions, see [Limits on transit router CIDR blocks](~~462635~~).
        *   Each transit router supports at most five CIDR blocks. The subnet mask of a CIDR block must be 16 bits to 24 bits in length.
        *   The following CIDR blocks and their subnets are not supported: 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, and 169.254.0.0/16.
        *   The CIDR block cannot overlap with CIDR blocks that network instances attached to the CEN instance use to communicate with each other.
        *   On the same CEN instance, each transit router CIDR block must be unique.
        *   When you create the first VPN connection after you add a CIDR block for a transit router, three CIDR blocks within the CIDR block are reserved. An IP address is allocated from the remaining CIDR blocks to the IPsec-VPN connection.
        You can call [ListTransitRouterCidrAllocation](~~464173~~) to query reserved CIDR blocks and IP addresses allocated to network connections.
        

        @param request: CreateTransitRouterCidrRequest

        @return: CreateTransitRouterCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_cidr_with_options(request, runtime)

    def create_transit_router_multicast_domain_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you have knowledge of the following rules:
        *   Only Enterprise Edition transit routers in the Australia (Sydney) and UK (London) regions support the multicast feature. Multicast is unavailable by default. If you want to enable multicast, contact your sales manager or [submit a ticket](https://selfservice.console.aliyun.com/ticket/category/cbn/today) to apply for multicast resources.
        *   Make sure that an Enterprise Edition transit router is deployed in the region where you want to create the multicast domain, and the multicast feature is enabled for the Enterprise Edition transit router. For more information, see [CreateTransitRouter](~~261169~~).
        If an Enterprise Edition transit router was created before you apply for multicast resources, the transit router does not support multicast. You can delete the transit router and create a new one. For more information about how to delete an Enterprise Edition transit router, see [DeleteTransitRouter](~~261218~~).
        *   When you call **CreateTransitRouterMulticastDomain**, if you set **CenId** and **RegionId**, you do not need to set **TransitRouterId**. If you set **TransitRouterId**, you do not need to set **CenId** or **RegionId**.
        

        @param request: CreateTransitRouterMulticastDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterMulticastDomainResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        Before you call this operation, make sure that you have knowledge of the following rules:
        *   Only Enterprise Edition transit routers in the Australia (Sydney) and UK (London) regions support the multicast feature. Multicast is unavailable by default. If you want to enable multicast, contact your sales manager or [submit a ticket](https://selfservice.console.aliyun.com/ticket/category/cbn/today) to apply for multicast resources.
        *   Make sure that an Enterprise Edition transit router is deployed in the region where you want to create the multicast domain, and the multicast feature is enabled for the Enterprise Edition transit router. For more information, see [CreateTransitRouter](~~261169~~).
        If an Enterprise Edition transit router was created before you apply for multicast resources, the transit router does not support multicast. You can delete the transit router and create a new one. For more information about how to delete an Enterprise Edition transit router, see [DeleteTransitRouter](~~261218~~).
        *   When you call **CreateTransitRouterMulticastDomain**, if you set **CenId** and **RegionId**, you do not need to set **TransitRouterId**. If you set **TransitRouterId**, you do not need to set **CenId** or **RegionId**.
        

        @param request: CreateTransitRouterMulticastDomainRequest

        @return: CreateTransitRouterMulticastDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_multicast_domain_with_options(request, runtime)

    def create_transit_router_peer_attachment_with_options(self, request, runtime):
        """
        ## Background information
        By default, 1 Kbit/s of bandwidth is provided for inter-region communication between transit routers. This allows you to test the connectivity of inter-region IPv4 networks. To allow services that are deployed in different regions to communicate with each other, you must create an inter-region connection and allocate bandwidth resources to the connection.
        Enterprise Edition transit routers allow you to allocate bandwidth resources to inter-region connections by using the following methods:
        - **Allocate bandwidth resources from a bandwidth plan**:  You must purchase a bandwidth plan, and then allocate bandwidth resources from the bandwidth plan to inter-region connections. For more information, see [CreateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createcenbandwidthpackage).
        - **Use pay-by-data-transfer bandwidth resources**:  You can set a maximum bandwidth value for an inter-region connection. Then, you are charged for the amount of data transfer over the connection. For more information, see [Cross-region data transfers](https://www.alibabacloud.com/help/en/cloud-data-transmission/latest/cross-region-data-transfers).
        ## Usage notes
        **CreateTransitRouterPeerAttachment** is an asynchronous operation. After you send a request, the system returns the inter-region connection ID but the operation is still being performed in the system background. You can call **ListTransitRouterPeerAttachments** to query the status of an inter-region connection.
        - If an inter-region connection is in the **Attaching** state, the inter-region connection is being created. You can query the inter-region connection but cannot perform other regions.
        - If an inter-region connection is in the **Attached** state, the inter-region connection is created.
        

        @param request: CreateTransitRouterPeerAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterPeerAttachmentResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Background information
        By default, 1 Kbit/s of bandwidth is provided for inter-region communication between transit routers. This allows you to test the connectivity of inter-region IPv4 networks. To allow services that are deployed in different regions to communicate with each other, you must create an inter-region connection and allocate bandwidth resources to the connection.
        Enterprise Edition transit routers allow you to allocate bandwidth resources to inter-region connections by using the following methods:
        - **Allocate bandwidth resources from a bandwidth plan**:  You must purchase a bandwidth plan, and then allocate bandwidth resources from the bandwidth plan to inter-region connections. For more information, see [CreateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createcenbandwidthpackage).
        - **Use pay-by-data-transfer bandwidth resources**:  You can set a maximum bandwidth value for an inter-region connection. Then, you are charged for the amount of data transfer over the connection. For more information, see [Cross-region data transfers](https://www.alibabacloud.com/help/en/cloud-data-transmission/latest/cross-region-data-transfers).
        ## Usage notes
        **CreateTransitRouterPeerAttachment** is an asynchronous operation. After you send a request, the system returns the inter-region connection ID but the operation is still being performed in the system background. You can call **ListTransitRouterPeerAttachments** to query the status of an inter-region connection.
        - If an inter-region connection is in the **Attaching** state, the inter-region connection is being created. You can query the inter-region connection but cannot perform other regions.
        - If an inter-region connection is in the **Attached** state, the inter-region connection is created.
        

        @param request: CreateTransitRouterPeerAttachmentRequest

        @return: CreateTransitRouterPeerAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_peer_attachment_with_options(request, runtime)

    def create_transit_router_prefix_list_association_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you begin, we recommend that you read and understand the limits, compatibility, and route advertising scope of a prefix. For more information, see [Prefix lists](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/prefix-lists).
        ## Prerequisites
        - A prefix list is created. For more information, see [CreateVpcPrefixList](https://www.alibabacloud.com/help/en/virtual-private-cloud/latest/creatvpcprefixlist).
        - The prefix list is shared with the Alibaba Cloud account that owns the Enterprise Edition transit router if the prefix list and the Enterprise Edition transit router belong to different Alibaba Cloud accounts. For more information about how to share a prefix list with another Alibaba Cloud account, see [Resource sharing overview](https://www.alibabacloud.com/help/en/resource-management/latest/resource-sharing-overview) and [API reference for resource sharing](https://www.alibabacloud.com/help/en/resource-management/latest/api-reference-3).
        

        @param request: CreateTransitRouterPrefixListAssociationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterPrefixListAssociationResponse
        """
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
        """
        ## Usage notes
        Before you begin, we recommend that you read and understand the limits, compatibility, and route advertising scope of a prefix. For more information, see [Prefix lists](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/prefix-lists).
        ## Prerequisites
        - A prefix list is created. For more information, see [CreateVpcPrefixList](https://www.alibabacloud.com/help/en/virtual-private-cloud/latest/creatvpcprefixlist).
        - The prefix list is shared with the Alibaba Cloud account that owns the Enterprise Edition transit router if the prefix list and the Enterprise Edition transit router belong to different Alibaba Cloud accounts. For more information about how to share a prefix list with another Alibaba Cloud account, see [Resource sharing overview](https://www.alibabacloud.com/help/en/resource-management/latest/resource-sharing-overview) and [API reference for resource sharing](https://www.alibabacloud.com/help/en/resource-management/latest/api-reference-3).
        

        @param request: CreateTransitRouterPrefixListAssociationRequest

        @return: CreateTransitRouterPrefixListAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_prefix_list_association_with_options(request, runtime)

    def create_transit_router_route_entry_with_options(self, request, runtime):
        """
        ## Usage notes
        **CreateTransitRouterRouteEntry** is an asynchronous operation. After you send a request, the route ID is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteEntries** to query the status of a route.
        *   If a route is in the **Creating** state, the route is being created. In this case, you can query the route but cannot perform other operations.
        *   If a route is in the **Active** state, the route is created.
        

        @param request: CreateTransitRouterRouteEntryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterRouteEntryResponse
        """
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
        """
        ## Usage notes
        **CreateTransitRouterRouteEntry** is an asynchronous operation. After you send a request, the route ID is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteEntries** to query the status of a route.
        *   If a route is in the **Creating** state, the route is being created. In this case, you can query the route but cannot perform other operations.
        *   If a route is in the **Active** state, the route is created.
        

        @param request: CreateTransitRouterRouteEntryRequest

        @return: CreateTransitRouterRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_route_entry_with_options(request, runtime)

    def create_transit_router_route_table_with_options(self, request, runtime):
        """
        ## Usage notes
        *   Only Enterprise Edition transit routers support custom route tables. For more information about the regions and zones that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   **CreateTransitRouterRouteTable** is an asynchronous operation. After you send a request, the route table ID is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTables** to query the status of a route table.
        *   If a route table is in the **Creating** state, the route table is being created. In this case, you can query the route table but cannot perform other operations.
        *   If a route table is in the **Active** state, the route table is created.
        

        @param request: CreateTransitRouterRouteTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterRouteTableResponse
        """
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
        if not UtilClient.is_unset(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Usage notes
        *   Only Enterprise Edition transit routers support custom route tables. For more information about the regions and zones that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   **CreateTransitRouterRouteTable** is an asynchronous operation. After you send a request, the route table ID is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTables** to query the status of a route table.
        *   If a route table is in the **Creating** state, the route table is being created. In this case, you can query the route table but cannot perform other operations.
        *   If a route table is in the **Active** state, the route table is created.
        

        @param request: CreateTransitRouterRouteTableRequest

        @return: CreateTransitRouterRouteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_route_table_with_options(request, runtime)

    def create_transit_router_vbr_attachment_with_options(self, request, runtime):
        """
        For more information about the regions and zones that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   You can use the following methods to create a VBR connection on an Enterprise Edition transit router:
        *   If an Enterprise Edition transit router is already created in the region where you want to create a VBR connection, set the **VbrId** and **TransitRouterId** parameters.
        *   If no Enterprise Edition transit router is created in the region where you want to create a VBR connection, set the **VbrId**, **CenId**, and **RegionId** parameters. Then, the system automatically creates an Enterprise Edition transit router in the specified region.
        *   **CreateTransitRouterVbrAttachment** is an asynchronous operation. After you send a request, the ID of the VBR connection is returned but the operation is still being performed in the system background. You can call **ListTransitRouterVbrAttachments** to query the status of a VBR connection.
        *   If a VBR is in the **Attaching** state, the VBR connection is being created. You can query the VBR connection but cannot perform other operations.
        *   If a VBR connection is in the **Attached** state, the VBR connection is created.
        

        @param request: CreateTransitRouterVbrAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterVbrAttachmentResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        For more information about the regions and zones that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   You can use the following methods to create a VBR connection on an Enterprise Edition transit router:
        *   If an Enterprise Edition transit router is already created in the region where you want to create a VBR connection, set the **VbrId** and **TransitRouterId** parameters.
        *   If no Enterprise Edition transit router is created in the region where you want to create a VBR connection, set the **VbrId**, **CenId**, and **RegionId** parameters. Then, the system automatically creates an Enterprise Edition transit router in the specified region.
        *   **CreateTransitRouterVbrAttachment** is an asynchronous operation. After you send a request, the ID of the VBR connection is returned but the operation is still being performed in the system background. You can call **ListTransitRouterVbrAttachments** to query the status of a VBR connection.
        *   If a VBR is in the **Attaching** state, the VBR connection is being created. You can query the VBR connection but cannot perform other operations.
        *   If a VBR connection is in the **Attached** state, the VBR connection is created.
        

        @param request: CreateTransitRouterVbrAttachmentRequest

        @return: CreateTransitRouterVbrAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vbr_attachment_with_options(request, runtime)

    def create_transit_router_vpc_attachment_with_options(self, request, runtime):
        """
        ## Usage notes
        - You can use the following methods to create a VPC connection on an Enterprise Edition transit router:   - If an Enterprise Edition transit router is already created in the region where you want to create a VPC connection, set **VpcId**, **ZoneMappings.N.VSwitchId**, **ZoneMappings.N.ZoneId**, and **TransitRouterId**.
        - If no Enterprise Edition transit router is created in the region where you want to create a VPC connection, set **VpcId**, **ZoneMappings.N.VSwitchId**, **ZoneMappings.N.ZoneId**, **CenId**, and **RegionId**. When you create a VPC connection, the system automatically creates an Enterprise Edition transit router in the specified region.
        - **CreateTransitRouterVpcAttachment** is an asynchronous operation. After you send a request, the VPC connection ID is returned but the operation is still being performed in the system background. You can call [ListTransitRouterVpcAttachments](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/listtransitroutervpcattachments) to query the status of a VPC connection.    - If a VPC is in the **Attaching** state, the VPC connection is being created. You can query the VPC connection but cannot perform other operations.
        - If a VPC connection is in the **Attached** state, the VPC connection is created.
        - By default, route learning and associated forwarding are disabled between transit router route tables and VPC connections.
        ## Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        - At least one vSwitch is deployed for each VPC in the zones supported by Enterprise Edition transit routers. Each vSwitch must have at least one idle IP address. For more information, see [Regions and zones supported by Enterprise Edition transit routers](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/what-is-cen).
        - To connect to a network instance that belongs to another Alibaba Cloud account, you must first acquire the permissions from the account. For more information, see [Acquire permissions to connect to a network instance that belongs to another account](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/grant-permissions-to-another-alibaba-cloud-account).
        - VPC connections incur fees. Take note of the billing rules of VPC connections before you create a VPC connection. For more information, see [Billing](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/billing-billing).
        

        @param request: CreateTransitRouterVpcAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterVpcAttachmentResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Usage notes
        - You can use the following methods to create a VPC connection on an Enterprise Edition transit router:   - If an Enterprise Edition transit router is already created in the region where you want to create a VPC connection, set **VpcId**, **ZoneMappings.N.VSwitchId**, **ZoneMappings.N.ZoneId**, and **TransitRouterId**.
        - If no Enterprise Edition transit router is created in the region where you want to create a VPC connection, set **VpcId**, **ZoneMappings.N.VSwitchId**, **ZoneMappings.N.ZoneId**, **CenId**, and **RegionId**. When you create a VPC connection, the system automatically creates an Enterprise Edition transit router in the specified region.
        - **CreateTransitRouterVpcAttachment** is an asynchronous operation. After you send a request, the VPC connection ID is returned but the operation is still being performed in the system background. You can call [ListTransitRouterVpcAttachments](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/listtransitroutervpcattachments) to query the status of a VPC connection.    - If a VPC is in the **Attaching** state, the VPC connection is being created. You can query the VPC connection but cannot perform other operations.
        - If a VPC connection is in the **Attached** state, the VPC connection is created.
        - By default, route learning and associated forwarding are disabled between transit router route tables and VPC connections.
        ## Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        - At least one vSwitch is deployed for each VPC in the zones supported by Enterprise Edition transit routers. Each vSwitch must have at least one idle IP address. For more information, see [Regions and zones supported by Enterprise Edition transit routers](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/what-is-cen).
        - To connect to a network instance that belongs to another Alibaba Cloud account, you must first acquire the permissions from the account. For more information, see [Acquire permissions to connect to a network instance that belongs to another account](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/grant-permissions-to-another-alibaba-cloud-account).
        - VPC connections incur fees. Take note of the billing rules of VPC connections before you create a VPC connection. For more information, see [Billing](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/billing-billing).
        

        @param request: CreateTransitRouterVpcAttachmentRequest

        @return: CreateTransitRouterVpcAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vpc_attachment_with_options(request, runtime)

    def create_transit_router_vpn_attachment_with_options(self, request, runtime):
        """
        IPsec-VPN connections are supported only by Enterprise Edition transit routers deployed in some regions. If you want to create a VPN connection in regions that do not support IPsec-VPN connections, [submit a ticket](https://ia.aliyun.com/home?channel=ticket\\&mark=console-home) or contact your account manager. For more information about the regions, see [Connect a transit router to an IPsec-VPN connection](~~445769~~).
        *   By default, route learning and associated forwarding are disabled between transit router route tables and IPsec-VPN attachments.
        *   When you call `CreateTransitRouterVpnAttachment`, if you set **CenId** and **RegionId**, you do not need to set **TransitRouterId**. If you set **TransitRouterId** and **RegionId**, you do not need to set **CenId**.
        ## Prerequisites
        *   Before you connect a transit router to an IPsec-VPN connection, make sure that an IPsec-VPN connection is created in the region where the transit router is deployed. The IPsec-VPN connection cannot be associated with a resource. For more information, see [CreateVpnAttachment](~~442455~~).
        *   If the transit router needs to be associated with an IPsec-VPN connection within a different Alibaba Cloud account, make sure that the transit router has obtained the required permissions from the IPsec-VPN connection. For more information, see [GrantInstanceToTransitRouter](~~417520~~).
        

        @param request: CreateTransitRouterVpnAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTransitRouterVpnAttachmentResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        IPsec-VPN connections are supported only by Enterprise Edition transit routers deployed in some regions. If you want to create a VPN connection in regions that do not support IPsec-VPN connections, [submit a ticket](https://ia.aliyun.com/home?channel=ticket\\&mark=console-home) or contact your account manager. For more information about the regions, see [Connect a transit router to an IPsec-VPN connection](~~445769~~).
        *   By default, route learning and associated forwarding are disabled between transit router route tables and IPsec-VPN attachments.
        *   When you call `CreateTransitRouterVpnAttachment`, if you set **CenId** and **RegionId**, you do not need to set **TransitRouterId**. If you set **TransitRouterId** and **RegionId**, you do not need to set **CenId**.
        ## Prerequisites
        *   Before you connect a transit router to an IPsec-VPN connection, make sure that an IPsec-VPN connection is created in the region where the transit router is deployed. The IPsec-VPN connection cannot be associated with a resource. For more information, see [CreateVpnAttachment](~~442455~~).
        *   If the transit router needs to be associated with an IPsec-VPN connection within a different Alibaba Cloud account, make sure that the transit router has obtained the required permissions from the IPsec-VPN connection. For more information, see [GrantInstanceToTransitRouter](~~417520~~).
        

        @param request: CreateTransitRouterVpnAttachmentRequest

        @return: CreateTransitRouterVpnAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_transit_router_vpn_attachment_with_options(request, runtime)

    def deactive_flow_log_with_options(self, request, runtime):
        """
        ## Usage notes
        `DeactiveFlowLog` is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Modifying** state, the flow log is being disabled. You can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Inactive** state, the flow log is disabled.
        

        @param request: DeactiveFlowLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeactiveFlowLogResponse
        """
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
        """
        ## Usage notes
        `DeactiveFlowLog` is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Modifying** state, the flow log is being disabled. You can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Inactive** state, the flow log is disabled.
        

        @param request: DeactiveFlowLogRequest

        @return: DeactiveFlowLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    def delete_cen_with_options(self, request, runtime):
        """
        *DeleteCen** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCens** to query the status of a CEN instance.
        - If a CEN instance is in the **Deleting** state, the CEN instance is being deleted. In this case, you can query the CEN instance but cannot perform other operations.
        - If a CEN instance cannot be found, the CEN instance is deleted.
        ## Prerequisites
        The CEN instance that you want to delete is not associated with a bandwidth plan, and the transit router associated with the CEN instance does not have a network instance connection or a custom route table.
        - For more information about how to detach a network instance, see the following topics:   - [DeleteTransitRouterVpcAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpcattachment)
        - [DeleteTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervbrattachment)
        - [DeleteTransitRouterVpnAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpnattachment)
        - [DeleteTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterpeerattachment)>  For more information about how to detach network instances from a Basic Edition transit router, see [DetachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/detachcenchildinstance).
        - For more information about how to delete a custom route table, see [DeleteTransitRouterRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterroutetable).
        - For more information about how to disassociate a bandwidth plan from a CEN instance, see [UnassociateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/unassociatecenbandwidthpackage).
        

        @param request: DeleteCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenResponse
        """
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
        """
        *DeleteCen** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCens** to query the status of a CEN instance.
        - If a CEN instance is in the **Deleting** state, the CEN instance is being deleted. In this case, you can query the CEN instance but cannot perform other operations.
        - If a CEN instance cannot be found, the CEN instance is deleted.
        ## Prerequisites
        The CEN instance that you want to delete is not associated with a bandwidth plan, and the transit router associated with the CEN instance does not have a network instance connection or a custom route table.
        - For more information about how to detach a network instance, see the following topics:   - [DeleteTransitRouterVpcAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpcattachment)
        - [DeleteTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervbrattachment)
        - [DeleteTransitRouterVpnAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpnattachment)
        - [DeleteTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterpeerattachment)>  For more information about how to detach network instances from a Basic Edition transit router, see [DetachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/detachcenchildinstance).
        - For more information about how to delete a custom route table, see [DeleteTransitRouterRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterroutetable).
        - For more information about how to disassociate a bandwidth plan from a CEN instance, see [UnassociateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/unassociatecenbandwidthpackage).
        

        @param request: DeleteCenRequest

        @return: DeleteCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_with_options(request, runtime)

    def delete_cen_bandwidth_package_with_options(self, request, runtime):
        """
        ## Usage
        Before you delete a bandwidth plan, make sure that it is disassociated from all Cloud Enterprise Network (CEN) instances. For more information, see [UnassociateCenBandwidthPackage](~~65935~~).
        

        @param request: DeleteCenBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenBandwidthPackageResponse
        """
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
        """
        ## Usage
        Before you delete a bandwidth plan, make sure that it is disassociated from all Cloud Enterprise Network (CEN) instances. For more information, see [UnassociateCenBandwidthPackage](~~65935~~).
        

        @param request: DeleteCenBandwidthPackageRequest

        @return: DeleteCenBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_bandwidth_package_with_options(request, runtime)

    def delete_cen_child_instance_route_entry_to_attachment_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You can delete routes only from virtual private clouds (VPCs) and virtual border routers (VBRs) whose next hop is an **Enterprise Edition transit router connection**, which is the connection to the network instance.
        *   **DeleteCenChildInstanceRouteEntryToAttachment** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeRouteEntryList** to query the status of a route.
        *   If a route is in the **Deleting** state, the route is being deleted. You can query the route but cannot perform other operations.
        *   If a route cannot be found, the route is deleted.
        

        @param request: DeleteCenChildInstanceRouteEntryToAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenChildInstanceRouteEntryToAttachmentResponse
        """
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
        """
        ## Usage notes
        *   You can delete routes only from virtual private clouds (VPCs) and virtual border routers (VBRs) whose next hop is an **Enterprise Edition transit router connection**, which is the connection to the network instance.
        *   **DeleteCenChildInstanceRouteEntryToAttachment** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeRouteEntryList** to query the status of a route.
        *   If a route is in the **Deleting** state, the route is being deleted. You can query the route but cannot perform other operations.
        *   If a route cannot be found, the route is deleted.
        

        @param request: DeleteCenChildInstanceRouteEntryToAttachmentRequest

        @return: DeleteCenChildInstanceRouteEntryToAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_attachment_with_options(request, runtime)

    def delete_cen_child_instance_route_entry_to_cen_with_options(self, request, runtime):
        """
        ## Limits
        *   By default, the DeleteCenChildInstanceRouteEntryToCen operation is unavailable. To call this operation, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   You cannot delete a route entry from an Enterprise Edition transit router by calling the DeleteCenChildInstanceRouteEntryToCen operation.
        

        @param request: DeleteCenChildInstanceRouteEntryToCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenChildInstanceRouteEntryToCenResponse
        """
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
        """
        ## Limits
        *   By default, the DeleteCenChildInstanceRouteEntryToCen operation is unavailable. To call this operation, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   You cannot delete a route entry from an Enterprise Edition transit router by calling the DeleteCenChildInstanceRouteEntryToCen operation.
        

        @param request: DeleteCenChildInstanceRouteEntryToCenRequest

        @return: DeleteCenChildInstanceRouteEntryToCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    def delete_cen_inter_region_traffic_qos_policy_with_options(self, request, runtime):
        """
        ## Usage notes
        *   Before you delete a QoS policy, you must delete all queues in the QoS policy except the default queue. For more information, see [DeleteCenInterRegionTrafficQosQueue](~~419062~~).
        *   **DeleteCenInterRegionTrafficQosPolicy** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of a QoS policy.
        *   If a QoS policy is in the **Deleting** state, the QoS policy is being deleted. You can query the QoS policy but cannot perform other operations.
        *   If a QoS policy cannot be found, the QoS policy is deleted.
        

        @param request: DeleteCenInterRegionTrafficQosPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenInterRegionTrafficQosPolicyResponse
        """
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
        """
        ## Usage notes
        *   Before you delete a QoS policy, you must delete all queues in the QoS policy except the default queue. For more information, see [DeleteCenInterRegionTrafficQosQueue](~~419062~~).
        *   **DeleteCenInterRegionTrafficQosPolicy** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of a QoS policy.
        *   If a QoS policy is in the **Deleting** state, the QoS policy is being deleted. You can query the QoS policy but cannot perform other operations.
        *   If a QoS policy cannot be found, the QoS policy is deleted.
        

        @param request: DeleteCenInterRegionTrafficQosPolicyRequest

        @return: DeleteCenInterRegionTrafficQosPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_policy_with_options(request, runtime)

    def delete_cen_inter_region_traffic_qos_queue_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You cannot delete the default queue.
        *   **DeleteCenInterRegionTrafficQosQueue** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of a queue. If a queue cannot be found, the queue is deleted.
        

        @param request: DeleteCenInterRegionTrafficQosQueueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenInterRegionTrafficQosQueueResponse
        """
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
        """
        ## Usage notes
        *   You cannot delete the default queue.
        *   **DeleteCenInterRegionTrafficQosQueue** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListCenInterRegionTrafficQosPolicies** to query the status of a queue. If a queue cannot be found, the queue is deleted.
        

        @param request: DeleteCenInterRegionTrafficQosQueueRequest

        @return: DeleteCenInterRegionTrafficQosQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_inter_region_traffic_qos_queue_with_options(request, runtime)

    def delete_cen_route_map_with_options(self, request, runtime):
        """
        ## Usage notes
        `DeleteCenRouteMap` is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call `DescribeCenRouteMaps` to query the status of a routing policy.
        *   If a routing policy is in the **Deleting** state, the routing policy is being deleted. You can query the routing policy but cannot perform other operations.
        *   If a routing policy cannot be found, it is deleted.
        

        @param request: DeleteCenRouteMapRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCenRouteMapResponse
        """
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
        """
        ## Usage notes
        `DeleteCenRouteMap` is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call `DescribeCenRouteMaps` to query the status of a routing policy.
        *   If a routing policy is in the **Deleting** state, the routing policy is being deleted. You can query the routing policy but cannot perform other operations.
        *   If a routing policy cannot be found, it is deleted.
        

        @param request: DeleteCenRouteMapRequest

        @return: DeleteCenRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_route_map_with_options(request, runtime)

    def delete_flowlog_with_options(self, request, runtime):
        """
        ## Usage notes
        `DeleteFlowlog` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Deleting** state, the flow log is being deleted. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log cannot be found, the flow log is deleted.
        

        @param request: DeleteFlowlogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFlowlogResponse
        """
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
        """
        ## Usage notes
        `DeleteFlowlog` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Deleting** state, the flow log is being deleted. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log cannot be found, the flow log is deleted.
        

        @param request: DeleteFlowlogRequest

        @return: DeleteFlowlogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_flowlog_with_options(request, runtime)

    def delete_route_service_in_cen_with_options(self, request, runtime):
        """
        ## Usage notes
        **DeleteRouteServiceInCen** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **DescribeRouteServicesInCen** to query the status of the connection to a cloud service.
        *   If a cloud service is in the **Deleting** state, the connection to the cloud service is being deleted. You can query the connection but you cannot perform other operations.
        *   If no connection to a cloud service can be found, the connection to the cloud service is deleted.
        

        @param request: DeleteRouteServiceInCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRouteServiceInCenResponse
        """
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
        """
        ## Usage notes
        **DeleteRouteServiceInCen** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **DescribeRouteServicesInCen** to query the status of the connection to a cloud service.
        *   If a cloud service is in the **Deleting** state, the connection to the cloud service is being deleted. You can query the connection but you cannot perform other operations.
        *   If no connection to a cloud service can be found, the connection to the cloud service is deleted.
        

        @param request: DeleteRouteServiceInCenRequest

        @return: DeleteRouteServiceInCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_route_service_in_cen_with_options(request, runtime)

    def delete_traffic_marking_policy_with_options(self, request, runtime):
        """
        ## Usage notes
        *   **DeleteTrafficMarkingPolicy** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic marking policy.
        *   If a traffic marking policy is in the **Deleting** state, the traffic marking policy is being deleted. You can query the traffic marking policy, but cannot perform other operations.
        *   If a traffic marking policy cannot be found, the traffic marking policy is deleted.
        *   Before you delete a traffic marking policy, you must delete all traffic classification rules from the policy. For more information, see [RemoveTraficMatchRuleFromTrafficMarkingPolicy](~~419012~~).
        

        @param request: DeleteTrafficMarkingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTrafficMarkingPolicyResponse
        """
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
        """
        ## Usage notes
        *   **DeleteTrafficMarkingPolicy** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic marking policy.
        *   If a traffic marking policy is in the **Deleting** state, the traffic marking policy is being deleted. You can query the traffic marking policy, but cannot perform other operations.
        *   If a traffic marking policy cannot be found, the traffic marking policy is deleted.
        *   Before you delete a traffic marking policy, you must delete all traffic classification rules from the policy. For more information, see [RemoveTraficMatchRuleFromTrafficMarkingPolicy](~~419012~~).
        

        @param request: DeleteTrafficMarkingPolicyRequest

        @return: DeleteTrafficMarkingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_marking_policy_with_options(request, runtime)

    def delete_transit_route_table_aggregation_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not UtilClient.is_unset(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouteTableAggregation',
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
            cbn_20170912_models.DeleteTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_route_table_aggregation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_route_table_aggregation_with_options(request, runtime)

    def delete_transit_router_with_options(self, request, runtime):
        """
        *DeleteTransitRouter** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouters** to query the status of a transit router.
        - If a transit router is in the **Deleting** state, the transit router is being deleted. In this case, you can query the transit router but cannot perform other operations.
        - If a transit router cannot be found, the transit router is deleted.
        ## Prerequisites
        Before you delete a transit router, make sure that the following prerequisites are met:
        - No network instance connections are created on the transit router.    - For more information about how to delete a virtual private cloud (VPC) connection, see [DeleteTransitRouterVpcAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpcattachment).
        - For more information about how to delete a virtual border router (VBR) connection, see [DeleteTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervbrattachment).
        - For more information about how to delete a Cloud Connect Network (CCN) connection, see [DetachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/detachcenchildinstance).
        - For more information about how to delete a VPN connection, see [DeleteTransitRouterVpnAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpnattachment).
        - For more information about how to delete an inter-region connection, see [DeleteTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterpeerattachment).
        - No custom route tables are created on the transit router. For more information about how to delete a custom route table, see [DeleteTransitRouterRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterroutetable).
        

        @param request: DeleteTransitRouterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterResponse
        """
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
        """
        *DeleteTransitRouter** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouters** to query the status of a transit router.
        - If a transit router is in the **Deleting** state, the transit router is being deleted. In this case, you can query the transit router but cannot perform other operations.
        - If a transit router cannot be found, the transit router is deleted.
        ## Prerequisites
        Before you delete a transit router, make sure that the following prerequisites are met:
        - No network instance connections are created on the transit router.    - For more information about how to delete a virtual private cloud (VPC) connection, see [DeleteTransitRouterVpcAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpcattachment).
        - For more information about how to delete a virtual border router (VBR) connection, see [DeleteTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervbrattachment).
        - For more information about how to delete a Cloud Connect Network (CCN) connection, see [DetachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/detachcenchildinstance).
        - For more information about how to delete a VPN connection, see [DeleteTransitRouterVpnAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpnattachment).
        - For more information about how to delete an inter-region connection, see [DeleteTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterpeerattachment).
        - No custom route tables are created on the transit router. For more information about how to delete a custom route table, see [DeleteTransitRouterRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterroutetable).
        

        @param request: DeleteTransitRouterRequest

        @return: DeleteTransitRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_with_options(request, runtime)

    def delete_transit_router_cidr_with_options(self, request, runtime):
        """
        ## Usage notes
        If IP addresses within the CIDR block have been allocated to network instances, the CIDR block cannot be deleted.
        

        @param request: DeleteTransitRouterCidrRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterCidrResponse
        """
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
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTransitRouterCidr',
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
            cbn_20170912_models.DeleteTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transit_router_cidr(self, request):
        """
        ## Usage notes
        If IP addresses within the CIDR block have been allocated to network instances, the CIDR block cannot be deleted.
        

        @param request: DeleteTransitRouterCidrRequest

        @return: DeleteTransitRouterCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_cidr_with_options(request, runtime)

    def delete_transit_router_multicast_domain_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you delete a multicast domain, make sure that the following requirements are met:
        *   The multicast domain is disassociated from all vSwitches. For more information, see [DisassociateTransitRouterMulticastDomain](~~429774~~).
        *   All multicast sources and members are removed from the multicast domain. For more information, see [DeregisterTransitRouterMulticastGroupSources](~~429776~~) and [DeregisterTransitRouterMulticastGroupMembers](~~429779~~).
        *   The multicast domain is not added to other multicast domains as a multicast member. If the multicast domain is added to another multicast domain as a multicast member, you must remove the multicast domain from the other multicast domain. For more information, see [DeregisterTransitRouterMulticastGroupMembers](~~429779~~).
        

        @param request: DeleteTransitRouterMulticastDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterMulticastDomainResponse
        """
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
        """
        ## Usage notes
        Before you delete a multicast domain, make sure that the following requirements are met:
        *   The multicast domain is disassociated from all vSwitches. For more information, see [DisassociateTransitRouterMulticastDomain](~~429774~~).
        *   All multicast sources and members are removed from the multicast domain. For more information, see [DeregisterTransitRouterMulticastGroupSources](~~429776~~) and [DeregisterTransitRouterMulticastGroupMembers](~~429779~~).
        *   The multicast domain is not added to other multicast domains as a multicast member. If the multicast domain is added to another multicast domain as a multicast member, you must remove the multicast domain from the other multicast domain. For more information, see [DeregisterTransitRouterMulticastGroupMembers](~~429779~~).
        

        @param request: DeleteTransitRouterMulticastDomainRequest

        @return: DeleteTransitRouterMulticastDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_multicast_domain_with_options(request, runtime)

    def delete_transit_router_peer_attachment_with_options(self, request, runtime):
        """
        ## Usage notes
        **DeleteTransitRouterPeerAttachment** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterPeerAttachments** to query the status of an inter-region connection.
        - If an inter-region connection is in the **Detaching** state, the inter-region connection is being deleted. You can query the inter-region connection but cannot perform other operations.
        - If an inter-region connection cannot be found, the inter-region connection is deleted.
        ## Prerequisites
        Before you begin, make sure that the Enterprise Edition transit router that you use to create inter-region connections meets the following prerequisites:
        - No associated forwarding correlation is established between the inter-region connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/dissociatetransitrouterattachmentfromroutetable).
        - No route learning correlation is established between the inter-region connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/disabletransitrouterroutetablepropagation).
        - The route tables of the Enterprise Edition transit router do not contain a custom route entry whose next hop is the network instance connection. For more information about how to delete custom routes from route tables of Enterprise Edition transit routers, see [DeleteTransitRouterRouteEntry](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterrouteentry).
        - The route table does not contain a route whose next hop is the inter-region connection and that is generated from a prefix list. You can delete such routes by disassociating the route table from the prefix list. For more information, see [DeleteTransitRouterPrefixListAssociation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterprefixlistassociation).
        - No quality of service (QoS) policy is configured for the inter-region connection. For more information about how to delete QoS policies, see [DeleteCenInterRegionTrafficQosPolicy](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deleteceninterregiontrafficqospolicy).
        

        @param request: DeleteTransitRouterPeerAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterPeerAttachmentResponse
        """
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
        """
        ## Usage notes
        **DeleteTransitRouterPeerAttachment** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterPeerAttachments** to query the status of an inter-region connection.
        - If an inter-region connection is in the **Detaching** state, the inter-region connection is being deleted. You can query the inter-region connection but cannot perform other operations.
        - If an inter-region connection cannot be found, the inter-region connection is deleted.
        ## Prerequisites
        Before you begin, make sure that the Enterprise Edition transit router that you use to create inter-region connections meets the following prerequisites:
        - No associated forwarding correlation is established between the inter-region connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/dissociatetransitrouterattachmentfromroutetable).
        - No route learning correlation is established between the inter-region connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/disabletransitrouterroutetablepropagation).
        - The route tables of the Enterprise Edition transit router do not contain a custom route entry whose next hop is the network instance connection. For more information about how to delete custom routes from route tables of Enterprise Edition transit routers, see [DeleteTransitRouterRouteEntry](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterrouteentry).
        - The route table does not contain a route whose next hop is the inter-region connection and that is generated from a prefix list. You can delete such routes by disassociating the route table from the prefix list. For more information, see [DeleteTransitRouterPrefixListAssociation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterprefixlistassociation).
        - No quality of service (QoS) policy is configured for the inter-region connection. For more information about how to delete QoS policies, see [DeleteCenInterRegionTrafficQosPolicy](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deleteceninterregiontrafficqospolicy).
        

        @param request: DeleteTransitRouterPeerAttachmentRequest

        @return: DeleteTransitRouterPeerAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_peer_attachment_with_options(request, runtime)

    def delete_transit_router_prefix_list_association_with_options(self, request, runtime):
        """
        ## Usage notes
        After you disassociate a route table of an Enterprise Edition transit router from a prefix list, the routes that point to the CIDR blocks in the prefix list are automatically withdrawn from the route table. Before you disassociate the route table of an Enterprise Edition transit router from a prefix list, you must migrate workloads that use the routes in case services are interrupted.
        

        @param request: DeleteTransitRouterPrefixListAssociationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterPrefixListAssociationResponse
        """
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
        """
        ## Usage notes
        After you disassociate a route table of an Enterprise Edition transit router from a prefix list, the routes that point to the CIDR blocks in the prefix list are automatically withdrawn from the route table. Before you disassociate the route table of an Enterprise Edition transit router from a prefix list, you must migrate workloads that use the routes in case services are interrupted.
        

        @param request: DeleteTransitRouterPrefixListAssociationRequest

        @return: DeleteTransitRouterPrefixListAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_prefix_list_association_with_options(request, runtime)

    def delete_transit_router_route_entry_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you call this operation, take note of the following items:
        - If **TransitRouterRouteEntryId** is set, you must not specify **TransitRouterRouteTableId** or **TransitRouterRouteEntryDestinationCidrBlock**. Otherwise, parameter conflicts will occur.
        - If **TransitRouterRouteEntryId** is not set, you must specify the following parameters based on the type of the next hop:   - To delete a black hole route, you must set **TransitRouterRouteTableId**, **TransitRouterRouteEntryDestinationCidrBlock**, and **TransitRouterRouteEntryNextHopType**.
        - If the route that you want to delete is not a black hole route, you must set **TransitRouterRouteTableId**, **TransitRouterRouteEntryDestinationCidrBlock**, **TransitRouterRouteEntryNextHopType**, and **TransitRouterRouteEntryNextHopId**.
        - **DeleteTransitRouterRouteEntry** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteEntries** to query the status of a route entry.     - If a route entry is in the **Deleting** state, the route entry is being deleted. You can query the route entry but cannot perform other operations.
        - If a route entry cannot be found, it is deleted.
        ## Limits
        You can call this operation to delete only static routes. Automatically learned routes are not supported. You can call the [ListTransitRouterRouteEntries](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/listtransitrouterrouteentries) operation to query route types.
        

        @param request: DeleteTransitRouterRouteEntryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterRouteEntryResponse
        """
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
        """
        ## Usage notes
        Before you call this operation, take note of the following items:
        - If **TransitRouterRouteEntryId** is set, you must not specify **TransitRouterRouteTableId** or **TransitRouterRouteEntryDestinationCidrBlock**. Otherwise, parameter conflicts will occur.
        - If **TransitRouterRouteEntryId** is not set, you must specify the following parameters based on the type of the next hop:   - To delete a black hole route, you must set **TransitRouterRouteTableId**, **TransitRouterRouteEntryDestinationCidrBlock**, and **TransitRouterRouteEntryNextHopType**.
        - If the route that you want to delete is not a black hole route, you must set **TransitRouterRouteTableId**, **TransitRouterRouteEntryDestinationCidrBlock**, **TransitRouterRouteEntryNextHopType**, and **TransitRouterRouteEntryNextHopId**.
        - **DeleteTransitRouterRouteEntry** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteEntries** to query the status of a route entry.     - If a route entry is in the **Deleting** state, the route entry is being deleted. You can query the route entry but cannot perform other operations.
        - If a route entry cannot be found, it is deleted.
        ## Limits
        You can call this operation to delete only static routes. Automatically learned routes are not supported. You can call the [ListTransitRouterRouteEntries](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/listtransitrouterrouteentries) operation to query route types.
        

        @param request: DeleteTransitRouterRouteEntryRequest

        @return: DeleteTransitRouterRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_route_entry_with_options(request, runtime)

    def delete_transit_router_route_table_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You cannot delete the default route table of an Enterprise Edition transit router.
        *   **DeleteTransitRouterRouteTable** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTables** to query the status of a custom route table.
        *   If a custom route table is in the Deleting state, the custom route table is being deleted. In this case, you can query the custom route table but cannot perform other operations.
        *   If a custom route table cannot be found, the custom route table is deleted.
        

        @param request: DeleteTransitRouterRouteTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterRouteTableResponse
        """
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
        """
        ## Usage notes
        *   You cannot delete the default route table of an Enterprise Edition transit router.
        *   **DeleteTransitRouterRouteTable** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTables** to query the status of a custom route table.
        *   If a custom route table is in the Deleting state, the custom route table is being deleted. In this case, you can query the custom route table but cannot perform other operations.
        *   If a custom route table cannot be found, the custom route table is deleted.
        

        @param request: DeleteTransitRouterRouteTableRequest

        @return: DeleteTransitRouterRouteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_route_table_with_options(request, runtime)

    def delete_transit_router_vbr_attachment_with_options(self, request, runtime):
        """
        ## Usage notes
        **DeleteTransitRouterVbrAttachment** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVbrAttachments** to query the status of VBR connection.
        - If a VBR connection is in the **Detaching** state, the VBR connection is being deleted. You can query the VBR connection but cannot perform other operations.
        - If a VBR connection cannot be found, the VBR connection is deleted.
        ## Prerequisites
        Before you delete a VBR connection for an Enterprise Edition transit router, make sure that the following requirements are met:
        - No associated forwarding correlation is established between the VBR connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/dissociatetransitrouterattachmentfromroutetable).
        - No route learning correlation is established between the VBR connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/disabletransitrouterroutetablepropagation).
        - The route tables of the Enterprise Edition transit router do not contain a custom route entry whose next hop is the network instance connection. For more information about how to delete custom route entries, see [DeleteTransitRouterRouteEntry](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterrouteentry).
        - The route tables of the Enterprise Edition transit router do not contain a route whose next hop is the VBR connection and that is generated from a prefix list. You can delete such routes by disassociating the route table from the prefix list. For more information, see [DeleteTransitRouterPrefixListAssociation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterprefixlistassociation).
        

        @param request: DeleteTransitRouterVbrAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterVbrAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        """
        ## Usage notes
        **DeleteTransitRouterVbrAttachment** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVbrAttachments** to query the status of VBR connection.
        - If a VBR connection is in the **Detaching** state, the VBR connection is being deleted. You can query the VBR connection but cannot perform other operations.
        - If a VBR connection cannot be found, the VBR connection is deleted.
        ## Prerequisites
        Before you delete a VBR connection for an Enterprise Edition transit router, make sure that the following requirements are met:
        - No associated forwarding correlation is established between the VBR connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/dissociatetransitrouterattachmentfromroutetable).
        - No route learning correlation is established between the VBR connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/disabletransitrouterroutetablepropagation).
        - The route tables of the Enterprise Edition transit router do not contain a custom route entry whose next hop is the network instance connection. For more information about how to delete custom route entries, see [DeleteTransitRouterRouteEntry](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterrouteentry).
        - The route tables of the Enterprise Edition transit router do not contain a route whose next hop is the VBR connection and that is generated from a prefix list. You can delete such routes by disassociating the route table from the prefix list. For more information, see [DeleteTransitRouterPrefixListAssociation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterprefixlistassociation).
        

        @param request: DeleteTransitRouterVbrAttachmentRequest

        @return: DeleteTransitRouterVbrAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vbr_attachment_with_options(request, runtime)

    def delete_transit_router_vpc_attachment_with_options(self, request, runtime):
        """
        ## Usage notes
        **DeleteTransitRouterVpcAttachment** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVpcAttachments** to query the status of a VPC connection.
        - If a VPC is in the **Detaching** state, the VPC connection is being deleted. You can query the VPC connection but cannot perform other operations.
        - If a VPC connection cannot be found, it is deleted.
        ## Prerequisites
        Before you delete a VPC connection, make sure that the following requirements are met:
        - No associated forwarding correlation is established between the VPC connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/dissociatetransitrouterattachmentfromroutetable).
        - No route learning correlation is established between the VPC connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/disabletransitrouterroutetablepropagation).
        - The route table of the VPC does not contain routes that point to the VPC connection. For more information about how to delete routes from a VPC route table, see [DeleteRouteEntry](https://www.alibabacloud.com/help/en/virtual-private-cloud/latest/deleterouteentry).
        - The route tables of the Enterprise Edition transit router do not contain a custom route entry whose next hop is the network instance connection. For more information about how to delete custom routes from the route tables of an Enterprise Edition transit router, see [DeleteTransitRouterRouteEntry](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterrouteentry).
        - The route tables of the Enterprise Edition transit router do not contain a route that is generated from a prefix list and the next hop is the VPC connection. You can delete routes from a route table by disassociating the route table from the prefix list. For more information, see [DeleteTransitRouterPrefixListAssociation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterprefixlistassociation).
        

        @param request: DeleteTransitRouterVpcAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterVpcAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        """
        ## Usage notes
        **DeleteTransitRouterVpcAttachment** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVpcAttachments** to query the status of a VPC connection.
        - If a VPC is in the **Detaching** state, the VPC connection is being deleted. You can query the VPC connection but cannot perform other operations.
        - If a VPC connection cannot be found, it is deleted.
        ## Prerequisites
        Before you delete a VPC connection, make sure that the following requirements are met:
        - No associated forwarding correlation is established between the VPC connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/dissociatetransitrouterattachmentfromroutetable).
        - No route learning correlation is established between the VPC connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/disabletransitrouterroutetablepropagation).
        - The route table of the VPC does not contain routes that point to the VPC connection. For more information about how to delete routes from a VPC route table, see [DeleteRouteEntry](https://www.alibabacloud.com/help/en/virtual-private-cloud/latest/deleterouteentry).
        - The route tables of the Enterprise Edition transit router do not contain a custom route entry whose next hop is the network instance connection. For more information about how to delete custom routes from the route tables of an Enterprise Edition transit router, see [DeleteTransitRouterRouteEntry](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterrouteentry).
        - The route tables of the Enterprise Edition transit router do not contain a route that is generated from a prefix list and the next hop is the VPC connection. You can delete routes from a route table by disassociating the route table from the prefix list. For more information, see [DeleteTransitRouterPrefixListAssociation](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterprefixlistassociation).
        

        @param request: DeleteTransitRouterVpcAttachmentRequest

        @return: DeleteTransitRouterVpcAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vpc_attachment_with_options(request, runtime)

    def delete_transit_router_vpn_attachment_with_options(self, request, runtime):
        """
        ## Usage note
        Before you delete a VPN connection, make sure that the following requirements are met:
        *   No associated forwarding correlation is established between the VPN connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](~~260944~~).
        *   No route learning correlation is established between the VPN connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](~~260945~~).
        *   No route in the route table of the Enterprise Edition transit router points to the VPN connection. For more information, see [DeleteTransitRouterRouteEntry](~~261240~~).
        

        @param request: DeleteTransitRouterVpnAttachmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTransitRouterVpnAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
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
        """
        ## Usage note
        Before you delete a VPN connection, make sure that the following requirements are met:
        *   No associated forwarding correlation is established between the VPN connection and the route tables of the Enterprise Edition transit router. For more information about how to delete an associated forwarding correlation, see [DissociateTransitRouterAttachmentFromRouteTable](~~260944~~).
        *   No route learning correlation is established between the VPN connection and the route tables of the Enterprise Edition transit router. For more information about how to delete a route learning correlation, see [DisableTransitRouterRouteTablePropagation](~~260945~~).
        *   No route in the route table of the Enterprise Edition transit router points to the VPN connection. For more information, see [DeleteTransitRouterRouteEntry](~~261240~~).
        

        @param request: DeleteTransitRouterVpnAttachmentRequest

        @return: DeleteTransitRouterVpnAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_transit_router_vpn_attachment_with_options(request, runtime)

    def deregister_transit_router_multicast_group_members_with_options(self, request, runtime):
        """
        ## Usage notes
        `RegisterTransitRouterMulticastGroupMembers` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast member.
        *   If a multicast member is in the **Deregistering** state, the multicast member is being removed. In this case, you can query the multicast member but cannot perform other operations.
        *   If a multicast member cannot be found, the multicast member is removed from the multicast group.
        

        @param request: DeregisterTransitRouterMulticastGroupMembersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeregisterTransitRouterMulticastGroupMembersResponse
        """
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
        """
        ## Usage notes
        `RegisterTransitRouterMulticastGroupMembers` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast member.
        *   If a multicast member is in the **Deregistering** state, the multicast member is being removed. In this case, you can query the multicast member but cannot perform other operations.
        *   If a multicast member cannot be found, the multicast member is removed from the multicast group.
        

        @param request: DeregisterTransitRouterMulticastGroupMembersRequest

        @return: DeregisterTransitRouterMulticastGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deregister_transit_router_multicast_group_members_with_options(request, runtime)

    def deregister_transit_router_multicast_group_sources_with_options(self, request, runtime):
        """
        ## Usage notes
        `DeregisterTransitRouterMulticastGroupSources` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast source.
        *   If a multicast source is in the **Deregistering** state, the multicast source is being deleted. You can query the multicast source but cannot perform other operations.
        *   If a multicast source cannot be found, the multicast source is deleted.
        

        @param request: DeregisterTransitRouterMulticastGroupSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeregisterTransitRouterMulticastGroupSourcesResponse
        """
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
        """
        ## Usage notes
        `DeregisterTransitRouterMulticastGroupSources` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast source.
        *   If a multicast source is in the **Deregistering** state, the multicast source is being deleted. You can query the multicast source but cannot perform other operations.
        *   If a multicast source cannot be found, the multicast source is deleted.
        

        @param request: DeregisterTransitRouterMulticastGroupSourcesRequest

        @return: DeregisterTransitRouterMulticastGroupSourcesResponse
        """
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
        """
        ## Description
        You can use one of the following methods to query the information about the network instances that are attached to a CEN instance:
        *   You can query all the network instances that are attached to a CEN instance by setting the `CenId` parameter.
        *   You can query the network instances that are attached to a CEN instance in a specified region by setting the `CenId` and `ChildInstanceRegionId` parameters.
        *   You can query a specified type of network instances that are attached to a CEN instance by setting the `CenId` and `ChildInstanceType` parameters.
        

        @param request: DescribeCenAttachedChildInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCenAttachedChildInstancesResponse
        """
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
        """
        ## Description
        You can use one of the following methods to query the information about the network instances that are attached to a CEN instance:
        *   You can query all the network instances that are attached to a CEN instance by setting the `CenId` parameter.
        *   You can query the network instances that are attached to a CEN instance in a specified region by setting the `CenId` and `ChildInstanceRegionId` parameters.
        *   You can query a specified type of network instances that are attached to a CEN instance by setting the `CenId` and `ChildInstanceType` parameters.
        

        @param request: DescribeCenAttachedChildInstancesRequest

        @return: DescribeCenAttachedChildInstancesResponse
        """
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
        """
        ## Description
        The regions that support CEN vary based on the network instance type. To query the regions where you can attach a specified type of network instances to CEN, set the `ProductType` parameter. If you do not set the `ProductType` parameter, the system queries all regions where you can attach network instances to CEN, regardless of the network instance type.
        

        @param request: DescribeChildInstanceRegionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeChildInstanceRegionsResponse
        """
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
        """
        ## Description
        The regions that support CEN vary based on the network instance type. To query the regions where you can attach a specified type of network instances to CEN, set the `ProductType` parameter. If you do not set the `ProductType` parameter, the system queries all regions where you can attach network instances to CEN, regardless of the network instance type.
        

        @param request: DescribeChildInstanceRegionsRequest

        @return: DescribeChildInstanceRegionsResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
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

    def describe_transit_route_table_aggregation_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not UtilClient.is_unset(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitRouteTableAggregation',
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
            cbn_20170912_models.DescribeTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_transit_route_table_aggregation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_transit_route_table_aggregation_with_options(request, runtime)

    def describe_transit_route_table_aggregation_detail_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not UtilClient.is_unset(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransitRouteTableAggregationDetail',
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
            cbn_20170912_models.DescribeTransitRouteTableAggregationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_transit_route_table_aggregation_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_transit_route_table_aggregation_detail_with_options(request, runtime)

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
        """
        ## Usage notes
        **DisableCenVbrHealthCheck** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenVbrHealthCheck** to query the status of health check configurations. If the health check configurations cannot be found, the health check configurations are deleted.
        

        @param request: DisableCenVbrHealthCheckRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableCenVbrHealthCheckResponse
        """
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
        """
        ## Usage notes
        **DisableCenVbrHealthCheck** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenVbrHealthCheck** to query the status of health check configurations. If the health check configurations cannot be found, the health check configurations are deleted.
        

        @param request: DisableCenVbrHealthCheckRequest

        @return: DisableCenVbrHealthCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_cen_vbr_health_check_with_options(request, runtime)

    def disable_transit_router_route_table_propagation_with_options(self, request, runtime):
        """
        ## Usage notes
        **DisableTransitRouterRouteTablePropagation** is an synchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTablePropagations** to query the status of a route learning correlation.
        *   If a route learning correlation is in the **Disabling** state, the route learning correlation is being deleted. You can query the route learning correlation but cannot perform other operations.
        *   If a route learning correlation cannot be found, the route learning correlation is deleted.
        

        @param request: DisableTransitRouterRouteTablePropagationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableTransitRouterRouteTablePropagationResponse
        """
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
        """
        ## Usage notes
        **DisableTransitRouterRouteTablePropagation** is an synchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTablePropagations** to query the status of a route learning correlation.
        *   If a route learning correlation is in the **Disabling** state, the route learning correlation is being deleted. You can query the route learning correlation but cannot perform other operations.
        *   If a route learning correlation cannot be found, the route learning correlation is deleted.
        

        @param request: DisableTransitRouterRouteTablePropagationRequest

        @return: DisableTransitRouterRouteTablePropagationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_transit_router_route_table_propagation_with_options(request, runtime)

    def disassociate_transit_router_multicast_domain_with_options(self, request, runtime):
        """
        ## Usage notes
        *   After a vSwitch is disassociated from a multicast domain, the multicast sources and members on the vSwitch are also removed from the multicast domain.
        *   **DisassociateTransitRouterMulticastDomain** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterMulticastDomainAssociations** to query the status between a vSwitch and a multicast domain.
        *   The **Dissociating** indicates that the vSwitch is being disassociated from the multicast domain. You can query the vSwitch but you cannot perform other operations.
        *   If the vSwitch cannot be found, the vSwitch is disassociated from the multicast domain.
        

        @param request: DisassociateTransitRouterMulticastDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisassociateTransitRouterMulticastDomainResponse
        """
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
        """
        ## Usage notes
        *   After a vSwitch is disassociated from a multicast domain, the multicast sources and members on the vSwitch are also removed from the multicast domain.
        *   **DisassociateTransitRouterMulticastDomain** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterMulticastDomainAssociations** to query the status between a vSwitch and a multicast domain.
        *   The **Dissociating** indicates that the vSwitch is being disassociated from the multicast domain. You can query the vSwitch but you cannot perform other operations.
        *   If the vSwitch cannot be found, the vSwitch is disassociated from the multicast domain.
        

        @param request: DisassociateTransitRouterMulticastDomainRequest

        @return: DisassociateTransitRouterMulticastDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_transit_router_multicast_domain_with_options(request, runtime)

    def dissociate_transit_router_attachment_from_route_table_with_options(self, request, runtime):
        """
        ## Usage notes
        **DissociateTransitRouterAttachmentFromRouteTable** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTableAssociations** to query an associated forwarding correlation between a network instance connection and a route table.
        *   If an associated forwarding correlation is in the **Dissociating** state, the associated forwarding correlation is being deleted. You can query the associated forwarding correlation but cannot perform other operations.
        *   If an associated forwarding correlation cannot be found, the associated forwarding correlation is deleted.
        

        @param request: DissociateTransitRouterAttachmentFromRouteTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DissociateTransitRouterAttachmentFromRouteTableResponse
        """
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
        """
        ## Usage notes
        **DissociateTransitRouterAttachmentFromRouteTable** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTableAssociations** to query an associated forwarding correlation between a network instance connection and a route table.
        *   If an associated forwarding correlation is in the **Dissociating** state, the associated forwarding correlation is being deleted. You can query the associated forwarding correlation but cannot perform other operations.
        *   If an associated forwarding correlation cannot be found, the associated forwarding correlation is deleted.
        

        @param request: DissociateTransitRouterAttachmentFromRouteTableRequest

        @return: DissociateTransitRouterAttachmentFromRouteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_transit_router_attachment_from_route_table_with_options(request, runtime)

    def enable_cen_vbr_health_check_with_options(self, request, runtime):
        """
        ## Usage notes
        You can configure the health check feature for a VBR to monitor the Express Connect circuit between your data center and Alibaba Cloud. This helps you detect connection issues in a timely manner.
        Before you use the health check feature, take note of the following information:
        *   If your VBR uses static routing, you must add a static route for the data center that is connected to the VBR after you configure the health check feature.
        Set the destination CIDR block to the source IP address of health checks, set the mask length to 32, and set the next hop to the IP address of the VBR on the Alibaba Cloud side.
        *   If your VBR uses dynamic Border Gateway Protocol (BGP) routing, you do not need to add routes for the data center.
        *   **EnableCenVbrHealthCheck** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenVbrHealthCheck** to query the status of health check configurations. If health check configurations can be found, health check is configured or modified.
        

        @param request: EnableCenVbrHealthCheckRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableCenVbrHealthCheckResponse
        """
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
        """
        ## Usage notes
        You can configure the health check feature for a VBR to monitor the Express Connect circuit between your data center and Alibaba Cloud. This helps you detect connection issues in a timely manner.
        Before you use the health check feature, take note of the following information:
        *   If your VBR uses static routing, you must add a static route for the data center that is connected to the VBR after you configure the health check feature.
        Set the destination CIDR block to the source IP address of health checks, set the mask length to 32, and set the next hop to the IP address of the VBR on the Alibaba Cloud side.
        *   If your VBR uses dynamic Border Gateway Protocol (BGP) routing, you do not need to add routes for the data center.
        *   **EnableCenVbrHealthCheck** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenVbrHealthCheck** to query the status of health check configurations. If health check configurations can be found, health check is configured or modified.
        

        @param request: EnableCenVbrHealthCheckRequest

        @return: EnableCenVbrHealthCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_cen_vbr_health_check_with_options(request, runtime)

    def enable_transit_router_route_table_propagation_with_options(self, request, runtime):
        """
        ## Usage notes
        After you establish a network instance connection on a transit router, you can create a route learning correlation for the network instance connection. Then, the routes of the connected network instance are automatically advertised to the route table of the transit router. Before you begin, we recommend that you read and understand the following rules:
        *   You can create route learning correlations only on Enterprise Edition transit routers. For more information about the regions and zones that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   **EnableTransitRouterRouteTablePropagation** is an asynchronous operation. After you send a request, the system returns a **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTablePropagations** to query the route learning status between a network instance connection and a route table.
        *   **Enabling** indicates that a route learning correlation is being created between the network instance connection and route table. You can query the route learning correlation but cannot perform other operations.
        *   **Active** indicates that the route learning correlation is created between the network instance connection and route table.
        

        @param request: EnableTransitRouterRouteTablePropagationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableTransitRouterRouteTablePropagationResponse
        """
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
        """
        ## Usage notes
        After you establish a network instance connection on a transit router, you can create a route learning correlation for the network instance connection. Then, the routes of the connected network instance are automatically advertised to the route table of the transit router. Before you begin, we recommend that you read and understand the following rules:
        *   You can create route learning correlations only on Enterprise Edition transit routers. For more information about the regions and zones that support Enterprise Edition transit routers, see [What is CEN?](~~181681~~)
        *   **EnableTransitRouterRouteTablePropagation** is an asynchronous operation. After you send a request, the system returns a **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTablePropagations** to query the route learning status between a network instance connection and a route table.
        *   **Enabling** indicates that a route learning correlation is being created between the network instance connection and route table. You can query the route learning correlation but cannot perform other operations.
        *   **Active** indicates that the route learning correlation is created between the network instance connection and route table.
        

        @param request: EnableTransitRouterRouteTablePropagationRequest

        @return: EnableTransitRouterRouteTablePropagationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_transit_router_route_table_propagation_with_options(request, runtime)

    def grant_instance_to_transit_router_with_options(self, request, runtime):
        """
        ## Description
        *   `GrantInstanceToTransitRouter` grants transit routes permissions to connect only to virtual private clouds (VPCs), virtual border routers (VBRs), and IPsec-VPN connections that belong to another Alibaba Cloud account.
        If you want to grant transit routers permissions to connect to Cloud Connect Network (CCN) instances, call the [GrantInstanceToCbn](~~126141~~) operation.
        *   Before you call `GrantInstanceToTransitRouter`, take note of the billing rules, permission limits, and prerequisites on permission management of transit routers. For more information, see [Acquire permissions to connect to a network instance that belongs to another account](~~181553~~).
        

        @param request: GrantInstanceToTransitRouterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantInstanceToTransitRouterResponse
        """
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
        """
        ## Description
        *   `GrantInstanceToTransitRouter` grants transit routes permissions to connect only to virtual private clouds (VPCs), virtual border routers (VBRs), and IPsec-VPN connections that belong to another Alibaba Cloud account.
        If you want to grant transit routers permissions to connect to Cloud Connect Network (CCN) instances, call the [GrantInstanceToCbn](~~126141~~) operation.
        *   Before you call `GrantInstanceToTransitRouter`, take note of the billing rules, permission limits, and prerequisites on permission management of transit routers. For more information, see [Acquire permissions to connect to a network instance that belongs to another account](~~181553~~).
        

        @param request: GrantInstanceToTransitRouterRequest

        @return: GrantInstanceToTransitRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_instance_to_transit_router_with_options(request, runtime)

    def list_cen_inter_region_traffic_qos_policies_with_options(self, request, runtime):
        """
        ## Usage notes
        When you call the **ListCenInterRegionTrafficQosPolicies** operation, take note of the following information:
        - If you do not set the **TrafficQosPolicyId** parameter, the system returns information about QoS policies based on the values of the **TransitRouterId**, **TransitRouterAttachmentId**, **TrafficQosPolicyName**, and **TrafficQosPolicyDescription** parameters, but does not return information about the queues in the QoS policies. The **TrafficQosQueues** parameter is not included in the response.
        - If you specify a QoS policy ID in the **TrafficMarkingPolicyId** parameter, the system returns the information about the QoS policy and the queues. The **TrafficQosQueues** parameter is included in the response.
        If the **TrafficQosQueues** parameter contains an empty array, it indicates that the QoS policy contains only the default queue.
        

        @param request: ListCenInterRegionTrafficQosPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCenInterRegionTrafficQosPoliciesResponse
        """
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
        """
        ## Usage notes
        When you call the **ListCenInterRegionTrafficQosPolicies** operation, take note of the following information:
        - If you do not set the **TrafficQosPolicyId** parameter, the system returns information about QoS policies based on the values of the **TransitRouterId**, **TransitRouterAttachmentId**, **TrafficQosPolicyName**, and **TrafficQosPolicyDescription** parameters, but does not return information about the queues in the QoS policies. The **TrafficQosQueues** parameter is not included in the response.
        - If you specify a QoS policy ID in the **TrafficMarkingPolicyId** parameter, the system returns the information about the QoS policy and the queues. The **TrafficQosQueues** parameter is included in the response.
        If the **TrafficQosQueues** parameter contains an empty array, it indicates that the QoS policy contains only the default queue.
        

        @param request: ListCenInterRegionTrafficQosPoliciesRequest

        @return: ListCenInterRegionTrafficQosPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cen_inter_region_traffic_qos_policies_with_options(request, runtime)

    def list_cen_inter_region_traffic_qos_queues_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.traffic_qos_policy_id):
            query['TrafficQosPolicyId'] = request.traffic_qos_policy_id
        if not UtilClient.is_unset(request.traffic_qos_queue_description):
            query['TrafficQosQueueDescription'] = request.traffic_qos_queue_description
        if not UtilClient.is_unset(request.traffic_qos_queue_id):
            query['TrafficQosQueueId'] = request.traffic_qos_queue_id
        if not UtilClient.is_unset(request.traffic_qos_queue_name):
            query['TrafficQosQueueName'] = request.traffic_qos_queue_name
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCenInterRegionTrafficQosQueues',
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
            cbn_20170912_models.ListCenInterRegionTrafficQosQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cen_inter_region_traffic_qos_queues(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cen_inter_region_traffic_qos_queues_with_options(request, runtime)

    def list_grant_vswitch_enis_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you call `ListGrantVSwitchEnis`, make sure that the VPC is attached to a Cloud Enterprise Network (CEN) instance. For more information, see [CreateTransitRouterVpcAttachment](~~261358~~).
        

        @param request: ListGrantVSwitchEnisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListGrantVSwitchEnisResponse
        """
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
        """
        ## Usage notes
        Before you call `ListGrantVSwitchEnis`, make sure that the VPC is attached to a Cloud Enterprise Network (CEN) instance. For more information, see [CreateTransitRouterVpcAttachment](~~261358~~).
        

        @param request: ListGrantVSwitchEnisRequest

        @return: ListGrantVSwitchEnisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_grant_vswitch_enis_with_options(request, runtime)

    def list_grant_vswitches_to_cen_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you call the `ListGrantVSwitchesToCen` operation, make sure that the following requirements are met:
        *   The permissions on the VPC are granted to the CEN instance. For more information, see [GrantInstanceToCen](~~126224~~).
        *   The VPC is attached to the CEN instance.
        *   For more information about how to connect an Enterprise Edition transit router to a VPC, see [CreateTransitRouterVpcAttachment](~~261358~~).
        *   For more information about how to connect a Basic Edition transit router to a VPC, see [AttachCenChildInstance](~~65902~~).
        

        @param request: ListGrantVSwitchesToCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListGrantVSwitchesToCenResponse
        """
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
        """
        ## Usage notes
        Before you call the `ListGrantVSwitchesToCen` operation, make sure that the following requirements are met:
        *   The permissions on the VPC are granted to the CEN instance. For more information, see [GrantInstanceToCen](~~126224~~).
        *   The VPC is attached to the CEN instance.
        *   For more information about how to connect an Enterprise Edition transit router to a VPC, see [CreateTransitRouterVpcAttachment](~~261358~~).
        *   For more information about how to connect a Basic Edition transit router to a VPC, see [AttachCenChildInstance](~~65902~~).
        

        @param request: ListGrantVSwitchesToCenRequest

        @return: ListGrantVSwitchesToCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_grant_vswitches_to_cen_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        To call this operation, you must set at least one of *ResourceId** and **Tag.N.Key**.
        *   If you set only **ResourceId**, the tags that are added to the specified CEN instances are returned.
        *   If you set only **Tag.N.Key**, the CEN instances that have the specified tags are returned.
        *   If you set both **ResourceId** and **Tag.N.Key**, the specified tags that are added to the specified CEN instances are returned.
        *   Make sure that the CEN instance specified by **ResourceId** has the tag specified by **Tag.N.Key**. Otherwise, the response returns null.
        *   If multiple tag keys are specified, the logical operator among these tag keys is **AND**.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        To call this operation, you must set at least one of *ResourceId** and **Tag.N.Key**.
        *   If you set only **ResourceId**, the tags that are added to the specified CEN instances are returned.
        *   If you set only **Tag.N.Key**, the CEN instances that have the specified tags are returned.
        *   If you set both **ResourceId** and **Tag.N.Key**, the specified tags that are added to the specified CEN instances are returned.
        *   Make sure that the CEN instance specified by **ResourceId** has the tag specified by **Tag.N.Key**. Otherwise, the response returns null.
        *   If multiple tag keys are specified, the logical operator among these tag keys is **AND**.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_traffic_marking_policies_with_options(self, request, runtime):
        """
        ## Usage notes
        Take note of the following rules when you call the **ListTrafficMarkingPolicies** operation:
        - If you do not specify a traffic marking policy ID in the **TrafficMarkingPolicyId** parameter, the system returns the information about the traffic marking policy based on the **TransitRouterId**, **TrafficMarkingPolicyName**, and **TrafficMarkingPolicyDescription** parameters. The information about the traffic classification rules in the policy is not returned. The **TrafficMatchRules** parameter is not included in the response.
        - If you specify a traffic marking policy ID in the **TrafficMarkingPolicyId** parameter, this operation returns the information about the traffic marking policy and the traffic classification rules. The **TrafficMatchRules** parameter is included in the response.
        If the **TrafficMatchRules** parameter contains an empty array, it indicates that the traffic marking policy does not contain a traffic classification rule.
        

        @param request: ListTrafficMarkingPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTrafficMarkingPoliciesResponse
        """
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
        """
        ## Usage notes
        Take note of the following rules when you call the **ListTrafficMarkingPolicies** operation:
        - If you do not specify a traffic marking policy ID in the **TrafficMarkingPolicyId** parameter, the system returns the information about the traffic marking policy based on the **TransitRouterId**, **TrafficMarkingPolicyName**, and **TrafficMarkingPolicyDescription** parameters. The information about the traffic classification rules in the policy is not returned. The **TrafficMatchRules** parameter is not included in the response.
        - If you specify a traffic marking policy ID in the **TrafficMarkingPolicyId** parameter, this operation returns the information about the traffic marking policy and the traffic classification rules. The **TrafficMatchRules** parameter is included in the response.
        If the **TrafficMatchRules** parameter contains an empty array, it indicates that the traffic marking policy does not contain a traffic classification rule.
        

        @param request: ListTrafficMarkingPoliciesRequest

        @return: ListTrafficMarkingPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_traffic_marking_policies_with_options(request, runtime)

    def list_transit_router_available_resource_with_options(self, request, runtime):
        """
        You can call **ListTransitRouterAvailableResource** to query the zones that support Enterprise Edition transit routers in a specified region.
        *   If you do not set **SupportMulticast** to **true**, general-purpose zones that support Enterprise Edition transit routers are queried.
        *   If you set **SupportMulticast** to **true**, zones in which Enterprise Edition transit routers support multicast are queried.
        *   On May 31, 2022, VPC-connected Enterprise Edition transit routers were optimized. Optimized Enterprise Edition transit routers do not require you to specify the primary and secondary zones when you connect VPCs to the Enterprise Edition transit routers. You can specify one or more zones.
        *   If your Enterprise Edition transit router has not been optimized, you must specify the primary and secondary zones when you connect a VPC to your Enterprise Edition transit router. After you call **ListTransitRouterAvailableResource**, you can call **MasterZones** and **SlaveZones** to query the primary and secondary zones.
        *   If your Enterprise Edition transit router has been optimized, you can specify a zone as needed when you connect a VPC to your Enterprise Edition transit router. After you call **ListTransitRouterAvailableResource**, you can call **AvailableZones** to query the zones.
        For more information about the optimization, see [Announcement: Optimization on VPC-connected Enterprise Edition transit routers](~~434191~~).
        

        @param request: ListTransitRouterAvailableResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterAvailableResourceResponse
        """
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
        """
        You can call **ListTransitRouterAvailableResource** to query the zones that support Enterprise Edition transit routers in a specified region.
        *   If you do not set **SupportMulticast** to **true**, general-purpose zones that support Enterprise Edition transit routers are queried.
        *   If you set **SupportMulticast** to **true**, zones in which Enterprise Edition transit routers support multicast are queried.
        *   On May 31, 2022, VPC-connected Enterprise Edition transit routers were optimized. Optimized Enterprise Edition transit routers do not require you to specify the primary and secondary zones when you connect VPCs to the Enterprise Edition transit routers. You can specify one or more zones.
        *   If your Enterprise Edition transit router has not been optimized, you must specify the primary and secondary zones when you connect a VPC to your Enterprise Edition transit router. After you call **ListTransitRouterAvailableResource**, you can call **MasterZones** and **SlaveZones** to query the primary and secondary zones.
        *   If your Enterprise Edition transit router has been optimized, you can specify a zone as needed when you connect a VPC to your Enterprise Edition transit router. After you call **ListTransitRouterAvailableResource**, you can call **AvailableZones** to query the zones.
        For more information about the optimization, see [Announcement: Optimization on VPC-connected Enterprise Edition transit routers](~~434191~~).
        

        @param request: ListTransitRouterAvailableResourceRequest

        @return: ListTransitRouterAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_available_resource_with_options(request, runtime)

    def list_transit_router_cidr_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterCidr',
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
            cbn_20170912_models.ListTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_cidr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_cidr_with_options(request, runtime)

    def list_transit_router_cidr_allocation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not UtilClient.is_unset(request.attachment_name):
            query['AttachmentName'] = request.attachment_name
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_owner_id):
            query['DedicatedOwnerId'] = request.dedicated_owner_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTransitRouterCidrAllocation',
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
            cbn_20170912_models.ListTransitRouterCidrAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transit_router_cidr_allocation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_cidr_allocation_with_options(request, runtime)

    def list_transit_router_multicast_domain_associations_with_options(self, request, runtime):
        """
        ## Usage notes
        Multicast domains can be associated only with vSwitches that are in VPCs. You can call **ListTransitRouterMulticastDomainAssociations** to query whether vSwitches in VPCs are associated with a specified multicast domain.
        

        @param request: ListTransitRouterMulticastDomainAssociationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterMulticastDomainAssociationsResponse
        """
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
        """
        ## Usage notes
        Multicast domains can be associated only with vSwitches that are in VPCs. You can call **ListTransitRouterMulticastDomainAssociations** to query whether vSwitches in VPCs are associated with a specified multicast domain.
        

        @param request: ListTransitRouterMulticastDomainAssociationsRequest

        @return: ListTransitRouterMulticastDomainAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_domain_associations_with_options(request, runtime)

    def list_transit_router_multicast_domain_vswitches_with_options(self, request, runtime):
        """
        ## Usage notes
        You can query vSwitches only in VPCs that are connected to Enterprise Edition transit routers.
        

        @param request: ListTransitRouterMulticastDomainVSwitchesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterMulticastDomainVSwitchesResponse
        """
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
        """
        ## Usage notes
        You can query vSwitches only in VPCs that are connected to Enterprise Edition transit routers.
        

        @param request: ListTransitRouterMulticastDomainVSwitchesRequest

        @return: ListTransitRouterMulticastDomainVSwitchesResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        You can call `ListTransitRouterMulticastGroups` to query the multicast sources and members in a multicast domain. Multicast sources and members are also known as multicast resources.
        *   If you set **GroupIpAddress**, the system queries multicast resources in the multicast domain by multicast group.
        *   If you set **VSwitchIds**, the system queries multicast resources in the multicast domain by vSwitch.
        *   If you set **PeerTransitRouterMulticastDomains**, the system queries multicast resources that are also deployed in a different region.
        *   If you set **ResourceType**, the system queries the multicast resources of the specified type in the multicast domain.
        *   If you set **ResourceId**, the system queries multicast resources by resource.
        *   If you set only **TransitRouterMulticastDomainId**, the system queries all the multicast resources in the multicast domain.
        

        @param request: ListTransitRouterMulticastGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterMulticastGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_ip_address):
            query['GroupIpAddress'] = request.group_ip_address
        if not UtilClient.is_unset(request.is_group_member):
            query['IsGroupMember'] = request.is_group_member
        if not UtilClient.is_unset(request.is_group_source):
            query['IsGroupSource'] = request.is_group_source
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_interface_ids):
            query['NetworkInterfaceIds'] = request.network_interface_ids
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
        """
        You can call `ListTransitRouterMulticastGroups` to query the multicast sources and members in a multicast domain. Multicast sources and members are also known as multicast resources.
        *   If you set **GroupIpAddress**, the system queries multicast resources in the multicast domain by multicast group.
        *   If you set **VSwitchIds**, the system queries multicast resources in the multicast domain by vSwitch.
        *   If you set **PeerTransitRouterMulticastDomains**, the system queries multicast resources that are also deployed in a different region.
        *   If you set **ResourceType**, the system queries the multicast resources of the specified type in the multicast domain.
        *   If you set **ResourceId**, the system queries multicast resources by resource.
        *   If you set only **TransitRouterMulticastDomainId**, the system queries all the multicast resources in the multicast domain.
        

        @param request: ListTransitRouterMulticastGroupsRequest

        @return: ListTransitRouterMulticastGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_multicast_groups_with_options(request, runtime)

    def list_transit_router_peer_attachments_with_options(self, request, runtime):
        """
        ## Description
        You can use the following methods to query the cross-region connections on an Enterprise Edition transit router:
        *   Query all cross-region connections on an Enterprise Edition transit router by specifying the ID of the Enterprise Edition transit router.
        *   Query all cross-region connections on an Enterprise Edition transit router by specifying the ID of the Cloud Enterprise Network (CEN) instance and the ID of the region where the transit router is deployed.
        

        @param request: ListTransitRouterPeerAttachmentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterPeerAttachmentsResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Description
        You can use the following methods to query the cross-region connections on an Enterprise Edition transit router:
        *   Query all cross-region connections on an Enterprise Edition transit router by specifying the ID of the Enterprise Edition transit router.
        *   Query all cross-region connections on an Enterprise Edition transit router by specifying the ID of the Cloud Enterprise Network (CEN) instance and the ID of the region where the transit router is deployed.
        

        @param request: ListTransitRouterPeerAttachmentsRequest

        @return: ListTransitRouterPeerAttachmentsResponse
        """
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
        """
        When calling the *ListTransitRouterRouteTableAssociations** interface, at least one of the request parameters **TransitRouterRouteTableId** and **TransitRouterAttachmentId** must be entered:
        - If only the value of the **TransitRouterRouteTableId** parameter is specified, it means that you want to query the connection information of the network instance associated with the routing table of the enterprise edition forwarding router.
        - If only the value of the **TransitRouterAttachmentId** parameter is specified, it means that you want to query the routing table information of the enterprise edition forwarding router that is connected to the network instance to create an associated forwarding relationship.
        - If the values of **TransitRouterRouteTableId** and **TransitRouterAttachmentId** are specified at the same time, it means that you want to query the associated forwarding relationship between the network instance connection and the routing table of the forwarding router of the enterprise version.
        - If there is an associated forwarding relationship between the network instance connection and the routing table of the forwarding router of the enterprise edition, the system will normally return information about the associated forwarding relationship.
        - If there is no associated forwarding relationship between the network instance connection and the enterprise edition forwarding router routing table, the **TransitRouterAssociations** array returns an empty value.
        

        @param request: ListTransitRouterRouteTableAssociationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterRouteTableAssociationsResponse
        """
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_resource_id):
            query['TransitRouterAttachmentResourceId'] = request.transit_router_attachment_resource_id
        if not UtilClient.is_unset(request.transit_router_attachment_resource_type):
            query['TransitRouterAttachmentResourceType'] = request.transit_router_attachment_resource_type
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
        """
        When calling the *ListTransitRouterRouteTableAssociations** interface, at least one of the request parameters **TransitRouterRouteTableId** and **TransitRouterAttachmentId** must be entered:
        - If only the value of the **TransitRouterRouteTableId** parameter is specified, it means that you want to query the connection information of the network instance associated with the routing table of the enterprise edition forwarding router.
        - If only the value of the **TransitRouterAttachmentId** parameter is specified, it means that you want to query the routing table information of the enterprise edition forwarding router that is connected to the network instance to create an associated forwarding relationship.
        - If the values of **TransitRouterRouteTableId** and **TransitRouterAttachmentId** are specified at the same time, it means that you want to query the associated forwarding relationship between the network instance connection and the routing table of the forwarding router of the enterprise version.
        - If there is an associated forwarding relationship between the network instance connection and the routing table of the forwarding router of the enterprise edition, the system will normally return information about the associated forwarding relationship.
        - If there is no associated forwarding relationship between the network instance connection and the enterprise edition forwarding router routing table, the **TransitRouterAssociations** array returns an empty value.
        

        @param request: ListTransitRouterRouteTableAssociationsRequest

        @return: ListTransitRouterRouteTableAssociationsResponse
        """
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_attachment_resource_id):
            query['TransitRouterAttachmentResourceId'] = request.transit_router_attachment_resource_id
        if not UtilClient.is_unset(request.transit_router_attachment_resource_type):
            query['TransitRouterAttachmentResourceType'] = request.transit_router_attachment_resource_type
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
        if not UtilClient.is_unset(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Description
        You can use the following methods to query VBR connections on an Enterprise Edition transit router:
        *   Specify the ID of the Enterprise Edition transit router.
        *   Specify the ID of the relevant Cloud Enterprise Network (CEN) instance and the region ID of the Enterprise Edition transit router.
        

        @param request: ListTransitRouterVbrAttachmentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterVbrAttachmentsResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Description
        You can use the following methods to query VBR connections on an Enterprise Edition transit router:
        *   Specify the ID of the Enterprise Edition transit router.
        *   Specify the ID of the relevant Cloud Enterprise Network (CEN) instance and the region ID of the Enterprise Edition transit router.
        

        @param request: ListTransitRouterVbrAttachmentsRequest

        @return: ListTransitRouterVbrAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vbr_attachments_with_options(request, runtime)

    def list_transit_router_vpc_attachments_with_options(self, request, runtime):
        """
        You can use the following methods to query VPC connections on an Enterprise Edition transit router:
        *   Specify the ID of the Enterprise Edition transit router.
        *   Specify the ID of the relevant Cloud Enterprise Network (CEN) instance and the region ID of the Enterprise Edition transit router.
        

        @param request: ListTransitRouterVpcAttachmentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterVpcAttachmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_attachment_id):
            query['TransitRouterAttachmentId'] = request.transit_router_attachment_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
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
        """
        You can use the following methods to query VPC connections on an Enterprise Edition transit router:
        *   Specify the ID of the Enterprise Edition transit router.
        *   Specify the ID of the relevant Cloud Enterprise Network (CEN) instance and the region ID of the Enterprise Edition transit router.
        

        @param request: ListTransitRouterVpcAttachmentsRequest

        @return: ListTransitRouterVpcAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vpc_attachments_with_options(request, runtime)

    def list_transit_router_vpn_attachments_with_options(self, request, runtime):
        """
        ## Usage note
        When you call the **ListTransitRouterVpnAttachments** operation, take note of the following items:
        - If you set only **CenId** and **RegionId**, the VPN attachments in the current region are queried.
        - If you set **CenId**, **RegionId**, and **TransitRouterAttachmentId**, only the specified VPN attachment is queried.
        - If you set **CenId** and **RegionId**, you do not need to set **TransitRouterId**. If you set **TransitRouterId**, you do not need to set **CenId** or **RegionId**.
        

        @param request: ListTransitRouterVpnAttachmentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRouterVpnAttachmentsResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        ## Usage note
        When you call the **ListTransitRouterVpnAttachments** operation, take note of the following items:
        - If you set only **CenId** and **RegionId**, the VPN attachments in the current region are queried.
        - If you set **CenId**, **RegionId**, and **TransitRouterAttachmentId**, only the specified VPN attachment is queried.
        - If you set **CenId** and **RegionId**, you do not need to set **TransitRouterId**. If you set **TransitRouterId**, you do not need to set **CenId** or **RegionId**.
        

        @param request: ListTransitRouterVpnAttachmentsRequest

        @return: ListTransitRouterVpnAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_router_vpn_attachments_with_options(request, runtime)

    def list_transit_routers_with_options(self, request, runtime):
        """
        ## Usage notes
        You can set the **RegionId** and **TransitRouterId** parameters based on your requirements.
        *   If you do not set **RegionId** or **TransitRouterId**, the system queries all transit routers connected to the specified CEN instance.
        *   If you set only **RegionId**, the system queries transit routers that are deployed in the specified region.
        *   If you set only **TransitRouterId**, the system queries the specified transit router.
        *   If you set both **RegionId** and **TransitRouterId**, the system queries the specified transit router in the specified region.
        

        @param request: ListTransitRoutersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTransitRoutersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.feature_filter):
            query['FeatureFilter'] = request.feature_filter
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not UtilClient.is_unset(request.transit_router_name):
            query['TransitRouterName'] = request.transit_router_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
        """
        ## Usage notes
        You can set the **RegionId** and **TransitRouterId** parameters based on your requirements.
        *   If you do not set **RegionId** or **TransitRouterId**, the system queries all transit routers connected to the specified CEN instance.
        *   If you set only **RegionId**, the system queries transit routers that are deployed in the specified region.
        *   If you set only **TransitRouterId**, the system queries the specified transit router.
        *   If you set both **RegionId** and **TransitRouterId**, the system queries the specified transit router in the specified region.
        

        @param request: ListTransitRoutersRequest

        @return: ListTransitRoutersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_transit_routers_with_options(request, runtime)

    def modify_cen_attribute_with_options(self, request, runtime):
        """
        *ModifyCenAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **DescribeCens** to query the status of a CEN instance.
        *   If a CEN instance is in the **Modifying** state, the CEN instance is being modified. You can query the CEN instance but cannot perform other operations.
        *   If a CEN instance is in the **Active** state, the CEN instance is modified.
        

        @param request: ModifyCenAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyCenAttributeResponse
        """
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
        """
        *ModifyCenAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **DescribeCens** to query the status of a CEN instance.
        *   If a CEN instance is in the **Modifying** state, the CEN instance is being modified. You can query the CEN instance but cannot perform other operations.
        *   If a CEN instance is in the **Active** state, the CEN instance is modified.
        

        @param request: ModifyCenAttributeRequest

        @return: ModifyCenAttributeResponse
        """
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
        """
        ## Usage notes
        `ModifyCenRouteMap` is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call `DescribeCenRouteMaps` to query the status of a routing policy.
        *   **Modifying**: indicates that the system is modifying the routing policy. You can only query the routing policy, but cannot perform other operations.
        *   **Active**: indicates that the routing policy is modified.
        

        @param request: ModifyCenRouteMapRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyCenRouteMapResponse
        """
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
        """
        ## Usage notes
        `ModifyCenRouteMap` is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call `DescribeCenRouteMaps` to query the status of a routing policy.
        *   **Modifying**: indicates that the system is modifying the routing policy. You can only query the routing policy, but cannot perform other operations.
        *   **Active**: indicates that the routing policy is modified.
        

        @param request: ModifyCenRouteMapRequest

        @return: ModifyCenRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_route_map_with_options(request, runtime)

    def modify_flow_log_attribute_with_options(self, request, runtime):
        """
        ## Usage notes
        `ModifyFlowLogAttribute` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Modifying** state, the flow log is being modified. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Active** state, the flow log is modified.
        

        @param request: ModifyFlowLogAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyFlowLogAttributeResponse
        """
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
        """
        ## Usage notes
        `ModifyFlowLogAttribute` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `DescribeFlowlogs` to query the status of a flow log.
        *   If a flow log is in the **Modifying** state, the flow log is being modified. In this case, you can query the flow log but cannot perform other operations.
        *   If a flow log is in the **Active** state, the flow log is modified.
        

        @param request: ModifyFlowLogAttributeRequest

        @return: ModifyFlowLogAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    def modify_transit_router_cidr_with_options(self, request, runtime):
        """
        ## Usage notes
        *   Before you modify the CIDR block of a transit router, we recommend that you read the [limits on transit router CIDR blocks](~~462635~~).
        *   If IP addresses within the CIDR block have been allocated to network instances, you cannot modify the CIDR block.
        *   When you call **ModifyTransitRouterCidr**, if no parameter of the **PublishCidrRoute** operation is modified, ModifyTransitRouterCidr is a synchronous operation. After you call the operation, the new settings are immediately applied.
        *   If a parameter of the **PublishCidrRoute** operation is modified, **ModifyTransitRouterCidr** is an asynchronous operation. After you call the operation, the request ID (**RequestId**) is returned but the operation is still being performed in the system background. You can call **ListTransitRouterCidr** to query the status of the CIDR block of the transit router.
        *   If the CIDR block of the transit router remains unchanged, the CIDR block is still being modified.
        *   If the CIDR block of the transit router is changed to the one that you specify in the request, the CIDR block has been modified.
        

        @param request: ModifyTransitRouterCidrRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyTransitRouterCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_cidr_route):
            query['PublishCidrRoute'] = request.publish_cidr_route
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.transit_router_cidr_id):
            query['TransitRouterCidrId'] = request.transit_router_cidr_id
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTransitRouterCidr',
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
            cbn_20170912_models.ModifyTransitRouterCidrResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_transit_router_cidr(self, request):
        """
        ## Usage notes
        *   Before you modify the CIDR block of a transit router, we recommend that you read the [limits on transit router CIDR blocks](~~462635~~).
        *   If IP addresses within the CIDR block have been allocated to network instances, you cannot modify the CIDR block.
        *   When you call **ModifyTransitRouterCidr**, if no parameter of the **PublishCidrRoute** operation is modified, ModifyTransitRouterCidr is a synchronous operation. After you call the operation, the new settings are immediately applied.
        *   If a parameter of the **PublishCidrRoute** operation is modified, **ModifyTransitRouterCidr** is an asynchronous operation. After you call the operation, the request ID (**RequestId**) is returned but the operation is still being performed in the system background. You can call **ListTransitRouterCidr** to query the status of the CIDR block of the transit router.
        *   If the CIDR block of the transit router remains unchanged, the CIDR block is still being modified.
        *   If the CIDR block of the transit router is changed to the one that you specify in the request, the CIDR block has been modified.
        

        @param request: ModifyTransitRouterCidrRequest

        @return: ModifyTransitRouterCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_transit_router_cidr_with_options(request, runtime)

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
        """
        ## Usage notes
        By default, CEN instances and bandwidth plans are in the default resource group. You can call `MoveResourceGroup` to move CEN instances or bandwidth plans to another resource group.
        

        @param request: MoveResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MoveResourceGroupResponse
        """
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
        """
        ## Usage notes
        By default, CEN instances and bandwidth plans are in the default resource group. You can call `MoveResourceGroup` to move CEN instances or bandwidth plans to another resource group.
        

        @param request: MoveResourceGroupRequest

        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def open_transit_router_service_with_options(self, request, runtime):
        """
        You can call `OpenTransitRouterService` to activate the transit router feature free of charge. After the `OpenTransitRouterService` operation succeeds, an order is automatically generated. You can use the returned order ID to query the order information in [Alibaba Cloud User Center](https://usercenter2-intl.aliyun.com/order/list?pageIndex=1\\&pageSize=20).
        

        @param request: OpenTransitRouterServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenTransitRouterServiceResponse
        """
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
        """
        You can call `OpenTransitRouterService` to activate the transit router feature free of charge. After the `OpenTransitRouterService` operation succeeds, an order is automatically generated. You can use the returned order ID to query the order information in [Alibaba Cloud User Center](https://usercenter2-intl.aliyun.com/order/list?pageIndex=1\\&pageSize=20).
        

        @param request: OpenTransitRouterServiceRequest

        @return: OpenTransitRouterServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_transit_router_service_with_options(request, runtime)

    def publish_route_entries_with_options(self, request, runtime):
        """
        ## Supported route entries
        The following table lists the route entries that can be published to CEN:
        | Route entry | Network | Published to CEN by default? |
        | ----------- | ------- | ---------------------------- |
        | A route entry pointing to an ECS instance | VPC | No |
        | A route entry pointing to a VPN Gateway | VPC | No |
        | A route entry pointing to a High-Availability Virtual IP Address (HaVip) | VPC | No |
        | A VPC system route entry | VPC | Yes |
        | A route entry pointing to an on-premises data center | VPC | Yes |
        | A BGP route entry | VPC | Yes |
        

        @param request: PublishRouteEntriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublishRouteEntriesResponse
        """
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
        """
        ## Supported route entries
        The following table lists the route entries that can be published to CEN:
        | Route entry | Network | Published to CEN by default? |
        | ----------- | ------- | ---------------------------- |
        | A route entry pointing to an ECS instance | VPC | No |
        | A route entry pointing to a VPN Gateway | VPC | No |
        | A route entry pointing to a High-Availability Virtual IP Address (HaVip) | VPC | No |
        | A VPC system route entry | VPC | Yes |
        | A route entry pointing to an on-premises data center | VPC | Yes |
        | A BGP route entry | VPC | Yes |
        

        @param request: PublishRouteEntriesRequest

        @return: PublishRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_route_entries_with_options(request, runtime)

    def refresh_transit_route_table_aggregation_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.transit_route_table_aggregation_cidr):
            query['TransitRouteTableAggregationCidr'] = request.transit_route_table_aggregation_cidr
        if not UtilClient.is_unset(request.transit_route_table_id):
            query['TransitRouteTableId'] = request.transit_route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshTransitRouteTableAggregation',
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
            cbn_20170912_models.RefreshTransitRouteTableAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_transit_route_table_aggregation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_transit_route_table_aggregation_with_options(request, runtime)

    def register_transit_router_multicast_group_members_with_options(self, request, runtime):
        """
        ## Usage notes
        Enterprise Edition transit routers allow you to specify elastic network interfaces (ENIs) as multicast members. You can call `RegisterTransitRouterMulticastGroupMembers` to add ENIs in the same region or in different regions to a multicast group as multicast members.
        *   If you set **NetworkInterfaceIds**, ENIs in the current region are specified as multicast members. Make sure that the vSwitches of the ENIs are associated with the multicast domain. For more information, see [AssociateTransitRouterMulticastDomain](~~429778~~).
        *   If you set **PeerTransitRouterMulticastDomains**, multicast members in the multicast group that has the same IP address as the current multicast group but is in a different region are added to the current multicast group. Make sure that an inter-region connection is created. For more information, see [CreateTransitRouterPeerAttachment](~~261363~~).
        For example, Alice created a multicast domain (Domain A) in the Australia (Sydney) region and a multicast domain (Domain B) in the UK (London) region. Domain A contains a multicast group (Group A), and Domain B contains a multicast group (Group B). Group A and Group B have the same multicast IP address. Group B in UK (London) contains a multicast member (Member B). If Alice sets **PeerTransitRouterMulticastDomains** to the ID of Domain B in UK (London) when Alice calls `RegisterTransitRouterMulticastGroupMembers` to add multicast members to Group A in Australia (Sydney), Member B is added to Group A in Australia (Sydney).
        *   `RegisterTransitRouterMulticastGroupMembers` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast member.
        *   If a multicast member is in the **Registering** state, the multicast member is being added. You can query the multicast member but cannot perform other operations.
        *   If a multicast member is in the **Registered** state, the multicast member is added.
        

        @param request: RegisterTransitRouterMulticastGroupMembersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RegisterTransitRouterMulticastGroupMembersResponse
        """
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
        """
        ## Usage notes
        Enterprise Edition transit routers allow you to specify elastic network interfaces (ENIs) as multicast members. You can call `RegisterTransitRouterMulticastGroupMembers` to add ENIs in the same region or in different regions to a multicast group as multicast members.
        *   If you set **NetworkInterfaceIds**, ENIs in the current region are specified as multicast members. Make sure that the vSwitches of the ENIs are associated with the multicast domain. For more information, see [AssociateTransitRouterMulticastDomain](~~429778~~).
        *   If you set **PeerTransitRouterMulticastDomains**, multicast members in the multicast group that has the same IP address as the current multicast group but is in a different region are added to the current multicast group. Make sure that an inter-region connection is created. For more information, see [CreateTransitRouterPeerAttachment](~~261363~~).
        For example, Alice created a multicast domain (Domain A) in the Australia (Sydney) region and a multicast domain (Domain B) in the UK (London) region. Domain A contains a multicast group (Group A), and Domain B contains a multicast group (Group B). Group A and Group B have the same multicast IP address. Group B in UK (London) contains a multicast member (Member B). If Alice sets **PeerTransitRouterMulticastDomains** to the ID of Domain B in UK (London) when Alice calls `RegisterTransitRouterMulticastGroupMembers` to add multicast members to Group A in Australia (Sydney), Member B is added to Group A in Australia (Sydney).
        *   `RegisterTransitRouterMulticastGroupMembers` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast member.
        *   If a multicast member is in the **Registering** state, the multicast member is being added. You can query the multicast member but cannot perform other operations.
        *   If a multicast member is in the **Registered** state, the multicast member is added.
        

        @param request: RegisterTransitRouterMulticastGroupMembersRequest

        @return: RegisterTransitRouterMulticastGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_transit_router_multicast_group_members_with_options(request, runtime)

    def register_transit_router_multicast_group_sources_with_options(self, request, runtime):
        """
        ## Usage notes
        - You can specify only elastic network interfaces (ENIs) as multicast sources.
        - `RegisterTransitRouterMulticastGroupSources` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast source.     - If a multicast source is in the **Registering** state, the multicast source is being created. You can query the multicast source but cannot perform other operations.
        - If a multicast source is in the **Registered** state, the multicast source is created.
        ## Prerequisites
        Before you call `RegisterTransitRouterMulticastGroupSources`, make sure that the vSwitch on which the ENI is created is associated with the multicast domain. For more information, see [AssociateTransitRouterMulticastDomain](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/associatetransitroutermulticastdomain).
        

        @param request: RegisterTransitRouterMulticastGroupSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RegisterTransitRouterMulticastGroupSourcesResponse
        """
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
        """
        ## Usage notes
        - You can specify only elastic network interfaces (ENIs) as multicast sources.
        - `RegisterTransitRouterMulticastGroupSources` is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call `ListTransitRouterMulticastGroups` to query the status of a multicast source.     - If a multicast source is in the **Registering** state, the multicast source is being created. You can query the multicast source but cannot perform other operations.
        - If a multicast source is in the **Registered** state, the multicast source is created.
        ## Prerequisites
        Before you call `RegisterTransitRouterMulticastGroupSources`, make sure that the vSwitch on which the ENI is created is associated with the multicast domain. For more information, see [AssociateTransitRouterMulticastDomain](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/associatetransitroutermulticastdomain).
        

        @param request: RegisterTransitRouterMulticastGroupSourcesRequest

        @return: RegisterTransitRouterMulticastGroupSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_transit_router_multicast_group_sources_with_options(request, runtime)

    def remove_traffic_match_rule_from_traffic_marking_policy_with_options(self, request, runtime):
        """
        ## Usage note
        *   When you call **RemoveTrafficMatchRuleFromTrafficMarkingPolicy**, take note of the following rules:
        *   If you specify the ID of a traffic classification rule in the **TrafficMarkRuleIds** parameter, the specified traffic classification rule is deleted.
        *   If you do not specify a traffic classification rule ID in the **TrafficMarkRuleIds** parameter, no operation is performed after you call this operation.
        If you want to delete a traffic classification rule, you must specify the rule ID before you call this operation.
        *   **RemoveTrafficMatchRuleFromTrafficMarkingPolicy** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic classification rule.
        *   If traffic classification rule is in the **Deleting** state, the traffic classification rule is being deleted. In this case, you can query the traffic classification rule but cannot perform other operations.
        *   If a traffic classification rule cannot be found, the traffic classification rule is deleted.
        

        @param request: RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse
        """
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
        """
        ## Usage note
        *   When you call **RemoveTrafficMatchRuleFromTrafficMarkingPolicy**, take note of the following rules:
        *   If you specify the ID of a traffic classification rule in the **TrafficMarkRuleIds** parameter, the specified traffic classification rule is deleted.
        *   If you do not specify a traffic classification rule ID in the **TrafficMarkRuleIds** parameter, no operation is performed after you call this operation.
        If you want to delete a traffic classification rule, you must specify the rule ID before you call this operation.
        *   **RemoveTrafficMatchRuleFromTrafficMarkingPolicy** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **ListTrafficMarkingPolicies** to query the status of a traffic classification rule.
        *   If traffic classification rule is in the **Deleting** state, the traffic classification rule is being deleted. In this case, you can query the traffic classification rule but cannot perform other operations.
        *   If a traffic classification rule cannot be found, the traffic classification rule is deleted.
        

        @param request: RemoveTrafficMatchRuleFromTrafficMarkingPolicyRequest

        @return: RemoveTrafficMatchRuleFromTrafficMarkingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    def remove_trafic_match_rule_from_traffic_marking_policy_with_options(self, request, runtime):
        """
        @deprecated : RemoveTraficMatchRuleFromTrafficMarkingPolicy is deprecated, please use Cbn::2017-09-12::RemoveTrafficMatchRuleFromTrafficMarkingPolicy instead.
        ## Usage notes
        The **RemoveTraficMatchRuleFromTrafficMarkingPolicy** is deprecated and will be discontinued soon. If you need to delete traffic classification rules from a traffic marking policy, call the [RemoveTrafficMatchRuleFromTrafficMarkingPolicy](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/removetrafficmatchrulefromtrafficmarkingpolicy) operation.
        

        @param request: RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse
        Deprecated
        """
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
        """
        @deprecated : RemoveTraficMatchRuleFromTrafficMarkingPolicy is deprecated, please use Cbn::2017-09-12::RemoveTrafficMatchRuleFromTrafficMarkingPolicy instead.
        ## Usage notes
        The **RemoveTraficMatchRuleFromTrafficMarkingPolicy** is deprecated and will be discontinued soon. If you need to delete traffic classification rules from a traffic marking policy, call the [RemoveTrafficMatchRuleFromTrafficMarkingPolicy](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/removetrafficmatchrulefromtrafficmarkingpolicy) operation.
        

        @param request: RemoveTraficMatchRuleFromTrafficMarkingPolicyRequest

        @return: RemoveTraficMatchRuleFromTrafficMarkingPolicyResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_trafic_match_rule_from_traffic_marking_policy_with_options(request, runtime)

    def replace_transit_router_route_table_association_with_options(self, request, runtime):
        """
        ## Usage notes
        *   The network instance connection that you want to associate with another route table must be created on an Enterprise Edition transit router.
        *   **ReplaceTransitRouterRouteTableAssociation** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTableAssociations** to query the associated forwarding status between a network instance connection and transit router route table.
        *   The **Replacing** state indicates that the network instance connection is being associated with the specified transit router route table. You can query the associate forwarding correlation between the network instance connection and the transit router route table but cannot perform other operations.
        *   The **Active** state indicates that the network instance connection is associated with the specified transit router route table.
        

        @param request: ReplaceTransitRouterRouteTableAssociationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReplaceTransitRouterRouteTableAssociationResponse
        """
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
        """
        ## Usage notes
        *   The network instance connection that you want to associate with another route table must be created on an Enterprise Edition transit router.
        *   **ReplaceTransitRouterRouteTableAssociation** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterRouteTableAssociations** to query the associated forwarding status between a network instance connection and transit router route table.
        *   The **Replacing** state indicates that the network instance connection is being associated with the specified transit router route table. You can query the associate forwarding correlation between the network instance connection and the transit router route table but cannot perform other operations.
        *   The **Active** state indicates that the network instance connection is associated with the specified transit router route table.
        

        @param request: ReplaceTransitRouterRouteTableAssociationRequest

        @return: ReplaceTransitRouterRouteTableAssociationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.replace_transit_router_route_table_association_with_options(request, runtime)

    def resolve_and_route_service_in_cen_with_options(self, request, runtime):
        """
        ## Background information
        Cloud services refer to the Alibaba Cloud services that use the 100.64.0.0/10 CIDR block to provide services. These cloud services include Object Storage Service (OSS), Log Service, and Data Transmission Service (DTS). If your on-premises network needs to access a cloud service, you must attach the virtual border router (VBR) or Cloud Connect Network (CCN) instance that is connected to your on-premises network to a Cloud Enterprise Network (CEN) instance. In addition, you must attach a virtual private cloud (VPC) that is deployed in the same region as the cloud service to the CEN instance. This way, your on-premises network can connect to the VPC that is deployed in the same region as the cloud service and access the cloud service through the VPC.
        ## Usage notes
        - An on-premises network associated with a VBR can use CEN to access only a cloud service that is deployed in the same region.
        For example, if cloud services are deployed in the China (Beijing) region, only on-premises networks connected to VBRs in the China (Beijing) region can access the cloud services.
        - **ResolveAndRouteServiceInCen** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeRouteServicesInCen** to query the status of a cloud service.     - If a cloud service is in the **Creating** state, the connection to the cloud service is being created. In this case, you can query the cloud service but cannot perform other operations.
        - If a cloud service is in the **Active** state, the connection to the cloud service is created.
        - If a cloud service is in the **Failed** state, the connection to the cloud service failed.
        ## Prerequisites
        Before you call this operation, make sure that the following conditions are met:
        - The VBR or CCN instance to which your on-premises network is connected is attached to a CEN instance.
        - A VPC that is deployed in the same region as the cloud service is also attached to the CEN instance. For more information, see [AttachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/attachcenchildinstance).
        

        @param request: ResolveAndRouteServiceInCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResolveAndRouteServiceInCenResponse
        """
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
        """
        ## Background information
        Cloud services refer to the Alibaba Cloud services that use the 100.64.0.0/10 CIDR block to provide services. These cloud services include Object Storage Service (OSS), Log Service, and Data Transmission Service (DTS). If your on-premises network needs to access a cloud service, you must attach the virtual border router (VBR) or Cloud Connect Network (CCN) instance that is connected to your on-premises network to a Cloud Enterprise Network (CEN) instance. In addition, you must attach a virtual private cloud (VPC) that is deployed in the same region as the cloud service to the CEN instance. This way, your on-premises network can connect to the VPC that is deployed in the same region as the cloud service and access the cloud service through the VPC.
        ## Usage notes
        - An on-premises network associated with a VBR can use CEN to access only a cloud service that is deployed in the same region.
        For example, if cloud services are deployed in the China (Beijing) region, only on-premises networks connected to VBRs in the China (Beijing) region can access the cloud services.
        - **ResolveAndRouteServiceInCen** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeRouteServicesInCen** to query the status of a cloud service.     - If a cloud service is in the **Creating** state, the connection to the cloud service is being created. In this case, you can query the cloud service but cannot perform other operations.
        - If a cloud service is in the **Active** state, the connection to the cloud service is created.
        - If a cloud service is in the **Failed** state, the connection to the cloud service failed.
        ## Prerequisites
        Before you call this operation, make sure that the following conditions are met:
        - The VBR or CCN instance to which your on-premises network is connected is attached to a CEN instance.
        - A VPC that is deployed in the same region as the cloud service is also attached to the CEN instance. For more information, see [AttachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/attachcenchildinstance).
        

        @param request: ResolveAndRouteServiceInCenRequest

        @return: ResolveAndRouteServiceInCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resolve_and_route_service_in_cen_with_options(request, runtime)

    def revoke_instance_from_transit_router_with_options(self, request, runtime):
        """
        ## Usage notes
        `RevokeInstanceFromTransitRouter` disallows transit routers only from connecting to virtual private clouds (VPCs), virtual border routers (VBRs), and IPsec-VPN connections.
        If you want to disallow transit routers from connecting to Cloud Connect Network (CCN) instances, call the [RevokeInstanceFromCbn](https://www.alibabacloud.com/help/en/smart-access-gateway/latest/revokeinstancefromcbn) operation.
        ## Prerequisites
        Before you call `RevokeInstanceFromTransitRouter`, you must detach the network instances from the transit router.
        - For more information about how to detach VPCs from an Enterprise Edition transit router, see [DeleteTransitRouterVpcAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpcattachment).
        - For more information about how to detach VBRs from an Enterprise Edition transit router, see [DeleteTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervbrattachment).
        - For more information about how to detach network instances from a Basic Edition transit router, see [DetachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/detachcenchildinstance).
        

        @param request: RevokeInstanceFromTransitRouterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RevokeInstanceFromTransitRouterResponse
        """
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
        """
        ## Usage notes
        `RevokeInstanceFromTransitRouter` disallows transit routers only from connecting to virtual private clouds (VPCs), virtual border routers (VBRs), and IPsec-VPN connections.
        If you want to disallow transit routers from connecting to Cloud Connect Network (CCN) instances, call the [RevokeInstanceFromCbn](https://www.alibabacloud.com/help/en/smart-access-gateway/latest/revokeinstancefromcbn) operation.
        ## Prerequisites
        Before you call `RevokeInstanceFromTransitRouter`, you must detach the network instances from the transit router.
        - For more information about how to detach VPCs from an Enterprise Edition transit router, see [DeleteTransitRouterVpcAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervpcattachment).
        - For more information about how to detach VBRs from an Enterprise Edition transit router, see [DeleteTransitRouterVbrAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitroutervbrattachment).
        - For more information about how to detach network instances from a Basic Edition transit router, see [DetachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/detachcenchildinstance).
        

        @param request: RevokeInstanceFromTransitRouterRequest

        @return: RevokeInstanceFromTransitRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_transit_router_with_options(request, runtime)

    def route_private_zone_in_cen_to_vpc_with_options(self, request, runtime):
        """
        ## Background information
        Alibaba Cloud DNS PrivateZone (PrivateZone) is an Alibaba Cloud private domain name resolution and management service based on Virtual Private Cloud (VPC). After you attach virtual border routers (VBRs) and Cloud Connect Network (CCN) instances to a Cloud Enterprise Network (CEN) instance, you can enable the on-premises networks connected to the VBRs and CCN instances to access PrivateZone through the CEN instance.
        ## Usage notes
        - The on-premises networks connected to VBRs or CCN instances must be deployed in the same region as the PrivateZone service.
        For example, if the PrivateZone service is deployed in the China (Beijing) region, only on-premises networks connected to VBRs or CCN instances in the China (Beijing) region can access the PrivateZone service.
        - **RoutePrivateZoneInCenToVpc** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenPrivateZoneRoutes** to query the status of PrivateZone.     - If PrivateZone is in the **Creating** state, access to PrivateZone is being configured. In this case, you can query PrivateZone configurations but cannot perform other operations.
        - If PrivateZone is in the **Active** state, access to PrivateZone is enabled.
        - If PrivateZone is in the **Failed** state, configurations of access to PrivateZone failed.
        ## Prerequisites
        Before you call **RoutePrivateZoneInCenToVpc**, make sure that the following conditions are met:
        - PrivateZone is deployed. For more information, see [PrivateZone quick start](https://www.alibabacloud.com/help/en/privatezone/latest/subscribe-service).
        - The following network instances are attached to the same CEN instance: the VPC that is associated with the PrivateZone service, and the VBR and CCN instance that want to access the PrivateZone service. For more information, see [AttachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/attachcenchildinstance).
        - If your on-premises network uses a CCN instance to connect to Alibaba Cloud and the account that owns the CCN instance is different from the account that owns the VPC or CEN instance, you must grant the CCN instance required permissions. For more information, see [Grant permissions to CCN](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/215e75).
        

        @param request: RoutePrivateZoneInCenToVpcRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RoutePrivateZoneInCenToVpcResponse
        """
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
        """
        ## Background information
        Alibaba Cloud DNS PrivateZone (PrivateZone) is an Alibaba Cloud private domain name resolution and management service based on Virtual Private Cloud (VPC). After you attach virtual border routers (VBRs) and Cloud Connect Network (CCN) instances to a Cloud Enterprise Network (CEN) instance, you can enable the on-premises networks connected to the VBRs and CCN instances to access PrivateZone through the CEN instance.
        ## Usage notes
        - The on-premises networks connected to VBRs or CCN instances must be deployed in the same region as the PrivateZone service.
        For example, if the PrivateZone service is deployed in the China (Beijing) region, only on-premises networks connected to VBRs or CCN instances in the China (Beijing) region can access the PrivateZone service.
        - **RoutePrivateZoneInCenToVpc** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenPrivateZoneRoutes** to query the status of PrivateZone.     - If PrivateZone is in the **Creating** state, access to PrivateZone is being configured. In this case, you can query PrivateZone configurations but cannot perform other operations.
        - If PrivateZone is in the **Active** state, access to PrivateZone is enabled.
        - If PrivateZone is in the **Failed** state, configurations of access to PrivateZone failed.
        ## Prerequisites
        Before you call **RoutePrivateZoneInCenToVpc**, make sure that the following conditions are met:
        - PrivateZone is deployed. For more information, see [PrivateZone quick start](https://www.alibabacloud.com/help/en/privatezone/latest/subscribe-service).
        - The following network instances are attached to the same CEN instance: the VPC that is associated with the PrivateZone service, and the VBR and CCN instance that want to access the PrivateZone service. For more information, see [AttachCenChildInstance](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/attachcenchildinstance).
        - If your on-premises network uses a CCN instance to connect to Alibaba Cloud and the account that owns the CCN instance is different from the account that owns the VPC or CEN instance, you must grant the CCN instance required permissions. For more information, see [Grant permissions to CCN](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/215e75).
        

        @param request: RoutePrivateZoneInCenToVpcRequest

        @return: RoutePrivateZoneInCenToVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.route_private_zone_in_cen_to_vpc_with_options(request, runtime)

    def set_cen_inter_region_bandwidth_limit_with_options(self, request, runtime):
        """
        ## Prerequisites
        The Cloud Enterprise Network (CEN) instance is associated with a bandwidth plan. For more information, see the [CreateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createcenbandwidthpackage) and [AssociateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/associatecenbandwidthpackage) topics.
        ## Usage notes
        You can call the **SetCenInterRegionBandwidthLimit** operation to configure, modify, or remove the maximum bandwidth value of an inter-region connection.
        - If you set **BandwidthLimit** to a value other than 0, the maximum bandwidth value of the inter-region connection is set or changed to the specified value.
        - If you set **BandwidthLimit** to 0, no bandwidth resource is allocated to the inter-region connection.
        ## Limits
        - The maximum bandwidth value of an inter-region connection cannot exceed that of the associated bandwidth plan.
        - The sum of the maximum bandwidth values of all inter-region connections cannot exceed the maximum bandwidth value of the associated bandwidth plan.
        - If bandwidth multiplexing is enabled for an inter-region connection, you cannot change the maximum bandwidth value of the inter-region connection.
        - You can call **SetCenInterRegionBandwidthLimit** to configure, modify, and remove the maximum bandwidth values of inter-region connections only on Basic Edition transit routers.
        For more information about how to configure, modify, and remove the maximum bandwidth values of inter-region connections on Enterprise Edition transit routers, see [CreateTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createtransitrouterpeerattachment), [UpdateTransitRouterPeerAttachmentAttribute](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/updatetransitrouterpeerattachmentattribute), and [DeleteTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterpeerattachment).
        

        @param request: SetCenInterRegionBandwidthLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetCenInterRegionBandwidthLimitResponse
        """
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
        """
        ## Prerequisites
        The Cloud Enterprise Network (CEN) instance is associated with a bandwidth plan. For more information, see the [CreateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createcenbandwidthpackage) and [AssociateCenBandwidthPackage](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/associatecenbandwidthpackage) topics.
        ## Usage notes
        You can call the **SetCenInterRegionBandwidthLimit** operation to configure, modify, or remove the maximum bandwidth value of an inter-region connection.
        - If you set **BandwidthLimit** to a value other than 0, the maximum bandwidth value of the inter-region connection is set or changed to the specified value.
        - If you set **BandwidthLimit** to 0, no bandwidth resource is allocated to the inter-region connection.
        ## Limits
        - The maximum bandwidth value of an inter-region connection cannot exceed that of the associated bandwidth plan.
        - The sum of the maximum bandwidth values of all inter-region connections cannot exceed the maximum bandwidth value of the associated bandwidth plan.
        - If bandwidth multiplexing is enabled for an inter-region connection, you cannot change the maximum bandwidth value of the inter-region connection.
        - You can call **SetCenInterRegionBandwidthLimit** to configure, modify, and remove the maximum bandwidth values of inter-region connections only on Basic Edition transit routers.
        For more information about how to configure, modify, and remove the maximum bandwidth values of inter-region connections on Enterprise Edition transit routers, see [CreateTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/createtransitrouterpeerattachment), [UpdateTransitRouterPeerAttachmentAttribute](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/updatetransitrouterpeerattachmentattribute), and [DeleteTransitRouterPeerAttachment](https://www.alibabacloud.com/help/en/cloud-enterprise-network/latest/deletetransitrouterpeerattachment).
        

        @param request: SetCenInterRegionBandwidthLimitRequest

        @return: SetCenInterRegionBandwidthLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_cen_inter_region_bandwidth_limit_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        ## Description
        *   Each tag consists of a tag key and a tag value. When you add a tag, you must specify the tag key and tag value.
        *   If you want to add multiple tags to a Cloud Enterprise Network (CEN) instance, each tag key must be unique.
        *   You can add at most 20 tags to a CEN instance.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        ## Description
        *   Each tag consists of a tag key and a tag value. When you add a tag, you must specify the tag key and tag value.
        *   If you want to add multiple tags to a Cloud Enterprise Network (CEN) instance, each tag key must be unique.
        *   You can add at most 20 tags to a CEN instance.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def temp_upgrade_cen_bandwidth_package_spec_with_options(self, request, runtime):
        """
        ## Background information
        Subscription bandwidth plans support temporary upgrades. This topic describes how to temporarily upgrade a subscription bandwidth plan. You can increase the bandwidth limit of a bandwidth plan within a specified time window. This way, you can manage your bandwidth to handle traffic spikes in a more efficient manner.
        The minimum time window for a temporary upgrade is 3 hours. The bandwidth plan is upgraded immediately after you complete the payment. The upgrade process does not interrupt workloads.
        >  After the specified time window ends, the bandwidth limit of the subscription bandwidth plan is restored to the original value. If the actual bandwidth exceeds the bandwidth limit, packets may be dropped due to network traffic throttling. We recommend that you set a proper time window for the temporary upgrade and make sure that the bandwidth limit meets your business requirements.
        

        @param request: TempUpgradeCenBandwidthPackageSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TempUpgradeCenBandwidthPackageSpecResponse
        """
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
        """
        ## Background information
        Subscription bandwidth plans support temporary upgrades. This topic describes how to temporarily upgrade a subscription bandwidth plan. You can increase the bandwidth limit of a bandwidth plan within a specified time window. This way, you can manage your bandwidth to handle traffic spikes in a more efficient manner.
        The minimum time window for a temporary upgrade is 3 hours. The bandwidth plan is upgraded immediately after you complete the payment. The upgrade process does not interrupt workloads.
        >  After the specified time window ends, the bandwidth limit of the subscription bandwidth plan is restored to the original value. If the actual bandwidth exceeds the bandwidth limit, packets may be dropped due to network traffic throttling. We recommend that you set a proper time window for the temporary upgrade and make sure that the bandwidth limit meets your business requirements.
        

        @param request: TempUpgradeCenBandwidthPackageSpecRequest

        @return: TempUpgradeCenBandwidthPackageSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.temp_upgrade_cen_bandwidth_package_spec_with_options(request, runtime)

    def unassociate_cen_bandwidth_package_with_options(self, request, runtime):
        """
        ## Prerequisites
        No cross-region connections are configured in the bandwidth plan. For more information about how to delete cross-region connections, see [SetCenInterRegionBandwidthLimit](~~65942~~).
        

        @param request: UnassociateCenBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnassociateCenBandwidthPackageResponse
        """
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
        """
        ## Prerequisites
        No cross-region connections are configured in the bandwidth plan. For more information about how to delete cross-region connections, see [SetCenInterRegionBandwidthLimit](~~65942~~).
        

        @param request: UnassociateCenBandwidthPackageRequest

        @return: UnassociateCenBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unassociate_cen_bandwidth_package_with_options(request, runtime)

    def unroute_private_zone_in_cen_to_vpc_with_options(self, request, runtime):
        """
        ## Usage notes
        **UnroutePrivateZoneInCenToVpc** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenPrivateZoneRoutes** to query the status of PrivateZone.
        *   If PrivateZone is in the **Deleting** state, access to PrivateZone is being disabled. In this case, you can query PrivateZone configurations but cannot perform other operations.
        *   If configurations of access to PrivateZone cannot be found, access to PrivateZone is disabled.
        

        @param request: UnroutePrivateZoneInCenToVpcRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UnroutePrivateZoneInCenToVpcResponse
        """
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
        """
        ## Usage notes
        **UnroutePrivateZoneInCenToVpc** is an asynchronous operation. After you send a request, the **request ID** is returned but the operation is still being performed in the system background. You can call **DescribeCenPrivateZoneRoutes** to query the status of PrivateZone.
        *   If PrivateZone is in the **Deleting** state, access to PrivateZone is being disabled. In this case, you can query PrivateZone configurations but cannot perform other operations.
        *   If configurations of access to PrivateZone cannot be found, access to PrivateZone is disabled.
        

        @param request: UnroutePrivateZoneInCenToVpcRequest

        @return: UnroutePrivateZoneInCenToVpcResponse
        """
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.add_traffic_match_rules):
            query['AddTrafficMatchRules'] = request.add_traffic_match_rules
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_traffic_match_rules):
            query['DeleteTrafficMatchRules'] = request.delete_traffic_match_rules
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
        """
        *UpdateTransitRouter** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouters** to query the status of a transit router.
        *   If a transit router is in the **Modifying** state, the configuration of the transit router is being modified. You can query the transit router but cannot perform other operations.
        *   If a transit router is in the **Active** state, the configuration of the transit router is modified.
        

        @param request: UpdateTransitRouterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTransitRouterResponse
        """
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
        """
        *UpdateTransitRouter** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouters** to query the status of a transit router.
        *   If a transit router is in the **Modifying** state, the configuration of the transit router is being modified. You can query the transit router but cannot perform other operations.
        *   If a transit router is in the **Active** state, the configuration of the transit router is modified.
        

        @param request: UpdateTransitRouterRequest

        @return: UpdateTransitRouterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_with_options(request, runtime)

    def update_transit_router_peer_attachment_attribute_with_options(self, request, runtime):
        """
        ## Usage notes
        **UpdateTransitRouterPeerAttachmentAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterPeerAttachments** to query the status of an inter-region connection.
        *   If an inter-region connection is in the **Modifying** state, the inter-region connection is being modified. You can query the inter-region connection but cannot perform other operations.
        *   If an inter-region connection is in the **Attached** state, the inter-region connection is modified.
        

        @param request: UpdateTransitRouterPeerAttachmentAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTransitRouterPeerAttachmentAttributeResponse
        """
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
        """
        ## Usage notes
        **UpdateTransitRouterPeerAttachmentAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterPeerAttachments** to query the status of an inter-region connection.
        *   If an inter-region connection is in the **Modifying** state, the inter-region connection is being modified. You can query the inter-region connection but cannot perform other operations.
        *   If an inter-region connection is in the **Attached** state, the inter-region connection is modified.
        

        @param request: UpdateTransitRouterPeerAttachmentAttributeRequest

        @return: UpdateTransitRouterPeerAttachmentAttributeResponse
        """
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
        if not UtilClient.is_unset(request.route_table_options):
            query['RouteTableOptions'] = request.route_table_options
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
        """
        ## Usage notes
        **UpdateTransitRouterVbrAttachmentAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVbrAttachments** to query the status of a VBR connection.
        *   If a VBR connection is in the **Modifying** state, the VBR connection is being modified. You can query the VBR connection but cannot perform other operations.
        *   If the VBR connection is in the **Attached** state, the VBR connection is modified.
        

        @param request: UpdateTransitRouterVbrAttachmentAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTransitRouterVbrAttachmentAttributeResponse
        """
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
        """
        ## Usage notes
        **UpdateTransitRouterVbrAttachmentAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVbrAttachments** to query the status of a VBR connection.
        *   If a VBR connection is in the **Modifying** state, the VBR connection is being modified. You can query the VBR connection but cannot perform other operations.
        *   If the VBR connection is in the **Attached** state, the VBR connection is modified.
        

        @param request: UpdateTransitRouterVbrAttachmentAttributeRequest

        @return: UpdateTransitRouterVbrAttachmentAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vbr_attachment_attribute_with_options(request, runtime)

    def update_transit_router_vpc_attachment_attribute_with_options(self, request, runtime):
        """
        ## Usage notes
        **UpdateTransitRouterVpcAttachmentAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVpcAttachments** to query the status of a VPC connection.
        *   If a VPC connection is in the **Modifying** state, the VPC connection is being modified. You can query the VPC connection but cannot perform other operations.
        *   If a VPC connection is in the **Attached** state, the VPC connection is modified.
        

        @param request: UpdateTransitRouterVpcAttachmentAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTransitRouterVpcAttachmentAttributeResponse
        """
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
        """
        ## Usage notes
        **UpdateTransitRouterVpcAttachmentAttribute** is an asynchronous operation. After you send a request, the system returns the **request ID** but the operation is still being performed in the system background. You can call **ListTransitRouterVpcAttachments** to query the status of a VPC connection.
        *   If a VPC connection is in the **Modifying** state, the VPC connection is being modified. You can query the VPC connection but cannot perform other operations.
        *   If a VPC connection is in the **Attached** state, the VPC connection is modified.
        

        @param request: UpdateTransitRouterVpcAttachmentAttributeRequest

        @return: UpdateTransitRouterVpcAttachmentAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_transit_router_vpc_attachment_attribute_with_options(request, runtime)

    def update_transit_router_vpc_attachment_zones_with_options(self, request, runtime):
        """
        ## Usage notes
        *   When you add a zone and a vSwitch for a VPC connection, make sure that the vSwitch has at least one idle IP address. When you modify the zones and vSwitches of a VPC connection, the Enterprise Edition transit router creates an elastic network interface (ENI) in the vSwitch. The ENI occupies one IP address in the vSwitch. The ENI forwards traffic between the VPC and the Enterprise Edition transit router.
        *   The **UpdateTransitRouterVpcAttachmentZones** operation is asynchronous. After you send the request, the system returns a request ID (**RequestId**). However, the operation is still being performed in the system background. You can call the **ListTransitRouterVpcAttachments** operation to query the status of a VPC connection.
        *   If a VPC connection is in the **Modifying** state, the VPC connection is being modified. You can query the VPC connection but cannot perform other operations.
        *   If a VPC connection is in the **Attached** state, the VPC connection is modified.
        

        @param request: UpdateTransitRouterVpcAttachmentZonesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTransitRouterVpcAttachmentZonesResponse
        """
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
        """
        ## Usage notes
        *   When you add a zone and a vSwitch for a VPC connection, make sure that the vSwitch has at least one idle IP address. When you modify the zones and vSwitches of a VPC connection, the Enterprise Edition transit router creates an elastic network interface (ENI) in the vSwitch. The ENI occupies one IP address in the vSwitch. The ENI forwards traffic between the VPC and the Enterprise Edition transit router.
        *   The **UpdateTransitRouterVpcAttachmentZones** operation is asynchronous. After you send the request, the system returns a request ID (**RequestId**). However, the operation is still being performed in the system background. You can call the **ListTransitRouterVpcAttachments** operation to query the status of a VPC connection.
        *   If a VPC connection is in the **Modifying** state, the VPC connection is being modified. You can query the VPC connection but cannot perform other operations.
        *   If a VPC connection is in the **Attached** state, the VPC connection is modified.
        

        @param request: UpdateTransitRouterVpcAttachmentZonesRequest

        @return: UpdateTransitRouterVpcAttachmentZonesResponse
        """
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
