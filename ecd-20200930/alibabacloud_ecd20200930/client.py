# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

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

    def add_user_to_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToDesktopGroupResponse(),
            self.do_rpcrequest('AddUserToDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_user_to_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_desktop_group_with_options(request, runtime)

    def add_user_to_security_center_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToSecurityCenterWhiteListResponse(),
            self.do_rpcrequest('AddUserToSecurityCenterWhiteList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_user_to_security_center_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_security_center_white_list_with_options(request, runtime)

    def attach_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachCenResponse(),
            self.do_rpcrequest('AttachCen', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_with_options(request, runtime)

    def check_user_in_security_center_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CheckUserInSecurityCenterWhiteListResponse(),
            self.do_rpcrequest('CheckUserInSecurityCenterWhiteList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_user_in_security_center_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_user_in_security_center_white_list_with_options(request, runtime)

    def clone_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ClonePolicyGroupResponse(),
            self.do_rpcrequest('ClonePolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_policy_group_with_options(request, runtime)

    def create_adconnector_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorDirectoryResponse(),
            self.do_rpcrequest('CreateADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adconnector_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    def create_adconnector_office_site_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorOfficeSiteResponse(),
            self.do_rpcrequest('CreateADConnectorOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_adconnector_office_site(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_office_site_with_options(request, runtime)

    def create_bundle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateBundleResponse(),
            self.do_rpcrequest('CreateBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bundle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    def create_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopGroupResponse(),
            self.do_rpcrequest('CreateDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_desktop_group_with_options(request, runtime)

    def create_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsResponse(),
            self.do_rpcrequest('CreateDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    def create_desktops_lite_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsLiteResponse(),
            self.do_rpcrequest('CreateDesktopsLite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_desktops_lite(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_lite_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateImageResponse(),
            self.do_rpcrequest('CreateImage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_nasfile_system_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNASFileSystemResponse(),
            self.do_rpcrequest('CreateNASFileSystem', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nasfile_system(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_nasfile_system_with_options(request, runtime)

    def create_network_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNetworkPackageResponse(),
            self.do_rpcrequest('CreateNetworkPackage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_package_with_options(request, runtime)

    def create_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreatePolicyGroupResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.CreateRAMDirectoryResponse(),
            self.do_rpcrequest('CreateRAMDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ramdirectory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    def create_scale_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateScaleStrategyResponse(),
            self.do_rpcrequest('CreateScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scale_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scale_strategy_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def create_simple_office_site_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSimpleOfficeSiteResponse(),
            self.do_rpcrequest('CreateSimpleOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_simple_office_site(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_simple_office_site_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSnapshotResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DeleteBundlesResponse(),
            self.do_rpcrequest('DeleteBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    def delete_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopGroupResponse(),
            self.do_rpcrequest('DeleteDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_desktop_group_with_options(request, runtime)

    def delete_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopsResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDirectoriesResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DeleteImagesResponse(),
            self.do_rpcrequest('DeleteImages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    def delete_nasfile_systems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNASFileSystemsResponse(),
            self.do_rpcrequest('DeleteNASFileSystems', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nasfile_systems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nasfile_systems_with_options(request, runtime)

    def delete_network_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNetworkPackagesResponse(),
            self.do_rpcrequest('DeleteNetworkPackages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_packages_with_options(request, runtime)

    def delete_office_sites_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteOfficeSitesResponse(),
            self.do_rpcrequest('DeleteOfficeSites', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_office_sites(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_office_sites_with_options(request, runtime)

    def delete_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeletePolicyGroupsResponse(),
            self.do_rpcrequest('DeletePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    def delete_scale_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteScaleStrategyResponse(),
            self.do_rpcrequest('DeleteScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scale_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scale_strategy_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteSnapshotResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DeleteVirtualMFADeviceResponse(),
            self.do_rpcrequest('DeleteVirtualMFADevice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    def describe_alarm_event_stack_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAlarmEventStackInfoResponse(),
            self.do_rpcrequest('DescribeAlarmEventStackInfo', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarm_event_stack_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_stack_info_with_options(request, runtime)

    def describe_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeBundlesResponse(),
            self.do_rpcrequest('DescribeBundles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    def describe_cens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCensResponse(),
            self.do_rpcrequest('DescribeCens', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    def describe_client_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeClientEventsResponse(),
            self.do_rpcrequest('DescribeClientEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_client_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

    def describe_desktop_ids_by_vul_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse(),
            self.do_rpcrequest('DescribeDesktopIdsByVulNames', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktop_ids_by_vul_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_ids_by_vul_names_with_options(request, runtime)

    def describe_desktop_policys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopPolicysResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsResponse(),
            self.do_rpcrequest('DescribeDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    def describe_desktops_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsInGroupResponse(),
            self.do_rpcrequest('DescribeDesktopsInGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_desktops_in_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_in_group_with_options(request, runtime)

    def describe_desktop_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopTypesResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDirectoriesResponse(),
            self.do_rpcrequest('DescribeDirectories', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def describe_front_vul_patch_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFrontVulPatchListResponse(),
            self.do_rpcrequest('DescribeFrontVulPatchList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_front_vul_patch_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    def describe_grouped_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeGroupedVulResponse(),
            self.do_rpcrequest('DescribeGroupedVul', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grouped_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagesResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DescribeInvocationsResponse(),
            self.do_rpcrequest('DescribeInvocations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    def describe_modification_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeModificationPriceResponse(),
            self.do_rpcrequest('DescribeModificationPrice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_modification_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_modification_price_with_options(request, runtime)

    def describe_nasfile_systems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNASFileSystemsResponse(),
            self.do_rpcrequest('DescribeNASFileSystems', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_nasfile_systems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nasfile_systems_with_options(request, runtime)

    def describe_network_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNetworkPackagesResponse(),
            self.do_rpcrequest('DescribeNetworkPackages', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_packages_with_options(request, runtime)

    def describe_office_sites_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeOfficeSitesResponse(),
            self.do_rpcrequest('DescribeOfficeSites', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_office_sites(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_office_sites_with_options(request, runtime)

    def describe_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePolicyGroupsResponse(),
            self.do_rpcrequest('DescribePolicyGroups', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    def describe_post_paid_desktop_bills_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePostPaidDesktopBillsResponse(),
            self.do_rpcrequest('DescribePostPaidDesktopBills', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_post_paid_desktop_bills(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_post_paid_desktop_bills_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_scale_strategys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScaleStrategysResponse(),
            self.do_rpcrequest('DescribeScaleStrategys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scale_strategys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scale_strategys_with_options(request, runtime)

    def describe_scan_task_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScanTaskProgressResponse(),
            self.do_rpcrequest('DescribeScanTaskProgress', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scan_task_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    def describe_security_event_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationsResponse(),
            self.do_rpcrequest('DescribeSecurityEventOperations', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_event_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    def describe_security_event_operation_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationStatusResponse(),
            self.do_rpcrequest('DescribeSecurityEventOperationStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_event_operation_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSnapshotsResponse(),
            self.do_rpcrequest('DescribeSnapshots', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_susp_event_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventOverviewResponse(),
            self.do_rpcrequest('DescribeSuspEventOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_event_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_overview_with_options(request, runtime)

    def describe_susp_event_quara_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventQuaraFilesResponse(),
            self.do_rpcrequest('DescribeSuspEventQuaraFiles', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_event_quara_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    def describe_susp_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventsResponse(),
            self.do_rpcrequest('DescribeSuspEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_susp_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    def describe_user_connection_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserConnectionRecordsResponse(),
            self.do_rpcrequest('DescribeUserConnectionRecords', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_connection_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_connection_records_with_options(request, runtime)

    def describe_users_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersInGroupResponse(),
            self.do_rpcrequest('DescribeUsersInGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_users_in_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_users_in_group_with_options(request, runtime)

    def describe_virtual_mfadevices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVirtualMFADevicesResponse(),
            self.do_rpcrequest('DescribeVirtualMFADevices', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_mfadevices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_mfadevices_with_options(request, runtime)

    def describe_vul_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulDetailsResponse(),
            self.do_rpcrequest('DescribeVulDetails', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    def describe_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulListResponse(),
            self.do_rpcrequest('DescribeVulList', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    def describe_vul_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulOverviewResponse(),
            self.do_rpcrequest('DescribeVulOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_overview_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def detach_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachCenResponse(),
            self.do_rpcrequest('DetachCen', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_with_options(request, runtime)

    def do_check_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.DoCheckResourceResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DoLogicalDeleteResourceResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.DoPhysicalDeleteResourceResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.GetConnectionTicketResponse(),
            self.do_rpcrequest('GetConnectionTicket', '2020-09-30', 'HTTP', 'POST', 'AK', 'json', req, runtime)
        )

    def get_connection_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    def get_desktop_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopGroupDetailResponse(),
            self.do_rpcrequest('GetDesktopGroupDetail', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_desktop_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_desktop_group_detail_with_options(request, runtime)

    def get_desktop_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopUsersResponse(),
            self.do_rpcrequest('GetDesktopUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_desktop_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_desktop_users_with_options(request, runtime)

    def get_directory_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDirectorySsoStatusResponse(),
            self.do_rpcrequest('GetDirectorySsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_directory_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_directory_sso_status_with_options(request, runtime)

    def get_office_site_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetOfficeSiteSsoStatusResponse(),
            self.do_rpcrequest('GetOfficeSiteSsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_office_site_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_office_site_sso_status_with_options(request, runtime)

    def get_sp_metadata_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetSpMetadataResponse(),
            self.do_rpcrequest('GetSpMetadata', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sp_metadata(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sp_metadata_with_options(request, runtime)

    def handle_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.HandleSecurityEventsResponse(),
            self.do_rpcrequest('HandleSecurityEvents', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def handle_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    def list_directory_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListDirectoryUsersResponse(),
            self.do_rpcrequest('ListDirectoryUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_directory_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    def list_office_site_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteOverviewResponse(),
            self.do_rpcrequest('ListOfficeSiteOverview', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_office_site_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_overview_with_options(request, runtime)

    def list_office_site_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteUsersResponse(),
            self.do_rpcrequest('ListOfficeSiteUsers', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_office_site_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_users_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListTagResourcesResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.LockVirtualMFADeviceResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorDirectoryResponse(),
            self.do_rpcrequest('ModifyADConnectorDirectory', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_adconnector_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    def modify_adconnector_office_site_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorOfficeSiteResponse(),
            self.do_rpcrequest('ModifyADConnectorOfficeSite', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_adconnector_office_site(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_office_site_with_options(request, runtime)

    def modify_bundle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyBundleResponse(),
            self.do_rpcrequest('ModifyBundle', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bundle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_bundle_with_options(request, runtime)

    def modify_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopGroupResponse(),
            self.do_rpcrequest('ModifyDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_group_with_options(request, runtime)

    def modify_desktop_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopNameResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopPolicysResponse(),
            self.do_rpcrequest('ModifyDesktopPolicys', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_policys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_policys_with_options(request, runtime)

    def modify_desktop_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopSpecResponse(),
            self.do_rpcrequest('ModifyDesktopSpec', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_desktop_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_spec_with_options(request, runtime)

    def modify_desktops_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopsPolicyGroupResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.ModifyEntitlementResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImageAttributeResponse(),
            self.do_rpcrequest('ModifyImageAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_nasdefault_mount_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNASDefaultMountTargetResponse(),
            self.do_rpcrequest('ModifyNASDefaultMountTarget', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_nasdefault_mount_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_nasdefault_mount_target_with_options(request, runtime)

    def modify_network_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageResponse(),
            self.do_rpcrequest('ModifyNetworkPackage', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_with_options(request, runtime)

    def modify_network_package_enabled_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageEnabledResponse(),
            self.do_rpcrequest('ModifyNetworkPackageEnabled', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_package_enabled(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_enabled_with_options(request, runtime)

    def modify_office_site_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteAttributeResponse(),
            self.do_rpcrequest('ModifyOfficeSiteAttribute', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_office_site_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_attribute_with_options(request, runtime)

    def modify_office_site_cross_desktop_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse(),
            self.do_rpcrequest('ModifyOfficeSiteCrossDesktopAccess', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_office_site_cross_desktop_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_cross_desktop_access_with_options(request, runtime)

    def modify_office_site_mfa_enabled_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse(),
            self.do_rpcrequest('ModifyOfficeSiteMfaEnabled', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_office_site_mfa_enabled(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_mfa_enabled_with_options(request, runtime)

    def modify_operate_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOperateVulResponse(),
            self.do_rpcrequest('ModifyOperateVul', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_operate_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    def modify_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyPolicyGroupResponse(),
            self.do_rpcrequest('ModifyPolicyGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    def modify_scale_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyScaleStrategyResponse(),
            self.do_rpcrequest('ModifyScaleStrategy', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scale_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scale_strategy_with_options(request, runtime)

    def modify_user_to_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserToDesktopGroupResponse(),
            self.do_rpcrequest('ModifyUserToDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_to_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_to_desktop_group_with_options(request, runtime)

    def operate_vuls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.OperateVulsResponse(),
            self.do_rpcrequest('OperateVuls', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def operate_vuls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    def pay_order_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.PayOrderCallbackResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.RebootDesktopsResponse(),
            self.do_rpcrequest('RebootDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    def rebuild_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebuildDesktopsResponse(),
            self.do_rpcrequest('RebuildDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rebuild_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebuild_desktops_with_options(request, runtime)

    def recreate_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RecreateDesktopGroupResponse(),
            self.do_rpcrequest('RecreateDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recreate_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recreate_desktop_group_with_options(request, runtime)

    def remove_user_from_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveUserFromDesktopGroupResponse(),
            self.do_rpcrequest('RemoveUserFromDesktopGroup', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_user_from_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_desktop_group_with_options(request, runtime)

    def renew_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewDesktopsResponse(),
            self.do_rpcrequest('RenewDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_desktops_with_options(request, runtime)

    def reset_nasdefault_mount_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetNASDefaultMountTargetResponse(),
            self.do_rpcrequest('ResetNASDefaultMountTarget', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_nasdefault_mount_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_nasdefault_mount_target_with_options(request, runtime)

    def reset_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetSnapshotResponse(),
            self.do_rpcrequest('ResetSnapshot', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    def rollback_susp_event_quara_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RollbackSuspEventQuaraFileResponse(),
            self.do_rpcrequest('RollbackSuspEventQuaraFile', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_susp_event_quara_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    def run_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.RunCommandResponse(),
            self.do_rpcrequest('RunCommand', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    def set_directory_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDirectorySsoStatusResponse(),
            self.do_rpcrequest('SetDirectorySsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_directory_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_directory_sso_status_with_options(request, runtime)

    def set_idp_metadata_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetIdpMetadataResponse(),
            self.do_rpcrequest('SetIdpMetadata', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_idp_metadata(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_idp_metadata_with_options(request, runtime)

    def set_office_site_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetOfficeSiteSsoStatusResponse(),
            self.do_rpcrequest('SetOfficeSiteSsoStatus', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_office_site_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_office_site_sso_status_with_options(request, runtime)

    def start_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartDesktopsResponse(),
            self.do_rpcrequest('StartDesktops', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    def start_virus_scan_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartVirusScanTaskResponse(),
            self.do_rpcrequest('StartVirusScanTask', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_virus_scan_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    def stop_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopDesktopsResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.StopInvocationResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.TagResourcesResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.UnlockVirtualMFADeviceResponse(),
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
        return TeaCore.from_map(
            ecd_20200930_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
