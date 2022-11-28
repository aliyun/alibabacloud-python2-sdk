2022-11-28 Version: 1.0.5
- Add CreateTransitRouterCidr support create TR Cidr.
- Add ModifyTransitRouterCidr support modify TR Cidr.
- Add DeleteTransitRouterCidr support delete TR Cidr.
- Add ListTransitRouterCidr support list TR Cidr.
- Add ListTransitRouterCidrAllocation support list TR Cidr allocation.
- Update CreateTransitRouter support TR Cidr list.
- Update ListTransitRouters support Cidr list.
- Update ListTransitRouterVpnAttachments response support ChargeType.
- CreateFlowlog add parameter tag.
- DescribeFlowlogs add parameter tag and add response tags.
- CreateTransitRouterMulticastDomain add parameter tag.
- ListTransitRouterMulticastDomains add parameter tag and add response tags.
- CreateTransitRouterRouteTable add parameter tag.
- ListTransitRouterRouteTables add parameter tag and add response tags.
- CreateTransitRouter add parameter tag.
- ListTransitRouters add parameter tag and add response tags.

2022-11-22 Version: 1.0.4
- Update ListTransitRouterMulticastGroups offline parameter ConnectPeerId.
- Update CreateCenBandwidthPackage offline parameter ServiceType.
- Update ModifyCenBandwidthPackageSpec offline parameter ServiceType.
- Update DescribeCenBandwidthPackages offline parameter ServiceType.

2022-11-02 Version: 1.0.3
- Update ListTransitRouterPrefixListAssociation support NextHop and NextHopType filter.
- Update ListTransitRouterPrefixListAssociation support TransitRouterRouteTableId  filter.
- Update ListTrafficMarkingPolicies no TrafficMatchRules field in response if no TrafficMarkingPolicyId in request.
- Update ListCenInterRegionTrafficQosPolicies no TrafficQosQueues field in response if no TrafficQosPolicyId in request.

2022-09-23 Version: 1.0.2
- Add new API DescribeGrantRulesToResource .
- Update DescribeGrantRulesToCen support MaxResult and nextToken .
- Update ListTransitRouterPrefixlistAssociation return TransitRouterId and TransitRouterTableId .

2022-08-26 Version: 1.0.1
- Update param NextHopType visibility for DeleteTransitRouterPrefixListAssociation .

2022-08-26 Version: 1.0.0
- Add AvailableZones for ListTransitRouterAvailableResource.

