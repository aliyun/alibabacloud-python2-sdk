# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecd20200930 import models as ecd_20200930_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_adconnector_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreateADConnectorDirectoryResponse().from_map(
            self.do_rpcrequest('CreateADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adconnector_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    def create_bundle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreateBundleResponse().from_map(
            self.do_rpcrequest('CreateBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bundle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    def create_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreateDesktopsResponse().from_map(
            self.do_rpcrequest('CreateDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreateImageResponse().from_map(
            self.do_rpcrequest('CreateImage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreatePolicyGroupResponse().from_map(
            self.do_rpcrequest('CreatePolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    def create_ramdirectory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreateRAMDirectoryResponse().from_map(
            self.do_rpcrequest('CreateRAMDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ramdirectory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.CreateSnapshotResponse().from_map(
            self.do_rpcrequest('CreateSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def delete_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeleteBundlesResponse().from_map(
            self.do_rpcrequest('DeleteBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    def delete_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeleteDesktopsResponse().from_map(
            self.do_rpcrequest('DeleteDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_desktops_with_options(request, runtime)

    def delete_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeleteDirectoriesResponse().from_map(
            self.do_rpcrequest('DeleteDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    def delete_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeleteImagesResponse().from_map(
            self.do_rpcrequest('DeleteImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    def delete_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeletePolicyGroupsResponse().from_map(
            self.do_rpcrequest('DeletePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeleteSnapshotResponse().from_map(
            self.do_rpcrequest('DeleteSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DeleteVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('DeleteVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    def describe_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeBundlesResponse().from_map(
            self.do_rpcrequest('DescribeBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    def describe_client_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeClientEventsResponse().from_map(
            self.do_rpcrequest('DescribeClientEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_client_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

    def describe_desktop_policys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeDesktopPolicysResponse().from_map(
            self.do_rpcrequest('DescribeDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktop_policys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_policys_with_options(request, runtime)

    def describe_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeDesktopsResponse().from_map(
            self.do_rpcrequest('DescribeDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    def describe_desktop_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeDesktopTypesResponse().from_map(
            self.do_rpcrequest('DescribeDesktopTypes', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktop_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_types_with_options(request, runtime)

    def describe_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeDirectoriesResponse().from_map(
            self.do_rpcrequest('DescribeDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeImagesResponse().from_map(
            self.do_rpcrequest('DescribeImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def describe_invocations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeInvocationsResponse().from_map(
            self.do_rpcrequest('DescribeInvocations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    def describe_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribePolicyGroupsResponse().from_map(
            self.do_rpcrequest('DescribePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeSnapshotsResponse().from_map(
            self.do_rpcrequest('DescribeSnapshots', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_virtual_mfadevices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeVirtualMFADevicesResponse().from_map(
            self.do_rpcrequest('DescribeVirtualMFADevices', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_mfadevices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_mfadevices_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def do_check_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DoCheckResourceResponse().from_map(
            self.do_rpcrequest('DoCheckResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_check_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_check_resource_with_options(request, runtime)

    def do_logical_delete_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DoLogicalDeleteResourceResponse().from_map(
            self.do_rpcrequest('DoLogicalDeleteResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_logical_delete_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_logical_delete_resource_with_options(request, runtime)

    def do_physical_delete_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.DoPhysicalDeleteResourceResponse().from_map(
            self.do_rpcrequest('DoPhysicalDeleteResource', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_physical_delete_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_physical_delete_resource_with_options(request, runtime)

    def get_connection_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.GetConnectionTicketResponse().from_map(
            self.do_rpcrequest('GetConnectionTicket', '2020-09-30', 'HTTP', 'POST', 'AK', 'json', req, runtime)
        )

    def get_connection_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    def list_directory_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ListDirectoryUsersResponse().from_map(
            self.do_rpcrequest('ListDirectoryUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_directory_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def lock_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.LockVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('LockVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lock_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_virtual_mfadevice_with_options(request, runtime)

    def modify_adconnector_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyADConnectorDirectoryResponse().from_map(
            self.do_rpcrequest('ModifyADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_adconnector_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    def modify_desktop_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyDesktopNameResponse().from_map(
            self.do_rpcrequest('ModifyDesktopName', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_name_with_options(request, runtime)

    def modify_desktop_policys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyDesktopPolicysResponse().from_map(
            self.do_rpcrequest('ModifyDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_policys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_policys_with_options(request, runtime)

    def modify_desktops_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyDesktopsPolicyGroupResponse().from_map(
            self.do_rpcrequest('ModifyDesktopsPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktops_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    def modify_entitlement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyEntitlementResponse().from_map(
            self.do_rpcrequest('ModifyEntitlement', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_entitlement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyImageAttributeResponse().from_map(
            self.do_rpcrequest('ModifyImageAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ModifyPolicyGroupResponse().from_map(
            self.do_rpcrequest('ModifyPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    def pay_order_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.PayOrderCallbackResponse().from_map(
            self.do_rpcrequest('PayOrderCallback', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pay_order_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pay_order_callback_with_options(request, runtime)

    def reboot_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.RebootDesktopsResponse().from_map(
            self.do_rpcrequest('RebootDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    def renew_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.RenewDesktopsResponse().from_map(
            self.do_rpcrequest('RenewDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_desktops_with_options(request, runtime)

    def reset_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.ResetSnapshotResponse().from_map(
            self.do_rpcrequest('ResetSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    def run_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.RunCommandResponse().from_map(
            self.do_rpcrequest('RunCommand', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    def start_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.StartDesktopsResponse().from_map(
            self.do_rpcrequest('StartDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    def stop_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.StopDesktopsResponse().from_map(
            self.do_rpcrequest('StopDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    def stop_invocation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.StopInvocationResponse().from_map(
            self.do_rpcrequest('StopInvocation', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_invocation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unlock_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.UnlockVirtualMFADeviceResponse().from_map(
            self.do_rpcrequest('UnlockVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_virtual_mfadevice_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecd_20200930_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
