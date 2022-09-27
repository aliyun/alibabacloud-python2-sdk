# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'ecs.aliyuncs.com',
            'ap-northeast-2-pop': 'ecs.aliyuncs.com',
            'cn-beijing-finance-pop': 'ecs.aliyuncs.com',
            'cn-beijing-gov-1': 'ecs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-edge-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'cn-fujian': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-finance': 'ecs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-test-306': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ecs.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-inner': 'ecs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-inner': 'ecs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-wuhan': 'ecs.aliyuncs.com',
            'cn-yushanfang': 'ecs.aliyuncs.com',
            'cn-zhangbei': 'ecs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ecs.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'ecs.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'ecs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_inquired_system_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.choice):
            query['Choice'] = request.choice
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='AcceptInquiredSystemEvent',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AcceptInquiredSystemEventResponse(),
            self.call_api(params, req, runtime)
        )

    def accept_inquired_system_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_inquired_system_event_with_options(request, runtime)

    def activate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_interface_id):
            query['RouterInterfaceId'] = request.router_interface_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateRouterInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ActivateRouterInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def activate_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.activate_router_interface_with_options(request, runtime)

    def add_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_count):
            query['IpCount'] = request.ip_count
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
            action='AddBandwidthPackageIps',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AddBandwidthPackageIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_bandwidth_package_ips_with_options(request, runtime)

    def add_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='AddTags',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    def allocate_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.auto_placement):
            query['AutoPlacement'] = request.auto_placement
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu_over_commit_ratio):
            query['CpuOverCommitRatio'] = request.cpu_over_commit_ratio
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.min_quantity):
            query['MinQuantity'] = request.min_quantity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.network_attributes):
            query['NetworkAttributes'] = request.network_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateDedicatedHosts',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AllocateDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_dedicated_hosts_with_options(request, runtime)

    def allocate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
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
            action='AllocateEipAddress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AllocateEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_with_options(request, runtime)

    def allocate_public_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_address):
            query['IpAddress'] = request.ip_address
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vlan_id):
            query['VlanId'] = request.vlan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicIpAddress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AllocatePublicIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_public_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_ip_address_with_options(request, runtime)

    def apply_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['autoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.disk_ids):
            query['diskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    def assign_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='AssignIpv6Addresses',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssignIpv6AddressesResponse(),
            self.call_api(params, req, runtime)
        )

    def assign_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_ipv_6addresses_with_options(request, runtime)

    def assign_private_ip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_private_ip_address_count):
            query['SecondaryPrivateIpAddressCount'] = request.secondary_private_ip_address_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddresses',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssignPrivateIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    def assign_private_ip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_addresses_with_options(request, runtime)

    def associate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
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
            action='AssociateEipAddress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssociateEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_address_with_options(request, runtime)

    def associate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ha_vip_id):
            query['HaVipId'] = request.ha_vip_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='AssociateHaVip',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssociateHaVipResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_ha_vip_with_options(request, runtime)

    def attach_classic_link_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachClassicLinkVpc',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachClassicLinkVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_classic_link_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_classic_link_vpc_with_options(request, runtime)

    def attach_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bootable):
            query['Bootable'] = request.bootable
        if not UtilClient.is_unset(request.delete_with_instance):
            query['DeleteWithInstance'] = request.delete_with_instance
        if not UtilClient.is_unset(request.device):
            query['Device'] = request.device
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_disk_with_options(request, runtime)

    def attach_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
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
            action='AttachInstanceRamRole',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachInstanceRamRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_instance_ram_role_with_options(request, runtime)

    def attach_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
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
            action='AttachKeyPair',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    def attach_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trunk_network_instance_id):
            query['TrunkNetworkInstanceId'] = request.trunk_network_instance_id
        if not UtilClient.is_unset(request.wait_for_network_configuration_ready):
            query['WaitForNetworkConfigurationReady'] = request.wait_for_network_configuration_ready
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachNetworkInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_network_interface_with_options(request, runtime)

    def authorize_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.ipv_6dest_cidr_ip):
            query['Ipv6DestCidrIp'] = request.ipv_6dest_cidr_ip
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not UtilClient.is_unset(request.source_group_owner_account):
            query['SourceGroupOwnerAccount'] = request.source_group_owner_account
        if not UtilClient.is_unset(request.source_group_owner_id):
            query['SourceGroupOwnerId'] = request.source_group_owner_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.source_prefix_list_id):
            query['SourcePrefixListId'] = request.source_prefix_list_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AuthorizeSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_with_options(request, runtime)

    def authorize_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.dest_group_id):
            query['DestGroupId'] = request.dest_group_id
        if not UtilClient.is_unset(request.dest_group_owner_account):
            query['DestGroupOwnerAccount'] = request.dest_group_owner_account
        if not UtilClient.is_unset(request.dest_group_owner_id):
            query['DestGroupOwnerId'] = request.dest_group_owner_id
        if not UtilClient.is_unset(request.dest_prefix_list_id):
            query['DestPrefixListId'] = request.dest_prefix_list_id
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.ipv_6dest_cidr_ip):
            query['Ipv6DestCidrIp'] = request.ipv_6dest_cidr_ip
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroupEgress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.AuthorizeSecurityGroupEgressResponse(),
            self.call_api(params, req, runtime)
        )

    def authorize_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_egress_with_options(request, runtime)

    def cancel_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.disk_ids):
            query['diskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    def cancel_copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
            action='CancelCopyImage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelCopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_copy_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_copy_image_with_options(request, runtime)

    def cancel_image_pipeline_execution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelImagePipelineExecution',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelImagePipelineExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_image_pipeline_execution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_image_pipeline_execution_with_options(request, runtime)

    def cancel_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPhysicalConnection',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelPhysicalConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_physical_connection_with_options(request, runtime)

    def cancel_simulated_system_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CancelSimulatedSystemEvents',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelSimulatedSystemEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_simulated_system_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_simulated_system_events_with_options(request, runtime)

    def cancel_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    def connect_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_interface_id):
            query['RouterInterfaceId'] = request.router_interface_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConnectRouterInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ConnectRouterInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def connect_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.connect_router_interface_with_options(request, runtime)

    def convert_nat_public_ip_to_eip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ConvertNatPublicIpToEip',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ConvertNatPublicIpToEipResponse(),
            self.call_api(params, req, runtime)
        )

    def convert_nat_public_ip_to_eip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_nat_public_ip_to_eip_with_options(request, runtime)

    def copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_description):
            query['DestinationDescription'] = request.destination_description
        if not UtilClient.is_unset(request.destination_image_name):
            query['DestinationImageName'] = request.destination_image_name
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='CopyImage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    def copy_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_snapshot_description):
            query['DestinationSnapshotDescription'] = request.destination_snapshot_description
        if not UtilClient.is_unset(request.destination_snapshot_name):
            query['DestinationSnapshotName'] = request.destination_snapshot_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopySnapshot',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CopySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_snapshot_with_options(request, runtime)

    def create_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_count):
            query['InstanceCount'] = request.instance_count
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip_address_range):
            query['IpAddressRange'] = request.ip_address_range
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.time_to_live_in_hours):
            query['TimeToLiveInHours'] = request.time_to_live_in_hours
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateActivation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateActivationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_activation_with_options(request, runtime)

    def create_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_name):
            query['AutoProvisioningGroupName'] = request.auto_provisioning_group_name
        if not UtilClient.is_unset(request.auto_provisioning_group_type):
            query['AutoProvisioningGroupType'] = request.auto_provisioning_group_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_disk_config):
            query['DataDiskConfig'] = request.data_disk_config
        if not UtilClient.is_unset(request.default_target_capacity_type):
            query['DefaultTargetCapacityType'] = request.default_target_capacity_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.excess_capacity_termination_policy):
            query['ExcessCapacityTerminationPolicy'] = request.excess_capacity_termination_policy
        if not UtilClient.is_unset(request.hibernation_options_configured):
            query['HibernationOptionsConfigured'] = request.hibernation_options_configured
        if not UtilClient.is_unset(request.launch_template_config):
            query['LaunchTemplateConfig'] = request.launch_template_config
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_spot_price):
            query['MaxSpotPrice'] = request.max_spot_price
        if not UtilClient.is_unset(request.min_target_capacity):
            query['MinTargetCapacity'] = request.min_target_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_as_you_go_allocation_strategy):
            query['PayAsYouGoAllocationStrategy'] = request.pay_as_you_go_allocation_strategy
        if not UtilClient.is_unset(request.pay_as_you_go_target_capacity):
            query['PayAsYouGoTargetCapacity'] = request.pay_as_you_go_target_capacity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_interruption_behavior):
            query['SpotInstanceInterruptionBehavior'] = request.spot_instance_interruption_behavior
        if not UtilClient.is_unset(request.spot_instance_pools_to_use_count):
            query['SpotInstancePoolsToUseCount'] = request.spot_instance_pools_to_use_count
        if not UtilClient.is_unset(request.spot_target_capacity):
            query['SpotTargetCapacity'] = request.spot_target_capacity
        if not UtilClient.is_unset(request.system_disk_config):
            query['SystemDiskConfig'] = request.system_disk_config
        if not UtilClient.is_unset(request.terminate_instances):
            query['TerminateInstances'] = request.terminate_instances
        if not UtilClient.is_unset(request.terminate_instances_with_expiration):
            query['TerminateInstancesWithExpiration'] = request.terminate_instances_with_expiration
        if not UtilClient.is_unset(request.total_target_capacity):
            query['TotalTargetCapacity'] = request.total_target_capacity
        if not UtilClient.is_unset(request.valid_from):
            query['ValidFrom'] = request.valid_from
        if not UtilClient.is_unset(request.valid_until):
            query['ValidUntil'] = request.valid_until
        if not UtilClient.is_unset(request.launch_configuration):
            query['LaunchConfiguration'] = request.launch_configuration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoProvisioningGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateAutoProvisioningGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auto_provisioning_group_with_options(request, runtime)

    def create_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copied_snapshots_retention_days):
            query['CopiedSnapshotsRetentionDays'] = request.copied_snapshots_retention_days
        if not UtilClient.is_unset(request.enable_cross_region_copy):
            query['EnableCrossRegionCopy'] = request.enable_cross_region_copy
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_copy_regions):
            query['TargetCopyRegions'] = request.target_copy_regions
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['autoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['repeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['retentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['timePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    def create_capacity_reservation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_time_type):
            query['EndTimeType'] = request.end_time_type
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_capacity_reservation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_capacity_reservation_with_options(request, runtime)

    def create_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def create_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    def create_dedicated_block_storage_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_name):
            query['DedicatedBlockStorageClusterName'] = request.dedicated_block_storage_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedBlockStorageCluster',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDedicatedBlockStorageClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_block_storage_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_block_storage_cluster_with_options(request, runtime)

    def create_dedicated_host_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostCluster',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDedicatedHostClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_host_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_cluster_with_options(request, runtime)

    def create_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.demand_description):
            query['DemandDescription'] = request.demand_description
        if not UtilClient.is_unset(request.demand_name):
            query['DemandName'] = request.demand_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDemand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def create_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_demand_with_options(request, runtime)

    def create_deployment_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_set_name):
            query['DeploymentSetName'] = request.deployment_set_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.group_count):
            query['GroupCount'] = request.group_count
        if not UtilClient.is_unset(request.on_unable_to_redeploy_failed_instance):
            query['OnUnableToRedeployFailedInstance'] = request.on_unable_to_redeploy_failed_instance
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
        if not UtilClient.is_unset(request.strategy):
            query['Strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeploymentSet',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDeploymentSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_deployment_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_deployment_set_with_options(request, runtime)

    def create_diagnostic_metric_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.metric_ids):
            query['MetricIds'] = request.metric_ids
        if not UtilClient.is_unset(request.metric_set_name):
            query['MetricSetName'] = request.metric_set_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticMetricSet',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDiagnosticMetricSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_diagnostic_metric_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_metric_set_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_set_id):
            query['MetricSetId'] = request.metric_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticReport',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDiagnosticReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def create_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_features):
            query['AdvancedFeatures'] = request.advanced_features
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.encrypt_algorithm):
            query['EncryptAlgorithm'] = request.encrypt_algorithm
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.multi_attach):
            query['MultiAttach'] = request.multi_attach
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_cluster_id):
            query['StorageClusterId'] = request.storage_cluster_id
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disk_with_options(request, runtime)

    def create_elasticity_assurance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assurance_times):
            query['AssuranceTimes'] = request.assurance_times
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticityAssurance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateElasticityAssuranceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_elasticity_assurance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_elasticity_assurance_with_options(request, runtime)

    def create_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.external_port):
            query['ExternalPort'] = request.external_port
        if not UtilClient.is_unset(request.forward_table_id):
            query['ForwardTableId'] = request.forward_table_id
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
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
            action='CreateForwardEntry',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateForwardEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_forward_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_forward_entry_with_options(request, runtime)

    def create_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_address):
            query['IpAddress'] = request.ip_address
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
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHaVip',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateHaVipResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ha_vip_with_options(request, runtime)

    def create_hpc_cluster_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CreateHpcCluster',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateHpcClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hpc_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_hpc_cluster_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture):
            query['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.boot_mode):
            query['BootMode'] = request.boot_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_device_mapping):
            query['DiskDeviceMapping'] = request.disk_device_mapping
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_version):
            query['ImageVersion'] = request.image_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateImageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_image_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.system_type):
            query['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageComponent',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateImageComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_component_with_options(request, runtime)

    def create_image_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.base_image):
            query['BaseImage'] = request.base_image
        if not UtilClient.is_unset(request.base_image_type):
            query['BaseImageType'] = request.base_image_type
        if not UtilClient.is_unset(request.build_content):
            query['BuildContent'] = request.build_content
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_instance_on_failure):
            query['DeleteInstanceOnFailure'] = request.delete_instance_on_failure
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.system_disk_size):
            query['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.to_region_id):
            query['ToRegionId'] = request.to_region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImagePipeline',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateImagePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_pipeline_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.inner_ip_address):
            query['InnerIpAddress'] = request.inner_ip_address
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.node_controller_id):
            query['NodeControllerId'] = request.node_controller_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.use_additional_service):
            query['UseAdditionalService'] = request.use_additional_service
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vlan_id):
            query['VlanId'] = request.vlan_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.hibernation_options):
            query['HibernationOptions'] = request.hibernation_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='CreateKeyPair',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    def create_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    def create_launch_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_vm_os_config):
            query['EnableVmOsConfig'] = request.enable_vm_os_config
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_owner_alias):
            query['ImageOwnerAlias'] = request.image_owner_alias
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_resource_group_id):
            query['TemplateResourceGroupId'] = request.template_resource_group_id
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.version_description):
            query['VersionDescription'] = request.version_description
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLaunchTemplate',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateLaunchTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_launch_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_launch_template_with_options(request, runtime)

    def create_launch_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_vm_os_config):
            query['EnableVmOsConfig'] = request.enable_vm_os_config
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_owner_alias):
            query['ImageOwnerAlias'] = request.image_owner_alias
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.version_description):
            query['VersionDescription'] = request.version_description
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLaunchTemplateVersion',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateLaunchTemplateVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_launch_template_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_launch_template_version_with_options(request, runtime)

    def create_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package):
            query['BandwidthPackage'] = request.bandwidth_package
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNatGateway',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateNatGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def create_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_nat_gateway_with_options(request, runtime)

    def create_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not UtilClient.is_unset(request.network_interface_traffic_mode):
            query['NetworkInterfaceTrafficMode'] = request.network_interface_traffic_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.primary_ip_address):
            query['PrimaryIpAddress'] = request.primary_ip_address
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.queue_number):
            query['QueueNumber'] = request.queue_number
        if not UtilClient.is_unset(request.queue_pair_number):
            query['QueuePairNumber'] = request.queue_pair_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.secondary_private_ip_address_count):
            query['SecondaryPrivateIpAddressCount'] = request.secondary_private_ip_address_count
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.visible):
            query['Visible'] = request.visible
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_interface_with_options(request, runtime)

    def create_network_interface_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CreateNetworkInterfacePermission',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateNetworkInterfacePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_network_interface_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_interface_permission_with_options(request, runtime)

    def create_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.circuit_code):
            query['CircuitCode'] = request.circuit_code
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.line_operator):
            query['LineOperator'] = request.line_operator
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_location):
            query['PeerLocation'] = request.peer_location
        if not UtilClient.is_unset(request.port_type):
            query['PortType'] = request.port_type
        if not UtilClient.is_unset(request.redundant_physical_connection_id):
            query['RedundantPhysicalConnectionId'] = request.redundant_physical_connection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.bandwidth):
            query['bandwidth'] = request.bandwidth
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePhysicalConnection',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreatePhysicalConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_physical_connection_with_options(request, runtime)

    def create_prefix_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_family):
            query['AddressFamily'] = request.address_family
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.entry):
            query['Entry'] = request.entry
        if not UtilClient.is_unset(request.max_entries):
            query['MaxEntries'] = request.max_entries
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_name):
            query['PrefixListName'] = request.prefix_list_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CreatePrefixList',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreatePrefixListResponse(),
            self.call_api(params, req, runtime)
        )

    def create_prefix_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_prefix_list_with_options(request, runtime)

    def create_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.next_hop_id):
            query['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_list):
            query['NextHopList'] = request.next_hop_list
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
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
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRouteEntry',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_route_entry_with_options(request, runtime)

    def create_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not UtilClient.is_unset(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opposite_access_point_id):
            query['OppositeAccessPointId'] = request.opposite_access_point_id
        if not UtilClient.is_unset(request.opposite_interface_id):
            query['OppositeInterfaceId'] = request.opposite_interface_id
        if not UtilClient.is_unset(request.opposite_interface_owner_id):
            query['OppositeInterfaceOwnerId'] = request.opposite_interface_owner_id
        if not UtilClient.is_unset(request.opposite_region_id):
            query['OppositeRegionId'] = request.opposite_region_id
        if not UtilClient.is_unset(request.opposite_router_id):
            query['OppositeRouterId'] = request.opposite_router_id
        if not UtilClient.is_unset(request.opposite_router_type):
            query['OppositeRouterType'] = request.opposite_router_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.router_type):
            query['RouterType'] = request.router_type
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRouterInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateRouterInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_router_interface_with_options(request, runtime)

    def create_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        if not UtilClient.is_unset(request.security_group_type):
            query['SecurityGroupType'] = request.security_group_type
        if not UtilClient.is_unset(request.service_managed):
            query['ServiceManaged'] = request.service_managed
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_security_group_with_options(request, runtime)

    def create_simulated_system_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.not_before):
            query['NotBefore'] = request.not_before
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='CreateSimulatedSystemEvents',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSimulatedSystemEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_simulated_system_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_simulated_system_events_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instant_access):
            query['InstantAccess'] = request.instant_access
        if not UtilClient.is_unset(request.instant_access_retention_days):
            query['InstantAccessRetentionDays'] = request.instant_access_retention_days
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def create_snapshot_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.exclude_disk_id):
            query['ExcludeDiskId'] = request.exclude_disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instant_access):
            query['InstantAccess'] = request.instant_access
        if not UtilClient.is_unset(request.instant_access_retention_days):
            query['InstantAccessRetentionDays'] = request.instant_access_retention_days
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='CreateSnapshotGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSnapshotGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_snapshot_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_group_with_options(request, runtime)

    def create_storage_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_partition_number):
            query['MaxPartitionNumber'] = request.max_partition_number
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
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStorageSet',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateStorageSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_storage_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_storage_set_with_options(request, runtime)

    def create_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVSwitch',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vswitch_with_options(request, runtime)

    def create_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.circuit_code):
            query['CircuitCode'] = request.circuit_code
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.local_gateway_ip):
            query['LocalGatewayIp'] = request.local_gateway_ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_gateway_ip):
            query['PeerGatewayIp'] = request.peer_gateway_ip
        if not UtilClient.is_unset(request.peering_subnet_mask):
            query['PeeringSubnetMask'] = request.peering_subnet_mask
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vbr_owner_id):
            query['VbrOwnerId'] = request.vbr_owner_id
        if not UtilClient.is_unset(request.vlan_id):
            query['VlanId'] = request.vlan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualBorderRouter',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateVirtualBorderRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_border_router_with_options(request, runtime)

    def create_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpc',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_with_options(request, runtime)

    def deactivate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_interface_id):
            query['RouterInterfaceId'] = request.router_interface_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateRouterInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeactivateRouterInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def deactivate_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deactivate_router_interface_with_options(request, runtime)

    def delete_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activation_id):
            query['ActivationId'] = request.activation_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteActivation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteActivationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_activation_with_options(request, runtime)

    def delete_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
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
        if not UtilClient.is_unset(request.terminate_instances):
            query['TerminateInstances'] = request.terminate_instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoProvisioningGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteAutoProvisioningGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_provisioning_group_with_options(request, runtime)

    def delete_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['autoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
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
            action='DeleteBandwidthPackage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    def delete_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteCommand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    def delete_dedicated_host_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
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
            action='DeleteDedicatedHostCluster',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDedicatedHostClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dedicated_host_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_cluster_with_options(request, runtime)

    def delete_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
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
            action='DeleteDemand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_demand_with_options(request, runtime)

    def delete_deployment_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
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
            action='DeleteDeploymentSet',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDeploymentSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_deployment_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_deployment_set_with_options(request, runtime)

    def delete_diagnostic_metric_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_set_ids):
            query['MetricSetIds'] = request.metric_set_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiagnosticMetricSets',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDiagnosticMetricSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_diagnostic_metric_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_diagnostic_metric_sets_with_options(request, runtime)

    def delete_diagnostic_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.report_ids):
            query['ReportIds'] = request.report_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiagnosticReports',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDiagnosticReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_diagnostic_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_diagnostic_reports_with_options(request, runtime)

    def delete_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
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
            action='DeleteDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_with_options(request, runtime)

    def delete_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_table_id):
            query['ForwardTableId'] = request.forward_table_id
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
            action='DeleteForwardEntry',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteForwardEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_forward_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_forward_entry_with_options(request, runtime)

    def delete_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ha_vip_id):
            query['HaVipId'] = request.ha_vip_id
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
            action='DeleteHaVip',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteHaVipResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ha_vip_with_options(request, runtime)

    def delete_hpc_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteHpcCluster',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteHpcClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hpc_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_hpc_cluster_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
            action='DeleteImage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_image_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_component_id):
            query['ImageComponentId'] = request.image_component_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteImageComponent',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteImageComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_component_with_options(request, runtime)

    def delete_image_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_pipeline_id):
            query['ImagePipelineId'] = request.image_pipeline_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteImagePipeline',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteImagePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_pipeline_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.terminate_subscription):
            query['TerminateSubscription'] = request.terminate_subscription
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.terminate_subscription):
            query['TerminateSubscription'] = request.terminate_subscription
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instances_with_options(request, runtime)

    def delete_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_names):
            query['KeyPairNames'] = request.key_pair_names
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
            action='DeleteKeyPairs',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_key_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    def delete_launch_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
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
            action='DeleteLaunchTemplate',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteLaunchTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_launch_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_launch_template_with_options(request, runtime)

    def delete_launch_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_version):
            query['DeleteVersion'] = request.delete_version
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
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
            action='DeleteLaunchTemplateVersion',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteLaunchTemplateVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_launch_template_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_launch_template_version_with_options(request, runtime)

    def delete_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
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
            action='DeleteNatGateway',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteNatGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_gateway_with_options(request, runtime)

    def delete_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteNetworkInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_interface_with_options(request, runtime)

    def delete_network_interface_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.network_interface_permission_id):
            query['NetworkInterfacePermissionId'] = request.network_interface_permission_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeleteNetworkInterfacePermission',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteNetworkInterfacePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_network_interface_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_interface_permission_with_options(request, runtime)

    def delete_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
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
            action='DeletePhysicalConnection',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeletePhysicalConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_connection_with_options(request, runtime)

    def delete_prefix_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeletePrefixList',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeletePrefixListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prefix_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prefix_list_with_options(request, runtime)

    def delete_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.next_hop_id):
            query['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_list):
            query['NextHopList'] = request.next_hop_list
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
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteEntry',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_route_entry_with_options(request, runtime)

    def delete_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.router_interface_id):
            query['RouterInterfaceId'] = request.router_interface_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouterInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteRouterInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_router_interface_with_options(request, runtime)

    def delete_security_group_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_snapshot_group_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.snapshot_group_id):
            query['SnapshotGroupId'] = request.snapshot_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteSnapshotGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_group_with_options(request, runtime)

    def delete_storage_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStorageSet',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteStorageSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_storage_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_storage_set_with_options(request, runtime)

    def delete_vswitch_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVSwitch',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    def delete_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualBorderRouter',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteVirtualBorderRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_border_router_with_options(request, runtime)

    def delete_vpc_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpc',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_with_options(request, runtime)

    def deregister_managed_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DeregisterManagedInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeregisterManagedInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_managed_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_managed_instance_with_options(request, runtime)

    def describe_access_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessPoints',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_points(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_points_with_options(request, runtime)

    def describe_account_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAttributes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAccountAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_account_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_attributes_with_options(request, runtime)

    def describe_activations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activation_id):
            query['ActivationId'] = request.activation_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
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
            action='DescribeActivations',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeActivationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_activations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_activations_with_options(request, runtime)

    def describe_auto_provisioning_group_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoProvisioningGroupHistory',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_provisioning_group_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_history_with_options(request, runtime)

    def describe_auto_provisioning_group_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoProvisioningGroupInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_provisioning_group_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_instances_with_options(request, runtime)

    def describe_auto_provisioning_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
        if not UtilClient.is_unset(request.auto_provisioning_group_name):
            query['AutoProvisioningGroupName'] = request.auto_provisioning_group_name
        if not UtilClient.is_unset(request.auto_provisioning_group_status):
            query['AutoProvisioningGroupStatus'] = request.auto_provisioning_group_status
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoProvisioningGroups',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoProvisioningGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_provisioning_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_groups_with_options(request, runtime)

    def describe_auto_snapshot_policy_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='DescribeAutoSnapshotPolicyEx',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_snapshot_policy_ex(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policy_ex_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.data_disk_category):
            query['DataDiskCategory'] = request.data_disk_category
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.destination_resource):
            query['DestinationResource'] = request.destination_resource
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_category):
            query['NetworkCategory'] = request.network_category
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_bandwidth_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
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
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthLimitation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeBandwidthLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bandwidth_limitation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_limitation_with_options(request, runtime)

    def describe_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthPackages',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_packages_with_options(request, runtime)

    def describe_capacity_reservation_instances_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityReservationInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCapacityReservationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_capacity_reservation_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservation_instances_with_options(request, runtime)

    def describe_capacity_reservations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCapacityReservations',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCapacityReservationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_capacity_reservations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservations_with_options(request, runtime)

    def describe_classic_link_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClassicLinkInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeClassicLinkInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_classic_link_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_classic_link_instances_with_options(request, runtime)

    def describe_cloud_assistant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
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
            action='DescribeCloudAssistantStatus',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCloudAssistantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_assistant_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    def describe_clusters_with_options(self, request, runtime):
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusters',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    def describe_commands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.latest):
            query['Latest'] = request.latest
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommands',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_commands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_commands_with_options(request, runtime)

    def describe_dedicated_block_storage_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_id):
            query['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusters',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedBlockStorageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_block_storage_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_block_storage_clusters_with_options(request, runtime)

    def describe_dedicated_host_auto_renew_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
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
            action='DescribeDedicatedHostAutoRenew',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_auto_renew(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_auto_renew_with_options(request, runtime)

    def describe_dedicated_host_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_ids):
            query['DedicatedHostClusterIds'] = request.dedicated_host_cluster_ids
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostClusters',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_clusters_with_options(request, runtime)

    def describe_dedicated_host_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
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
        if not UtilClient.is_unset(request.supported_instance_type_family):
            query['SupportedInstanceTypeFamily'] = request.supported_instance_type_family
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHostTypes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_host_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_types_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_demands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.demand_status):
            query['DemandStatus'] = request.demand_status
        if not UtilClient.is_unset(request.demand_type):
            query['DemandType'] = request.demand_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDemands',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDemandsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_demands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_demands_with_options(request, runtime)

    def describe_deployment_set_supported_instance_type_family_with_options(self, request, runtime):
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeploymentSetSupportedInstanceTypeFamily',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deployment_set_supported_instance_type_family(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_set_supported_instance_type_family_with_options(request, runtime)

    def describe_deployment_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_set_ids):
            query['DeploymentSetIds'] = request.deployment_set_ids
        if not UtilClient.is_unset(request.deployment_set_name):
            query['DeploymentSetName'] = request.deployment_set_name
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
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
        if not UtilClient.is_unset(request.strategy):
            query['Strategy'] = request.strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeploymentSets',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDeploymentSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deployment_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_sets_with_options(request, runtime)

    def describe_diagnostic_metric_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.metric_set_ids):
            query['MetricSetIds'] = request.metric_set_ids
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticMetricSets',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDiagnosticMetricSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnostic_metric_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_metric_sets_with_options(request, runtime)

    def describe_diagnostic_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.metric_ids):
            query['MetricIds'] = request.metric_ids
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticMetrics',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDiagnosticMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnostic_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_metrics_with_options(request, runtime)

    def describe_diagnostic_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.report_ids):
            query['ReportIds'] = request.report_ids
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticReports',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDiagnosticReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnostic_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_reports_with_options(request, runtime)

    def describe_disk_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDiskMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_disk_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_with_options(request, runtime)

    def describe_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_attributes):
            query['AdditionalAttributes'] = request.additional_attributes
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.delete_auto_snapshot):
            query['DeleteAutoSnapshot'] = request.delete_auto_snapshot
        if not UtilClient.is_unset(request.delete_with_instance):
            query['DeleteWithInstance'] = request.delete_with_instance
        if not UtilClient.is_unset(request.disk_charge_type):
            query['DiskChargeType'] = request.disk_charge_type
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_auto_snapshot):
            query['EnableAutoSnapshot'] = request.enable_auto_snapshot
        if not UtilClient.is_unset(request.enable_automated_snapshot_policy):
            query['EnableAutomatedSnapshotPolicy'] = request.enable_automated_snapshot_policy
        if not UtilClient.is_unset(request.enable_shared):
            query['EnableShared'] = request.enable_shared
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.multi_attach):
            query['MultiAttach'] = request.multi_attach
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.portable):
            query['Portable'] = request.portable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDisks',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDisksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_disks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_with_options(request, runtime)

    def describe_disks_full_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.event_time):
            query['EventTime'] = request.event_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDisksFullStatus',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDisksFullStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_disks_full_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_full_status_with_options(request, runtime)

    def describe_eip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.associated_instance_id):
            query['AssociatedInstanceId'] = request.associated_instance_id
        if not UtilClient.is_unset(request.associated_instance_type):
            query['AssociatedInstanceType'] = request.associated_instance_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.eip_address):
            query['EipAddress'] = request.eip_address
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
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
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEipAddresses',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeEipAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_eip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_addresses_with_options(request, runtime)

    def describe_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEipMonitorData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeEipMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_monitor_data_with_options(request, runtime)

    def describe_elasticity_assurance_instances_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticityAssuranceInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_elasticity_assurance_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elasticity_assurance_instances_with_options(request, runtime)

    def describe_elasticity_assurances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticityAssurances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeElasticityAssurancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_elasticity_assurances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elasticity_assurances_with_options(request, runtime)

    def describe_eni_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.eni_id):
            query['EniId'] = request.eni_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEniMonitorData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeEniMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_eni_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eni_monitor_data_with_options(request, runtime)

    def describe_forward_table_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_table_id):
            query['ForwardTableId'] = request.forward_table_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeForwardTableEntries',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeForwardTableEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_forward_table_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_forward_table_entries_with_options(request, runtime)

    def describe_ha_vips_with_options(self, request, runtime):
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
            action='DescribeHaVips',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeHaVipsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ha_vips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ha_vips_with_options(request, runtime)

    def describe_hpc_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.hpc_cluster_ids):
            query['HpcClusterIds'] = request.hpc_cluster_ids
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
            action='DescribeHpcClusters',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeHpcClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hpc_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hpc_clusters_with_options(request, runtime)

    def describe_image_components_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_component_id):
            query['ImageComponentId'] = request.image_component_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='DescribeImageComponents',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_components(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_components_with_options(request, runtime)

    def describe_image_from_family_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
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
            action='DescribeImageFromFamily',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageFromFamilyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_from_family(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_from_family_with_options(request, runtime)

    def describe_image_pipeline_executions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not UtilClient.is_unset(request.image_pipeline_id):
            query['ImagePipelineId'] = request.image_pipeline_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePipelineExecutions',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImagePipelineExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_pipeline_executions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_pipeline_executions_with_options(request, runtime)

    def describe_image_pipelines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_pipeline_id):
            query['ImagePipelineId'] = request.image_pipeline_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='DescribeImagePipelines',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImagePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_pipelines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_pipelines_with_options(request, runtime)

    def describe_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageSharePermission',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_share_permission_with_options(request, runtime)

    def describe_image_support_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
            action='DescribeImageSupportInstanceTypes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageSupportInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_support_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_support_instance_types_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.architecture):
            query['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_owner_alias):
            query['ImageOwnerAlias'] = request.image_owner_alias
        if not UtilClient.is_unset(request.image_owner_id):
            query['ImageOwnerId'] = request.image_owner_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_public):
            query['IsPublic'] = request.is_public
        if not UtilClient.is_unset(request.is_support_cloudinit):
            query['IsSupportCloudinit'] = request.is_support_cloudinit
        if not UtilClient.is_unset(request.is_support_io_optimized):
            query['IsSupportIoOptimized'] = request.is_support_io_optimized
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.show_expired):
            query['ShowExpired'] = request.show_expired
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImages',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def describe_instance_attachment_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttachmentAttributes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_attachment_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attachment_attributes_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstanceAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    def describe_instance_history_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_cycle_status):
            query['EventCycleStatus'] = request.event_cycle_status
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.impact_level):
            query['ImpactLevel'] = request.impact_level
        if not UtilClient.is_unset(request.instance_event_cycle_status):
            query['InstanceEventCycleStatus'] = request.instance_event_cycle_status
        if not UtilClient.is_unset(request.instance_event_type):
            query['InstanceEventType'] = request.instance_event_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        if not UtilClient.is_unset(request.event_publish_time):
            query['EventPublishTime'] = request.event_publish_time
        if not UtilClient.is_unset(request.not_before):
            query['NotBefore'] = request.not_before
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceHistoryEvents',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceHistoryEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_history_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_history_events_with_options(request, runtime)

    def describe_instance_maintenance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMaintenanceAttributes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_maintenance_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_maintenance_attributes_with_options(request, runtime)

    def describe_instance_modification_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
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
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceModificationPrice',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceModificationPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_modification_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_modification_price_with_options(request, runtime)

    def describe_instance_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMonitorData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_monitor_data_with_options(request, runtime)

    def describe_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
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
            action='DescribeInstanceRamRole',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceRamRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ram_role_with_options(request, runtime)

    def describe_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStatus',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    def describe_instance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
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
            action='DescribeInstanceTopology',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_topology_with_options(request, runtime)

    def describe_instance_type_families_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.generation):
            query['Generation'] = request.generation
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
            action='DescribeInstanceTypeFamilies',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceTypeFamiliesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_type_families(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_families_with_options(request, runtime)

    def describe_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_architecture):
            query['CpuArchitecture'] = request.cpu_architecture
        if not UtilClient.is_unset(request.gpuspec):
            query['GPUSpec'] = request.gpuspec
        if not UtilClient.is_unset(request.instance_category):
            query['InstanceCategory'] = request.instance_category
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.local_storage_category):
            query['LocalStorageCategory'] = request.local_storage_category
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.maximum_cpu_core_count):
            query['MaximumCpuCoreCount'] = request.maximum_cpu_core_count
        if not UtilClient.is_unset(request.maximum_cpu_speed_frequency):
            query['MaximumCpuSpeedFrequency'] = request.maximum_cpu_speed_frequency
        if not UtilClient.is_unset(request.maximum_cpu_turbo_frequency):
            query['MaximumCpuTurboFrequency'] = request.maximum_cpu_turbo_frequency
        if not UtilClient.is_unset(request.maximum_gpuamount):
            query['MaximumGPUAmount'] = request.maximum_gpuamount
        if not UtilClient.is_unset(request.maximum_memory_size):
            query['MaximumMemorySize'] = request.maximum_memory_size
        if not UtilClient.is_unset(request.minimum_baseline_credit):
            query['MinimumBaselineCredit'] = request.minimum_baseline_credit
        if not UtilClient.is_unset(request.minimum_cpu_core_count):
            query['MinimumCpuCoreCount'] = request.minimum_cpu_core_count
        if not UtilClient.is_unset(request.minimum_cpu_speed_frequency):
            query['MinimumCpuSpeedFrequency'] = request.minimum_cpu_speed_frequency
        if not UtilClient.is_unset(request.minimum_cpu_turbo_frequency):
            query['MinimumCpuTurboFrequency'] = request.minimum_cpu_turbo_frequency
        if not UtilClient.is_unset(request.minimum_disk_quantity):
            query['MinimumDiskQuantity'] = request.minimum_disk_quantity
        if not UtilClient.is_unset(request.minimum_eni_ipv_6address_quantity):
            query['MinimumEniIpv6AddressQuantity'] = request.minimum_eni_ipv_6address_quantity
        if not UtilClient.is_unset(request.minimum_eni_private_ip_address_quantity):
            query['MinimumEniPrivateIpAddressQuantity'] = request.minimum_eni_private_ip_address_quantity
        if not UtilClient.is_unset(request.minimum_eni_quantity):
            query['MinimumEniQuantity'] = request.minimum_eni_quantity
        if not UtilClient.is_unset(request.minimum_eri_quantity):
            query['MinimumEriQuantity'] = request.minimum_eri_quantity
        if not UtilClient.is_unset(request.minimum_gpuamount):
            query['MinimumGPUAmount'] = request.minimum_gpuamount
        if not UtilClient.is_unset(request.minimum_initial_credit):
            query['MinimumInitialCredit'] = request.minimum_initial_credit
        if not UtilClient.is_unset(request.minimum_instance_bandwidth_rx):
            query['MinimumInstanceBandwidthRx'] = request.minimum_instance_bandwidth_rx
        if not UtilClient.is_unset(request.minimum_instance_bandwidth_tx):
            query['MinimumInstanceBandwidthTx'] = request.minimum_instance_bandwidth_tx
        if not UtilClient.is_unset(request.minimum_instance_pps_rx):
            query['MinimumInstancePpsRx'] = request.minimum_instance_pps_rx
        if not UtilClient.is_unset(request.minimum_instance_pps_tx):
            query['MinimumInstancePpsTx'] = request.minimum_instance_pps_tx
        if not UtilClient.is_unset(request.minimum_local_storage_amount):
            query['MinimumLocalStorageAmount'] = request.minimum_local_storage_amount
        if not UtilClient.is_unset(request.minimum_local_storage_capacity):
            query['MinimumLocalStorageCapacity'] = request.minimum_local_storage_capacity
        if not UtilClient.is_unset(request.minimum_memory_size):
            query['MinimumMemorySize'] = request.minimum_memory_size
        if not UtilClient.is_unset(request.minimum_primary_eni_queue_number):
            query['MinimumPrimaryEniQueueNumber'] = request.minimum_primary_eni_queue_number
        if not UtilClient.is_unset(request.minimum_queue_pair_number):
            query['MinimumQueuePairNumber'] = request.minimum_queue_pair_number
        if not UtilClient.is_unset(request.minimum_secondary_eni_queue_number):
            query['MinimumSecondaryEniQueueNumber'] = request.minimum_secondary_eni_queue_number
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.nvme_support):
            query['NvmeSupport'] = request.nvme_support
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physical_processor_model):
            query['PhysicalProcessorModel'] = request.physical_processor_model
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    def describe_instance_vnc_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstanceVncPasswd',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceVncPasswdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_vnc_passwd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_passwd_with_options(request, runtime)

    def describe_instance_vnc_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeInstanceVncUrl',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceVncUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_vnc_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_attributes):
            query['AdditionalAttributes'] = request.additional_attributes
        if not UtilClient.is_unset(request.device_available):
            query['DeviceAvailable'] = request.device_available
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.eip_addresses):
            query['EipAddresses'] = request.eip_addresses
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.inner_ip_addresses):
            query['InnerIpAddresses'] = request.inner_ip_addresses
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.need_sale_cycle):
            query['NeedSaleCycle'] = request.need_sale_cycle
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip_addresses):
            query['PrivateIpAddresses'] = request.private_ip_addresses
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.rdma_ip_addresses):
            query['RdmaIpAddresses'] = request.rdma_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_instances_full_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_event_type):
            query['InstanceEventType'] = request.instance_event_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.event_publish_time):
            query['EventPublishTime'] = request.event_publish_time
        if not UtilClient.is_unset(request.not_before):
            query['NotBefore'] = request.not_before
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancesFullStatus',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstancesFullStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances_full_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_full_status_with_options(request, runtime)

    def describe_invocation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.include_history):
            query['IncludeHistory'] = request.include_history
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.invoke_record_status):
            query['InvokeRecordStatus'] = request.invoke_record_status
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeInvocationResults',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInvocationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_invocation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_results_with_options(request, runtime)

    def describe_invocations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.include_output):
            query['IncludeOutput'] = request.include_output
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_mode):
            query['RepeatMode'] = request.repeat_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.timed):
            query['Timed'] = request.timed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_invocations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    def describe_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_finger_print):
            query['KeyPairFingerPrint'] = request.key_pair_finger_print
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='DescribeKeyPairs',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_key_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    def describe_launch_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_version):
            query['DefaultVersion'] = request.default_version
        if not UtilClient.is_unset(request.detail_flag):
            query['DetailFlag'] = request.detail_flag
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_version):
            query['MaxVersion'] = request.max_version
        if not UtilClient.is_unset(request.min_version):
            query['MinVersion'] = request.min_version
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLaunchTemplateVersions',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeLaunchTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_launch_template_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_launch_template_versions_with_options(request, runtime)

    def describe_launch_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
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
        if not UtilClient.is_unset(request.template_resource_group_id):
            query['TemplateResourceGroupId'] = request.template_resource_group_id
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLaunchTemplates',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeLaunchTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_launch_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_launch_templates_with_options(request, runtime)

    def describe_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limitation):
            query['Limitation'] = request.limitation
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
            action='DescribeLimitation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_limitation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    def describe_managed_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activation_id):
            query['ActivationId'] = request.activation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
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
            action='DescribeManagedInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeManagedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_managed_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_managed_instances_with_options(request, runtime)

    def describe_nat_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatGateways',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNatGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nat_gateways(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_gateways_with_options(request, runtime)

    def describe_network_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute):
            query['Attribute'] = request.attribute
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeNetworkInterfaceAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interface_attribute_with_options(request, runtime)

    def describe_network_interface_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.network_interface_permission_id):
            query['NetworkInterfacePermissionId'] = request.network_interface_permission_id
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
            action='DescribeNetworkInterfacePermissions',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_interface_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interface_permissions_with_options(request, runtime)

    def describe_network_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.primary_ip_address):
            query['PrimaryIpAddress'] = request.primary_ip_address
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.service_managed):
            query['ServiceManaged'] = request.service_managed
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInterfaces',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_network_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interfaces_with_options(request, runtime)

    def describe_new_project_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewProjectEipMonitorData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_new_project_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_new_project_eip_monitor_data_with_options(request, runtime)

    def describe_physical_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePhysicalConnections',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePhysicalConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_physical_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_physical_connections_with_options(request, runtime)

    def describe_prefix_list_associations_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribePrefixListAssociations',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePrefixListAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_prefix_list_associations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_list_associations_with_options(request, runtime)

    def describe_prefix_list_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribePrefixListAttributes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePrefixListAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_prefix_list_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_list_attributes_with_options(request, runtime)

    def describe_prefix_lists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_family):
            query['AddressFamily'] = request.address_family
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.prefix_list_name):
            query['PrefixListName'] = request.prefix_list_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribePrefixLists',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePrefixListsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_prefix_lists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_lists_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.assurance_times):
            query['AssuranceTimes'] = request.assurance_times
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.dedicated_host_type):
            query['DedicatedHostType'] = request.dedicated_host_type
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_cpu_core_count):
            query['InstanceCpuCoreCount'] = request.instance_cpu_core_count
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.price_unit):
            query['PriceUnit'] = request.price_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_recommend_instance_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.max_price):
            query['MaxPrice'] = request.max_price
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority_strategy):
            query['PriorityStrategy'] = request.priority_strategy
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.system_disk_category):
            query['SystemDiskCategory'] = request.system_disk_category
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_match_mode):
            query['ZoneMatchMode'] = request.zone_match_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendInstanceType',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRecommendInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_instance_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_instance_type_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeRegions',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expected_renew_day):
            query['ExpectedRenewDay'] = request.expected_renew_day
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.price_unit):
            query['PriceUnit'] = request.price_unit
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenewalPrice',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRenewalPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_type):
            query['AllocationType'] = request.allocation_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.lock_reason):
            query['LockReason'] = request.lock_reason
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReservedInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeReservedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instances_with_options(request, runtime)

    def describe_resource_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceByTags',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeResourceByTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_by_tags_with_options(request, runtime)

    def describe_resources_modification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.destination_resource):
            query['DestinationResource'] = request.destination_resource
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.migrate_across_zone):
            query['MigrateAcrossZone'] = request.migrate_across_zone
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcesModification',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeResourcesModificationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resources_modification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resources_modification_with_options(request, runtime)

    def describe_route_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        if not UtilClient.is_unset(request.route_table_name):
            query['RouteTableName'] = request.route_table_name
        if not UtilClient.is_unset(request.router_id):
            query['RouterId'] = request.router_id
        if not UtilClient.is_unset(request.router_type):
            query['RouterType'] = request.router_type
        if not UtilClient.is_unset(request.vrouter_id):
            query['VRouterId'] = request.vrouter_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouteTables',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRouteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_route_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_route_tables_with_options(request, runtime)

    def describe_router_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRouterInterfaces',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRouterInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_router_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_router_interfaces_with_options(request, runtime)

    def describe_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSecurityGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_attribute_with_options(request, runtime)

    def describe_security_group_references_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupReferences',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSecurityGroupReferencesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_group_references(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_references_with_options(request, runtime)

    def describe_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.fuzzy_query):
            query['FuzzyQuery'] = request.fuzzy_query
        if not UtilClient.is_unset(request.is_query_ecs_count):
            query['IsQueryEcsCount'] = request.is_query_ecs_count
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        if not UtilClient.is_unset(request.security_group_type):
            query['SecurityGroupType'] = request.security_group_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroups',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    def describe_send_file_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='DescribeSendFileResults',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSendFileResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_send_file_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_send_file_results_with_options(request, runtime)

    def describe_snapshot_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_attributes):
            query['AdditionalAttributes'] = request.additional_attributes
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_group_id):
            query['SnapshotGroupId'] = request.snapshot_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshotGroups',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshot_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_groups_with_options(request, runtime)

    def describe_snapshot_links_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.snapshot_link_ids):
            query['SnapshotLinkIds'] = request.snapshot_link_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshotLinks',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotLinksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshot_links(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_links_with_options(request, runtime)

    def describe_snapshot_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshotMonitorData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshot_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_monitor_data_with_options(request, runtime)

    def describe_snapshot_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshotPackage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshot_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_package_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_link_id):
            query['SnapshotLinkId'] = request.snapshot_link_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.usage):
            query['Usage'] = request.usage
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_snapshots_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeSnapshotsUsage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotsUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshots_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_usage_with_options(request, runtime)

    def describe_spot_advice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cores):
            query['Cores'] = request.cores
        if not UtilClient.is_unset(request.gpu_amount):
            query['GpuAmount'] = request.gpu_amount
        if not UtilClient.is_unset(request.gpu_spec):
            query['GpuSpec'] = request.gpu_spec
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.min_cores):
            query['MinCores'] = request.min_cores
        if not UtilClient.is_unset(request.min_memory):
            query['MinMemory'] = request.min_memory
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpotAdvice',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSpotAdviceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_spot_advice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_advice_with_options(request, runtime)

    def describe_spot_price_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpotPriceHistory',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSpotPriceHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_spot_price_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_price_history_with_options(request, runtime)

    def describe_storage_capacity_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_type):
            query['AllocationType'] = request.allocation_type
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.storage_capacity_unit_id):
            query['StorageCapacityUnitId'] = request.storage_capacity_unit_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageCapacityUnits',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeStorageCapacityUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_storage_capacity_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_capacity_units_with_options(request, runtime)

    def describe_storage_set_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageSetDetails',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeStorageSetDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_storage_set_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_set_details_with_options(request, runtime)

    def describe_storage_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.storage_set_ids):
            query['StorageSetIds'] = request.storage_set_ids
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStorageSets',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeStorageSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_storage_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_sets_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
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
            action='DescribeTags',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_task_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_task_attribute_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def describe_user_business_behavior_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.status_key):
            query['statusKey'] = request.status_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBusinessBehavior',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeUserBusinessBehaviorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_business_behavior(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_business_behavior_with_options(request, runtime)

    def describe_user_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DescribeUserData',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeUserDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_data_with_options(request, runtime)

    def describe_vrouters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vrouter_id):
            query['VRouterId'] = request.vrouter_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVRouters',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVRoutersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vrouters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vrouters_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
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
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    def describe_virtual_border_routers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualBorderRouters',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVirtualBorderRoutersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_virtual_border_routers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_with_options(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
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
            action='DescribeVirtualBorderRoutersForPhysicalConnection',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_virtual_border_routers_for_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    def describe_vpcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vpcs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
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
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def detach_classic_link_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachClassicLinkVpc',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachClassicLinkVpcResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_classic_link_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_classic_link_vpc_with_options(request, runtime)

    def detach_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_with_instance):
            query['DeleteWithInstance'] = request.delete_with_instance
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='DetachDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_disk_with_options(request, runtime)

    def detach_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
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
            action='DetachInstanceRamRole',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachInstanceRamRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_instance_ram_role_with_options(request, runtime)

    def detach_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
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
            action='DetachKeyPair',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    def detach_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trunk_network_instance_id):
            query['TrunkNetworkInstanceId'] = request.trunk_network_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachNetworkInterface',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_network_interface_with_options(request, runtime)

    def disable_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.activation_id):
            query['ActivationId'] = request.activation_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DisableActivation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.DisableActivationResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_activation_with_options(request, runtime)

    def eip_fill_params_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EipFillParams',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.EipFillParamsResponse(),
            self.call_api(params, req, runtime)
        )

    def eip_fill_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_params_with_options(request, runtime)

    def eip_fill_product_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EipFillProduct',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.EipFillProductResponse(),
            self.call_api(params, req, runtime)
        )

    def eip_fill_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_product_with_options(request, runtime)

    def eip_notify_paid_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EipNotifyPaid',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.EipNotifyPaidResponse(),
            self.call_api(params, req, runtime)
        )

    def eip_notify_paid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.eip_notify_paid_with_options(request, runtime)

    def enable_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnablePhysicalConnection',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.EnablePhysicalConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_physical_connection_with_options(request, runtime)

    def export_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.ossprefix):
            query['OSSPrefix'] = request.ossprefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportImage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ExportImageResponse(),
            self.call_api(params, req, runtime)
        )

    def export_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    def export_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportSnapshot',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ExportSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def export_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_snapshot_with_options(request, runtime)

    def get_instance_console_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_symbols):
            query['RemoveSymbols'] = request.remove_symbols
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceConsoleOutput',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.GetInstanceConsoleOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_console_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_console_output_with_options(request, runtime)

    def get_instance_screenshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.wake_up):
            query['WakeUp'] = request.wake_up
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceScreenshot',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.GetInstanceScreenshotResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_screenshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_screenshot_with_options(request, runtime)

    def import_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture):
            query['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.boot_mode):
            query['BootMode'] = request.boot_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.detection_strategy):
            query['DetectionStrategy'] = request.detection_strategy
        if not UtilClient.is_unset(request.disk_device_mapping):
            query['DiskDeviceMapping'] = request.disk_device_mapping
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportImage',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ImportImageResponse(),
            self.call_api(params, req, runtime)
        )

    def import_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_image_with_options(request, runtime)

    def import_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='ImportKeyPair',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    def import_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    def import_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportSnapshot',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ImportSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def import_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_snapshot_with_options(request, runtime)

    def install_cloud_assistant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='InstallCloudAssistant',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.InstallCloudAssistantResponse(),
            self.call_api(params, req, runtime)
        )

    def install_cloud_assistant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_assistant_with_options(request, runtime)

    def invoke_command_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_mode):
            query['RepeatMode'] = request.repeat_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timed):
            query['Timed'] = request.timed
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeCommand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.InvokeCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_command_with_options(request, runtime)

    def join_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action='JoinResourceGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.JoinResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def join_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    def join_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinSecurityGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.JoinSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def join_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    def leave_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LeaveSecurityGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.LeaveSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def leave_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    def list_plugin_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='ListPluginStatus',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ListPluginStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_plugin_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_plugin_status_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_provisioning_group_id):
            query['AutoProvisioningGroupId'] = request.auto_provisioning_group_id
        if not UtilClient.is_unset(request.auto_provisioning_group_name):
            query['AutoProvisioningGroupName'] = request.auto_provisioning_group_name
        if not UtilClient.is_unset(request.default_target_capacity_type):
            query['DefaultTargetCapacityType'] = request.default_target_capacity_type
        if not UtilClient.is_unset(request.excess_capacity_termination_policy):
            query['ExcessCapacityTerminationPolicy'] = request.excess_capacity_termination_policy
        if not UtilClient.is_unset(request.launch_template_config):
            query['LaunchTemplateConfig'] = request.launch_template_config
        if not UtilClient.is_unset(request.max_spot_price):
            query['MaxSpotPrice'] = request.max_spot_price
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_as_you_go_target_capacity):
            query['PayAsYouGoTargetCapacity'] = request.pay_as_you_go_target_capacity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_target_capacity):
            query['SpotTargetCapacity'] = request.spot_target_capacity
        if not UtilClient.is_unset(request.terminate_instances_with_expiration):
            query['TerminateInstancesWithExpiration'] = request.terminate_instances_with_expiration
        if not UtilClient.is_unset(request.total_target_capacity):
            query['TotalTargetCapacity'] = request.total_target_capacity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoProvisioningGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyAutoProvisioningGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_provisioning_group_with_options(request, runtime)

    def modify_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk_policy_enabled):
            query['DataDiskPolicyEnabled'] = request.data_disk_policy_enabled
        if not UtilClient.is_unset(request.data_disk_policy_retention_days):
            query['DataDiskPolicyRetentionDays'] = request.data_disk_policy_retention_days
        if not UtilClient.is_unset(request.data_disk_policy_retention_last_week):
            query['DataDiskPolicyRetentionLastWeek'] = request.data_disk_policy_retention_last_week
        if not UtilClient.is_unset(request.data_disk_policy_time_period):
            query['DataDiskPolicyTimePeriod'] = request.data_disk_policy_time_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.system_disk_policy_enabled):
            query['SystemDiskPolicyEnabled'] = request.system_disk_policy_enabled
        if not UtilClient.is_unset(request.system_disk_policy_retention_days):
            query['SystemDiskPolicyRetentionDays'] = request.system_disk_policy_retention_days
        if not UtilClient.is_unset(request.system_disk_policy_retention_last_week):
            query['SystemDiskPolicyRetentionLastWeek'] = request.system_disk_policy_retention_last_week
        if not UtilClient.is_unset(request.system_disk_policy_time_period):
            query['SystemDiskPolicyTimePeriod'] = request.system_disk_policy_time_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    def modify_auto_snapshot_policy_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copied_snapshots_retention_days):
            query['CopiedSnapshotsRetentionDays'] = request.copied_snapshots_retention_days
        if not UtilClient.is_unset(request.enable_cross_region_copy):
            query['EnableCrossRegionCopy'] = request.enable_cross_region_copy
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_copy_regions):
            query['TargetCopyRegions'] = request.target_copy_regions
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['autoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['autoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['repeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['retentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['timePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicyEx',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_auto_snapshot_policy_ex(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_ex_with_options(request, runtime)

    def modify_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
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
            action='ModifyBandwidthPackageSpec',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyBandwidthPackageSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_bandwidth_package_spec_with_options(request, runtime)

    def modify_capacity_reservation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_time_type):
            query['EndTimeType'] = request.end_time_type
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCapacityReservation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_capacity_reservation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_capacity_reservation_with_options(request, runtime)

    def modify_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCommand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_command_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.auto_placement):
            query['AutoPlacement'] = request.auto_placement
        if not UtilClient.is_unset(request.cpu_over_commit_ratio):
            query['CpuOverCommitRatio'] = request.cpu_over_commit_ratio
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.dedicated_host_name):
            query['DedicatedHostName'] = request.dedicated_host_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.network_attributes):
            query['NetworkAttributes'] = request.network_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def modify_dedicated_host_auto_release_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='ModifyDedicatedHostAutoReleaseTime',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_auto_release_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_release_time_with_options(request, runtime)

    def modify_dedicated_host_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_with_ecs):
            query['AutoRenewWithEcs'] = request.auto_renew_with_ecs
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostAutoRenewAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_renew_attribute_with_options(request, runtime)

    def modify_dedicated_host_cluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_cluster_name):
            query['DedicatedHostClusterName'] = request.dedicated_host_cluster_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
            action='ModifyDedicatedHostClusterAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_host_cluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_cluster_attribute_with_options(request, runtime)

    def modify_dedicated_hosts_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_charge_type):
            query['DedicatedHostChargeType'] = request.dedicated_host_charge_type
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.detail_fee):
            query['DetailFee'] = request.detail_fee
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='ModifyDedicatedHostsChargeType',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dedicated_hosts_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_hosts_charge_type_with_options(request, runtime)

    def modify_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.demand_description):
            query['DemandDescription'] = request.demand_description
        if not UtilClient.is_unset(request.demand_id):
            query['DemandId'] = request.demand_id
        if not UtilClient.is_unset(request.demand_name):
            query['DemandName'] = request.demand_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDemand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_demand_with_options(request, runtime)

    def modify_deployment_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.deployment_set_name):
            query['DeploymentSetName'] = request.deployment_set_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
            action='ModifyDeploymentSetAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDeploymentSetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_deployment_set_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_deployment_set_attribute_with_options(request, runtime)

    def modify_diagnostic_metric_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.metric_ids):
            query['MetricIds'] = request.metric_ids
        if not UtilClient.is_unset(request.metric_set_id):
            query['MetricSetId'] = request.metric_set_id
        if not UtilClient.is_unset(request.metric_set_name):
            query['MetricSetName'] = request.metric_set_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiagnosticMetricSet',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiagnosticMetricSetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_diagnostic_metric_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_diagnostic_metric_set_with_options(request, runtime)

    def modify_disk_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bursting_enabled):
            query['BurstingEnabled'] = request.bursting_enabled
        if not UtilClient.is_unset(request.delete_auto_snapshot):
            query['DeleteAutoSnapshot'] = request.delete_auto_snapshot
        if not UtilClient.is_unset(request.delete_with_instance):
            query['DeleteWithInstance'] = request.delete_with_instance
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.enable_auto_snapshot):
            query['EnableAutoSnapshot'] = request.enable_auto_snapshot
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
            action='ModifyDiskAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_disk_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_attribute_with_options(request, runtime)

    def modify_disk_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_charge_type):
            query['DiskChargeType'] = request.disk_charge_type
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyDiskChargeType',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiskChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_disk_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_charge_type_with_options(request, runtime)

    def modify_disk_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.performance_level):
            query['PerformanceLevel'] = request.performance_level
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSpec',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiskSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_disk_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    def modify_eip_address_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
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
            action='ModifyEipAddressAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyEipAddressAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_eip_address_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_eip_address_attribute_with_options(request, runtime)

    def modify_elasticity_assurance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticityAssurance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyElasticityAssuranceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_elasticity_assurance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_elasticity_assurance_with_options(request, runtime)

    def modify_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.external_port):
            query['ExternalPort'] = request.external_port
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_table_id):
            query['ForwardTableId'] = request.forward_table_id
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
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
            action='ModifyForwardEntry',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyForwardEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_forward_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_forward_entry_with_options(request, runtime)

    def modify_ha_vip_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ha_vip_id):
            query['HaVipId'] = request.ha_vip_id
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
            action='ModifyHaVipAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyHaVipAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ha_vip_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    def modify_hpc_cluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyHpcClusterAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyHpcClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hpc_cluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hpc_cluster_attribute_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.boot_mode):
            query['BootMode'] = request.boot_mode
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.features):
            query['Features'] = request.features
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyImageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_image_share_group_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
        if not UtilClient.is_unset(request.add_group):
            query['AddGroup'] = request.add_group
        if not UtilClient.is_unset(request.remove_group):
            query['RemoveGroup'] = request.remove_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageShareGroupPermission',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyImageShareGroupPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_image_share_group_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_group_permission_with_options(request, runtime)

    def modify_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.is_public):
            query['IsPublic'] = request.is_public
        if not UtilClient.is_unset(request.launch_permission):
            query['LaunchPermission'] = request.launch_permission
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_account):
            query['RemoveAccount'] = request.remove_account
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageSharePermission',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyImageSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_permission_with_options(request, runtime)

    def modify_instance_attachment_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttachmentAttributes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_attachment_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attachment_attributes_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network_interface_queue_number):
            query['NetworkInterfaceQueueNumber'] = request.network_interface_queue_number
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.recyclable):
            query['Recyclable'] = request.recyclable
        if not UtilClient.is_unset(request.remote_connection_options):
            query['RemoteConnectionOptions'] = request.remote_connection_options
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_instance_auto_release_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyInstanceAutoReleaseTime',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_auto_release_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_release_time_with_options(request, runtime)

    def modify_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renew_attribute_with_options(request, runtime)

    def modify_instance_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.include_data_disks):
            query['IncludeDataDisks'] = request.include_data_disks
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.is_detail_fee):
            query['IsDetailFee'] = request.is_detail_fee
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='ModifyInstanceChargeType',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    def modify_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.migration_type):
            query['MigrationType'] = request.migration_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_from_deployment_set):
            query['RemoveFromDeploymentSet'] = request.remove_from_deployment_set
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceDeployment',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_deployment_with_options(request, runtime)

    def modify_instance_maintenance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_on_maintenance):
            query['ActionOnMaintenance'] = request.action_on_maintenance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.maintenance_window):
            query['MaintenanceWindow'] = request.maintenance_window
        if not UtilClient.is_unset(request.notify_on_maintenance):
            query['NotifyOnMaintenance'] = request.notify_on_maintenance
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
            action='ModifyInstanceMaintenanceAttributes',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_maintenance_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintenance_attributes_with_options(request, runtime)

    def modify_instance_metadata_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ModifyInstanceMetadataOptions',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceMetadataOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_metadata_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_metadata_options_with_options(request, runtime)

    def modify_instance_network_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocate_public_ip):
            query['AllocatePublicIp'] = request.allocate_public_ip
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.network_charge_type):
            query['NetworkChargeType'] = request.network_charge_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceNetworkSpec',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceNetworkSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_network_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_network_spec_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_migrate_across_zone):
            query['AllowMigrateAcrossZone'] = request.allow_migrate_across_zone
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        if not UtilClient.is_unset(request.temporary):
            query['Temporary'] = request.temporary
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_instance_vnc_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVncPasswd',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceVncPasswdResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_vnc_passwd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vnc_passwd_with_options(request, runtime)

    def modify_instance_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVpcAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceVpcAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_attribute_with_options(request, runtime)

    def modify_launch_template_default_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_version_number):
            query['DefaultVersionNumber'] = request.default_version_number
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
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
            action='ModifyLaunchTemplateDefaultVersion',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_launch_template_default_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_launch_template_default_version_with_options(request, runtime)

    def modify_managed_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ModifyManagedInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyManagedInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_managed_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_managed_instance_with_options(request, runtime)

    def modify_network_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.queue_number):
            query['QueueNumber'] = request.queue_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkInterfaceAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_network_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_interface_attribute_with_options(request, runtime)

    def modify_physical_connection_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.circuit_code):
            query['CircuitCode'] = request.circuit_code
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.line_operator):
            query['LineOperator'] = request.line_operator
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_location):
            query['PeerLocation'] = request.peer_location
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
        if not UtilClient.is_unset(request.port_type):
            query['PortType'] = request.port_type
        if not UtilClient.is_unset(request.redundant_physical_connection_id):
            query['RedundantPhysicalConnectionId'] = request.redundant_physical_connection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.bandwidth):
            query['bandwidth'] = request.bandwidth
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhysicalConnectionAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_physical_connection_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    def modify_prefix_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_entry):
            query['AddEntry'] = request.add_entry
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix_list_id):
            query['PrefixListId'] = request.prefix_list_id
        if not UtilClient.is_unset(request.prefix_list_name):
            query['PrefixListName'] = request.prefix_list_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_entry):
            query['RemoveEntry'] = request.remove_entry
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPrefixList',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyPrefixListResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_prefix_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_prefix_list_with_options(request, runtime)

    def modify_prepay_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.migrate_across_zone):
            query['MigrateAcrossZone'] = request.migrate_across_zone
        if not UtilClient.is_unset(request.operator_type):
            query['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reboot_time):
            query['RebootTime'] = request.reboot_time
        if not UtilClient.is_unset(request.reboot_when_finished):
            query['RebootWhenFinished'] = request.reboot_when_finished
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyPrepayInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_prepay_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    def modify_reserved_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReservedInstanceAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyReservedInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_reserved_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instance_attribute_with_options(request, runtime)

    def modify_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReservedInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyReservedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instances_with_options(request, runtime)

    def modify_router_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_source_ip):
            query['HealthCheckSourceIp'] = request.health_check_source_ip
        if not UtilClient.is_unset(request.health_check_target_ip):
            query['HealthCheckTargetIp'] = request.health_check_target_ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opposite_interface_id):
            query['OppositeInterfaceId'] = request.opposite_interface_id
        if not UtilClient.is_unset(request.opposite_interface_owner_id):
            query['OppositeInterfaceOwnerId'] = request.opposite_interface_owner_id
        if not UtilClient.is_unset(request.opposite_router_id):
            query['OppositeRouterId'] = request.opposite_router_id
        if not UtilClient.is_unset(request.opposite_router_type):
            query['OppositeRouterType'] = request.opposite_router_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.router_interface_id):
            query['RouterInterfaceId'] = request.router_interface_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRouterInterfaceAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyRouterInterfaceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_router_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_attribute_with_options(request, runtime)

    def modify_router_interface_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.router_interface_id):
            query['RouterInterfaceId'] = request.router_interface_id
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRouterInterfaceSpec',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyRouterInterfaceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_router_interface_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_spec_with_options(request, runtime)

    def modify_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_attribute_with_options(request, runtime)

    def modify_security_group_egress_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.dest_group_id):
            query['DestGroupId'] = request.dest_group_id
        if not UtilClient.is_unset(request.dest_group_owner_account):
            query['DestGroupOwnerAccount'] = request.dest_group_owner_account
        if not UtilClient.is_unset(request.dest_group_owner_id):
            query['DestGroupOwnerId'] = request.dest_group_owner_id
        if not UtilClient.is_unset(request.dest_prefix_list_id):
            query['DestPrefixListId'] = request.dest_prefix_list_id
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.ipv_6dest_cidr_ip):
            query['Ipv6DestCidrIp'] = request.ipv_6dest_cidr_ip
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupEgressRule',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupEgressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_group_egress_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_egress_rule_with_options(request, runtime)

    def modify_security_group_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.inner_access_policy):
            query['InnerAccessPolicy'] = request.inner_access_policy
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupPolicy',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_group_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_policy_with_options(request, runtime)

    def modify_security_group_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.ipv_6dest_cidr_ip):
            query['Ipv6DestCidrIp'] = request.ipv_6dest_cidr_ip
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not UtilClient.is_unset(request.source_group_owner_account):
            query['SourceGroupOwnerAccount'] = request.source_group_owner_account
        if not UtilClient.is_unset(request.source_group_owner_id):
            query['SourceGroupOwnerId'] = request.source_group_owner_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.source_prefix_list_id):
            query['SourcePrefixListId'] = request.source_prefix_list_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupRule',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_group_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_rule_with_options(request, runtime)

    def modify_snapshot_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_instant_access):
            query['DisableInstantAccess'] = request.disable_instant_access
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySnapshotAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySnapshotAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_snapshot_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_attribute_with_options(request, runtime)

    def modify_snapshot_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.snapshot_group_id):
            query['SnapshotGroupId'] = request.snapshot_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySnapshotGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySnapshotGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_snapshot_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_group_with_options(request, runtime)

    def modify_storage_capacity_unit_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.storage_capacity_unit_id):
            query['StorageCapacityUnitId'] = request.storage_capacity_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageCapacityUnitAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_storage_capacity_unit_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_capacity_unit_attribute_with_options(request, runtime)

    def modify_storage_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_name):
            query['StorageSetName'] = request.storage_set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageSetAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyStorageSetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_storage_set_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_set_attribute_with_options(request, runtime)

    def modify_user_business_behavior_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.status_key):
            query['statusKey'] = request.status_key
        if not UtilClient.is_unset(request.status_value):
            query['statusValue'] = request.status_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserBusinessBehavior',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyUserBusinessBehaviorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_business_behavior(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_business_behavior_with_options(request, runtime)

    def modify_vrouter_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.vrouter_id):
            query['VRouterId'] = request.vrouter_id
        if not UtilClient.is_unset(request.vrouter_name):
            query['VRouterName'] = request.vrouter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVRouterAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVRouterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vrouter_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vrouter_attribute_with_options(request, runtime)

    def modify_vswitch_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVSwitchAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVSwitchAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vswitch_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vswitch_attribute_with_options(request, runtime)

    def modify_virtual_border_router_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.circuit_code):
            query['CircuitCode'] = request.circuit_code
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.local_gateway_ip):
            query['LocalGatewayIp'] = request.local_gateway_ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.peer_gateway_ip):
            query['PeerGatewayIp'] = request.peer_gateway_ip
        if not UtilClient.is_unset(request.peering_subnet_mask):
            query['PeeringSubnetMask'] = request.peering_subnet_mask
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        if not UtilClient.is_unset(request.vlan_id):
            query['VlanId'] = request.vlan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVirtualBorderRouterAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_virtual_border_router_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    def modify_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcAttribute',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVpcAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_attribute_with_options(request, runtime)

    def purchase_reserved_instances_offering_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_amount):
            query['InstanceAmount'] = request.instance_amount
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.offering_type):
            query['OfferingType'] = request.offering_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_name):
            query['ReservedInstanceName'] = request.reserved_instance_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseReservedInstancesOffering',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.PurchaseReservedInstancesOfferingResponse(),
            self.call_api(params, req, runtime)
        )

    def purchase_reserved_instances_offering(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purchase_reserved_instances_offering_with_options(request, runtime)

    def purchase_storage_capacity_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurchaseStorageCapacityUnit',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.PurchaseStorageCapacityUnitResponse(),
            self.call_api(params, req, runtime)
        )

    def purchase_storage_capacity_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purchase_storage_capacity_unit_with_options(request, runtime)

    def re_activate_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='ReActivateInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReActivateInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def re_activate_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_activate_instances_with_options(request, runtime)

    def re_init_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start_instance):
            query['AutoStartInstance'] = request.auto_start_instance
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReInitDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReInitDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def re_init_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_init_disk_with_options(request, runtime)

    def reboot_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='RebootInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RebootInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def reboot_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    def reboot_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_optimization):
            query['BatchOptimization'] = request.batch_optimization
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force_reboot):
            query['ForceReboot'] = request.force_reboot
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='RebootInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RebootInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def reboot_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    def recover_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverVirtualBorderRouter',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RecoverVirtualBorderRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def recover_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recover_virtual_border_router_with_options(request, runtime)

    def redeploy_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='RedeployDedicatedHost',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RedeployDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    def redeploy_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.redeploy_dedicated_host_with_options(request, runtime)

    def redeploy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='RedeployInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RedeployInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def redeploy_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.redeploy_instance_with_options(request, runtime)

    def release_capacity_reservation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCapacityReservation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleaseCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    def release_capacity_reservation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_reservation_with_options(request, runtime)

    def release_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='ReleaseDedicatedHost',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleaseDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    def release_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_dedicated_host_with_options(request, runtime)

    def release_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
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
            action='ReleaseEipAddress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleaseEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def release_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    def release_public_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.public_ip_address):
            query['PublicIpAddress'] = request.public_ip_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicIpAddress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleasePublicIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def release_public_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_public_ip_address_with_options(request, runtime)

    def remove_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removed_ip_addresses):
            query['RemovedIpAddresses'] = request.removed_ip_addresses
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBandwidthPackageIps',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RemoveBandwidthPackageIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_bandwidth_package_ips_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='RemoveTags',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    def renew_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_ids):
            query['DedicatedHostIds'] = request.dedicated_host_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='RenewDedicatedHosts',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RenewDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_dedicated_hosts_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expected_renew_day):
            query['ExpectedRenewDay'] = request.expected_renew_day
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def renew_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserved_instance_id):
            query['ReservedInstanceId'] = request.reserved_instance_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewReservedInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RenewReservedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_reserved_instances_with_options(request, runtime)

    def replace_system_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.architecture):
            query['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.use_additional_service):
            query['UseAdditionalService'] = request.use_additional_service
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceSystemDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReplaceSystemDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_system_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_system_disk_with_options(request, runtime)

    def report_instances_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device):
            query['Device'] = request.device
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.issue_category):
            query['IssueCategory'] = request.issue_category
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportInstancesStatus',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReportInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def report_instances_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_instances_status_with_options(request, runtime)

    def reset_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
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
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ResetDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    def reset_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk):
            query['Disk'] = request.disk
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisks',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ResetDisksResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_disks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_disks_with_options(request, runtime)

    def resize_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.new_size):
            query['NewSize'] = request.new_size
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDisk',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.ResizeDiskResponse(),
            self.call_api(params, req, runtime)
        )

    def resize_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_with_options(request, runtime)

    def revoke_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.ipv_6dest_cidr_ip):
            query['Ipv6DestCidrIp'] = request.ipv_6dest_cidr_ip
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_group_id):
            query['SourceGroupId'] = request.source_group_id
        if not UtilClient.is_unset(request.source_group_owner_account):
            query['SourceGroupOwnerAccount'] = request.source_group_owner_account
        if not UtilClient.is_unset(request.source_group_owner_id):
            query['SourceGroupOwnerId'] = request.source_group_owner_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        if not UtilClient.is_unset(request.source_prefix_list_id):
            query['SourcePrefixListId'] = request.source_prefix_list_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSecurityGroup',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RevokeSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    def revoke_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.dest_group_id):
            query['DestGroupId'] = request.dest_group_id
        if not UtilClient.is_unset(request.dest_group_owner_account):
            query['DestGroupOwnerAccount'] = request.dest_group_owner_account
        if not UtilClient.is_unset(request.dest_group_owner_id):
            query['DestGroupOwnerId'] = request.dest_group_owner_id
        if not UtilClient.is_unset(request.dest_prefix_list_id):
            query['DestPrefixListId'] = request.dest_prefix_list_id
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.ipv_6dest_cidr_ip):
            query['Ipv6DestCidrIp'] = request.ipv_6dest_cidr_ip
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.nic_type):
            query['NicType'] = request.nic_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.permissions):
            query['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSecurityGroupEgress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RevokeSecurityGroupEgressResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_egress_with_options(request, runtime)

    def run_command_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.container_id):
            query['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keep_command):
            query['KeepCommand'] = request.keep_command
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat_mode):
            query['RepeatMode'] = request.repeat_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.timed):
            query['Timed'] = request.timed
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def run_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    def run_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.auto_release_time):
            query['AutoReleaseTime'] = request.auto_release_time
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_group_no):
            query['DeploymentSetGroupNo'] = request.deployment_set_group_no
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_names):
            query['HostNames'] = request.host_names
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.http_endpoint):
            query['HttpEndpoint'] = request.http_endpoint
        if not UtilClient.is_unset(request.http_put_response_hop_limit):
            query['HttpPutResponseHopLimit'] = request.http_put_response_hop_limit
        if not UtilClient.is_unset(request.http_tokens):
            query['HttpTokens'] = request.http_tokens
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_name):
            query['LaunchTemplateName'] = request.launch_template_name
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.min_amount):
            query['MinAmount'] = request.min_amount
        if not UtilClient.is_unset(request.network_interface):
            query['NetworkInterface'] = request.network_interface
        if not UtilClient.is_unset(request.network_interface_queue_number):
            query['NetworkInterfaceQueueNumber'] = request.network_interface_queue_number
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.cpu_options):
            query['CpuOptions'] = request.cpu_options
        if not UtilClient.is_unset(request.hibernation_options):
            query['HibernationOptions'] = request.hibernation_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.scheduler_options):
            query['SchedulerOptions'] = request.scheduler_options
        if not UtilClient.is_unset(request.security_options):
            query['SecurityOptions'] = request.security_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.RunInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def run_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    def send_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_group):
            query['FileGroup'] = request.file_group
        if not UtilClient.is_unset(request.file_mode):
            query['FileMode'] = request.file_mode
        if not UtilClient.is_unset(request.file_owner):
            query['FileOwner'] = request.file_owner
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_dir):
            query['TargetDir'] = request.target_dir
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.SendFileResponse(),
            self.call_api(params, req, runtime)
        )

    def send_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    def start_elasticity_assurance_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartElasticityAssurance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartElasticityAssuranceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_elasticity_assurance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_elasticity_assurance_with_options(request, runtime)

    def start_image_pipeline_execution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_pipeline_id):
            query['ImagePipelineId'] = request.image_pipeline_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_tag):
            query['TemplateTag'] = request.template_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartImagePipelineExecution',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartImagePipelineExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    def start_image_pipeline_execution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_image_pipeline_execution_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.init_local_disk):
            query['InitLocalDisk'] = request.init_local_disk
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def start_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_optimization):
            query['BatchOptimization'] = request.batch_optimization
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='StartInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def start_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    def start_terminal_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port_number):
            query['PortNumber'] = request.port_number
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='StartTerminalSession',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartTerminalSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def start_terminal_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_terminal_session_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm_stop):
            query['ConfirmStop'] = request.confirm_stop
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.hibernate):
            query['Hibernate'] = request.hibernate
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.stopped_mode):
            query['StoppedMode'] = request.stopped_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def stop_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_optimization):
            query['BatchOptimization'] = request.batch_optimization
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
        if not UtilClient.is_unset(request.stopped_mode):
            query['StoppedMode'] = request.stopped_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    def stop_invocation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='StopInvocation',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_invocation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def terminate_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.physical_connection_id):
            query['PhysicalConnectionId'] = request.physical_connection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminatePhysicalConnection',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.TerminatePhysicalConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_physical_connection_with_options(request, runtime)

    def terminate_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.user_cidr):
            query['UserCidr'] = request.user_cidr
        if not UtilClient.is_unset(request.vbr_id):
            query['VbrId'] = request.vbr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateVirtualBorderRouter',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.TerminateVirtualBorderRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_virtual_border_router_with_options(request, runtime)

    def unassign_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipv_6address):
            query['Ipv6Address'] = request.ipv_6address
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='UnassignIpv6Addresses',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassignIpv6AddressesResponse(),
            self.call_api(params, req, runtime)
        )

    def unassign_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassign_ipv_6addresses_with_options(request, runtime)

    def unassign_private_ip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='UnassignPrivateIpAddresses',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassignPrivateIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    def unassign_private_ip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassign_private_ip_addresses_with_options(request, runtime)

    def unassociate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
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
            action='UnassociateEipAddress',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassociateEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def unassociate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    def unassociate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.ha_vip_id):
            query['HaVipId'] = request.ha_vip_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
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
            action='UnassociateHaVip',
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassociateHaVipResponse(),
            self.call_api(params, req, runtime)
        )

    def unassociate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_ha_vip_with_options(request, runtime)

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
            version='2014-05-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecs_20140526_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
