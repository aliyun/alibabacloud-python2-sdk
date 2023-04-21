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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def activate_office_site_with_options(self, request, runtime):
        """
        To improve resource utilization, the system automatically locks a workspace of the convenience account type to release virtual private cloud (VPC) resources, and the workspace has been no longer used for a long time. If you want to continue using the locked workspace, you can call this operation to activate it. When you activate the locked workspace, the system recreates VPC resources based on the original configurations.
        

        @param request: ActivateOfficeSiteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ActivateOfficeSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ActivateOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    def activate_office_site(self, request):
        """
        To improve resource utilization, the system automatically locks a workspace of the convenience account type to release virtual private cloud (VPC) resources, and the workspace has been no longer used for a long time. If you want to continue using the locked workspace, you can call this operation to activate it. When you activate the locked workspace, the system recreates VPC resources based on the original configurations.
        

        @param request: ActivateOfficeSiteRequest

        @return: ActivateOfficeSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_office_site_with_options(request, runtime)

    def add_devices_with_options(self, request, runtime):
        """
        You can add only one device to a tenant.
        

        @param request: AddDevicesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_ids):
            query['DeviceIds'] = request.device_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDevices',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_devices(self, request):
        """
        You can add only one device to a tenant.
        

        @param request: AddDevicesRequest

        @return: AddDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_devices_with_options(request, runtime)

    def add_file_permission_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ecd_20200930_models.AddFilePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_list):
            request.member_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFilePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddFilePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def add_file_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_file_permission_with_options(request, runtime)

    def add_user_to_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_ids):
            query['DesktopGroupIds'] = request.desktop_group_ids
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user_to_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_desktop_group_with_options(request, runtime)

    def apply_auto_snapshot_policy_with_options(self, request, runtime):
        """
        You can also associate an automatic snapshot policy with a cloud desktop in the Elastic Desktop Service (EDS) console. To do so, perform the following steps: 1. Log on to the EDS console. 2. Choose Desktops and Groups > Desktops in the left-side navigation pane. 3. Find the cloud desktop that you want to manage on the Cloud Desktops page and choose More > Change Automatic Snapshot Policy in the Actions column. 4. Configure a policy for the cloud desktop as prompted in the Change Automatic Snapshot Policy panel.
        After you associate an automatic snapshot policy with the cloud desktop, the system creates snapshots for the cloud desktop based on the policy.
        

        @param request: ApplyAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApplyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_auto_snapshot_policy(self, request):
        """
        You can also associate an automatic snapshot policy with a cloud desktop in the Elastic Desktop Service (EDS) console. To do so, perform the following steps: 1. Log on to the EDS console. 2. Choose Desktops and Groups > Desktops in the left-side navigation pane. 3. Find the cloud desktop that you want to manage on the Cloud Desktops page and choose More > Change Automatic Snapshot Policy in the Actions column. 4. Configure a policy for the cloud desktop as prompted in the Change Automatic Snapshot Policy panel.
        After you associate an automatic snapshot policy with the cloud desktop, the system creates snapshots for the cloud desktop based on the policy.
        

        @param request: ApplyAutoSnapshotPolicyRequest

        @return: ApplyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    def apply_coordinate_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_id):
            query['CoId'] = request.co_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCoordinatePrivilege',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApplyCoordinatePrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_coordinate_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_coordinate_privilege_with_options(request, runtime)

    def apply_coordination_for_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coordinate_policy_type):
            query['CoordinatePolicyType'] = request.coordinate_policy_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.initiator_type):
            query['InitiatorType'] = request.initiator_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_candidates):
            query['ResourceCandidates'] = request.resource_candidates
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationForMonitoring',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApplyCoordinationForMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_coordination_for_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_coordination_for_monitoring_with_options(request, runtime)

    def approve_fota_update_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveFotaUpdate',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApproveFotaUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    def approve_fota_update(self, request):
        runtime = util_models.RuntimeOptions()
        return self.approve_fota_update_with_options(request, runtime)

    def associate_network_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AssociateNetworkPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_network_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_network_package_with_options(request, runtime)

    def attach_cen_with_options(self, request, runtime):
        """
        ## Description
        *   A Cloud Enterprise Network (CEN) instance is created.
        *   A workspace of the convenience account type is created.
        >  The secure office network of a workspace of the enterprise Active Directory (AD) account type is attached to a CEN instance when you create the workspace. The secure office network that corresponds to each workspace can be attached only to a single CEN instance.
        

        @param request: AttachCenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachCenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachCenResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_cen(self, request):
        """
        ## Description
        *   A Cloud Enterprise Network (CEN) instance is created.
        *   A workspace of the convenience account type is created.
        >  The secure office network of a workspace of the enterprise Active Directory (AD) account type is attached to a CEN instance when you create the workspace. The secure office network that corresponds to each workspace can be attached only to a single CEN instance.
        

        @param request: AttachCenRequest

        @return: AttachCenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_with_options(request, runtime)

    def attach_end_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEndUser',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_end_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_end_user_with_options(request, runtime)

    def cancel_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    def cancel_cds_file_share_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.share_id):
            query['ShareId'] = request.share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCdsFileShareLink',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCdsFileShareLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_cds_file_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_cds_file_share_link_with_options(request, runtime)

    def cancel_coordination_for_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_ids):
            query['CoIds'] = request.co_ids
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCoordinationForMonitoring',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCoordinationForMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_coordination_for_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_coordination_for_monitoring_with_options(request, runtime)

    def cancel_copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCopyImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_copy_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_copy_image_with_options(request, runtime)

    def clone_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClonePolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ClonePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_policy_group_with_options(request, runtime)

    def complete_cds_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.upload_id):
            query['UploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteCdsFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CompleteCdsFileResponse(),
            self.call_api(params, req, runtime)
        )

    def complete_cds_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_cds_file_with_options(request, runtime)

    def config_adconnector_trust_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.rds_license_domain):
            query['RdsLicenseDomain'] = request.rds_license_domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trust_key):
            query['TrustKey'] = request.trust_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigADConnectorTrust',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ConfigADConnectorTrustResponse(),
            self.call_api(params, req, runtime)
        )

    def config_adconnector_trust(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_adconnector_trust_with_options(request, runtime)

    def config_adconnector_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigADConnectorUser',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ConfigADConnectorUserResponse(),
            self.call_api(params, req, runtime)
        )

    def config_adconnector_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_adconnector_user_with_options(request, runtime)

    def copy_cds_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_rename):
            query['AutoRename'] = request.auto_rename
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCdsFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CopyCdsFileResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_cds_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_cds_file_with_options(request, runtime)

    def copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_description):
            query['DestinationDescription'] = request.destination_description
        if not UtilClient.is_unset(request.destination_image_name):
            query['DestinationImageName'] = request.destination_image_name
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    def create_adconnector_directory_with_options(self, request, runtime):
        """
        AD directories are used to connect to enterprise AD systems and are suitable for large-scale desktop deployments. You are charged for AD directories that are used to connect to enterprise AD systems. For more information, see [Billing overview](~~188395~~).
        

        @param request: CreateADConnectorDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateADConnectorDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateADConnectorDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_adconnector_directory(self, request):
        """
        AD directories are used to connect to enterprise AD systems and are suitable for large-scale desktop deployments. You are charged for AD directories that are used to connect to enterprise AD systems. For more information, see [Billing overview](~~188395~~).
        

        @param request: CreateADConnectorDirectoryRequest

        @return: CreateADConnectorDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    def create_adconnector_office_site_with_options(self, request, runtime):
        """
        - When you create a workspace of the enterprise Active Directory (AD) account type, AD connectors are automatically created for you to connect to enterprise AD systems. You are charged for the AD connectors. For more information, see [Billing overview](~~188395~~).
        - After you call this operation to create the AD workspace, you must configure the AD domain. To configure the AD domain, perform the following operations:
        1. Configure the conditional forwarder in the Domain Name System (DNS) server.
        2. Configure the trust relationship in the AD domain server, and call the [ConfigADConnectorTrust](~~311258~~) operation to configure the trust relationship for the AD workspace.
        3. Call the [ListUserAdOrganizationUnits](~~311259~~) operation to obtain the organizational unit (OU) details of the AD domain. Then, call the [ConfigADConnectorUser](~~311262~~) operation to specify an OU and an administrator for the AD workspace.
        > If you specify the DomainUserName and DomainPassword parameters when you create the AD workspace, you need to configure only the conditional forwarder. If you do not specify the DomainUserName and DomainPassword parameters, you need to configure the conditional forwarder, trust relationship, and OU.
        For more information, see [Create a workspace of the enterprise account type](~~214469~~).
        

        @param request: CreateADConnectorOfficeSiteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateADConnectorOfficeSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateADConnectorOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_adconnector_office_site(self, request):
        """
        - When you create a workspace of the enterprise Active Directory (AD) account type, AD connectors are automatically created for you to connect to enterprise AD systems. You are charged for the AD connectors. For more information, see [Billing overview](~~188395~~).
        - After you call this operation to create the AD workspace, you must configure the AD domain. To configure the AD domain, perform the following operations:
        1. Configure the conditional forwarder in the Domain Name System (DNS) server.
        2. Configure the trust relationship in the AD domain server, and call the [ConfigADConnectorTrust](~~311258~~) operation to configure the trust relationship for the AD workspace.
        3. Call the [ListUserAdOrganizationUnits](~~311259~~) operation to obtain the organizational unit (OU) details of the AD domain. Then, call the [ConfigADConnectorUser](~~311262~~) operation to specify an OU and an administrator for the AD workspace.
        > If you specify the DomainUserName and DomainPassword parameters when you create the AD workspace, you need to configure only the conditional forwarder. If you do not specify the DomainUserName and DomainPassword parameters, you need to configure the conditional forwarder, trust relationship, and OU.
        For more information, see [Create a workspace of the enterprise account type](~~214469~~).
        

        @param request: CreateADConnectorOfficeSiteRequest

        @return: CreateADConnectorOfficeSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_office_site_with_options(request, runtime)

    def create_and_bind_nas_file_system_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.file_system_name):
            query['FileSystemName'] = request.file_system_name
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndBindNasFileSystem',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateAndBindNasFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_and_bind_nas_file_system(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_and_bind_nas_file_system_with_options(request, runtime)

    def create_auto_snapshot_policy_with_options(self, request, runtime):
        """
        You can call the operation to create an automatic snapshot policy based on a CRON expression. Then, the system automatically creates snapshots of a cloud desktop based on the policy.
        

        @param request: CreateAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auto_snapshot_policy(self, request):
        """
        You can call the operation to create an automatic snapshot policy based on a CRON expression. Then, the system automatically creates snapshots of a cloud desktop based on the policy.
        

        @param request: CreateAutoSnapshotPolicyRequest

        @return: CreateAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    def create_bundle_with_options(self, request, runtime):
        """
        ## Description
        Desktop templates are categorized into system templates and custom templates. System templates are the templates provided by Alibaba Cloud. You can call this operation to create a custom template.
        

        @param request: CreateBundleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBundleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_name):
            query['BundleName'] = request.bundle_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_performance_level):
            query['RootDiskPerformanceLevel'] = request.root_disk_performance_level
        if not UtilClient.is_unset(request.root_disk_size_gib):
            query['RootDiskSizeGib'] = request.root_disk_size_gib
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_size_gib):
            query['UserDiskSizeGib'] = request.user_disk_size_gib
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBundle',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateBundleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_bundle(self, request):
        """
        ## Description
        Desktop templates are categorized into system templates and custom templates. System templates are the templates provided by Alibaba Cloud. You can call this operation to create a custom template.
        

        @param request: CreateBundleRequest

        @return: CreateBundleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    def create_cds_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_hash):
            query['FileHash'] = request.file_hash
        if not UtilClient.is_unset(request.file_length):
            query['FileLength'] = request.file_length
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.parent_file_id):
            query['ParentFileId'] = request.parent_file_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdsFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateCdsFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cds_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cds_file_with_options(request, runtime)

    def create_cds_file_share_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            query['DisableDownload'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            query['DisablePreview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            query['DisableSave'] = request.disable_save
        if not UtilClient.is_unset(request.download_limit):
            query['DownloadLimit'] = request.download_limit
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.preview_limit):
            query['PreviewLimit'] = request.preview_limit
        if not UtilClient.is_unset(request.save_limit):
            query['SaveLimit'] = request.save_limit
        if not UtilClient.is_unset(request.share_name):
            query['ShareName'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            query['SharePwd'] = request.share_pwd
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdsFileShareLink',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateCdsFileShareLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cds_file_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cds_file_share_link_with_options(request, runtime)

    def create_desktop_group_with_options(self, request, runtime):
        """
        # Description
        Before you call this operation to create a desktop group, make sure that the following operations are complete:
        *   You are familiar with the features, usage limits, and scaling policies of desktop groups. For more information, see [Overview](~~290959~~) of desktop groups.
        *   Resources, such as workspaces, users, desktop templates, and policies, are created.
        

        @param request: CreateDesktopGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDesktopGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_classify_users):
            query['AllClassifyUsers'] = request.all_classify_users
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.buy_desktops_count):
            query['BuyDesktopsCount'] = request.buy_desktops_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.connect_duration):
            query['ConnectDuration'] = request.connect_duration
        if not UtilClient.is_unset(request.default_init_desktop_count):
            query['DefaultInitDesktopCount'] = request.default_init_desktop_count
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.group_version):
            query['GroupVersion'] = request.group_version
        if not UtilClient.is_unset(request.idle_disconnect_duration):
            query['IdleDisconnectDuration'] = request.idle_disconnect_duration
        if not UtilClient.is_unset(request.keep_duration):
            query['KeepDuration'] = request.keep_duration
        if not UtilClient.is_unset(request.load_policy):
            query['LoadPolicy'] = request.load_policy
        if not UtilClient.is_unset(request.max_desktops_count):
            query['MaxDesktopsCount'] = request.max_desktops_count
        if not UtilClient.is_unset(request.min_desktops_count):
            query['MinDesktopsCount'] = request.min_desktops_count
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.own_type):
            query['OwnType'] = request.own_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.profile_follow_switch):
            query['ProfileFollowSwitch'] = request.profile_follow_switch
        if not UtilClient.is_unset(request.ratio_threshold):
            query['RatioThreshold'] = request.ratio_threshold
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.scale_strategy_id):
            query['ScaleStrategyId'] = request.scale_strategy_id
        if not UtilClient.is_unset(request.stop_duration):
            query['StopDuration'] = request.stop_duration
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        if not UtilClient.is_unset(request.volume_encryption_key):
            query['VolumeEncryptionKey'] = request.volume_encryption_key
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_desktop_group(self, request):
        """
        # Description
        Before you call this operation to create a desktop group, make sure that the following operations are complete:
        *   You are familiar with the features, usage limits, and scaling policies of desktop groups. For more information, see [Overview](~~290959~~) of desktop groups.
        *   Resources, such as workspaces, users, desktop templates, and policies, are created.
        

        @param request: CreateDesktopGroupRequest

        @return: CreateDesktopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_desktop_group_with_options(request, runtime)

    def create_desktops_with_options(self, request, runtime):
        """
        1\\. Before you create a cloud desktop in Elastic Desktop Service (EDS), make sure that the following operations are complete:
        *   A workspace and a user are created. For more information, see the following topics:
        *   Create a workspace of the convenience account type and a convenience user: [CreateSimpleOfficeSite](~~215416~~) and [Create a convenience user](~~214472~~)
        *   Create a workspace of the enterprise Active Directory (AD) account type and an enterprise AD user: [CreateADConnectorOfficeSite](~~215417~~) and [Create an enterprise AD user](~~188619~~)
        *   A cloud desktop template is created by calling the [CreateBundle](~~188883~~) operation, or an existing cloud desktop template is used.
        *   A policy is created by calling the [CreatePolicyGroup](~~188889~~) operation, or an existing policy is used.
        2\\. A custom command script that can be automatically executed after you create the cloud desktop is prepared. You can customize a command script by using the UserCommands parameter.
        

        @param request: CreateDesktopsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_models):
            query['BundleModels'] = request.bundle_models
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_name_suffix):
            query['DesktopNameSuffix'] = request.desktop_name_suffix
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_assign_mode):
            query['UserAssignMode'] = request.user_assign_mode
        if not UtilClient.is_unset(request.user_commands):
            query['UserCommands'] = request.user_commands
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        if not UtilClient.is_unset(request.volume_encryption_key):
            query['VolumeEncryptionKey'] = request.volume_encryption_key
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_desktops(self, request):
        """
        1\\. Before you create a cloud desktop in Elastic Desktop Service (EDS), make sure that the following operations are complete:
        *   A workspace and a user are created. For more information, see the following topics:
        *   Create a workspace of the convenience account type and a convenience user: [CreateSimpleOfficeSite](~~215416~~) and [Create a convenience user](~~214472~~)
        *   Create a workspace of the enterprise Active Directory (AD) account type and an enterprise AD user: [CreateADConnectorOfficeSite](~~215417~~) and [Create an enterprise AD user](~~188619~~)
        *   A cloud desktop template is created by calling the [CreateBundle](~~188883~~) operation, or an existing cloud desktop template is used.
        *   A policy is created by calling the [CreatePolicyGroup](~~188889~~) operation, or an existing policy is used.
        2\\. A custom command script that can be automatically executed after you create the cloud desktop is prepared. You can customize a command script by using the UserCommands parameter.
        

        @param request: CreateDesktopsRequest

        @return: CreateDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    def create_disk_encryption_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskEncryptionService',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDiskEncryptionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_disk_encryption_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disk_encryption_service_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_clean_userdata):
            query['AutoCleanUserdata'] = request.auto_clean_userdata
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_resource_type):
            query['ImageResourceType'] = request.image_resource_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateImageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_nasfile_system_with_options(self, request, runtime):
        """
        You can create a NAS file system for each standard workspace so that cloud desktops within the workspace can share files.
        *   The system creates a General-purpose NAS file system and generates a default mount target. The storage types of the NAS file system includes Capacity type and Performance type. The Capacity type provides 10 PiB of storage while the Performance type provides only 1 PiB of storage.
        *   NAS file systems are billed on a pay-as-you-go basis. You are charged based on the amount of used storage. You can also purchase resource plans to offset the storage fees of the NAS file systems.
        For more information, see [Create a NAS file system](~~214481~~).
        

        @param request: CreateNASFileSystemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNASFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNASFileSystem',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNASFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_nasfile_system(self, request):
        """
        You can create a NAS file system for each standard workspace so that cloud desktops within the workspace can share files.
        *   The system creates a General-purpose NAS file system and generates a default mount target. The storage types of the NAS file system includes Capacity type and Performance type. The Capacity type provides 10 PiB of storage while the Performance type provides only 1 PiB of storage.
        *   NAS file systems are billed on a pay-as-you-go basis. You are charged based on the amount of used storage. You can also purchase resource plans to offset the storage fees of the NAS file systems.
        For more information, see [Create a NAS file system](~~214481~~).
        

        @param request: CreateNASFileSystemRequest

        @return: CreateNASFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_nasfile_system_with_options(request, runtime)

    def create_network_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNetworkPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_network_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_package_with_options(request, runtime)

    def create_policy_group_with_options(self, request, runtime):
        """
        A policy is a set of security rules that are used to control security configurations when end users use cloud desktops. A policy contains basic features, such as USB redirection and watermarking, and other features, such as security group control. For more information, see [Policy overview](~~189345~~).
        

        @param request: CreatePolicyGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePolicyGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_content_protection):
            query['AppContentProtection'] = request.app_content_protection
        if not UtilClient.is_unset(request.authorize_access_policy_rule):
            query['AuthorizeAccessPolicyRule'] = request.authorize_access_policy_rule
        if not UtilClient.is_unset(request.authorize_security_policy_rule):
            query['AuthorizeSecurityPolicyRule'] = request.authorize_security_policy_rule
        if not UtilClient.is_unset(request.camera_redirect):
            query['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.end_user_apply_admin_coordinate):
            query['EndUserApplyAdminCoordinate'] = request.end_user_apply_admin_coordinate
        if not UtilClient.is_unset(request.end_user_group_coordinate):
            query['EndUserGroupCoordinate'] = request.end_user_group_coordinate
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.internet_communication_protocol):
            query['InternetCommunicationProtocol'] = request.internet_communication_protocol
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_redirect):
            query['NetRedirect'] = request.net_redirect
        if not UtilClient.is_unset(request.preempt_login):
            query['PreemptLogin'] = request.preempt_login
        if not UtilClient.is_unset(request.preempt_login_user):
            query['PreemptLoginUser'] = request.preempt_login_user
        if not UtilClient.is_unset(request.printer_redirection):
            query['PrinterRedirection'] = request.printer_redirection
        if not UtilClient.is_unset(request.record_content):
            query['RecordContent'] = request.record_content
        if not UtilClient.is_unset(request.record_content_expires):
            query['RecordContentExpires'] = request.record_content_expires
        if not UtilClient.is_unset(request.recording):
            query['Recording'] = request.recording
        if not UtilClient.is_unset(request.recording_audio):
            query['RecordingAudio'] = request.recording_audio
        if not UtilClient.is_unset(request.recording_duration):
            query['RecordingDuration'] = request.recording_duration
        if not UtilClient.is_unset(request.recording_end_time):
            query['RecordingEndTime'] = request.recording_end_time
        if not UtilClient.is_unset(request.recording_expires):
            query['RecordingExpires'] = request.recording_expires
        if not UtilClient.is_unset(request.recording_fps):
            query['RecordingFps'] = request.recording_fps
        if not UtilClient.is_unset(request.recording_start_time):
            query['RecordingStartTime'] = request.recording_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_coordinate):
            query['RemoteCoordinate'] = request.remote_coordinate
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.video_redirect):
            query['VideoRedirect'] = request.video_redirect
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_color):
            query['WatermarkColor'] = request.watermark_color
        if not UtilClient.is_unset(request.watermark_degree):
            query['WatermarkDegree'] = request.watermark_degree
        if not UtilClient.is_unset(request.watermark_font_size):
            query['WatermarkFontSize'] = request.watermark_font_size
        if not UtilClient.is_unset(request.watermark_font_style):
            query['WatermarkFontStyle'] = request.watermark_font_style
        if not UtilClient.is_unset(request.watermark_row_amount):
            query['WatermarkRowAmount'] = request.watermark_row_amount
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
        if not UtilClient.is_unset(request.watermark_transparency_value):
            query['WatermarkTransparencyValue'] = request.watermark_transparency_value
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreatePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_policy_group(self, request):
        """
        A policy is a set of security rules that are used to control security configurations when end users use cloud desktops. A policy contains basic features, such as USB redirection and watermarking, and other features, such as security group control. For more information, see [Policy overview](~~189345~~).
        

        @param request: CreatePolicyGroupRequest

        @return: CreatePolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    def create_ramdirectory_with_options(self, request, runtime):
        """
        Before you create a RAM directory, make sure that you have completed the following operations:
        *   You have created a virtual private cloud (VPC) by calling the [CreateVpc](~~35737~~) operation in a region where EDS is available.
        *   You have created a vSwitch in the VPC by calling the [CreateVSwitch](~~35745~~) operation, and the vSwitch resides in a zone where EDS is available.
        

        @param request: CreateRAMDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRAMDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRAMDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateRAMDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ramdirectory(self, request):
        """
        Before you create a RAM directory, make sure that you have completed the following operations:
        *   You have created a virtual private cloud (VPC) by calling the [CreateVpc](~~35737~~) operation in a region where EDS is available.
        *   You have created a vSwitch in the VPC by calling the [CreateVSwitch](~~35745~~) operation, and the vSwitch resides in a zone where EDS is available.
        

        @param request: CreateRAMDirectoryRequest

        @return: CreateRAMDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    def create_simple_office_site_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.cloud_box_office_site):
            query['CloudBoxOfficeSite'] = request.cloud_box_office_site
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.need_verify_zero_device):
            query['NeedVerifyZeroDevice'] = request.need_verify_zero_device
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimpleOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSimpleOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_simple_office_site(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_simple_office_site_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        """
        The cloud desktop for which you want to create a snapshot must be in the *Running** state or **Stopped** state.
        

        @param request: CreateSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_snapshot(self, request):
        """
        The cloud desktop for which you want to create a snapshot must be in the *Running** state or **Stopped** state.
        

        @param request: CreateSnapshotRequest

        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def delete_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    def delete_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBundles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteBundlesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    def delete_cds_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCdsFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteCdsFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cds_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cds_file_with_options(request, runtime)

    def delete_cloud_drive_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudDriveGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteCloudDriveGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cloud_drive_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_drive_groups_with_options(request, runtime)

    def delete_cloud_drive_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudDriveUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteCloudDriveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cloud_drive_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_drive_users_with_options(request, runtime)

    def delete_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_desktop_group_with_options(request, runtime)

    def delete_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_desktops_with_options(request, runtime)

    def delete_devices_with_options(self, request, runtime):
        """
        You can call the operation to manage client devices.
        

        @param request: DeleteDevicesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_ids):
            query['DeviceIds'] = request.device_ids
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_devices(self, request):
        """
        You can call the operation to manage client devices.
        

        @param request: DeleteDevicesRequest

        @return: DeleteDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_devices_with_options(request, runtime)

    def delete_directories_with_options(self, request, runtime):
        """
        You cannot delete directories that are in use by cloud desktops.
        

        @param request: DeleteDirectoriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_directories(self, request):
        """
        You cannot delete directories that are in use by cloud desktops.
        

        @param request: DeleteDirectoriesRequest

        @return: DeleteDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    def delete_images_with_options(self, request, runtime):
        """
        ## Description
        *   Images include system images and custom images. System images cannot be deleted.
        *   If an image to delete is used by a desktop bundle, call the [DeleteBundles](~~188885~~) operation to delete the desktop bundle.
        

        @param request: DeleteImagesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_cascaded_bundle):
            query['DeleteCascadedBundle'] = request.delete_cascaded_bundle
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_images(self, request):
        """
        ## Description
        *   Images include system images and custom images. System images cannot be deleted.
        *   If an image to delete is used by a desktop bundle, call the [DeleteBundles](~~188885~~) operation to delete the desktop bundle.
        

        @param request: DeleteImagesRequest

        @return: DeleteImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    def delete_nasfile_systems_with_options(self, request, runtime):
        """
        ## Description
        Before you delete a NAS file system, make sure that the data you want to retain is backed up.
        >  If a NAS file system is deleted, data stored in the NAS file system cannot be restored. Proceed with caution when you delete NAS file systems.
        

        @param request: DeleteNASFileSystemsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNASFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNASFileSystems',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNASFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nasfile_systems(self, request):
        """
        ## Description
        Before you delete a NAS file system, make sure that the data you want to retain is backed up.
        >  If a NAS file system is deleted, data stored in the NAS file system cannot be restored. Proceed with caution when you delete NAS file systems.
        

        @param request: DeleteNASFileSystemsRequest

        @return: DeleteNASFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nasfile_systems_with_options(request, runtime)

    def delete_network_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNetworkPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_network_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_packages_with_options(request, runtime)

    def delete_office_sites_with_options(self, request, runtime):
        """
        Before you delete a workspace, make sure that the following operations are complete:
        *   All cloud desktops in the workspace are released.
        *   The data that you want to retain is backed up.
        >  After a workspace is deleted, its resources and data cannot be restored. Proceed with caution.
        

        @param request: DeleteOfficeSitesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteOfficeSitesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOfficeSites',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteOfficeSitesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_office_sites(self, request):
        """
        Before you delete a workspace, make sure that the following operations are complete:
        *   All cloud desktops in the workspace are released.
        *   The data that you want to retain is backed up.
        >  After a workspace is deleted, its resources and data cannot be restored. Proceed with caution.
        

        @param request: DeleteOfficeSitesRequest

        @return: DeleteOfficeSitesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_office_sites_with_options(request, runtime)

    def delete_policy_groups_with_options(self, request, runtime):
        """
        System policies cannot be deleted.
        *   Custom policies that are associated with cloud desktops cannot be deleted.
        

        @param request: DeletePolicyGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePolicyGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeletePolicyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_policy_groups(self, request):
        """
        System policies cannot be deleted.
        *   Custom policies that are associated with cloud desktops cannot be deleted.
        

        @param request: DeletePolicyGroupsRequest

        @return: DeletePolicyGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        """
        If the IDs of the snapshots that you specify do not exist, requests are ignored.
        

        @param request: DeleteSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot(self, request):
        """
        If the IDs of the snapshots that you specify do not exist, requests are ignored.
        

        @param request: DeleteSnapshotRequest

        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_virtual_mfadevice_with_options(self, request, runtime):
        """
        ## Description
        If an MFA device is deleted, the device is unbound, reset, and disabled. When the Active Directory (AD) user wants to log on to the cloud desktop, the AD user must bind a new MFA device.
        

        @param request: DeleteVirtualMFADeviceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVirtualMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_virtual_mfadevice(self, request):
        """
        ## Description
        If an MFA device is deleted, the device is unbound, reset, and disabled. When the Active Directory (AD) user wants to log on to the cloud desktop, the AD user must bind a new MFA device.
        

        @param request: DeleteVirtualMFADeviceRequest

        @return: DeleteVirtualMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    def describe_alarm_event_stack_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventStackInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAlarmEventStackInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alarm_event_stack_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_stack_info_with_options(request, runtime)

    def describe_auto_snapshot_policy_with_options(self, request, runtime):
        """
        You can view an automatic snapshot policy that is associated with a cloud desktop in the Elastic Desktop Service (EDS) console. To view the automatic snapshot policy, you can go to the EDS console, choose Deployment > Snapshots in the left-side navigation pane, and then view an automatic snapshot policy on the Snapshots page.
        

        @param request: DescribeAutoSnapshotPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotPolicy',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_snapshot_policy(self, request):
        """
        You can view an automatic snapshot policy that is associated with a cloud desktop in the Elastic Desktop Service (EDS) console. To view the automatic snapshot policy, you can go to the EDS console, choose Deployment > Snapshots in the left-side navigation pane, and then view an automatic snapshot policy on the Snapshots page.
        

        @param request: DescribeAutoSnapshotPolicyRequest

        @return: DescribeAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policy_with_options(request, runtime)

    def describe_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_type):
            query['BundleType'] = request.bundle_type
        if not UtilClient.is_unset(request.check_stock):
            query['CheckStock'] = request.check_stock
        if not UtilClient.is_unset(request.cpu_count):
            query['CpuCount'] = request.cpu_count
        if not UtilClient.is_unset(request.desktop_type_family):
            query['DesktopTypeFamily'] = request.desktop_type_family
        if not UtilClient.is_unset(request.fota_channel):
            query['FotaChannel'] = request.fota_channel
        if not UtilClient.is_unset(request.from_desktop_group):
            query['FromDesktopGroup'] = request.from_desktop_group
        if not UtilClient.is_unset(request.gpu_count):
            query['GpuCount'] = request.gpu_count
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.memory_size):
            query['MemorySize'] = request.memory_size
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.selected_bundle):
            query['SelectedBundle'] = request.selected_bundle
        if not UtilClient.is_unset(request.session_type):
            query['SessionType'] = request.session_type
        if not UtilClient.is_unset(request.support_multi_session):
            query['SupportMultiSession'] = request.support_multi_session
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBundles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeBundlesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    def describe_cds_file_share_links_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.creators):
            query['Creators'] = request.creators
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.share_id):
            query['ShareId'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            query['ShareName'] = request.share_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdsFileShareLinks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCdsFileShareLinksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cds_file_share_links(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cds_file_share_links_with_options(request, runtime)

    def describe_cens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    def describe_client_events_with_options(self, request, runtime):
        """
        You can audit the operation logs of regular users to improve security. The operation logs record events such as desktop startup, shutdown, and session disconnection.
        

        @param request: DescribeClientEventsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClientEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_ip):
            query['DesktopIp'] = request.desktop_ip
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeClientEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_client_events(self, request):
        """
        You can audit the operation logs of regular users to improve security. The operation logs record events such as desktop startup, shutdown, and session disconnection.
        

        @param request: DescribeClientEventsRequest

        @return: DescribeClientEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

    def describe_cloud_drive_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.drive_status):
            query['DriveStatus'] = request.drive_status
        if not UtilClient.is_unset(request.drive_type):
            query['DriveType'] = request.drive_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_group_id):
            query['ParentGroupId'] = request.parent_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudDriveGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCloudDriveGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_drive_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_drive_groups_with_options(request, runtime)

    def describe_cloud_drive_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudDrivePermissions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCloudDrivePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_drive_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_drive_permissions_with_options(request, runtime)

    def describe_customized_list_headers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.list_type):
            query['ListType'] = request.list_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomizedListHeaders',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCustomizedListHeadersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_customized_list_headers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_customized_list_headers_with_options(request, runtime)

    def describe_desktop_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.excluded_end_user_ids):
            query['ExcludedEndUserIds'] = request.excluded_end_user_ids
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.own_type):
            query['OwnType'] = request.own_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_desktop_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_groups_with_options(request, runtime)

    def describe_desktop_ids_by_vul_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopIdsByVulNames',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_desktop_ids_by_vul_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_ids_by_vul_names_with_options(request, runtime)

    def describe_desktop_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applied_scope):
            query['AppliedScope'] = request.applied_scope
        if not UtilClient.is_unset(request.cpu_count):
            query['CpuCount'] = request.cpu_count
        if not UtilClient.is_unset(request.desktop_id_for_modify):
            query['DesktopIdForModify'] = request.desktop_id_for_modify
        if not UtilClient.is_unset(request.desktop_type_id):
            query['DesktopTypeId'] = request.desktop_type_id
        if not UtilClient.is_unset(request.gpu_count):
            query['GpuCount'] = request.gpu_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.memory_size):
            query['MemorySize'] = request.memory_size
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopTypes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_desktop_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_types_with_options(request, runtime)

    def describe_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.excluded_end_user_id):
            query['ExcludedEndUserId'] = request.excluded_end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.filter_desktop_group):
            query['FilterDesktopGroup'] = request.filter_desktop_group
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.management_flag):
            query['ManagementFlag'] = request.management_flag
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.only_desktop_group):
            query['OnlyDesktopGroup'] = request.only_desktop_group
        if not UtilClient.is_unset(request.os_types):
            query['OsTypes'] = request.os_types
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_policy_id):
            query['SnapshotPolicyId'] = request.snapshot_policy_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    def describe_desktops_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.ignore_deleted):
            query['IgnoreDeleted'] = request.ignore_deleted
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopsInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_desktops_in_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_in_group_with_options(request, runtime)

    def describe_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    def describe_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_status):
            query['DirectoryStatus'] = request.directory_status
        if not UtilClient.is_unset(request.directory_type):
            query['DirectoryType'] = request.directory_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def describe_flow_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowMetric',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFlowMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flow_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_metric_with_options(request, runtime)

    def describe_flow_statistic_with_options(self, request, runtime):
        """
        > You can query only the traffic data in the last 90 days.
        

        @param request: DescribeFlowStatisticRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeFlowStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowStatistic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFlowStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_flow_statistic(self, request):
        """
        > You can query only the traffic data in the last 90 days.
        

        @param request: DescribeFlowStatisticRequest

        @return: DescribeFlowStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_statistic_with_options(request, runtime)

    def describe_fota_pending_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFotaPendingDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFotaPendingDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fota_pending_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fota_pending_desktops_with_options(request, runtime)

    def describe_fota_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fota_status):
            query['FotaStatus'] = request.fota_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        if not UtilClient.is_unset(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFotaTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFotaTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fota_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fota_tasks_with_options(request, runtime)

    def describe_front_vul_patch_list_with_options(self, request, runtime):
        """
        You can query the information about patches of up to 50 vulnerabilities in each request before you fix the current vulnerability.
        

        @param request: DescribeFrontVulPatchListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeFrontVulPatchListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_info):
            query['VulInfo'] = request.vul_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFrontVulPatchList',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFrontVulPatchListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_front_vul_patch_list(self, request):
        """
        You can query the information about patches of up to 50 vulnerabilities in each request before you fix the current vulnerability.
        

        @param request: DescribeFrontVulPatchListRequest

        @return: DescribeFrontVulPatchListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    def describe_grouped_vul_with_options(self, request, runtime):
        """
        ## Description
        After security protection is enabled, the system scans your cloud desktops for vulnerabilities once every day.
        

        @param request: DescribeGroupedVulRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupedVulResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedVul',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeGroupedVulResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_grouped_vul(self, request):
        """
        ## Description
        After security protection is enabled, the system scans your cloud desktops for vulnerabilities once every day.
        

        @param request: DescribeGroupedVulRequest

        @return: DescribeGroupedVulResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    def describe_image_modified_records_with_options(self, request, runtime):
        """
        If you have changed the image for a cloud desktop, you can go to the Elastic Desktop Service (EDS) console to query the image change records. To query the image change records of a cloud desktop, find the cloud desktop that you want to manage, click *Change Image History** to the right of **Image ID/Name** on the **Basic Information** tab.
        

        @param request: DescribeImageModifiedRecordsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeImageModifiedRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageModifiedRecords',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImageModifiedRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_modified_records(self, request):
        """
        If you have changed the image for a cloud desktop, you can go to the Elastic Desktop Service (EDS) console to query the image change records. To query the image change records of a cloud desktop, find the cloud desktop that you want to manage, click *Change Image History** to the right of **Image ID/Name** on the **Basic Information** tab.
        

        @param request: DescribeImageModifiedRecordsRequest

        @return: DescribeImageModifiedRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_image_modified_records_with_options(request, runtime)

    def describe_image_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_permission_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_instance_type):
            query['DesktopInstanceType'] = request.desktop_instance_type
        if not UtilClient.is_unset(request.gpu_category):
            query['GpuCategory'] = request.gpu_category
        if not UtilClient.is_unset(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_status):
            query['ImageStatus'] = request.image_status
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.language_type):
            query['LanguageType'] = request.language_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_type):
            query['SessionType'] = request.session_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def describe_invocations_with_options(self, request, runtime):
        """
        After you run a command, the command may not succeed or return the expected results. You can call this operation to query the execution result.
        *   You can query the execution information in the previous two weeks. Up to 100,000 lines of execution information can be retained.
        

        @param request: DescribeInvocationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_ids):
            query['DesktopIds'] = request.desktop_ids
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.include_output):
            query['IncludeOutput'] = request.include_output
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_invocations(self, request):
        """
        After you run a command, the command may not succeed or return the expected results. You can call this operation to query the execution result.
        *   You can query the execution information in the previous two weeks. Up to 100,000 lines of execution information can be retained.
        

        @param request: DescribeInvocationsRequest

        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    def describe_kms_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_kms_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_kms_keys_with_options(request, runtime)

    def describe_nasfile_systems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.match_compatible_profile):
            query['MatchCompatibleProfile'] = request.match_compatible_profile
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNASFileSystems',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNASFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nasfile_systems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nasfile_systems_with_options(request, runtime)

    def describe_network_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNetworkPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_packages_with_options(request, runtime)

    def describe_office_sites_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_type):
            query['OfficeSiteType'] = request.office_site_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOfficeSites',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeOfficeSitesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_office_sites(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_office_sites_with_options(request, runtime)

    def describe_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePolicyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_scan_task_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskProgress',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScanTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scan_task_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    def describe_security_event_operation_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperationStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_event_operation_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    def describe_security_event_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperations',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_event_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_susp_event_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_event_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_overview_with_options(request, runtime)

    def describe_susp_event_quara_files_with_options(self, request, runtime):
        """
        ## Description
        When alerts are handled, the system quarantines the files that contain detected threats to the quarantine panel. You can call this operation to view the quarantined files.
        

        @param request: DescribeSuspEventQuaraFilesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSuspEventQuaraFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventQuaraFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventQuaraFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_event_quara_files(self, request):
        """
        ## Description
        When alerts are handled, the system quarantines the files that contain detected threats to the quarantine panel. You can call this operation to view the quarantined files.
        

        @param request: DescribeSuspEventQuaraFilesRequest

        @return: DescribeSuspEventQuaraFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    def describe_susp_events_with_options(self, request, runtime):
        """
        An alert event consists of alerts and exceptions. Each alert event corresponds to multiple exceptions.
        

        @param request: DescribeSuspEventsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSuspEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_type):
            query['ParentEventType'] = request.parent_event_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_susp_events(self, request):
        """
        An alert event consists of alerts and exceptions. Each alert event corresponds to multiple exceptions.
        

        @param request: DescribeSuspEventsRequest

        @return: DescribeSuspEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    def describe_user_connection_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_duration_from):
            query['ConnectDurationFrom'] = request.connect_duration_from
        if not UtilClient.is_unset(request.connect_duration_to):
            query['ConnectDurationTo'] = request.connect_duration_to
        if not UtilClient.is_unset(request.connect_end_time_from):
            query['ConnectEndTimeFrom'] = request.connect_end_time_from
        if not UtilClient.is_unset(request.connect_end_time_to):
            query['ConnectEndTimeTo'] = request.connect_end_time_to
        if not UtilClient.is_unset(request.connect_start_time_from):
            query['ConnectStartTimeFrom'] = request.connect_start_time_from
        if not UtilClient.is_unset(request.connect_start_time_to):
            query['ConnectStartTimeTo'] = request.connect_start_time_to
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.end_user_type):
            query['EndUserType'] = request.end_user_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserConnectionRecords',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserConnectionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_connection_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_connection_records_with_options(request, runtime)

    def describe_user_profile_path_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserProfilePathRules',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserProfilePathRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_profile_path_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_profile_path_rules_with_options(request, runtime)

    def describe_users_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_state):
            query['ConnectState'] = request.connect_state
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.query_user_detail):
            query['QueryUserDetail'] = request.query_user_detail
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsersInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_users_in_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_users_in_group_with_options(request, runtime)

    def describe_users_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsersPassword',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_users_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_users_password_with_options(request, runtime)

    def describe_virtual_mfadevices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualMFADevices',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVirtualMFADevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_virtual_mfadevices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_mfadevices_with_options(request, runtime)

    def describe_vul_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulDetails',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    def describe_vul_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulList',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    def describe_vul_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vul_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_overview_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def detach_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachCenResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_with_options(request, runtime)

    def detach_end_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachEndUser',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_end_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_end_user_with_options(request, runtime)

    def disable_desktops_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_ids):
            query['DesktopIds'] = request.desktop_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDesktopsInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DisableDesktopsInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_desktops_in_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_desktops_in_group_with_options(request, runtime)

    def dissociate_network_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DissociateNetworkPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_network_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_network_package_with_options(request, runtime)

    def export_client_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportClientEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportClientEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def export_client_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_client_events_with_options(request, runtime)

    def export_desktop_group_info_with_options(self, request, runtime):
        """
        You can call the operation to export desktop groups and then save the desktop groups in the .xlsx file. The information about exported desktop groups includes: the desktop group ID and name, the workspace ID and name, the desktop template, the security policy name, the number of authorized users, the billing method, and the creation time.
        

        @param request: ExportDesktopGroupInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportDesktopGroupInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDesktopGroupInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportDesktopGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def export_desktop_group_info(self, request):
        """
        You can call the operation to export desktop groups and then save the desktop groups in the .xlsx file. The information about exported desktop groups includes: the desktop group ID and name, the workspace ID and name, the desktop template, the security policy name, the number of authorized users, the billing method, and the creation time.
        

        @param request: ExportDesktopGroupInfoRequest

        @return: ExportDesktopGroupInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_desktop_group_info_with_options(request, runtime)

    def export_desktop_list_info_with_options(self, request, runtime):
        """
        The list of cloud desktops that are exported by calling the ExportDesktopListInfo operation is saved in a CSV file. The CSV file contains the information about each cloud desktop, including the IDs and names of cloud desktops, IDs and names of workspaces, IDs and names of desktop groups, vCPUs, memory, protocols, system disk capacity, data disk capacity, OSs, running status, current user, tags, IP addresses, billing methods, and creation time.
        

        @param request: ExportDesktopListInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExportDesktopListInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDesktopListInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportDesktopListInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def export_desktop_list_info(self, request):
        """
        The list of cloud desktops that are exported by calling the ExportDesktopListInfo operation is saved in a CSV file. The CSV file contains the information about each cloud desktop, including the IDs and names of cloud desktops, IDs and names of workspaces, IDs and names of desktop groups, vCPUs, memory, protocols, system disk capacity, data disk capacity, OSs, running status, current user, tags, IP addresses, billing methods, and creation time.
        

        @param request: ExportDesktopListInfoRequest

        @return: ExportDesktopListInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_desktop_list_info_with_options(request, runtime)

    def get_connection_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def get_connection_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    def get_desktop_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDesktopGroupDetail',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_desktop_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_desktop_group_detail_with_options(request, runtime)

    def get_office_site_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficeSiteSsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetOfficeSiteSsoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_office_site_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_office_site_sso_status_with_options(request, runtime)

    def get_sp_metadata_with_options(self, request, runtime):
        """
        ## Description
        You can call this operation only for workspaces of the Active Directory (AD) and convenience account types. You cannot call this operation for RAM directories.
        

        @param request: GetSpMetadataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSpMetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpMetadata',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetSpMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sp_metadata(self, request):
        """
        ## Description
        You can call this operation only for workspaces of the Active Directory (AD) and convenience account types. You cannot call this operation for RAM directories.
        

        @param request: GetSpMetadataRequest

        @return: GetSpMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sp_metadata_with_options(request, runtime)

    def handle_security_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event):
            query['SecurityEvent'] = request.security_event
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSecurityEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.HandleSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def handle_security_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    def list_cds_files_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ecd_20200930_models.ListCdsFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_ids):
            request.file_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_ids, 'FileIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_ids_shrink):
            query['FileIds'] = request.file_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.parent_file_id):
            query['ParentFileId'] = request.parent_file_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCdsFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListCdsFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cds_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cds_files_with_options(request, runtime)

    def list_directory_users_with_options(self, request, runtime):
        """
        If you use an AD directory to connect to an AD system of an enterprise, you can call this operation to obtain the information about users in the AD system.
        

        @param request: ListDirectoryUsersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDirectoryUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oupath):
            query['OUPath'] = request.oupath
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectoryUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListDirectoryUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_directory_users(self, request):
        """
        If you use an AD directory to connect to an AD system of an enterprise, you can call this operation to obtain the information about users in the AD system.
        

        @param request: ListDirectoryUsersRequest

        @return: ListDirectoryUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    def list_file_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListFilePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_file_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_permission_with_options(request, runtime)

    def list_office_site_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_refresh):
            query['ForceRefresh'] = request.force_refresh
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.query_range):
            query['QueryRange'] = request.query_range
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeSiteOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def list_office_site_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_overview_with_options(request, runtime)

    def list_office_site_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oupath):
            query['OUPath'] = request.oupath
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeSiteUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_office_site_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_users_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        ## Description
        You must specify at least one of the ResourceId.N, Tag.N.Key, and Tag.N.Value parameters in the request to specify the query objects.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        ## Description
        You must specify at least one of the ResourceId.N, Tag.N.Key, and Tag.N.Value parameters in the request to specify the query objects.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_ad_organization_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAdOrganizationUnits',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListUserAdOrganizationUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_ad_organization_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_ad_organization_units_with_options(request, runtime)

    def lock_virtual_mfadevice_with_options(self, request, runtime):
        """
        ## Description
        After a virtual MFA device is locked, its status changes to LOCKED. The AD user who uses the virtual MFA device is unable to pass MFA and is therefore unable to log on to the client. You can call the [UnlockVirtualMFADevice](~~206212~~) operation to unlock the device.
        

        @param request: LockVirtualMFADeviceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: LockVirtualMFADeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.LockVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_virtual_mfadevice(self, request):
        """
        ## Description
        After a virtual MFA device is locked, its status changes to LOCKED. The AD user who uses the virtual MFA device is unable to pass MFA and is therefore unable to log on to the client. You can call the [UnlockVirtualMFADevice](~~206212~~) operation to unlock the device.
        

        @param request: LockVirtualMFADeviceRequest

        @return: LockVirtualMFADeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_virtual_mfadevice_with_options(request, runtime)

    def migrate_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_office_site_id):
            query['TargetOfficeSiteId'] = request.target_office_site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.MigrateDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_desktops_with_options(request, runtime)

    def modify_adconnector_directory_with_options(self, request, runtime):
        """
        This operation modifies only the domain name and Domain Name System (DNS) parameters of AD directories in the ERROR or REGISTERING state. DNS parameters include DomainName, SubDomainName, DnsAddress.N, and SubDomainDnsAddress.
        

        @param request: ModifyADConnectorDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyADConnectorDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADConnectorDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_adconnector_directory(self, request):
        """
        This operation modifies only the domain name and Domain Name System (DNS) parameters of AD directories in the ERROR or REGISTERING state. DNS parameters include DomainName, SubDomainName, DnsAddress.N, and SubDomainDnsAddress.
        

        @param request: ModifyADConnectorDirectoryRequest

        @return: ModifyADConnectorDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    def modify_adconnector_office_site_with_options(self, request, runtime):
        """
        This operation modifies the domain name and DNS parameters of workspaces that are of enterprise AD account type and in the Error or Registering state. DNS parameters include DomainName, SubDomainName, DnsAddress.N, and SubDomainDnsAddress.N.
        

        @param request: ModifyADConnectorOfficeSiteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyADConnectorOfficeSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADConnectorOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_adconnector_office_site(self, request):
        """
        This operation modifies the domain name and DNS parameters of workspaces that are of enterprise AD account type and in the Error or Registering state. DNS parameters include DomainName, SubDomainName, DnsAddress.N, and SubDomainDnsAddress.N.
        

        @param request: ModifyADConnectorOfficeSiteRequest

        @return: ModifyADConnectorOfficeSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_office_site_with_options(request, runtime)

    def modify_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    def modify_bundle_with_options(self, request, runtime):
        """
        ## Description
        Only custom desktop templates can be modified.
        

        @param request: ModifyBundleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyBundleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_name):
            query['BundleName'] = request.bundle_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBundle',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyBundleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_bundle(self, request):
        """
        ## Description
        Only custom desktop templates can be modified.
        

        @param request: ModifyBundleRequest

        @return: ModifyBundleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_bundle_with_options(request, runtime)

    def modify_cds_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCdsFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCdsFileResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cds_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cds_file_with_options(request, runtime)

    def modify_cds_file_share_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            query['DisableDownload'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            query['DisablePreview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            query['DisableSave'] = request.disable_save
        if not UtilClient.is_unset(request.download_count):
            query['DownloadCount'] = request.download_count
        if not UtilClient.is_unset(request.download_limit):
            query['DownloadLimit'] = request.download_limit
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.preview_count):
            query['PreviewCount'] = request.preview_count
        if not UtilClient.is_unset(request.preview_limit):
            query['PreviewLimit'] = request.preview_limit
        if not UtilClient.is_unset(request.report_count):
            query['ReportCount'] = request.report_count
        if not UtilClient.is_unset(request.save_count):
            query['SaveCount'] = request.save_count
        if not UtilClient.is_unset(request.save_limit):
            query['SaveLimit'] = request.save_limit
        if not UtilClient.is_unset(request.share_id):
            query['ShareId'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            query['ShareName'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            query['SharePwd'] = request.share_pwd
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.video_preview_count):
            query['VideoPreviewCount'] = request.video_preview_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCdsFileShareLink',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCdsFileShareLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cds_file_share_link(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cds_file_share_link_with_options(request, runtime)

    def modify_cloud_drive_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            query['TotalSize'] = request.total_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudDriveGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCloudDriveGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cloud_drive_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cloud_drive_groups_with_options(request, runtime)

    def modify_cloud_drive_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.download_end_user_ids):
            query['DownloadEndUserIds'] = request.download_end_user_ids
        if not UtilClient.is_unset(request.download_upload_end_user_ids):
            query['DownloadUploadEndUserIds'] = request.download_upload_end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudDrivePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCloudDrivePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cloud_drive_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cloud_drive_permission_with_options(request, runtime)

    def modify_customized_list_headers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.headers):
            query['Headers'] = request.headers
        if not UtilClient.is_unset(request.list_type):
            query['ListType'] = request.list_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustomizedListHeaders',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCustomizedListHeadersResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_customized_list_headers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_customized_list_headers_with_options(request, runtime)

    def modify_desktop_charge_type_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that you are familiar with the billing methods of cloud desktops in Elastic Desktop Service (EDS). For more information, see [Billing overview](~~188395~~).
        *   Before you call this operation, make sure that the cloud desktop that you want to manage is in the Running or Stopped state and no overdue payments of the cloud desktop are generated.
        *   After the order payment is completed, the system starts to change the billing method of the cloud desktop. During the change, you cannot perform operations, such as starting or stopping the cloud desktop, and changing configurations of the cloud desktop.<props="china">
        After you change the billing method of the cloud desktop from subscription to pay-as-you-go, you may get a refund. For more information, see [Change a subscription cloud desktop to a pay-as-you-go one](https://help.aliyun.com/document_detail/439964.html).
        </props>
        

        @param request: ModifyDesktopChargeTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDesktopChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopChargeType',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_desktop_charge_type(self, request):
        """
        Before you call this operation, make sure that you are familiar with the billing methods of cloud desktops in Elastic Desktop Service (EDS). For more information, see [Billing overview](~~188395~~).
        *   Before you call this operation, make sure that the cloud desktop that you want to manage is in the Running or Stopped state and no overdue payments of the cloud desktop are generated.
        *   After the order payment is completed, the system starts to change the billing method of the cloud desktop. During the change, you cannot perform operations, such as starting or stopping the cloud desktop, and changing configurations of the cloud desktop.<props="china">
        After you change the billing method of the cloud desktop from subscription to pay-as-you-go, you may get a refund. For more information, see [Change a subscription cloud desktop to a pay-as-you-go one](https://help.aliyun.com/document_detail/439964.html).
        </props>
        

        @param request: ModifyDesktopChargeTypeRequest

        @return: ModifyDesktopChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_charge_type_with_options(request, runtime)

    def modify_desktop_group_with_options(self, request, runtime):
        """
        After you create a desktop group, the system creates a specific number of cloud desktops based on the scaling policy that you configure for the desktop group and the number of end users who request to connect to the cloud desktops. Cloud desktops in a desktop group are created by using the same desktop template and security policy. You can modify the configurations of the desktop group in different scenarios to manage cloud desktops in a centralized manner.
        *   By default, a desktop group has the same name as all cloud desktops in the group. You can modify the desktop group name, which is specified by the DesktopGroupName parameter, to distinguish the desktop group from the cloud desktops.
        *   If the number of vCPUs and memory size of the cloud desktop cannot meet your business requirements in high performance scenarios, you can change the desktop template that is used to create the cloud desktop to a desktop template (OwnBundleId) that has higher specifications.
        *   If a security policy that is associated with the desktop group cannot meet your requirements on security, you can change the policy to another policy (PolicyGroupId) that provides higher security.
        *   If the number of cloud desktops in the desktop group is insufficient to meet the business requirements of end users, you can modify the parameter settings in the scaling policy. The parameters include MinDesktopsCount, MaxDesktopsCount, and AllowBufferCount.
        

        @param request: ModifyDesktopGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDesktopGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.buy_desktops_count):
            query['BuyDesktopsCount'] = request.buy_desktops_count
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.connect_duration):
            query['ConnectDuration'] = request.connect_duration
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.disable_session_config):
            query['DisableSessionConfig'] = request.disable_session_config
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.idle_disconnect_duration):
            query['IdleDisconnectDuration'] = request.idle_disconnect_duration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keep_duration):
            query['KeepDuration'] = request.keep_duration
        if not UtilClient.is_unset(request.load_policy):
            query['LoadPolicy'] = request.load_policy
        if not UtilClient.is_unset(request.max_desktops_count):
            query['MaxDesktopsCount'] = request.max_desktops_count
        if not UtilClient.is_unset(request.min_desktops_count):
            query['MinDesktopsCount'] = request.min_desktops_count
        if not UtilClient.is_unset(request.own_bundle_id):
            query['OwnBundleId'] = request.own_bundle_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.policy_group_ids):
            query['PolicyGroupIds'] = request.policy_group_ids
        if not UtilClient.is_unset(request.profile_follow_switch):
            query['ProfileFollowSwitch'] = request.profile_follow_switch
        if not UtilClient.is_unset(request.ratio_threshold):
            query['RatioThreshold'] = request.ratio_threshold
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.scale_strategy_id):
            query['ScaleStrategyId'] = request.scale_strategy_id
        if not UtilClient.is_unset(request.stop_duration):
            query['StopDuration'] = request.stop_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_desktop_group(self, request):
        """
        After you create a desktop group, the system creates a specific number of cloud desktops based on the scaling policy that you configure for the desktop group and the number of end users who request to connect to the cloud desktops. Cloud desktops in a desktop group are created by using the same desktop template and security policy. You can modify the configurations of the desktop group in different scenarios to manage cloud desktops in a centralized manner.
        *   By default, a desktop group has the same name as all cloud desktops in the group. You can modify the desktop group name, which is specified by the DesktopGroupName parameter, to distinguish the desktop group from the cloud desktops.
        *   If the number of vCPUs and memory size of the cloud desktop cannot meet your business requirements in high performance scenarios, you can change the desktop template that is used to create the cloud desktop to a desktop template (OwnBundleId) that has higher specifications.
        *   If a security policy that is associated with the desktop group cannot meet your requirements on security, you can change the policy to another policy (PolicyGroupId) that provides higher security.
        *   If the number of cloud desktops in the desktop group is insufficient to meet the business requirements of end users, you can modify the parameter settings in the scaling policy. The parameters include MinDesktopsCount, MaxDesktopsCount, and AllowBufferCount.
        

        @param request: ModifyDesktopGroupRequest

        @return: ModifyDesktopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_group_with_options(request, runtime)

    def modify_desktop_host_name_with_options(self, request, runtime):
        """
        ## Description
        You can only change the hostname of a Windows cloud desktop in the workspace of the enterprise Active Directory (AD) account type. After the hostname is changed, the cloud desktop is recreated.
        

        @param request: ModifyDesktopHostNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDesktopHostNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.new_host_name):
            query['NewHostName'] = request.new_host_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopHostName',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopHostNameResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_desktop_host_name(self, request):
        """
        ## Description
        You can only change the hostname of a Windows cloud desktop in the workspace of the enterprise Active Directory (AD) account type. After the hostname is changed, the cloud desktop is recreated.
        

        @param request: ModifyDesktopHostNameRequest

        @return: ModifyDesktopHostNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_host_name_with_options(request, runtime)

    def modify_desktop_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.new_desktop_name):
            query['NewDesktopName'] = request.new_desktop_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopName',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopNameResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_desktop_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_name_with_options(request, runtime)

    def modify_desktop_spec_with_options(self, request, runtime):
        """
        You can call this operation to change the configurations, such as the desktop type and disk size, of a cloud desktop.
        *   Before you call this operation, take note of the cloud desktop types and the disk sizes for each type of cloud desktop that Elastic Desktop Service (EDS) provides. For more information, see [Cloud desktop types](~~188609~~).
        *   When you change the configurations of a cloud desktop, you must change the desktop type or the size of the system disk or data disk. You must configure at least one of the following parameters: DesktopType, RootDiskSizeGib, and UserDiskSizeGib. You must take note of the following items:
        *   Each desktop type contains different desktop specifications, such as vCPUs, memory, and GPUs. When you change the desktop configurations, you can only change the desktop type from one to another. However, you cannot change only one of the specifications, such as vCPUs, memory, and GPUs.
        *   You cannot change a cloud desktop from the General Office type to a non-General Office type, or from a non-General Office type to the General Office type. You cannot change a cloud desktop from the Graphics type to a non-Graphics type, or from a non-Graphics type to the Graphics type.
        *   You can only increase the sizes of system and data disks.
        *   If your cloud desktop uses the subscription billing method, the price difference is calculated based on the price before and after configuration changes. You may receive a refund, or pay for the price difference.
        *   If you want to change the configurations of your cloud desktop for multiple times, we recommend that you wait at least 5 minutes the next time you change the configurations of the same cloud desktop.
        *   The cloud desktop for which you want to change configurations must be in the Stopped state.
        *   The changes do not affect your personal data on the cloud desktop.
        

        @param request: ModifyDesktopSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDesktopSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_size_gib):
            query['RootDiskSizeGib'] = request.root_disk_size_gib
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_size_gib):
            query['UserDiskSizeGib'] = request.user_disk_size_gib
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopSpec',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_desktop_spec(self, request):
        """
        You can call this operation to change the configurations, such as the desktop type and disk size, of a cloud desktop.
        *   Before you call this operation, take note of the cloud desktop types and the disk sizes for each type of cloud desktop that Elastic Desktop Service (EDS) provides. For more information, see [Cloud desktop types](~~188609~~).
        *   When you change the configurations of a cloud desktop, you must change the desktop type or the size of the system disk or data disk. You must configure at least one of the following parameters: DesktopType, RootDiskSizeGib, and UserDiskSizeGib. You must take note of the following items:
        *   Each desktop type contains different desktop specifications, such as vCPUs, memory, and GPUs. When you change the desktop configurations, you can only change the desktop type from one to another. However, you cannot change only one of the specifications, such as vCPUs, memory, and GPUs.
        *   You cannot change a cloud desktop from the General Office type to a non-General Office type, or from a non-General Office type to the General Office type. You cannot change a cloud desktop from the Graphics type to a non-Graphics type, or from a non-Graphics type to the Graphics type.
        *   You can only increase the sizes of system and data disks.
        *   If your cloud desktop uses the subscription billing method, the price difference is calculated based on the price before and after configuration changes. You may receive a refund, or pay for the price difference.
        *   If you want to change the configurations of your cloud desktop for multiple times, we recommend that you wait at least 5 minutes the next time you change the configurations of the same cloud desktop.
        *   The cloud desktop for which you want to change configurations must be in the Stopped state.
        *   The changes do not affect your personal data on the cloud desktop.
        

        @param request: ModifyDesktopSpecRequest

        @return: ModifyDesktopSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_spec_with_options(request, runtime)

    def modify_desktops_policy_group_with_options(self, request, runtime):
        """
        The cloud desktops whose policy you want to modify must be in the Running state.
        

        @param request: ModifyDesktopsPolicyGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDesktopsPolicyGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.policy_group_ids):
            query['PolicyGroupIds'] = request.policy_group_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopsPolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopsPolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_desktops_policy_group(self, request):
        """
        The cloud desktops whose policy you want to modify must be in the Running state.
        

        @param request: ModifyDesktopsPolicyGroupRequest

        @return: ModifyDesktopsPolicyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    def modify_disk_spec_with_options(self, request, runtime):
        """
        You can call this operation to change the configurations, such as the desktop type and disk size, of a cloud desktop.
        *   Before you call this operation, you must know the cloud desktop types and the disk sizes for each type of cloud desktop that Elastic Desktop Service (EDS) provides.
        *   When you change the configurations of a cloud desktop, you must change the desktop type or the size of the system disk or data disk. You must configure at least one of the following parameters: DesktopType, RootDiskSizeGib, and UserDiskSizeGib. Take note of the following items:
        1\\. Desktop types include the specifications of vCPUs, memory, and GPUs. You can change only the desktop type, instead of one of the specifications.
        2\\. You cannot change a cloud desktop from the General Office type to a non-General Office type, or from a non-General Office type to the General Office type. You cannot change a cloud desktop from the Graphics type to a non-Graphics type, or from a non-Graphics type to the Graphics type.
        3\\. You can only increase the sizes of system and data disks. You cannot decrease the sizes of system and data disks.
        4\\. If your cloud desktop uses the subscription billing method, the price difference is calculated based on the price before and after configuration changes. You may receive a refund, or must pay for the price difference.
        5\\. If you need to change the configurations of a cloud desktop multiple times, we recommend that you wait at least 5 minutes between consecutive operations on the cloud desktop.
        6\\. The cloud desktop for which you want to change the desktop type must be in the Stopped state.
        *   The changes do not affect your personal data on the cloud desktop.
        

        @param request: ModifyDiskSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDiskSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_performance_level):
            query['RootDiskPerformanceLevel'] = request.root_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSpec',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDiskSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_disk_spec(self, request):
        """
        You can call this operation to change the configurations, such as the desktop type and disk size, of a cloud desktop.
        *   Before you call this operation, you must know the cloud desktop types and the disk sizes for each type of cloud desktop that Elastic Desktop Service (EDS) provides.
        *   When you change the configurations of a cloud desktop, you must change the desktop type or the size of the system disk or data disk. You must configure at least one of the following parameters: DesktopType, RootDiskSizeGib, and UserDiskSizeGib. Take note of the following items:
        1\\. Desktop types include the specifications of vCPUs, memory, and GPUs. You can change only the desktop type, instead of one of the specifications.
        2\\. You cannot change a cloud desktop from the General Office type to a non-General Office type, or from a non-General Office type to the General Office type. You cannot change a cloud desktop from the Graphics type to a non-Graphics type, or from a non-Graphics type to the Graphics type.
        3\\. You can only increase the sizes of system and data disks. You cannot decrease the sizes of system and data disks.
        4\\. If your cloud desktop uses the subscription billing method, the price difference is calculated based on the price before and after configuration changes. You may receive a refund, or must pay for the price difference.
        5\\. If you need to change the configurations of a cloud desktop multiple times, we recommend that you wait at least 5 minutes between consecutive operations on the cloud desktop.
        6\\. The cloud desktop for which you want to change the desktop type must be in the Stopped state.
        *   The changes do not affect your personal data on the cloud desktop.
        

        @param request: ModifyDiskSpecRequest

        @return: ModifyDiskSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    def modify_entitlement_with_options(self, request, runtime):
        """
        The cloud desktop must be in the Running state.
        

        @param request: ModifyEntitlementRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyEntitlementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEntitlement',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyEntitlementResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_entitlement(self, request):
        """
        The cloud desktop must be in the Running state.
        

        @param request: ModifyEntitlementRequest

        @return: ModifyEntitlementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        """
        ## Description
        You can call this operation to modify the properties of only custom images in the Available (Available) state.
        

        @param request: ModifyImageAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyImageAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAttribute',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_image_attribute(self, request):
        """
        ## Description
        You can call this operation to modify the properties of only custom images in the Available (Available) state.
        

        @param request: ModifyImageAttributeRequest

        @return: ModifyImageAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_image_permission_with_options(self, request, runtime):
        """
        ### Security of shared images
        Elastic Desktop Service (EDS) does not ensure the integrity and security of shared images on cloud desktops. Before you use shared images, make sure that the images come from trusted accounts. You must assume all risks.
        ### Quotas and billing
        *   Shared images do not count against the image quotas of the recipient Alibaba Cloud accounts.
        *   Alibaba Cloud accounts that share images are not charged if the recipient accounts use the shared images to create cloud desktops.
        *   There are no additional charges for sharing an image.
        ### Supported sharing behavior
        *   You can share custom images with other Alibaba Cloud accounts.
        *   You can share custom images between accounts in the China site (aliyun.com) and the international site (alibabacloud.com).
        ### Unsupported sharing behavior
        *   You cannot share images that are shared by other Alibaba Cloud accounts.
        *   You cannot share encrypted images.
        *   You cannot share images across regions. If you want to share images across regions, you can call the CopyImage operation to copy the images from the source region to the destination region.
        

        @param request: ModifyImagePermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyImagePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_account):
            query['RemoveAccount'] = request.remove_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImagePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImagePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_image_permission(self, request):
        """
        ### Security of shared images
        Elastic Desktop Service (EDS) does not ensure the integrity and security of shared images on cloud desktops. Before you use shared images, make sure that the images come from trusted accounts. You must assume all risks.
        ### Quotas and billing
        *   Shared images do not count against the image quotas of the recipient Alibaba Cloud accounts.
        *   Alibaba Cloud accounts that share images are not charged if the recipient accounts use the shared images to create cloud desktops.
        *   There are no additional charges for sharing an image.
        ### Supported sharing behavior
        *   You can share custom images with other Alibaba Cloud accounts.
        *   You can share custom images between accounts in the China site (aliyun.com) and the international site (alibabacloud.com).
        ### Unsupported sharing behavior
        *   You cannot share images that are shared by other Alibaba Cloud accounts.
        *   You cannot share encrypted images.
        *   You cannot share images across regions. If you want to share images across regions, you can call the CopyImage operation to copy the images from the source region to the destination region.
        

        @param request: ModifyImagePermissionRequest

        @return: ModifyImagePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_image_permission_with_options(request, runtime)

    def modify_nasdefault_mount_target_with_options(self, request, runtime):
        """
        ## Description
        When you create a NAS file system, a mount target is automatically generated. By default, the mount target does not need to be changed. If the mount target is accidentally deleted, you must specify a new mount target for the NAS file system in the workspace. You can call the [CreateMountTarget](~~62621~~) operation to create a mount target.
        

        @param request: ModifyNASDefaultMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyNASDefaultMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNASDefaultMountTarget',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNASDefaultMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_nasdefault_mount_target(self, request):
        """
        ## Description
        When you create a NAS file system, a mount target is automatically generated. By default, the mount target does not need to be changed. If the mount target is accidentally deleted, you must specify a new mount target for the NAS file system in the workspace. You can call the [CreateMountTarget](~~62621~~) operation to create a mount target.
        

        @param request: ModifyNASDefaultMountTargetRequest

        @return: ModifyNASDefaultMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_nasdefault_mount_target_with_options(request, runtime)

    def modify_network_package_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkPackageBandwidth',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_network_package_bandwidth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_bandwidth_with_options(request, runtime)

    def modify_network_package_enabled_with_options(self, request, runtime):
        """
        ## Description
        If you want to temporarily disable Internet access for a cloud desktop, you can disable the Internet access package. You can restore the package based on your requirements.
        

        @param request: ModifyNetworkPackageEnabledRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyNetworkPackageEnabledResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkPackageEnabled',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_network_package_enabled(self, request):
        """
        ## Description
        If you want to temporarily disable Internet access for a cloud desktop, you can disable the Internet access package. You can restore the package based on your requirements.
        

        @param request: ModifyNetworkPackageEnabledRequest

        @return: ModifyNetworkPackageEnabledResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_enabled_with_options(request, runtime)

    def modify_office_site_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.need_verify_login_risk):
            query['NeedVerifyLoginRisk'] = request.need_verify_login_risk
        if not UtilClient.is_unset(request.need_verify_zero_device):
            query['NeedVerifyZeroDevice'] = request.need_verify_zero_device
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteAttribute',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_office_site_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_attribute_with_options(request, runtime)

    def modify_office_site_cross_desktop_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_cross_desktop_access):
            query['EnableCrossDesktopAccess'] = request.enable_cross_desktop_access
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteCrossDesktopAccess',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_office_site_cross_desktop_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_cross_desktop_access_with_options(request, runtime)

    def modify_office_site_mfa_enabled_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteMfaEnabled',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_office_site_mfa_enabled(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_mfa_enabled_with_options(request, runtime)

    def modify_operate_vul_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_info):
            query['VulInfo'] = request.vul_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOperateVul',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOperateVulResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_operate_vul(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    def modify_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_content_protection):
            query['AppContentProtection'] = request.app_content_protection
        if not UtilClient.is_unset(request.authorize_access_policy_rule):
            query['AuthorizeAccessPolicyRule'] = request.authorize_access_policy_rule
        if not UtilClient.is_unset(request.authorize_security_policy_rule):
            query['AuthorizeSecurityPolicyRule'] = request.authorize_security_policy_rule
        if not UtilClient.is_unset(request.camera_redirect):
            query['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.end_user_apply_admin_coordinate):
            query['EndUserApplyAdminCoordinate'] = request.end_user_apply_admin_coordinate
        if not UtilClient.is_unset(request.end_user_group_coordinate):
            query['EndUserGroupCoordinate'] = request.end_user_group_coordinate
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.internet_communication_protocol):
            query['InternetCommunicationProtocol'] = request.internet_communication_protocol
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_redirect):
            query['NetRedirect'] = request.net_redirect
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.preempt_login):
            query['PreemptLogin'] = request.preempt_login
        if not UtilClient.is_unset(request.preempt_login_user):
            query['PreemptLoginUser'] = request.preempt_login_user
        if not UtilClient.is_unset(request.printer_redirection):
            query['PrinterRedirection'] = request.printer_redirection
        if not UtilClient.is_unset(request.record_content):
            query['RecordContent'] = request.record_content
        if not UtilClient.is_unset(request.record_content_expires):
            query['RecordContentExpires'] = request.record_content_expires
        if not UtilClient.is_unset(request.recording):
            query['Recording'] = request.recording
        if not UtilClient.is_unset(request.recording_audio):
            query['RecordingAudio'] = request.recording_audio
        if not UtilClient.is_unset(request.recording_duration):
            query['RecordingDuration'] = request.recording_duration
        if not UtilClient.is_unset(request.recording_end_time):
            query['RecordingEndTime'] = request.recording_end_time
        if not UtilClient.is_unset(request.recording_expires):
            query['RecordingExpires'] = request.recording_expires
        if not UtilClient.is_unset(request.recording_fps):
            query['RecordingFps'] = request.recording_fps
        if not UtilClient.is_unset(request.recording_start_time):
            query['RecordingStartTime'] = request.recording_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_coordinate):
            query['RemoteCoordinate'] = request.remote_coordinate
        if not UtilClient.is_unset(request.revoke_access_policy_rule):
            query['RevokeAccessPolicyRule'] = request.revoke_access_policy_rule
        if not UtilClient.is_unset(request.revoke_security_policy_rule):
            query['RevokeSecurityPolicyRule'] = request.revoke_security_policy_rule
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.video_redirect):
            query['VideoRedirect'] = request.video_redirect
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_color):
            query['WatermarkColor'] = request.watermark_color
        if not UtilClient.is_unset(request.watermark_degree):
            query['WatermarkDegree'] = request.watermark_degree
        if not UtilClient.is_unset(request.watermark_font_size):
            query['WatermarkFontSize'] = request.watermark_font_size
        if not UtilClient.is_unset(request.watermark_font_style):
            query['WatermarkFontStyle'] = request.watermark_font_style
        if not UtilClient.is_unset(request.watermark_row_amount):
            query['WatermarkRowAmount'] = request.watermark_row_amount
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
        if not UtilClient.is_unset(request.watermark_transparency_value):
            query['WatermarkTransparencyValue'] = request.watermark_transparency_value
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyPolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    def modify_user_entitlement_with_options(self, request, runtime):
        """
        You can modify permissions for regular users on cloud desktops that are only in the Running state.
        

        @param request: ModifyUserEntitlementRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyUserEntitlementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_desktop_id):
            query['AuthorizeDesktopId'] = request.authorize_desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.revoke_desktop_id):
            query['RevokeDesktopId'] = request.revoke_desktop_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserEntitlement',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserEntitlementResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_entitlement(self, request):
        """
        You can modify permissions for regular users on cloud desktops that are only in the Running state.
        

        @param request: ModifyUserEntitlementRequest

        @return: ModifyUserEntitlementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_entitlement_with_options(request, runtime)

    def modify_user_to_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.new_end_user_ids):
            query['NewEndUserIds'] = request.new_end_user_ids
        if not UtilClient.is_unset(request.old_end_user_ids):
            query['OldEndUserIds'] = request.old_end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserToDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserToDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_to_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_to_desktop_group_with_options(request, runtime)

    def move_cds_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveCdsFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.MoveCdsFileResponse(),
            self.call_api(params, req, runtime)
        )

    def move_cds_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_cds_file_with_options(request, runtime)

    def operate_vuls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.precondition):
            query['Precondition'] = request.precondition
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVuls',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.OperateVulsResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_vuls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    def reboot_desktops_with_options(self, request, runtime):
        """
        The cloud desktops that you want to restart by calling this operation must be in the Running state.
        

        @param request: RebootDesktopsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RebootDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebootDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def reboot_desktops(self, request):
        """
        The cloud desktops that you want to restart by calling this operation must be in the Running state.
        

        @param request: RebootDesktopsRequest

        @return: RebootDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    def rebuild_desktops_with_options(self, request, runtime):
        """
        Before you change the image of a cloud desktop, take note of the following limits:
        - You can select the OS of an image during image change. However, this operation is unavailable in the following regions: China (Hong Kong), Australia (Sydney), Singapore (Singapore), and Japan (Tokyo).
        - Image change between GPU and non-GPU images is not supported. If a cloud desktop is of the Graphics type, you can use only a GPU image. If the cloud desktop is of a non-Graphics type, you can use only a non-GPU image.
        After you change the image of the cloud desktop, the system uses the new image to initialize the system disk of the cloud desktop. Take note of the following impacts:
        - The system deletes data from the original system disk. The snapshots that are created from the original system disk of the cloud desktop become unavailable and are automatically deleted.
        - If you change the OS of the image, the system deletes data from the original data disk of the cloud desktop. The system also deletes snapshots that are created from the original data disk of the cloud desktop because original snapshots become unavailable. If you do not change the OS of the image, data on the original data disk is retained, and snapshots that are created from the data disk are still available.
        

        @param request: RebuildDesktopsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RebuildDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebuildDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def rebuild_desktops(self, request):
        """
        Before you change the image of a cloud desktop, take note of the following limits:
        - You can select the OS of an image during image change. However, this operation is unavailable in the following regions: China (Hong Kong), Australia (Sydney), Singapore (Singapore), and Japan (Tokyo).
        - Image change between GPU and non-GPU images is not supported. If a cloud desktop is of the Graphics type, you can use only a GPU image. If the cloud desktop is of a non-Graphics type, you can use only a non-GPU image.
        After you change the image of the cloud desktop, the system uses the new image to initialize the system disk of the cloud desktop. Take note of the following impacts:
        - The system deletes data from the original system disk. The snapshots that are created from the original system disk of the cloud desktop become unavailable and are automatically deleted.
        - If you change the OS of the image, the system deletes data from the original data disk of the cloud desktop. The system also deletes snapshots that are created from the original data disk of the cloud desktop because original snapshots become unavailable. If you do not change the OS of the image, data on the original data disk is retained, and snapshots that are created from the data disk are still available.
        

        @param request: RebuildDesktopsRequest

        @return: RebuildDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebuild_desktops_with_options(request, runtime)

    def remove_file_permission_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ecd_20200930_models.RemoveFilePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_list):
            request.member_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFilePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveFilePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_file_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_file_permission_with_options(request, runtime)

    def remove_user_from_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_ids):
            query['DesktopGroupIds'] = request.desktop_group_ids
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveUserFromDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_user_from_desktop_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_desktop_group_with_options(request, runtime)

    def renew_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_desktops_with_options(request, runtime)

    def renew_network_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewNetworkPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_network_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_network_packages_with_options(request, runtime)

    def reset_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_desktops_with_options(request, runtime)

    def reset_nasdefault_mount_target_with_options(self, request, runtime):
        """
        ## Description
        When you create a NAS file system, a mount target is automatically generated. By default, you do not need to modify the mount target of the NAS file system. If the mount target is disabled, you need to reset the mount target of the NAS file system.
        

        @param request: ResetNASDefaultMountTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetNASDefaultMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNASDefaultMountTarget',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetNASDefaultMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_nasdefault_mount_target(self, request):
        """
        ## Description
        When you create a NAS file system, a mount target is automatically generated. By default, you do not need to modify the mount target of the NAS file system. If the mount target is disabled, you need to reset the mount target of the NAS file system.
        

        @param request: ResetNASDefaultMountTargetRequest

        @return: ResetNASDefaultMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_nasdefault_mount_target_with_options(request, runtime)

    def reset_snapshot_with_options(self, request, runtime):
        """
        Before you call this operation, make sure that the following operations are performed:
        *   The data that you want to retain in the disk is backed up.
        **\
        **Note**The disk restoration operation is irreversible. After you restore data on a disk, the disk is restored to the status at the point in time when the snapshot was created. Data that is generated between the snapshot creation time and the current time is lost. Before you restore a disk from a snapshot, make sure that you back up important data.
        *   The cloud desktop whose disk you want to restore is stopped.
        

        @param request: ResetSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_snapshot(self, request):
        """
        Before you call this operation, make sure that the following operations are performed:
        *   The data that you want to retain in the disk is backed up.
        **\
        **Note**The disk restoration operation is irreversible. After you restore data on a disk, the disk is restored to the status at the point in time when the snapshot was created. Data that is generated between the snapshot creation time and the current time is lost. Before you restore a disk from a snapshot, make sure that you back up important data.
        *   The cloud desktop whose disk you want to restore is stopped.
        

        @param request: ResetSnapshotRequest

        @return: ResetSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    def revoke_coordinate_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_id):
            query['CoId'] = request.co_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeCoordinatePrivilege',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RevokeCoordinatePrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_coordinate_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_coordinate_privilege_with_options(request, runtime)

    def rollback_susp_event_quara_file_with_options(self, request, runtime):
        """
        ## Description
        When alerts are handled, the system quarantines the files that contain detected threats to the quarantine panel. You can call this operation to remove quarantined files from the quarantine panel.
        

        @param request: RollbackSuspEventQuaraFileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RollbackSuspEventQuaraFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.quara_field_id):
            query['QuaraFieldId'] = request.quara_field_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSuspEventQuaraFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RollbackSuspEventQuaraFileResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_susp_event_quara_file(self, request):
        """
        ## Description
        When alerts are handled, the system quarantines the files that contain detected threats to the quarantine panel. You can call this operation to remove quarantined files from the quarantine panel.
        

        @param request: RollbackSuspEventQuaraFileRequest

        @return: RollbackSuspEventQuaraFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    def run_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def run_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    def send_verify_code_with_options(self, request, runtime):
        """
        ## Description
        When you attach your workspace network to a Cloud Enterprise Network (CEN) instance in another Alibaba Cloud account, you need to call this operation to obtain a verification code. After the call is successful, the system sends a verification code to the email address associated with the Alibaba Cloud account.
        

        @param request: SendVerifyCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code_action):
            query['VerifyCodeAction'] = request.verify_code_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCode',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SendVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verify_code(self, request):
        """
        ## Description
        When you attach your workspace network to a Cloud Enterprise Network (CEN) instance in another Alibaba Cloud account, you need to call this operation to obtain a verification code. After the call is successful, the system sends a verification code to the email address associated with the Alibaba Cloud account.
        

        @param request: SendVerifyCodeRequest

        @return: SendVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_with_options(request, runtime)

    def set_desktop_group_scale_timer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scale_timer_infos):
            query['ScaleTimerInfos'] = request.scale_timer_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupScaleTimer',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupScaleTimerResponse(),
            self.call_api(params, req, runtime)
        )

    def set_desktop_group_scale_timer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_desktop_group_scale_timer_with_options(request, runtime)

    def set_desktop_group_timer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.timer_type):
            query['TimerType'] = request.timer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupTimer',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupTimerResponse(),
            self.call_api(params, req, runtime)
        )

    def set_desktop_group_timer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_desktop_group_timer_with_options(request, runtime)

    def set_desktop_group_timer_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.timer_type):
            query['TimerType'] = request.timer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupTimerStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupTimerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_desktop_group_timer_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_desktop_group_timer_status_with_options(request, runtime)

    def set_directory_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.enable_sso):
            query['EnableSso'] = request.enable_sso
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDirectorySsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDirectorySsoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_directory_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_directory_sso_status_with_options(request, runtime)

    def set_idp_metadata_with_options(self, request, runtime):
        """
        ## Description
        You can call this operation only for workspaces of the Active Directory (AD) and convenience account types. You cannot call this operation for RAM directories.
        

        @param request: SetIdpMetadataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetIdpMetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIdpMetadata',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetIdpMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    def set_idp_metadata(self, request):
        """
        ## Description
        You can call this operation only for workspaces of the Active Directory (AD) and convenience account types. You cannot call this operation for RAM directories.
        

        @param request: SetIdpMetadataRequest

        @return: SetIdpMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_idp_metadata_with_options(request, runtime)

    def set_office_site_sso_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_sso):
            query['EnableSso'] = request.enable_sso
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOfficeSiteSsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetOfficeSiteSsoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_office_site_sso_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_office_site_sso_status_with_options(request, runtime)

    def set_user_profile_path_rules_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ecd_20200930_models.SetUserProfilePathRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_profile_path_rule):
            request.user_profile_path_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_profile_path_rule, 'UserProfilePathRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_profile_path_rule_shrink):
            query['UserProfilePathRule'] = request.user_profile_path_rule_shrink
        if not UtilClient.is_unset(request.user_profile_rule_type):
            query['UserProfileRuleType'] = request.user_profile_rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserProfilePathRules',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetUserProfilePathRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_user_profile_path_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_profile_path_rules_with_options(request, runtime)

    def start_desktops_with_options(self, request, runtime):
        """
        The cloud desktop to be started must be in the Stopped (Stopped) state.
        

        @param request: StartDesktopsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def start_desktops(self, request):
        """
        The cloud desktop to be started must be in the Stopped (Stopped) state.
        

        @param request: StartDesktopsRequest

        @return: StartDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    def start_virus_scan_task_with_options(self, request, runtime):
        """
        When you call this operation, you must specify a workspace or a cloud desktop by specifying the OfficeSiteId or DesktopId parameter.
        > When you specify a workspace, all cloud desktops within the workspace are scanned.
        

        @param request: StartVirusScanTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartVirusScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVirusScanTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartVirusScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_virus_scan_task(self, request):
        """
        When you call this operation, you must specify a workspace or a cloud desktop by specifying the OfficeSiteId or DesktopId parameter.
        > When you specify a workspace, all cloud desktops within the workspace are scanned.
        

        @param request: StartVirusScanTaskRequest

        @return: StartVirusScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    def stop_desktops_with_options(self, request, runtime):
        """
        The cloud desktop must be in the Running state.
        

        @param request: StopDesktopsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stopped_mode):
            query['StoppedMode'] = request.stopped_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_desktops(self, request):
        """
        The cloud desktop must be in the Running state.
        

        @param request: StopDesktopsRequest

        @return: StopDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    def stop_invocation_with_options(self, request, runtime):
        """
        When you stop a one-time execution of a command, the command continues to run on the cloud desktops where it has started to run, and will not run on the cloud desktops where it has not started to run.
        

        @param request: StopInvocationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopInvocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInvocation',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_invocation(self, request):
        """
        When you stop a one-time execution of a command, the command continues to run on the cloud desktops where it has started to run, and will not run on the cloud desktops where it has not started to run.
        

        @param request: StopInvocationRequest

        @return: StopInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        If TagKey is specified, the new TagValue value overrides the original TagValue value.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        If TagKey is specified, the new TagValue value overrides the original TagValue value.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unlock_virtual_mfadevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UnlockVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_virtual_mfadevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_virtual_mfadevice_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_fota_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        if not UtilClient.is_unset(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFotaTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UpdateFotaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_fota_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_fota_task_with_options(request, runtime)

    def upload_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_security_check):
            query['EnableSecurityCheck'] = request.enable_security_check
        if not UtilClient.is_unset(request.gpu_category):
            query['GpuCategory'] = request.gpu_category
        if not UtilClient.is_unset(request.gpu_driver_type):
            query['GpuDriverType'] = request.gpu_driver_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.oss_object_path):
            query['OssObjectPath'] = request.oss_object_path
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UploadImageResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_image_with_options(request, runtime)

    def verify_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.VerifyCenResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_cen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_cen_with_options(request, runtime)
