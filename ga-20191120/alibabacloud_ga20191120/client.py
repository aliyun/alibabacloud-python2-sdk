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

    def describe_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeIpSetResponse(),
            self.do_rpcrequest('DescribeIpSet', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_set_with_options(request, runtime)

    def list_acls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAclsResponse(),
            self.do_rpcrequest('ListAcls', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_acls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    def create_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateAcceleratorResponse(),
            self.do_rpcrequest('CreateAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_accelerator_with_options(request, runtime)

    def describe_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeListenerResponse(),
            self.do_rpcrequest('DescribeListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_listener_with_options(request, runtime)

    def delete_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteSpareIpsResponse(),
            self.do_rpcrequest('DeleteSpareIps', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_spare_ips_with_options(request, runtime)

    def update_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateIpSetsResponse(),
            self.do_rpcrequest('UpdateIpSets', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ip_sets_with_options(request, runtime)

    def config_endpoint_probe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ConfigEndpointProbeResponse(),
            self.do_rpcrequest('ConfigEndpointProbe', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_endpoint_probe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_endpoint_probe_with_options(request, runtime)

    def remove_entries_from_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.RemoveEntriesFromAclResponse(),
            self.do_rpcrequest('RemoveEntriesFromAcl', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_entries_from_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    def describe_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeBandwidthPackageResponse(),
            self.do_rpcrequest('DescribeBandwidthPackage', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_package_with_options(request, runtime)

    def list_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBandwidthPackagesResponse(),
            self.do_rpcrequest('ListBandwidthPackages', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bandwidth_packages_with_options(request, runtime)

    def update_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupResponse(),
            self.do_rpcrequest('UpdateEndpointGroup', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_group_with_options(request, runtime)

    def attach_ddos_to_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.AttachDdosToAcceleratorResponse(),
            self.do_rpcrequest('AttachDdosToAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_ddos_to_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_ddos_to_accelerator_with_options(request, runtime)

    def get_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.GetAclResponse(),
            self.do_rpcrequest('GetAcl', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_acl_with_options(request, runtime)

    def associate_acls_with_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.AssociateAclsWithListenerResponse(),
            self.do_rpcrequest('AssociateAclsWithListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_acls_with_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    def list_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListForwardingRulesResponse(),
            self.do_rpcrequest('ListForwardingRules', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_forwarding_rules_with_options(request, runtime)

    def create_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBandwidthPackageResponse(),
            self.do_rpcrequest('CreateBandwidthPackage', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bandwidth_package_with_options(request, runtime)

    def list_bandwidthackages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBandwidthackagesResponse(),
            self.do_rpcrequest('ListBandwidthackages', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bandwidthackages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bandwidthackages_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBandwidthPackageResponse(),
            self.do_rpcrequest('DeleteBandwidthPackage', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    def get_health_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.GetHealthStatusResponse(),
            self.do_rpcrequest('GetHealthStatus', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_health_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_health_status_with_options(request, runtime)

    def describe_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeAcceleratorResponse(),
            self.do_rpcrequest('DescribeAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accelerator_with_options(request, runtime)

    def detach_log_store_from_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DetachLogStoreFromEndpointGroupResponse(),
            self.do_rpcrequest('DetachLogStoreFromEndpointGroup', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_log_store_from_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_log_store_from_endpoint_group_with_options(request, runtime)

    def create_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateIpSetsResponse(),
            self.do_rpcrequest('CreateIpSets', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ip_sets_with_options(request, runtime)

    def create_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateForwardingRulesResponse(),
            self.do_rpcrequest('CreateForwardingRules', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_forwarding_rules_with_options(request, runtime)

    def list_available_accelerate_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAvailableAccelerateAreasResponse(),
            self.do_rpcrequest('ListAvailableAccelerateAreas', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_available_accelerate_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_accelerate_areas_with_options(request, runtime)

    def delete_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteAclResponse(),
            self.do_rpcrequest('DeleteAcl', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    def add_entries_to_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.AddEntriesToAclResponse(),
            self.do_rpcrequest('AddEntriesToAcl', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_entries_to_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    def create_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateSpareIpsResponse(),
            self.do_rpcrequest('CreateSpareIps', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_spare_ips_with_options(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.do_rpcrequest('DissociateAdditionalCertificatesFromListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_additional_certificates_from_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    def list_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListEndpointGroupsResponse(),
            self.do_rpcrequest('ListEndpointGroups', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_endpoint_groups_with_options(request, runtime)

    def list_busi_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBusiRegionsResponse(),
            self.do_rpcrequest('ListBusiRegions', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_busi_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_busi_regions_with_options(request, runtime)

    def replace_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ReplaceBandwidthPackageResponse(),
            self.do_rpcrequest('ReplaceBandwidthPackage', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_bandwidth_package_with_options(request, runtime)

    def update_endpoint_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupAttributeResponse(),
            self.do_rpcrequest('UpdateEndpointGroupAttribute', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_endpoint_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_group_attribute_with_options(request, runtime)

    def update_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateForwardingRulesResponse(),
            self.do_rpcrequest('UpdateForwardingRules', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_forwarding_rules_with_options(request, runtime)

    def list_listeners_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListListenersResponse(),
            self.do_rpcrequest('ListListeners', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_listeners(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    def describe_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeEndpointGroupResponse(),
            self.do_rpcrequest('DescribeEndpointGroup', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_group_with_options(request, runtime)

    def delete_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteListenerResponse(),
            self.do_rpcrequest('DeleteListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    def associate_additional_certificates_with_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.do_rpcrequest('AssociateAdditionalCertificatesWithListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_additional_certificates_with_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    def attach_log_store_to_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.AttachLogStoreToEndpointGroupResponse(),
            self.do_rpcrequest('AttachLogStoreToEndpointGroup', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_log_store_to_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_log_store_to_endpoint_group_with_options(request, runtime)

    def update_cross_border_package_compliance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateCrossBorderPackageComplianceStatusResponse(),
            self.do_rpcrequest('UpdateCrossBorderPackageComplianceStatus', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cross_border_package_compliance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cross_border_package_compliance_status_with_options(request, runtime)

    def update_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBandwidthPackageResponse(),
            self.do_rpcrequest('UpdateBandwidthPackage', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_bandwidth_package_with_options(request, runtime)

    def delete_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteAcceleratorResponse(),
            self.do_rpcrequest('DeleteAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_accelerator_with_options(request, runtime)

    def create_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateEndpointGroupResponse(),
            self.do_rpcrequest('CreateEndpointGroup', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_group_with_options(request, runtime)

    def delete_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteEndpointGroupResponse(),
            self.do_rpcrequest('DeleteEndpointGroup', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_group_with_options(request, runtime)

    def list_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListIpSetsResponse(),
            self.do_rpcrequest('ListIpSets', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ip_sets_with_options(request, runtime)

    def update_accelerator_confirm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorConfirmResponse(),
            self.do_rpcrequest('UpdateAcceleratorConfirm', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_accelerator_confirm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_confirm_with_options(request, runtime)

    def bandwidth_package_remove_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.BandwidthPackageRemoveAcceleratorResponse(),
            self.do_rpcrequest('BandwidthPackageRemoveAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bandwidth_package_remove_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bandwidth_package_remove_accelerator_with_options(request, runtime)

    def delete_forwarding_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteForwardingRulesResponse(),
            self.do_rpcrequest('DeleteForwardingRules', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_forwarding_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_forwarding_rules_with_options(request, runtime)

    def dissociate_acls_from_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DissociateAclsFromListenerResponse(),
            self.do_rpcrequest('DissociateAclsFromListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_acls_from_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    def list_cross_border_package_for_compliance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCrossBorderPackageForComplianceResponse(),
            self.do_rpcrequest('ListCrossBorderPackageForCompliance', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cross_border_package_for_compliance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cross_border_package_for_compliance_with_options(request, runtime)

    def list_accelerate_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAccelerateAreasResponse(),
            self.do_rpcrequest('ListAccelerateAreas', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_accelerate_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accelerate_areas_with_options(request, runtime)

    def list_listener_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListListenerCertificatesResponse(),
            self.do_rpcrequest('ListListenerCertificates', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_listener_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    def update_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateIpSetResponse(),
            self.do_rpcrequest('UpdateIpSet', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ip_set_with_options(request, runtime)

    def create_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateAclResponse(),
            self.do_rpcrequest('CreateAcl', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def update_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateListenerResponse(),
            self.do_rpcrequest('UpdateListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_listener_with_options(request, runtime)

    def list_available_busi_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAvailableBusiRegionsResponse(),
            self.do_rpcrequest('ListAvailableBusiRegions', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_available_busi_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_busi_regions_with_options(request, runtime)

    def update_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorResponse(),
            self.do_rpcrequest('UpdateAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_with_options(request, runtime)

    def delete_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteEndpointGroupsResponse(),
            self.do_rpcrequest('DeleteEndpointGroups', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_groups_with_options(request, runtime)

    def delete_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteIpSetResponse(),
            self.do_rpcrequest('DeleteIpSet', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_set_with_options(request, runtime)

    def update_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupsResponse(),
            self.do_rpcrequest('UpdateEndpointGroups', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_groups_with_options(request, runtime)

    def delete_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteIpSetsResponse(),
            self.do_rpcrequest('DeleteIpSets', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_sets_with_options(request, runtime)

    def bandwidth_package_add_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.BandwidthPackageAddAcceleratorResponse(),
            self.do_rpcrequest('BandwidthPackageAddAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bandwidth_package_add_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bandwidth_package_add_accelerator_with_options(request, runtime)

    def update_acl_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAclAttributeResponse(),
            self.do_rpcrequest('UpdateAclAttribute', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_acl_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    def list_accelerators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAcceleratorsResponse(),
            self.do_rpcrequest('ListAccelerators', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_accelerators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accelerators_with_options(request, runtime)

    def create_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateListenerResponse(),
            self.do_rpcrequest('CreateListener', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    def list_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.ListSpareIpsResponse(),
            self.do_rpcrequest('ListSpareIps', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_spare_ips_with_options(request, runtime)

    def create_endpoint_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateEndpointGroupsResponse(),
            self.do_rpcrequest('CreateEndpointGroups', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_endpoint_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_groups_with_options(request, runtime)

    def detach_ddos_from_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.DetachDdosFromAcceleratorResponse(),
            self.do_rpcrequest('DetachDdosFromAccelerator', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_ddos_from_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_ddos_from_accelerator_with_options(request, runtime)

    def get_spare_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ga_20191120_models.GetSpareIpResponse(),
            self.do_rpcrequest('GetSpareIp', '2019-11-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_spare_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_spare_ip_with_options(request, runtime)
