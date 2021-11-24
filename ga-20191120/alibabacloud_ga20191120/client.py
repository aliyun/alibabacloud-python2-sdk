# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ga20191120 import models as ga_20191120_models
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
        self._endpoint = self.get_endpoint('ga', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_entries_to_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclEntries'] = request.acl_entries
        query['AclId'] = request.acl_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddEntriesToAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AddEntriesToAclResponse(),
            self.call_api(params, req, runtime)
        )

    def add_entries_to_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    def associate_acls_with_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclIds'] = request.acl_ids
        query['AclType'] = request.acl_type
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociateAclsWithListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AssociateAclsWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_acls_with_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    def associate_additional_certificates_with_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['Certificates'] = request.certificates
        query['ClientToken'] = request.client_token
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AssociateAdditionalCertificatesWithListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_additional_certificates_with_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    def attach_ddos_to_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['DdosId'] = request.ddos_id
        query['DdosRegionId'] = request.ddos_region_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachDdosToAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AttachDdosToAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_ddos_to_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_ddos_to_accelerator_with_options(request, runtime)

    def attach_log_store_to_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['EndpointGroupIds'] = request.endpoint_group_ids
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        query['SlsLogStoreName'] = request.sls_log_store_name
        query['SlsProjectName'] = request.sls_project_name
        query['SlsRegionId'] = request.sls_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachLogStoreToEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AttachLogStoreToEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_log_store_to_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_log_store_to_endpoint_group_with_options(request, runtime)

    def bandwidth_package_add_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BandwidthPackageAddAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.BandwidthPackageAddAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def bandwidth_package_add_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bandwidth_package_add_accelerator_with_options(request, runtime)

    def bandwidth_package_remove_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BandwidthPackageRemoveAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.BandwidthPackageRemoveAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def bandwidth_package_remove_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bandwidth_package_remove_accelerator_with_options(request, runtime)

    def config_endpoint_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Enable'] = request.enable
        query['Endpoint'] = request.endpoint
        query['EndpointGroupId'] = request.endpoint_group_id
        query['EndpointType'] = request.endpoint_type
        query['ProbePort'] = request.probe_port
        query['ProbeProtocol'] = request.probe_protocol
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConfigEndpointProbe',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ConfigEndpointProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def config_endpoint_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_endpoint_probe_with_options(request, runtime)

    def create_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['AutoRenew'] = request.auto_renew
        query['AutoRenewDuration'] = request.auto_renew_duration
        query['AutoUseCoupon'] = request.auto_use_coupon
        query['ClientToken'] = request.client_token
        query['Duration'] = request.duration
        query['Name'] = request.name
        query['PricingCycle'] = request.pricing_cycle
        query['RegionId'] = request.region_id
        query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_accelerator_with_options(request, runtime)

    def create_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclEntries'] = request.acl_entries
        query['AclName'] = request.acl_name
        query['AddressIPVersion'] = request.address_ipversion
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    def create_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    def create_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['AutoUseCoupon'] = request.auto_use_coupon
        query['Bandwidth'] = request.bandwidth
        query['BandwidthType'] = request.bandwidth_type
        query['BillingType'] = request.billing_type
        query['CbnGeographicRegionIdA'] = request.cbn_geographic_region_id_a
        query['CbnGeographicRegionIdB'] = request.cbn_geographic_region_id_b
        query['ChargeType'] = request.charge_type
        query['ClientToken'] = request.client_token
        query['Duration'] = request.duration
        query['PricingCycle'] = request.pricing_cycle
        query['Ratio'] = request.ratio
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bandwidth_package_with_options(request, runtime)

    def create_basic_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['AutoUseCoupon'] = request.auto_use_coupon
        query['ClientToken'] = request.client_token
        query['Duration'] = request.duration
        query['PricingCycle'] = request.pricing_cycle
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_basic_accelerator_with_options(request, runtime)

    def create_basic_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['EndpointAddress'] = request.endpoint_address
        query['EndpointGroupRegion'] = request.endpoint_group_region
        query['EndpointType'] = request.endpoint_type
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_basic_endpoint_group_with_options(request, runtime)

    def create_basic_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccelerateRegionId'] = request.accelerate_region_id
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_basic_ip_set_with_options(request, runtime)

    def create_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['EndpointConfigurations'] = request.endpoint_configurations
        query['EndpointGroupRegion'] = request.endpoint_group_region
        query['EndpointGroupType'] = request.endpoint_group_type
        query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        query['HealthCheckEnabled'] = request.health_check_enabled
        query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        query['HealthCheckPath'] = request.health_check_path
        query['HealthCheckPort'] = request.health_check_port
        query['HealthCheckProtocol'] = request.health_check_protocol
        query['ListenerId'] = request.listener_id
        query['Name'] = request.name
        query['PortOverrides'] = request.port_overrides
        query['RegionId'] = request.region_id
        query['ThresholdCount'] = request.threshold_count
        query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_group_with_options(request, runtime)

    def create_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_groups_with_options(request, runtime)

    def create_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['ForwardingRules'] = request.forwarding_rules
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_forwarding_rules_with_options(request, runtime)

    def create_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AccelerateRegion'] = request.accelerate_region
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ip_sets_with_options(request, runtime)

    def create_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['Certificates'] = request.certificates
        query['ClientAffinity'] = request.client_affinity
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Name'] = request.name
        query['PortRanges'] = request.port_ranges
        query['Protocol'] = request.protocol
        query['ProxyProtocol'] = request.proxy_protocol
        query['RegionId'] = request.region_id
        query['SecurityPolicyId'] = request.security_policy_id
        query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    def create_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        query['SpareIps'] = request.spare_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSpareIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_spare_ips_with_options(request, runtime)

    def delete_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_accelerator_with_options(request, runtime)

    def delete_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclId'] = request.acl_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['ClientToken'] = request.client_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    def delete_basic_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_accelerator_with_options(request, runtime)

    def delete_basic_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_endpoint_group_with_options(request, runtime)

    def delete_basic_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['IpSetId'] = request.ip_set_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_ip_set_with_options(request, runtime)

    def delete_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_group_with_options(request, runtime)

    def delete_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['EndpointGroupIds'] = request.endpoint_group_ids
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_groups_with_options(request, runtime)

    def delete_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['ForwardingRuleIds'] = request.forwarding_rule_ids
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_forwarding_rules_with_options(request, runtime)

    def delete_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['IpSetId'] = request.ip_set_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_set_with_options(request, runtime)

    def delete_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpSetIds'] = request.ip_set_ids
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_sets_with_options(request, runtime)

    def delete_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    def delete_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        query['SpareIps'] = request.spare_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSpareIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_spare_ips_with_options(request, runtime)

    def describe_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accelerator_with_options(request, runtime)

    def describe_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_package_with_options(request, runtime)

    def describe_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndpointGroupId'] = request.endpoint_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_group_with_options(request, runtime)

    def describe_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpSetId'] = request.ip_set_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_set_with_options(request, runtime)

    def describe_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_listener_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def detach_ddos_from_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachDdosFromAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DetachDdosFromAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_ddos_from_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_ddos_from_accelerator_with_options(request, runtime)

    def detach_log_store_from_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['EndpointGroupIds'] = request.endpoint_group_ids
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachLogStoreFromEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DetachLogStoreFromEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_log_store_from_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_log_store_from_endpoint_group_with_options(request, runtime)

    def dissociate_acls_from_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclIds'] = request.acl_ids
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DissociateAclsFromListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DissociateAclsFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_acls_from_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['Domains'] = request.domains
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DissociateAdditionalCertificatesFromListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_additional_certificates_from_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    def get_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclId'] = request.acl_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetAclResponse(),
            self.call_api(params, req, runtime)
        )

    def get_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_acl_with_options(request, runtime)

    def get_basic_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_accelerator_with_options(request, runtime)

    def get_basic_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['EndpointGroupId'] = request.endpoint_group_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_endpoint_group_with_options(request, runtime)

    def get_basic_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['IpSetId'] = request.ip_set_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_ip_set_with_options(request, runtime)

    def get_health_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHealthStatus',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_health_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_health_status_with_options(request, runtime)

    def get_spare_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        query['SpareIp'] = request.spare_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSpareIp',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetSpareIpResponse(),
            self.call_api(params, req, runtime)
        )

    def get_spare_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_spare_ip_with_options(request, runtime)

    def list_accelerate_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccelerateAreas',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAccelerateAreasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accelerate_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accelerate_areas_with_options(request, runtime)

    def list_accelerators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccelerators',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAcceleratorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accelerators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accelerators_with_options(request, runtime)

    def list_acls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclIds'] = request.acl_ids
        query['AclName'] = request.acl_name
        query['ClientToken'] = request.client_token
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAclsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_acls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    def list_available_accelerate_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAvailableAccelerateAreas',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAvailableAccelerateAreasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_accelerate_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_accelerate_areas_with_options(request, runtime)

    def list_available_busi_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAvailableBusiRegions',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAvailableBusiRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_busi_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_busi_regions_with_options(request, runtime)

    def list_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['State'] = request.state
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBandwidthPackages',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bandwidth_packages_with_options(request, runtime)

    def list_bandwidthackages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBandwidthackages',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBandwidthackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bandwidthackages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bandwidthackages_with_options(request, runtime)

    def list_basic_accelerators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBasicAccelerators',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBasicAcceleratorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_basic_accelerators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_basic_accelerators_with_options(request, runtime)

    def list_busi_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBusiRegions',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBusiRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_busi_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_busi_regions_with_options(request, runtime)

    def list_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['AccessLogSwitch'] = request.access_log_switch
        query['EndpointGroupId'] = request.endpoint_group_id
        query['EndpointGroupType'] = request.endpoint_group_type
        query['ListenerId'] = request.listener_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_endpoint_groups_with_options(request, runtime)

    def list_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['ForwardingRuleId'] = request.forwarding_rule_id
        query['ListenerId'] = request.listener_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_forwarding_rules_with_options(request, runtime)

    def list_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ip_sets_with_options(request, runtime)

    def list_listener_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ListenerId'] = request.listener_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['RegionId'] = request.region_id
        query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListListenerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_listener_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    def list_listeners_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_listeners(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    def list_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSpareIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_spare_ips_with_options(request, runtime)

    def list_system_security_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSystemSecurityPolicies',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListSystemSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_security_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policies_with_options(request, runtime)

    def remove_entries_from_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclEntries'] = request.acl_entries
        query['AclId'] = request.acl_id
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveEntriesFromAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.RemoveEntriesFromAclResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_entries_from_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    def replace_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['RegionId'] = request.region_id
        query['TargetBandwidthPackageId'] = request.target_bandwidth_package_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReplaceBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ReplaceBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_bandwidth_package_with_options(request, runtime)

    def update_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['AutoPay'] = request.auto_pay
        query['AutoUseCoupon'] = request.auto_use_coupon
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_with_options(request, runtime)

    def update_accelerator_confirm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAcceleratorConfirm',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator_confirm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_confirm_with_options(request, runtime)

    def update_acl_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AclId'] = request.acl_id
        query['AclName'] = request.acl_name
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAclAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_acl_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    def update_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['AutoUseCoupon'] = request.auto_use_coupon
        query['Bandwidth'] = request.bandwidth
        query['BandwidthPackageId'] = request.bandwidth_package_id
        query['BandwidthType'] = request.bandwidth_type
        query['Description'] = request.description
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_bandwidth_package_with_options(request, runtime)

    def update_basic_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_basic_accelerator_with_options(request, runtime)

    def update_basic_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['EndpointAddress'] = request.endpoint_address
        query['EndpointGroupId'] = request.endpoint_group_id
        query['EndpointType'] = request.endpoint_type
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_basic_endpoint_group_with_options(request, runtime)

    def update_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['EndpointConfigurations'] = request.endpoint_configurations
        query['EndpointGroupId'] = request.endpoint_group_id
        query['EndpointGroupRegion'] = request.endpoint_group_region
        query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        query['HealthCheckEnabled'] = request.health_check_enabled
        query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        query['HealthCheckPath'] = request.health_check_path
        query['HealthCheckPort'] = request.health_check_port
        query['HealthCheckProtocol'] = request.health_check_protocol
        query['Name'] = request.name
        query['PortOverrides'] = request.port_overrides
        query['RegionId'] = request.region_id
        query['ThresholdCount'] = request.threshold_count
        query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_group_with_options(request, runtime)

    def update_endpoint_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['EndpointGroupId'] = request.endpoint_group_id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEndpointGroupAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_endpoint_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_group_attribute_with_options(request, runtime)

    def update_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DryRun'] = request.dry_run
        query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_groups_with_options(request, runtime)

    def update_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AcceleratorId'] = request.accelerator_id
        query['ClientToken'] = request.client_token
        query['ForwardingRules'] = request.forwarding_rules
        query['ListenerId'] = request.listener_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_forwarding_rules_with_options(request, runtime)

    def update_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Bandwidth'] = request.bandwidth
        query['ClientToken'] = request.client_token
        query['IpSetId'] = request.ip_set_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ip_set_with_options(request, runtime)

    def update_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpSets'] = request.ip_sets
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ip_sets_with_options(request, runtime)

    def update_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BackendPorts'] = request.backend_ports
        query['Certificates'] = request.certificates
        query['ClientAffinity'] = request.client_affinity
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['ListenerId'] = request.listener_id
        query['Name'] = request.name
        query['PortRanges'] = request.port_ranges
        query['Protocol'] = request.protocol
        query['ProxyProtocol'] = request.proxy_protocol
        query['RegionId'] = request.region_id
        query['SecurityPolicyId'] = request.security_policy_id
        query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_listener_with_options(request, runtime)
