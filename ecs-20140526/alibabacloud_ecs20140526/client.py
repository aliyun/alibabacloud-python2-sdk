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
            'cn-qingdao': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'ecs-cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'us-west-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'us-east-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'ecs.aliyuncs.com',
            'ap-northeast-2-pop': 'ecs.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ecs.aliyuncs.com',
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
            'cn-shanghai-et15-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-inner': 'ecs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-inner': 'ecs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-wuhan': 'ecs.aliyuncs.com',
            'cn-yushanfang': 'ecs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ecs.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'ecs.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'ecs.ap-northeast-1.aliyuncs.com'
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AcceptInquiredSystemEventResponse(),
            self.do_rpcrequest('AcceptInquiredSystemEvent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_inquired_system_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_inquired_system_event_with_options(request, runtime)

    def activate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ActivateRouterInterfaceResponse(),
            self.do_rpcrequest('ActivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.activate_router_interface_with_options(request, runtime)

    def add_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AddBandwidthPackageIpsResponse(),
            self.do_rpcrequest('AddBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_bandwidth_package_ips_with_options(request, runtime)

    def add_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AddTagsResponse(),
            self.do_rpcrequest('AddTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    def allocate_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AllocateDedicatedHostsResponse(),
            self.do_rpcrequest('AllocateDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_dedicated_hosts_with_options(request, runtime)

    def allocate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AllocateEipAddressResponse(),
            self.do_rpcrequest('AllocateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_with_options(request, runtime)

    def allocate_public_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AllocatePublicIpAddressResponse(),
            self.do_rpcrequest('AllocatePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_public_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_ip_address_with_options(request, runtime)

    def apply_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ApplyAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('ApplyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    def assign_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssignIpv6AddressesResponse(),
            self.do_rpcrequest('AssignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_ipv_6addresses_with_options(request, runtime)

    def assign_private_ip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssignPrivateIpAddressesResponse(),
            self.do_rpcrequest('AssignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_private_ip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_addresses_with_options(request, runtime)

    def associate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssociateEipAddressResponse(),
            self.do_rpcrequest('AssociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_address_with_options(request, runtime)

    def associate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AssociateHaVipResponse(),
            self.do_rpcrequest('AssociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_ha_vip_with_options(request, runtime)

    def attach_classic_link_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachClassicLinkVpcResponse(),
            self.do_rpcrequest('AttachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_classic_link_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_classic_link_vpc_with_options(request, runtime)

    def attach_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachDiskResponse(),
            self.do_rpcrequest('AttachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_disk_with_options(request, runtime)

    def attach_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachInstanceRamRoleResponse(),
            self.do_rpcrequest('AttachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_instance_ram_role_with_options(request, runtime)

    def attach_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachKeyPairResponse(),
            self.do_rpcrequest('AttachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    def attach_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AttachNetworkInterfaceResponse(),
            self.do_rpcrequest('AttachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_network_interface_with_options(request, runtime)

    def authorize_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AuthorizeSecurityGroupResponse(),
            self.do_rpcrequest('AuthorizeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def authorize_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_with_options(request, runtime)

    def authorize_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.AuthorizeSecurityGroupEgressResponse(),
            self.do_rpcrequest('AuthorizeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def authorize_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_egress_with_options(request, runtime)

    def cancel_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('CancelAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    def cancel_copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelCopyImageResponse(),
            self.do_rpcrequest('CancelCopyImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_copy_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_copy_image_with_options(request, runtime)

    def cancel_image_pipeline_execution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelImagePipelineExecutionResponse(),
            self.do_rpcrequest('CancelImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_image_pipeline_execution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_image_pipeline_execution_with_options(request, runtime)

    def cancel_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelPhysicalConnectionResponse(),
            self.do_rpcrequest('CancelPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_physical_connection_with_options(request, runtime)

    def cancel_simulated_system_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelSimulatedSystemEventsResponse(),
            self.do_rpcrequest('CancelSimulatedSystemEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_simulated_system_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_simulated_system_events_with_options(request, runtime)

    def cancel_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CancelTaskResponse(),
            self.do_rpcrequest('CancelTask', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    def connect_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ConnectRouterInterfaceResponse(),
            self.do_rpcrequest('ConnectRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def connect_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.connect_router_interface_with_options(request, runtime)

    def convert_nat_public_ip_to_eip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ConvertNatPublicIpToEipResponse(),
            self.do_rpcrequest('ConvertNatPublicIpToEip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_nat_public_ip_to_eip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_nat_public_ip_to_eip_with_options(request, runtime)

    def copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CopyImageResponse(),
            self.do_rpcrequest('CopyImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    def copy_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CopySnapshotResponse(),
            self.do_rpcrequest('CopySnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_snapshot_with_options(request, runtime)

    def create_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateActivationResponse(),
            self.do_rpcrequest('CreateActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_activation_with_options(request, runtime)

    def create_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateAutoProvisioningGroupResponse(),
            self.do_rpcrequest('CreateAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auto_provisioning_group_with_options(request, runtime)

    def create_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('CreateAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    def create_capacity_reservation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateCapacityReservationResponse(),
            self.do_rpcrequest('CreateCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_capacity_reservation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_capacity_reservation_with_options(request, runtime)

    def create_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateCommandResponse(),
            self.do_rpcrequest('CreateCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    def create_dedicated_block_storage_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDedicatedBlockStorageClusterResponse(),
            self.do_rpcrequest('CreateDedicatedBlockStorageCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_block_storage_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_block_storage_cluster_with_options(request, runtime)

    def create_dedicated_host_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDedicatedHostClusterResponse(),
            self.do_rpcrequest('CreateDedicatedHostCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_cluster_with_options(request, runtime)

    def create_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDemandResponse(),
            self.do_rpcrequest('CreateDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_demand_with_options(request, runtime)

    def create_deployment_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDeploymentSetResponse(),
            self.do_rpcrequest('CreateDeploymentSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_deployment_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_deployment_set_with_options(request, runtime)

    def create_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDiskResponse(),
            self.do_rpcrequest('CreateDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disk_with_options(request, runtime)

    def create_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateDiskReplicaPairResponse(),
            self.do_rpcrequest('CreateDiskReplicaPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_pair_with_options(request, runtime)

    def create_elasticity_assurance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateElasticityAssuranceResponse(),
            self.do_rpcrequest('CreateElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_elasticity_assurance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_elasticity_assurance_with_options(request, runtime)

    def create_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateForwardEntryResponse(),
            self.do_rpcrequest('CreateForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_forward_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_forward_entry_with_options(request, runtime)

    def create_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateHaVipResponse(),
            self.do_rpcrequest('CreateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ha_vip_with_options(request, runtime)

    def create_hpc_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateHpcClusterResponse(),
            self.do_rpcrequest('CreateHpcCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_hpc_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_hpc_cluster_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateImageResponse(),
            self.do_rpcrequest('CreateImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_image_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateImageComponentResponse(),
            self.do_rpcrequest('CreateImageComponent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_component_with_options(request, runtime)

    def create_image_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateImagePipelineResponse(),
            self.do_rpcrequest('CreateImagePipeline', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_pipeline_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateKeyPairResponse(),
            self.do_rpcrequest('CreateKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    def create_launch_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateLaunchTemplateResponse(),
            self.do_rpcrequest('CreateLaunchTemplate', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_launch_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_launch_template_with_options(request, runtime)

    def create_launch_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateLaunchTemplateVersionResponse(),
            self.do_rpcrequest('CreateLaunchTemplateVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_launch_template_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_launch_template_version_with_options(request, runtime)

    def create_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateNatGatewayResponse(),
            self.do_rpcrequest('CreateNatGateway', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_nat_gateway_with_options(request, runtime)

    def create_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateNetworkInterfaceResponse(),
            self.do_rpcrequest('CreateNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_interface_with_options(request, runtime)

    def create_network_interface_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateNetworkInterfacePermissionResponse(),
            self.do_rpcrequest('CreateNetworkInterfacePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_interface_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_network_interface_permission_with_options(request, runtime)

    def create_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreatePhysicalConnectionResponse(),
            self.do_rpcrequest('CreatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_physical_connection_with_options(request, runtime)

    def create_prefix_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreatePrefixListResponse(),
            self.do_rpcrequest('CreatePrefixList', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_prefix_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_prefix_list_with_options(request, runtime)

    def create_resource_02with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateResource02Response(),
            self.do_rpcrequest('CreateResource02', '2014-05-26', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def create_resource_02(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_02with_options(request, runtime)

    def create_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateRouteEntryResponse(),
            self.do_rpcrequest('CreateRouteEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_route_entry_with_options(request, runtime)

    def create_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateRouterInterfaceResponse(),
            self.do_rpcrequest('CreateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_router_interface_with_options(request, runtime)

    def create_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSecurityGroupResponse(),
            self.do_rpcrequest('CreateSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_security_group_with_options(request, runtime)

    def create_simulated_system_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSimulatedSystemEventsResponse(),
            self.do_rpcrequest('CreateSimulatedSystemEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_simulated_system_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_simulated_system_events_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSnapshotResponse(),
            self.do_rpcrequest('CreateSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    def create_snapshot_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateSnapshotGroupResponse(),
            self.do_rpcrequest('CreateSnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_group_with_options(request, runtime)

    def create_storage_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateStorageSetResponse(),
            self.do_rpcrequest('CreateStorageSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_storage_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_storage_set_with_options(request, runtime)

    def create_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateVirtualBorderRouterResponse(),
            self.do_rpcrequest('CreateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_border_router_with_options(request, runtime)

    def create_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateVpcResponse(),
            self.do_rpcrequest('CreateVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_with_options(request, runtime)

    def create_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.CreateVSwitchResponse(),
            self.do_rpcrequest('CreateVSwitch', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vswitch_with_options(request, runtime)

    def deactivate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeactivateRouterInterfaceResponse(),
            self.do_rpcrequest('DeactivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactivate_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deactivate_router_interface_with_options(request, runtime)

    def delete_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteActivationResponse(),
            self.do_rpcrequest('DeleteActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_activation_with_options(request, runtime)

    def delete_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteAutoProvisioningGroupResponse(),
            self.do_rpcrequest('DeleteAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_provisioning_group_with_options(request, runtime)

    def delete_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('DeleteAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteBandwidthPackageResponse(),
            self.do_rpcrequest('DeleteBandwidthPackage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    def delete_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteCommandResponse(),
            self.do_rpcrequest('DeleteCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    def delete_dedicated_host_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDedicatedHostClusterResponse(),
            self.do_rpcrequest('DeleteDedicatedHostCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_cluster_with_options(request, runtime)

    def delete_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDemandResponse(),
            self.do_rpcrequest('DeleteDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_demand_with_options(request, runtime)

    def delete_deployment_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDeploymentSetResponse(),
            self.do_rpcrequest('DeleteDeploymentSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_deployment_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_deployment_set_with_options(request, runtime)

    def delete_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDiskResponse(),
            self.do_rpcrequest('DeleteDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_with_options(request, runtime)

    def delete_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteDiskReplicaPairResponse(),
            self.do_rpcrequest('DeleteDiskReplicaPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_pair_with_options(request, runtime)

    def delete_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteForwardEntryResponse(),
            self.do_rpcrequest('DeleteForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_forward_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_forward_entry_with_options(request, runtime)

    def delete_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteHaVipResponse(),
            self.do_rpcrequest('DeleteHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ha_vip_with_options(request, runtime)

    def delete_hpc_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteHpcClusterResponse(),
            self.do_rpcrequest('DeleteHpcCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_hpc_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_hpc_cluster_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteImageResponse(),
            self.do_rpcrequest('DeleteImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_image_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteImageComponentResponse(),
            self.do_rpcrequest('DeleteImageComponent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_component_with_options(request, runtime)

    def delete_image_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteImagePipelineResponse(),
            self.do_rpcrequest('DeleteImagePipeline', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_pipeline_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteInstancesResponse(),
            self.do_rpcrequest('DeleteInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instances_with_options(request, runtime)

    def delete_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteKeyPairsResponse(),
            self.do_rpcrequest('DeleteKeyPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_key_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    def delete_launch_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteLaunchTemplateResponse(),
            self.do_rpcrequest('DeleteLaunchTemplate', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_launch_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_launch_template_with_options(request, runtime)

    def delete_launch_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteLaunchTemplateVersionResponse(),
            self.do_rpcrequest('DeleteLaunchTemplateVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_launch_template_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_launch_template_version_with_options(request, runtime)

    def delete_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteNatGatewayResponse(),
            self.do_rpcrequest('DeleteNatGateway', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_gateway_with_options(request, runtime)

    def delete_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteNetworkInterfaceResponse(),
            self.do_rpcrequest('DeleteNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_interface_with_options(request, runtime)

    def delete_network_interface_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteNetworkInterfacePermissionResponse(),
            self.do_rpcrequest('DeleteNetworkInterfacePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_interface_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_network_interface_permission_with_options(request, runtime)

    def delete_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeletePhysicalConnectionResponse(),
            self.do_rpcrequest('DeletePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_connection_with_options(request, runtime)

    def delete_prefix_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeletePrefixListResponse(),
            self.do_rpcrequest('DeletePrefixList', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_prefix_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prefix_list_with_options(request, runtime)

    def delete_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteReplicaPairResponse(),
            self.do_rpcrequest('DeleteReplicaPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_replica_pair_with_options(request, runtime)

    def delete_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteRouteEntryResponse(),
            self.do_rpcrequest('DeleteRouteEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_route_entry_with_options(request, runtime)

    def delete_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteRouterInterfaceResponse(),
            self.do_rpcrequest('DeleteRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_router_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_router_interface_with_options(request, runtime)

    def delete_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteSecurityGroupResponse(),
            self.do_rpcrequest('DeleteSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteSnapshotResponse(),
            self.do_rpcrequest('DeleteSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    def delete_snapshot_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteSnapshotGroupResponse(),
            self.do_rpcrequest('DeleteSnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_group_with_options(request, runtime)

    def delete_storage_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteStorageSetResponse(),
            self.do_rpcrequest('DeleteStorageSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_storage_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_storage_set_with_options(request, runtime)

    def delete_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteVirtualBorderRouterResponse(),
            self.do_rpcrequest('DeleteVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_border_router_with_options(request, runtime)

    def delete_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteVpcResponse(),
            self.do_rpcrequest('DeleteVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_with_options(request, runtime)

    def delete_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeleteVSwitchResponse(),
            self.do_rpcrequest('DeleteVSwitch', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    def deregister_managed_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DeregisterManagedInstanceResponse(),
            self.do_rpcrequest('DeregisterManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_managed_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_managed_instance_with_options(request, runtime)

    def describe_access_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAccessPointsResponse(),
            self.do_rpcrequest('DescribeAccessPoints', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_points(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_points_with_options(request, runtime)

    def describe_account_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAccountAttributesResponse(),
            self.do_rpcrequest('DescribeAccountAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_attributes_with_options(request, runtime)

    def describe_activations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeActivationsResponse(),
            self.do_rpcrequest('DescribeActivations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_activations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_activations_with_options(request, runtime)

    def describe_auto_provisioning_group_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse(),
            self.do_rpcrequest('DescribeAutoProvisioningGroupHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_provisioning_group_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_history_with_options(request, runtime)

    def describe_auto_provisioning_group_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse(),
            self.do_rpcrequest('DescribeAutoProvisioningGroupInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_provisioning_group_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_instances_with_options(request, runtime)

    def describe_auto_provisioning_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoProvisioningGroupsResponse(),
            self.do_rpcrequest('DescribeAutoProvisioningGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_provisioning_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_groups_with_options(request, runtime)

    def describe_auto_snapshot_policy_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse(),
            self.do_rpcrequest('DescribeAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_snapshot_policy_ex(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policy_ex_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_bandwidth_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeBandwidthLimitationResponse(),
            self.do_rpcrequest('DescribeBandwidthLimitation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bandwidth_limitation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_limitation_with_options(request, runtime)

    def describe_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeBandwidthPackagesResponse(),
            self.do_rpcrequest('DescribeBandwidthPackages', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_packages_with_options(request, runtime)

    def describe_capacity_reservation_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCapacityReservationInstancesResponse(),
            self.do_rpcrequest('DescribeCapacityReservationInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_capacity_reservation_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservation_instances_with_options(request, runtime)

    def describe_capacity_reservations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCapacityReservationsResponse(),
            self.do_rpcrequest('DescribeCapacityReservations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_capacity_reservations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservations_with_options(request, runtime)

    def describe_classic_link_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeClassicLinkInstancesResponse(),
            self.do_rpcrequest('DescribeClassicLinkInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_classic_link_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_classic_link_instances_with_options(request, runtime)

    def describe_cloud_assistant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCloudAssistantStatusResponse(),
            self.do_rpcrequest('DescribeCloudAssistantStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_assistant_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    def describe_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeClustersResponse(),
            self.do_rpcrequest('DescribeClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    def describe_commands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeCommandsResponse(),
            self.do_rpcrequest('DescribeCommands', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_commands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_commands_with_options(request, runtime)

    def describe_dedicated_block_storage_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedBlockStorageClustersResponse(),
            self.do_rpcrequest('DescribeDedicatedBlockStorageClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_block_storage_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_block_storage_clusters_with_options(request, runtime)

    def describe_dedicated_host_auto_renew_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse(),
            self.do_rpcrequest('DescribeDedicatedHostAutoRenew', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_auto_renew(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_auto_renew_with_options(request, runtime)

    def describe_dedicated_host_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostClustersResponse(),
            self.do_rpcrequest('DescribeDedicatedHostClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_clusters_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_dedicated_host_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDedicatedHostTypesResponse(),
            self.do_rpcrequest('DescribeDedicatedHostTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_types_with_options(request, runtime)

    def describe_demands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDemandsResponse(),
            self.do_rpcrequest('DescribeDemands', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_demands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_demands_with_options(request, runtime)

    def describe_deployment_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDeploymentSetsResponse(),
            self.do_rpcrequest('DescribeDeploymentSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deployment_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_sets_with_options(request, runtime)

    def describe_deployment_set_supported_instance_type_family_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse(),
            self.do_rpcrequest('DescribeDeploymentSetSupportedInstanceTypeFamily', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deployment_set_supported_instance_type_family(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_set_supported_instance_type_family_with_options(request, runtime)

    def describe_disk_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDiskMonitorDataResponse(),
            self.do_rpcrequest('DescribeDiskMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disk_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_with_options(request, runtime)

    def describe_disk_replica_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDiskReplicaPairsResponse(),
            self.do_rpcrequest('DescribeDiskReplicaPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disk_replica_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pairs_with_options(request, runtime)

    def describe_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDisksResponse(),
            self.do_rpcrequest('DescribeDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_with_options(request, runtime)

    def describe_disks_full_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeDisksFullStatusResponse(),
            self.do_rpcrequest('DescribeDisksFullStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disks_full_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_full_status_with_options(request, runtime)

    def describe_eip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeEipAddressesResponse(),
            self.do_rpcrequest('DescribeEipAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_addresses_with_options(request, runtime)

    def describe_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeEipMonitorDataResponse(),
            self.do_rpcrequest('DescribeEipMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_monitor_data_with_options(request, runtime)

    def describe_elasticity_assurance_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse(),
            self.do_rpcrequest('DescribeElasticityAssuranceInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elasticity_assurance_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elasticity_assurance_instances_with_options(request, runtime)

    def describe_elasticity_assurances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeElasticityAssurancesResponse(),
            self.do_rpcrequest('DescribeElasticityAssurances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elasticity_assurances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_elasticity_assurances_with_options(request, runtime)

    def describe_eni_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeEniMonitorDataResponse(),
            self.do_rpcrequest('DescribeEniMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eni_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eni_monitor_data_with_options(request, runtime)

    def describe_forward_table_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeForwardTableEntriesResponse(),
            self.do_rpcrequest('DescribeForwardTableEntries', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_forward_table_entries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_forward_table_entries_with_options(request, runtime)

    def describe_ha_vips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeHaVipsResponse(),
            self.do_rpcrequest('DescribeHaVips', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ha_vips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ha_vips_with_options(request, runtime)

    def describe_hpc_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeHpcClustersResponse(),
            self.do_rpcrequest('DescribeHpcClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hpc_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hpc_clusters_with_options(request, runtime)

    def describe_image_components_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageComponentsResponse(),
            self.do_rpcrequest('DescribeImageComponents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_components(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_components_with_options(request, runtime)

    def describe_image_from_family_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageFromFamilyResponse(),
            self.do_rpcrequest('DescribeImageFromFamily', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_from_family(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_from_family_with_options(request, runtime)

    def describe_image_pipeline_executions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImagePipelineExecutionsResponse(),
            self.do_rpcrequest('DescribeImagePipelineExecutions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_pipeline_executions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_pipeline_executions_with_options(request, runtime)

    def describe_image_pipelines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImagePipelinesResponse(),
            self.do_rpcrequest('DescribeImagePipelines', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_pipelines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_pipelines_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImagesResponse(),
            self.do_rpcrequest('DescribeImages', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def describe_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageSharePermissionResponse(),
            self.do_rpcrequest('DescribeImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_share_permission_with_options(request, runtime)

    def describe_image_support_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeImageSupportInstanceTypesResponse(),
            self.do_rpcrequest('DescribeImageSupportInstanceTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_support_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_support_instance_types_with_options(request, runtime)

    def describe_instance_attachment_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse(),
            self.do_rpcrequest('DescribeInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attachment_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attachment_attributes_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    def describe_instance_history_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceHistoryEventsResponse(),
            self.do_rpcrequest('DescribeInstanceHistoryEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_history_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_history_events_with_options(request, runtime)

    def describe_instance_maintenance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse(),
            self.do_rpcrequest('DescribeInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_maintenance_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_maintenance_attributes_with_options(request, runtime)

    def describe_instance_modification_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceModificationPriceResponse(),
            self.do_rpcrequest('DescribeInstanceModificationPrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_modification_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_modification_price_with_options(request, runtime)

    def describe_instance_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceMonitorDataResponse(),
            self.do_rpcrequest('DescribeInstanceMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_monitor_data_with_options(request, runtime)

    def describe_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceRamRoleResponse(),
            self.do_rpcrequest('DescribeInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ram_role_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_instances_full_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstancesFullStatusResponse(),
            self.do_rpcrequest('DescribeInstancesFullStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances_full_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_full_status_with_options(request, runtime)

    def describe_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceStatusResponse(),
            self.do_rpcrequest('DescribeInstanceStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    def describe_instance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceTopologyResponse(),
            self.do_rpcrequest('DescribeInstanceTopology', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_topology_with_options(request, runtime)

    def describe_instance_type_families_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceTypeFamiliesResponse(),
            self.do_rpcrequest('DescribeInstanceTypeFamilies', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_type_families(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_families_with_options(request, runtime)

    def describe_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceTypesResponse(),
            self.do_rpcrequest('DescribeInstanceTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    def describe_instance_vnc_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceVncPasswdResponse(),
            self.do_rpcrequest('DescribeInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_vnc_passwd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_passwd_with_options(request, runtime)

    def describe_instance_vnc_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInstanceVncUrlResponse(),
            self.do_rpcrequest('DescribeInstanceVncUrl', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_vnc_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    def describe_invocation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInvocationResultsResponse(),
            self.do_rpcrequest('DescribeInvocationResults', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_results_with_options(request, runtime)

    def describe_invocations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeInvocationsResponse(),
            self.do_rpcrequest('DescribeInvocations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    def describe_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeKeyPairsResponse(),
            self.do_rpcrequest('DescribeKeyPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_key_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    def describe_launch_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeLaunchTemplatesResponse(),
            self.do_rpcrequest('DescribeLaunchTemplates', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_launch_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_launch_templates_with_options(request, runtime)

    def describe_launch_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeLaunchTemplateVersionsResponse(),
            self.do_rpcrequest('DescribeLaunchTemplateVersions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_launch_template_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_launch_template_versions_with_options(request, runtime)

    def describe_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeLimitationResponse(),
            self.do_rpcrequest('DescribeLimitation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_limitation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    def describe_managed_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeManagedInstancesResponse(),
            self.do_rpcrequest('DescribeManagedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_managed_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_managed_instances_with_options(request, runtime)

    def describe_nat_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNatGatewaysResponse(),
            self.do_rpcrequest('DescribeNatGateways', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_nat_gateways(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_gateways_with_options(request, runtime)

    def describe_network_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse(),
            self.do_rpcrequest('DescribeNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interface_attribute_with_options(request, runtime)

    def describe_network_interface_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse(),
            self.do_rpcrequest('DescribeNetworkInterfacePermissions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_interface_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interface_permissions_with_options(request, runtime)

    def describe_network_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNetworkInterfacesResponse(),
            self.do_rpcrequest('DescribeNetworkInterfaces', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interfaces_with_options(request, runtime)

    def describe_new_project_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse(),
            self.do_rpcrequest('DescribeNewProjectEipMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_new_project_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_new_project_eip_monitor_data_with_options(request, runtime)

    def describe_physical_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePhysicalConnectionsResponse(),
            self.do_rpcrequest('DescribePhysicalConnections', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_physical_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_physical_connections_with_options(request, runtime)

    def describe_prefix_list_associations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePrefixListAssociationsResponse(),
            self.do_rpcrequest('DescribePrefixListAssociations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_prefix_list_associations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_list_associations_with_options(request, runtime)

    def describe_prefix_list_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePrefixListAttributesResponse(),
            self.do_rpcrequest('DescribePrefixListAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_prefix_list_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_list_attributes_with_options(request, runtime)

    def describe_prefix_lists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePrefixListsResponse(),
            self.do_rpcrequest('DescribePrefixLists', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_prefix_lists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_lists_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_recommend_instance_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRecommendInstanceTypeResponse(),
            self.do_rpcrequest('DescribeRecommendInstanceType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_recommend_instance_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_instance_type_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRenewalPriceResponse(),
            self.do_rpcrequest('DescribeRenewalPrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeReservedInstancesResponse(),
            self.do_rpcrequest('DescribeReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instances_with_options(request, runtime)

    def describe_resource_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeResourceByTagsResponse(),
            self.do_rpcrequest('DescribeResourceByTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_by_tags_with_options(request, runtime)

    def describe_resources_modification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeResourcesModificationResponse(),
            self.do_rpcrequest('DescribeResourcesModification', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resources_modification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resources_modification_with_options(request, runtime)

    def describe_router_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRouterInterfacesResponse(),
            self.do_rpcrequest('DescribeRouterInterfaces', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_router_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_router_interfaces_with_options(request, runtime)

    def describe_route_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeRouteTablesResponse(),
            self.do_rpcrequest('DescribeRouteTables', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_route_tables_with_options(request, runtime)

    def describe_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSecurityGroupAttributeResponse(),
            self.do_rpcrequest('DescribeSecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_attribute_with_options(request, runtime)

    def describe_security_group_references_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSecurityGroupReferencesResponse(),
            self.do_rpcrequest('DescribeSecurityGroupReferences', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_references(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_references_with_options(request, runtime)

    def describe_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSecurityGroupsResponse(),
            self.do_rpcrequest('DescribeSecurityGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    def describe_send_file_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSendFileResultsResponse(),
            self.do_rpcrequest('DescribeSendFileResults', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_send_file_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_send_file_results_with_options(request, runtime)

    def describe_snapshot_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotGroupsResponse(),
            self.do_rpcrequest('DescribeSnapshotGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_groups_with_options(request, runtime)

    def describe_snapshot_links_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotLinksResponse(),
            self.do_rpcrequest('DescribeSnapshotLinks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_links(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_links_with_options(request, runtime)

    def describe_snapshot_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotMonitorDataResponse(),
            self.do_rpcrequest('DescribeSnapshotMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_monitor_data_with_options(request, runtime)

    def describe_snapshot_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotPackageResponse(),
            self.do_rpcrequest('DescribeSnapshotPackage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_package_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotsResponse(),
            self.do_rpcrequest('DescribeSnapshots', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    def describe_snapshots_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSnapshotsUsageResponse(),
            self.do_rpcrequest('DescribeSnapshotsUsage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_usage_with_options(request, runtime)

    def describe_spot_advice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSpotAdviceResponse(),
            self.do_rpcrequest('DescribeSpotAdvice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_spot_advice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_advice_with_options(request, runtime)

    def describe_spot_price_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeSpotPriceHistoryResponse(),
            self.do_rpcrequest('DescribeSpotPriceHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_spot_price_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_price_history_with_options(request, runtime)

    def describe_storage_capacity_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeStorageCapacityUnitsResponse(),
            self.do_rpcrequest('DescribeStorageCapacityUnits', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_capacity_units(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_capacity_units_with_options(request, runtime)

    def describe_storage_set_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeStorageSetDetailsResponse(),
            self.do_rpcrequest('DescribeStorageSetDetails', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_set_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_set_details_with_options(request, runtime)

    def describe_storage_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeStorageSetsResponse(),
            self.do_rpcrequest('DescribeStorageSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_sets_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_task_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeTaskAttributeResponse(),
            self.do_rpcrequest('DescribeTaskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_task_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_task_attribute_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeTasksResponse(),
            self.do_rpcrequest('DescribeTasks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def describe_user_business_behavior_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeUserBusinessBehaviorResponse(),
            self.do_rpcrequest('DescribeUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_business_behavior(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_business_behavior_with_options(request, runtime)

    def describe_user_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeUserDataResponse(),
            self.do_rpcrequest('DescribeUserData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_data_with_options(request, runtime)

    def describe_virtual_border_routers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVirtualBorderRoutersResponse(),
            self.do_rpcrequest('DescribeVirtualBorderRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_with_options(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse(),
            self.do_rpcrequest('DescribeVirtualBorderRoutersForPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers_for_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    def describe_vpcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVpcsResponse(),
            self.do_rpcrequest('DescribeVpcs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpcs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    def describe_vrouters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVRoutersResponse(),
            self.do_rpcrequest('DescribeVRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vrouters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vrouters_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeVSwitchesResponse(),
            self.do_rpcrequest('DescribeVSwitches', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def detach_classic_link_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachClassicLinkVpcResponse(),
            self.do_rpcrequest('DetachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_classic_link_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_classic_link_vpc_with_options(request, runtime)

    def detach_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachDiskResponse(),
            self.do_rpcrequest('DetachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_disk_with_options(request, runtime)

    def detach_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachInstanceRamRoleResponse(),
            self.do_rpcrequest('DetachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_instance_ram_role_with_options(request, runtime)

    def detach_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachKeyPairResponse(),
            self.do_rpcrequest('DetachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    def detach_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DetachNetworkInterfaceResponse(),
            self.do_rpcrequest('DetachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_network_interface(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_network_interface_with_options(request, runtime)

    def disable_activation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.DisableActivationResponse(),
            self.do_rpcrequest('DisableActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_activation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_activation_with_options(request, runtime)

    def eip_fill_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.EipFillParamsResponse(),
            self.do_rpcrequest('EipFillParams', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_fill_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_params_with_options(request, runtime)

    def eip_fill_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.EipFillProductResponse(),
            self.do_rpcrequest('EipFillProduct', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_fill_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_product_with_options(request, runtime)

    def eip_notify_paid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.EipNotifyPaidResponse(),
            self.do_rpcrequest('EipNotifyPaid', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_notify_paid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.eip_notify_paid_with_options(request, runtime)

    def enable_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.EnablePhysicalConnectionResponse(),
            self.do_rpcrequest('EnablePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_physical_connection_with_options(request, runtime)

    def export_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ExportImageResponse(),
            self.do_rpcrequest('ExportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    def export_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ExportSnapshotResponse(),
            self.do_rpcrequest('ExportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_snapshot_with_options(request, runtime)

    def get_instance_console_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.GetInstanceConsoleOutputResponse(),
            self.do_rpcrequest('GetInstanceConsoleOutput', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_console_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_console_output_with_options(request, runtime)

    def get_instance_screenshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.GetInstanceScreenshotResponse(),
            self.do_rpcrequest('GetInstanceScreenshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_screenshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_screenshot_with_options(request, runtime)

    def import_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ImportImageResponse(),
            self.do_rpcrequest('ImportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_image_with_options(request, runtime)

    def import_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ImportKeyPairResponse(),
            self.do_rpcrequest('ImportKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    def import_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ImportSnapshotResponse(),
            self.do_rpcrequest('ImportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_snapshot_with_options(request, runtime)

    def install_cloud_assistant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.InstallCloudAssistantResponse(),
            self.do_rpcrequest('InstallCloudAssistant', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.InvokeCommandResponse(),
            self.do_rpcrequest('InvokeCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_command_with_options(request, runtime)

    def join_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.JoinResourceGroupResponse(),
            self.do_rpcrequest('JoinResourceGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    def join_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.JoinSecurityGroupResponse(),
            self.do_rpcrequest('JoinSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    def leave_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.LeaveSecurityGroupResponse(),
            self.do_rpcrequest('LeaveSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def leave_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyAutoProvisioningGroupResponse(),
            self.do_rpcrequest('ModifyAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_provisioning_group_with_options(request, runtime)

    def modify_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyAutoSnapshotPolicyResponse(),
            self.do_rpcrequest('ModifyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    def modify_auto_snapshot_policy_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse(),
            self.do_rpcrequest('ModifyAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy_ex(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_ex_with_options(request, runtime)

    def modify_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyBandwidthPackageSpecResponse(),
            self.do_rpcrequest('ModifyBandwidthPackageSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_bandwidth_package_spec_with_options(request, runtime)

    def modify_capacity_reservation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyCapacityReservationResponse(),
            self.do_rpcrequest('ModifyCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_capacity_reservation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_capacity_reservation_with_options(request, runtime)

    def modify_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyCommandResponse(),
            self.do_rpcrequest('ModifyCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_command_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def modify_dedicated_host_auto_release_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_auto_release_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_release_time_with_options(request, runtime)

    def modify_dedicated_host_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_renew_attribute_with_options(request, runtime)

    def modify_dedicated_host_cluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_cluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_cluster_attribute_with_options(request, runtime)

    def modify_dedicated_hosts_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostsChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_hosts_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_hosts_charge_type_with_options(request, runtime)

    def modify_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDemandResponse(),
            self.do_rpcrequest('ModifyDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_demand_with_options(request, runtime)

    def modify_deployment_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDeploymentSetAttributeResponse(),
            self.do_rpcrequest('ModifyDeploymentSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_deployment_set_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_deployment_set_attribute_with_options(request, runtime)

    def modify_disk_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiskAttributeResponse(),
            self.do_rpcrequest('ModifyDiskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_attribute_with_options(request, runtime)

    def modify_disk_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiskChargeTypeResponse(),
            self.do_rpcrequest('ModifyDiskChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_charge_type_with_options(request, runtime)

    def modify_disk_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyDiskSpecResponse(),
            self.do_rpcrequest('ModifyDiskSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    def modify_eip_address_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyEipAddressAttributeResponse(),
            self.do_rpcrequest('ModifyEipAddressAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_eip_address_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_eip_address_attribute_with_options(request, runtime)

    def modify_elasticity_assurance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyElasticityAssuranceResponse(),
            self.do_rpcrequest('ModifyElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elasticity_assurance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_elasticity_assurance_with_options(request, runtime)

    def modify_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyForwardEntryResponse(),
            self.do_rpcrequest('ModifyForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_forward_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_forward_entry_with_options(request, runtime)

    def modify_ha_vip_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyHaVipAttributeResponse(),
            self.do_rpcrequest('ModifyHaVipAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ha_vip_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    def modify_hpc_cluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyHpcClusterAttributeResponse(),
            self.do_rpcrequest('ModifyHpcClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hpc_cluster_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hpc_cluster_attribute_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyImageAttributeResponse(),
            self.do_rpcrequest('ModifyImageAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_image_share_group_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyImageShareGroupPermissionResponse(),
            self.do_rpcrequest('ModifyImageShareGroupPermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_group_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_group_permission_with_options(request, runtime)

    def modify_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyImageSharePermissionResponse(),
            self.do_rpcrequest('ModifyImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_permission_with_options(request, runtime)

    def modify_instance_attachment_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse(),
            self.do_rpcrequest('ModifyInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attachment_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attachment_attributes_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_instance_auto_release_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse(),
            self.do_rpcrequest('ModifyInstanceAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_release_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_release_time_with_options(request, runtime)

    def modify_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renew_attribute_with_options(request, runtime)

    def modify_instance_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceChargeTypeResponse(),
            self.do_rpcrequest('ModifyInstanceChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    def modify_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceDeploymentResponse(),
            self.do_rpcrequest('ModifyInstanceDeployment', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_deployment_with_options(request, runtime)

    def modify_instance_maintenance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse(),
            self.do_rpcrequest('ModifyInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_maintenance_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintenance_attributes_with_options(request, runtime)

    def modify_instance_metadata_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceMetadataOptionsResponse(),
            self.do_rpcrequest('ModifyInstanceMetadataOptions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_metadata_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_metadata_options_with_options(request, runtime)

    def modify_instance_network_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceNetworkSpecResponse(),
            self.do_rpcrequest('ModifyInstanceNetworkSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_network_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_network_spec_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceSpecResponse(),
            self.do_rpcrequest('ModifyInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_instance_vnc_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceVncPasswdResponse(),
            self.do_rpcrequest('ModifyInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vnc_passwd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vnc_passwd_with_options(request, runtime)

    def modify_instance_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyInstanceVpcAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_attribute_with_options(request, runtime)

    def modify_launch_template_default_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse(),
            self.do_rpcrequest('ModifyLaunchTemplateDefaultVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_launch_template_default_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_launch_template_default_version_with_options(request, runtime)

    def modify_managed_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyManagedInstanceResponse(),
            self.do_rpcrequest('ModifyManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_managed_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_managed_instance_with_options(request, runtime)

    def modify_network_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse(),
            self.do_rpcrequest('ModifyNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_network_interface_attribute_with_options(request, runtime)

    def modify_physical_connection_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse(),
            self.do_rpcrequest('ModifyPhysicalConnectionAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_physical_connection_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    def modify_prefix_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyPrefixListResponse(),
            self.do_rpcrequest('ModifyPrefixList', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prefix_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_prefix_list_with_options(request, runtime)

    def modify_prepay_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyPrepayInstanceSpecResponse(),
            self.do_rpcrequest('ModifyPrepayInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    def modify_reserved_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyReservedInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyReservedInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_reserved_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instance_attribute_with_options(request, runtime)

    def modify_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyReservedInstancesResponse(),
            self.do_rpcrequest('ModifyReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instances_with_options(request, runtime)

    def modify_router_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyRouterInterfaceAttributeResponse(),
            self.do_rpcrequest('ModifyRouterInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_attribute_with_options(request, runtime)

    def modify_router_interface_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyRouterInterfaceSpecResponse(),
            self.do_rpcrequest('ModifyRouterInterfaceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_spec_with_options(request, runtime)

    def modify_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupAttributeResponse(),
            self.do_rpcrequest('ModifySecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_attribute_with_options(request, runtime)

    def modify_security_group_egress_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupEgressRuleResponse(),
            self.do_rpcrequest('ModifySecurityGroupEgressRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_egress_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_egress_rule_with_options(request, runtime)

    def modify_security_group_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupPolicyResponse(),
            self.do_rpcrequest('ModifySecurityGroupPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_policy_with_options(request, runtime)

    def modify_security_group_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySecurityGroupRuleResponse(),
            self.do_rpcrequest('ModifySecurityGroupRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_rule_with_options(request, runtime)

    def modify_snapshot_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySnapshotAttributeResponse(),
            self.do_rpcrequest('ModifySnapshotAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snapshot_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_attribute_with_options(request, runtime)

    def modify_snapshot_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifySnapshotGroupResponse(),
            self.do_rpcrequest('ModifySnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snapshot_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_group_with_options(request, runtime)

    def modify_storage_capacity_unit_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse(),
            self.do_rpcrequest('ModifyStorageCapacityUnitAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_capacity_unit_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_capacity_unit_attribute_with_options(request, runtime)

    def modify_storage_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyStorageSetAttributeResponse(),
            self.do_rpcrequest('ModifyStorageSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_set_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_set_attribute_with_options(request, runtime)

    def modify_user_business_behavior_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyUserBusinessBehaviorResponse(),
            self.do_rpcrequest('ModifyUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_business_behavior(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_business_behavior_with_options(request, runtime)

    def modify_virtual_border_router_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse(),
            self.do_rpcrequest('ModifyVirtualBorderRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_virtual_border_router_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    def modify_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVpcAttributeResponse(),
            self.do_rpcrequest('ModifyVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_attribute_with_options(request, runtime)

    def modify_vrouter_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVRouterAttributeResponse(),
            self.do_rpcrequest('ModifyVRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vrouter_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vrouter_attribute_with_options(request, runtime)

    def modify_vswitch_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ModifyVSwitchAttributeResponse(),
            self.do_rpcrequest('ModifyVSwitchAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vswitch_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vswitch_attribute_with_options(request, runtime)

    def purchase_reserved_instances_offering_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.PurchaseReservedInstancesOfferingResponse(),
            self.do_rpcrequest('PurchaseReservedInstancesOffering', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purchase_reserved_instances_offering(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purchase_reserved_instances_offering_with_options(request, runtime)

    def purchase_storage_capacity_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.PurchaseStorageCapacityUnitResponse(),
            self.do_rpcrequest('PurchaseStorageCapacityUnit', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purchase_storage_capacity_unit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purchase_storage_capacity_unit_with_options(request, runtime)

    def re_activate_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReActivateInstancesResponse(),
            self.do_rpcrequest('ReActivateInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_activate_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_activate_instances_with_options(request, runtime)

    def reboot_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RebootInstanceResponse(),
            self.do_rpcrequest('RebootInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    def reboot_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RebootInstancesResponse(),
            self.do_rpcrequest('RebootInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    def recover_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RecoverVirtualBorderRouterResponse(),
            self.do_rpcrequest('RecoverVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recover_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recover_virtual_border_router_with_options(request, runtime)

    def redeploy_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RedeployDedicatedHostResponse(),
            self.do_rpcrequest('RedeployDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def redeploy_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.redeploy_dedicated_host_with_options(request, runtime)

    def redeploy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RedeployInstanceResponse(),
            self.do_rpcrequest('RedeployInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def redeploy_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.redeploy_instance_with_options(request, runtime)

    def re_init_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReInitDiskResponse(),
            self.do_rpcrequest('ReInitDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_init_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_init_disk_with_options(request, runtime)

    def release_capacity_reservation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleaseCapacityReservationResponse(),
            self.do_rpcrequest('ReleaseCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_capacity_reservation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_reservation_with_options(request, runtime)

    def release_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleaseDedicatedHostResponse(),
            self.do_rpcrequest('ReleaseDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_dedicated_host_with_options(request, runtime)

    def release_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleaseEipAddressResponse(),
            self.do_rpcrequest('ReleaseEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    def release_public_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReleasePublicIpAddressResponse(),
            self.do_rpcrequest('ReleasePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_public_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_public_ip_address_with_options(request, runtime)

    def remove_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RemoveBandwidthPackageIpsResponse(),
            self.do_rpcrequest('RemoveBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_bandwidth_package_ips_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RemoveTagsResponse(),
            self.do_rpcrequest('RemoveTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    def renew_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RenewDedicatedHostsResponse(),
            self.do_rpcrequest('RenewDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_dedicated_hosts_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RenewInstanceResponse(),
            self.do_rpcrequest('RenewInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def replace_system_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReplaceSystemDiskResponse(),
            self.do_rpcrequest('ReplaceSystemDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_system_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_system_disk_with_options(request, runtime)

    def report_instances_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ReportInstancesStatusResponse(),
            self.do_rpcrequest('ReportInstancesStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_instances_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_instances_status_with_options(request, runtime)

    def reset_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ResetDiskResponse(),
            self.do_rpcrequest('ResetDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    def reset_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ResetDisksResponse(),
            self.do_rpcrequest('ResetDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_disks_with_options(request, runtime)

    def resize_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.ResizeDiskResponse(),
            self.do_rpcrequest('ResizeDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_with_options(request, runtime)

    def revoke_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RevokeSecurityGroupResponse(),
            self.do_rpcrequest('RevokeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    def revoke_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RevokeSecurityGroupEgressResponse(),
            self.do_rpcrequest('RevokeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RunCommandResponse(),
            self.do_rpcrequest('RunCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    def run_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.RunInstancesResponse(),
            self.do_rpcrequest('RunInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    def send_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.SendFileResponse(),
            self.do_rpcrequest('SendFile', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    def start_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartDiskReplicaPairResponse(),
            self.do_rpcrequest('StartDiskReplicaPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_pair_with_options(request, runtime)

    def start_elasticity_assurance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartElasticityAssuranceResponse(),
            self.do_rpcrequest('StartElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_elasticity_assurance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_elasticity_assurance_with_options(request, runtime)

    def start_image_pipeline_execution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartImagePipelineExecutionResponse(),
            self.do_rpcrequest('StartImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_image_pipeline_execution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_image_pipeline_execution_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def start_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartInstancesResponse(),
            self.do_rpcrequest('StartInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    def start_terminal_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StartTerminalSessionResponse(),
            self.do_rpcrequest('StartTerminalSession', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_terminal_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_terminal_session_with_options(request, runtime)

    def stop_disk_replica_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopDiskReplicaPairResponse(),
            self.do_rpcrequest('StopDiskReplicaPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_disk_replica_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_pair_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopInstanceResponse(),
            self.do_rpcrequest('StopInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def stop_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopInstancesResponse(),
            self.do_rpcrequest('StopInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    def stop_invocation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.StopInvocationResponse(),
            self.do_rpcrequest('StopInvocation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            ecs_20140526_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def terminate_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.TerminatePhysicalConnectionResponse(),
            self.do_rpcrequest('TerminatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_physical_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_physical_connection_with_options(request, runtime)

    def terminate_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.TerminateVirtualBorderRouterResponse(),
            self.do_rpcrequest('TerminateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_virtual_border_router_with_options(request, runtime)

    def unassign_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassignIpv6AddressesResponse(),
            self.do_rpcrequest('UnassignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassign_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassign_ipv_6addresses_with_options(request, runtime)

    def unassign_private_ip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassignPrivateIpAddressesResponse(),
            self.do_rpcrequest('UnassignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassign_private_ip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassign_private_ip_addresses_with_options(request, runtime)

    def unassociate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassociateEipAddressResponse(),
            self.do_rpcrequest('UnassociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    def unassociate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.UnassociateHaVipResponse(),
            self.do_rpcrequest('UnassociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_ha_vip_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ecs_20140526_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
