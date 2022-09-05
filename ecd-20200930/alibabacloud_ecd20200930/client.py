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
        runtime = util_models.RuntimeOptions()
        return self.activate_office_site_with_options(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_with_options(request, runtime)

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

    def config_adconnector_trust_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
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
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    def create_adconnector_office_site_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_office_site_with_options(request, runtime)

    def create_bundle_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    def create_desktop_group_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
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
        runtime = util_models.RuntimeOptions()
        return self.create_desktop_group_with_options(request, runtime)

    def create_desktops_with_options(self, request, runtime):
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

    def create_drive_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.drive_name):
            query['DriveName'] = request.drive_name
        if not UtilClient.is_unset(request.external_domain_id):
            query['ExternalDomainId'] = request.external_domain_id
        if not UtilClient.is_unset(request.profile_roaming):
            query['ProfileRoaming'] = request.profile_roaming
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.total_size):
            query['TotalSize'] = request.total_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_size):
            query['UsedSize'] = request.used_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrive',
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
            ecd_20200930_models.CreateDriveResponse(),
            self.call_api(params, req, runtime)
        )

    def create_drive(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_drive_with_options(request, runtime)

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
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
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
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
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
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    def create_ramdirectory_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

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

    def delete_directories_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    def delete_drive_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drive_id):
            query['DriveId'] = request.drive_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
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
            ecd_20200930_models.DeleteDriveResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_drive(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_drive_with_options(request, runtime)

    def delete_images_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    def delete_nasfile_systems_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_office_sites_with_options(request, runtime)

    def delete_policy_groups_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_virtual_mfadevice_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

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

    def describe_desktop_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.excluded_end_user_ids):
            query['ExcludedEndUserIds'] = request.excluded_end_user_ids
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
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
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
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
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

    def describe_drives_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_ids):
            query['DomainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrives',
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
            ecd_20200930_models.DescribeDrivesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_drives(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_drives_with_options(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    def describe_grouped_vul_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    def describe_image_modified_records_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.fota_channel):
            query['FotaChannel'] = request.fota_channel
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
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
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    def describe_susp_events_with_options(self, request, runtime):
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

    def describe_users_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_state):
            query['ConnectState'] = request.connect_state
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        runtime = util_models.RuntimeOptions()
        return self.export_desktop_group_info_with_options(request, runtime)

    def export_desktop_list_info_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.export_desktop_list_info_with_options(request, runtime)

    def get_connection_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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

    def list_directory_users_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_ad_organization_units_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.lock_virtual_mfadevice_with_options(request, runtime)

    def modify_adconnector_directory_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    def modify_adconnector_office_site_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_office_site_with_options(request, runtime)

    def modify_bundle_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_bundle_with_options(request, runtime)

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

    def modify_desktop_charge_type_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_charge_type_with_options(request, runtime)

    def modify_desktop_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
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
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_group_with_options(request, runtime)

    def modify_desktop_host_name_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_spec_with_options(request, runtime)

    def modify_desktops_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
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
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    def modify_disk_spec_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    def modify_entitlement_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_image_permission_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_image_permission_with_options(request, runtime)

    def modify_nasdefault_mount_target_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_enabled_with_options(request, runtime)

    def modify_office_site_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
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
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
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
        if not UtilClient.is_unset(request.revoke_access_policy_rule):
            query['RevokeAccessPolicyRule'] = request.revoke_access_policy_rule
        if not UtilClient.is_unset(request.revoke_security_policy_rule):
            query['RevokeSecurityPolicyRule'] = request.revoke_security_policy_rule
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
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
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    def rebuild_desktops_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.rebuild_desktops_with_options(request, runtime)

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
        runtime = util_models.RuntimeOptions()
        return self.reset_nasdefault_mount_target_with_options(request, runtime)

    def reset_snapshot_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    def rollback_susp_event_quara_file_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_with_options(request, runtime)

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

    def set_idp_metadata_with_options(self, request, runtime):
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

    def start_desktops_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    def start_virus_scan_task_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    def stop_desktops_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    def stop_invocation_with_options(self, request, runtime):
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
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
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
