# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ess20220222 import models as ess_20220222_models
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
            'cn-qingdao': 'ess.aliyuncs.com',
            'cn-beijing': 'ess.aliyuncs.com',
            'cn-hangzhou': 'ess.aliyuncs.com',
            'cn-shanghai': 'ess.aliyuncs.com',
            'cn-shenzhen': 'ess.aliyuncs.com',
            'cn-hongkong': 'ess.aliyuncs.com',
            'ap-southeast-1': 'ess.aliyuncs.com',
            'us-east-1': 'ess.aliyuncs.com',
            'us-west-1': 'ess.aliyuncs.com',
            'cn-shanghai-finance-1': 'ess.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ess.aliyuncs.com',
            'cn-north-2-gov-1': 'ess.aliyuncs.com',
            'ap-northeast-2-pop': 'ess.aliyuncs.com',
            'cn-beijing-finance-pop': 'ess.aliyuncs.com',
            'cn-beijing-gov-1': 'ess.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ess.aliyuncs.com',
            'cn-edge-1': 'ess.aliyuncs.com',
            'cn-fujian': 'ess.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ess.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ess.aliyuncs.com',
            'cn-hangzhou-finance': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ess.aliyuncs.com',
            'cn-hangzhou-test-306': 'ess.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ess.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ess.aliyuncs.com',
            'cn-qingdao-nebula': 'ess.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ess.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ess.aliyuncs.com',
            'cn-shanghai-inner': 'ess.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ess.aliyuncs.com',
            'cn-shenzhen-inner': 'ess.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ess.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ess.aliyuncs.com',
            'cn-wuhan': 'ess.aliyuncs.com',
            'cn-yushanfang': 'ess.aliyuncs.com',
            'cn-zhangbei': 'ess.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ess.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ess.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ess.aliyuncs.com',
            'eu-west-1-oxs': 'ess.aliyuncs.com',
            'rus-west-1-pop': 'ess.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_eci_scaling_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ApplyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_eci_scaling_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_eci_scaling_configuration_with_options(request, runtime)

    def apply_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ApplyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_scaling_group_with_options(request, runtime)

    def attach_alb_server_groups_with_options(self, request, runtime):
        """
        Before you associate an ALB server group with a scaling group, make sure that the following requirements are met:
        *   The scaling group resides in a virtual private cloud (VPC). The scaling group and the ALB server group must reside in the same VPC.
        *   The ALB server group is in the Available state.
        *   You can associate only a limited number of ALB server groups with a scaling group. To view the quota or manually request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        

        @param request: AttachAlbServerGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_alb_server_groups(self, request):
        """
        Before you associate an ALB server group with a scaling group, make sure that the following requirements are met:
        *   The scaling group resides in a virtual private cloud (VPC). The scaling group and the ALB server group must reside in the same VPC.
        *   The ALB server group is in the Available state.
        *   You can associate only a limited number of ALB server groups with a scaling group. To view the quota or manually request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        

        @param request: AttachAlbServerGroupsRequest

        @return: AttachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_alb_server_groups_with_options(request, runtime)

    def attach_dbinstances_with_options(self, request, runtime):
        """
        Before you associate an ApsaraDB RDS instance with a scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        *   The ApsaraDB RDS instance and the scaling group must belong to the same Alibaba Cloud account.
        *   The ApsaraDB RDS instance must be unlocked. For more information about the lock policy, see [ApsaraDB RDS usage notes](~~41872~~).
        *   The ApsaraDB RDS instance must be in the Running state.
        After an ApsaraDB RDS instance is associated with the scaling group, the default IP address whitelist of the ApsaraDB RDS instance can contain no more than 1,000 IP addresses. For more information, see [Set the whitelist](~~43185~~).
        

        @param request: AttachDBInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_dbinstances(self, request):
        """
        Before you associate an ApsaraDB RDS instance with a scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        *   The ApsaraDB RDS instance and the scaling group must belong to the same Alibaba Cloud account.
        *   The ApsaraDB RDS instance must be unlocked. For more information about the lock policy, see [ApsaraDB RDS usage notes](~~41872~~).
        *   The ApsaraDB RDS instance must be in the Running state.
        After an ApsaraDB RDS instance is associated with the scaling group, the default IP address whitelist of the ApsaraDB RDS instance can contain no more than 1,000 IP addresses. For more information, see [Set the whitelist](~~43185~~).
        

        @param request: AttachDBInstancesRequest

        @return: AttachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_dbinstances_with_options(request, runtime)

    def attach_instances_with_options(self, request, runtime):
        """
        Before you call this operation, take note of the following items:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        The ECS instances or the elastic container instances that you want to add to a scaling group must meet the following requirements:
        *   The instances reside in the same region as the scaling group.
        *   The instances must be in the Running state.
        *   The instances are not added to other scaling groups.
        *   The instances use the subscription or pay-as-you-go billing method, or are preemptible instances.
        *   If the VswitchID parameter is specified for a scaling group, the instances that are in the classic network or those that are not in the same virtual private cloud (VPC) as the specified vSwitch cannot be added to the scaling group.
        *   If the VswitchID parameter is not specified for a scaling group, the instances that are in VPCs cannot be added to the scaling group.
        If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the sum of the number of instances that you want to add and the number of existing instances in the scaling group is greater than the value of the MaxSize parameter, the call fails.
        Instances that are manually added by calling the AttachInstances operation are not associated with the active scaling configuration of the scaling group.
        

        @param request: AttachInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_instances(self, request):
        """
        Before you call this operation, take note of the following items:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        The ECS instances or the elastic container instances that you want to add to a scaling group must meet the following requirements:
        *   The instances reside in the same region as the scaling group.
        *   The instances must be in the Running state.
        *   The instances are not added to other scaling groups.
        *   The instances use the subscription or pay-as-you-go billing method, or are preemptible instances.
        *   If the VswitchID parameter is specified for a scaling group, the instances that are in the classic network or those that are not in the same virtual private cloud (VPC) as the specified vSwitch cannot be added to the scaling group.
        *   If the VswitchID parameter is not specified for a scaling group, the instances that are in VPCs cannot be added to the scaling group.
        If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the sum of the number of instances that you want to add and the number of existing instances in the scaling group is greater than the value of the MaxSize parameter, the call fails.
        Instances that are manually added by calling the AttachInstances operation are not associated with the active scaling configuration of the scaling group.
        

        @param request: AttachInstancesRequest

        @return: AttachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    def attach_load_balancers_with_options(self, request, runtime):
        """
        Before you call this operation to attach a CLB instance to your scaling group, take note of the following items:
        *   The CLB instance and the scaling group must belong to the same Alibaba Cloud account.
        *   The CLB instance and the scaling group must reside in the same region.
        *   The CLB instance must be in the Running state.
        *   The CLB instance must be configured with at least one listener. Health check is enabled for the CLB instance.
        *   The CLB instance and the scaling group must be in the same virtual private cloud (VPC) if their network type is VPC.
        *   If the network type of the scaling group is VPC, the network type of the CLB instance is classic network, and the CLB backend server groups contain instances of the VPC network type, the instances and the scaling group must be in the same VPC.
        *   You can attach only a limited number of CLB instances to a scaling group. Fore more information, see [Limits](~~25863~~).
        

        @param request: AttachLoadBalancersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_load_balancers(self, request):
        """
        Before you call this operation to attach a CLB instance to your scaling group, take note of the following items:
        *   The CLB instance and the scaling group must belong to the same Alibaba Cloud account.
        *   The CLB instance and the scaling group must reside in the same region.
        *   The CLB instance must be in the Running state.
        *   The CLB instance must be configured with at least one listener. Health check is enabled for the CLB instance.
        *   The CLB instance and the scaling group must be in the same virtual private cloud (VPC) if their network type is VPC.
        *   If the network type of the scaling group is VPC, the network type of the CLB instance is classic network, and the CLB backend server groups contain instances of the VPC network type, the instances and the scaling group must be in the same VPC.
        *   You can attach only a limited number of CLB instances to a scaling group. Fore more information, see [Limits](~~25863~~).
        

        @param request: AttachLoadBalancersRequest

        @return: AttachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_load_balancers_with_options(request, runtime)

    def attach_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_server_groups_with_options(request, runtime)

    def attach_vserver_groups_with_options(self, request, runtime):
        """
        Before you call this operation to attach a vServer group to your scaling group, take note of the following items:
        *   The CLB instance and the scaling group must belong to the same Alibaba Cloud account.
        *   The CLB instance and the scaling group must reside in the same region.
        *   The CLB instance must be in the Running state.
        *   The CLB instance must be configured with at least one listener. Health check is enabled for the CLB instance.
        *   The CLB instance and the scaling group must be in the same VPC if their network type is VPC.
        *   If the network type of the scaling group is VPC, the network type of the CLB instance is classic network, and the vServer groups of the CLB instance contain instances of the VPC network type, the instances and the scaling group must be in the same VPC.
        *   The vServer group that you want to attach to your scaling group must belong to the CLB instance.
        *   You can attach only a limited number of vServer groups to a scaling group. For information about the quota on vServer groups, see [Limits](~~25863~~).
        When you call this operation, you must specify the following parameters:
        *   LoadBalancerId: the ID of the CLB instance.
        *   VServerGroupId: the ID of the vServer group.
        *   Port: the port number of the vServer group.
        If a vServer group is attached to a scaling group by using different ports, Auto Scaling considers that more than one vServer group is attached to the scaling group. If multiple vServer groups with the same group ID and port number are specified in the request parameters, only the first vServer group is used. The other vServer groups are ignored.
        

        @param request: AttachVServerGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_vserver_groups(self, request):
        """
        Before you call this operation to attach a vServer group to your scaling group, take note of the following items:
        *   The CLB instance and the scaling group must belong to the same Alibaba Cloud account.
        *   The CLB instance and the scaling group must reside in the same region.
        *   The CLB instance must be in the Running state.
        *   The CLB instance must be configured with at least one listener. Health check is enabled for the CLB instance.
        *   The CLB instance and the scaling group must be in the same VPC if their network type is VPC.
        *   If the network type of the scaling group is VPC, the network type of the CLB instance is classic network, and the vServer groups of the CLB instance contain instances of the VPC network type, the instances and the scaling group must be in the same VPC.
        *   The vServer group that you want to attach to your scaling group must belong to the CLB instance.
        *   You can attach only a limited number of vServer groups to a scaling group. For information about the quota on vServer groups, see [Limits](~~25863~~).
        When you call this operation, you must specify the following parameters:
        *   LoadBalancerId: the ID of the CLB instance.
        *   VServerGroupId: the ID of the vServer group.
        *   Port: the port number of the vServer group.
        If a vServer group is attached to a scaling group by using different ports, Auto Scaling considers that more than one vServer group is attached to the scaling group. If multiple vServer groups with the same group ID and port number are specified in the request parameters, only the first vServer group is used. The other vServer groups are ignored.
        

        @param request: AttachVServerGroupsRequest

        @return: AttachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_vserver_groups_with_options(request, runtime)

    def change_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def complete_lifecycle_action_with_options(self, request, runtime):
        """
        If you set the LifecycleActionResult parameter for a lifecycle hook of a scaling group to CONTINUE in the operation, Auto Scaling continues to complete the scaling activity in the scaling group after the lifecycle hook times out. If you set the LifecycleActionResult parameter to ABANDON, Auto Scaling stops the scaling activity in the scaling group after the lifecycle hook times out.
        

        @param request: CompleteLifecycleActionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CompleteLifecycleActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteLifecycleAction',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CompleteLifecycleActionResponse(),
            self.call_api(params, req, runtime)
        )

    def complete_lifecycle_action(self, request):
        """
        If you set the LifecycleActionResult parameter for a lifecycle hook of a scaling group to CONTINUE in the operation, Auto Scaling continues to complete the scaling activity in the scaling group after the lifecycle hook times out. If you set the LifecycleActionResult parameter to ABANDON, Auto Scaling stops the scaling activity in the scaling group after the lifecycle hook times out.
        

        @param request: CompleteLifecycleActionRequest

        @return: CompleteLifecycleActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.complete_lifecycle_action_with_options(request, runtime)

    def create_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    def create_eci_scaling_configuration_with_options(self, request, runtime):
        """
        A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        

        @param request: CreateEciScalingConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_eci_scaling_configuration(self, request):
        """
        A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        

        @param request: CreateEciScalingConfigurationRequest

        @return: CreateEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eci_scaling_configuration_with_options(request, runtime)

    def create_lifecycle_hook_with_options(self, request, runtime):
        """
        You can create up to six lifecycle hooks for each scaling group. Elastic Compute Service (ECS) instances are not immediately added to or removed from scaling groups that have effective lifecycle hooks during scaling activities. The ECS instances are added to or removed from the scaling groups only after the lifecycle hooks time out. The period of time before the lifecycle hooks time out is specified by the HeartbeatTimeout parameter. Before lifecycle hooks time out, you can initialize the configurations of ECS instances and query data on the ECS instances.
        If lifecycle hooks take effect for scale-out activities, the private IP addresses of ECS instances are added to the IP address whitelists of the associated ApsaraDB RDS instances and the ECS instances are added to the backend server groups of the associated Server Load Balancer (SLB) instances only after the lifecycle hooks time out. If lifecycle hooks take effect for scale-in activities, the private IP addresses of ECS instances are removed from the IP address whitelists of the disassociated ApsaraDB RDS instances and the ECS instances are removed from the backend server groups of the disassociated SLB instances only after the lifecycle hooks time out.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook takes effect, a notification can be sent by using a Message Service (MNS) topic, an MNS queue, or an Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a RAM role for OOS. For more information, see [Grant RAM permissions to OOS](~~120810~~).
        > If your scaling group contains ECS instances and you configure an OOS template to add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the IP address whitelists of cloud databases other than ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to the IP address whitelists of the cloud databases.
        

        @param request: CreateLifecycleHookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    def create_lifecycle_hook(self, request):
        """
        You can create up to six lifecycle hooks for each scaling group. Elastic Compute Service (ECS) instances are not immediately added to or removed from scaling groups that have effective lifecycle hooks during scaling activities. The ECS instances are added to or removed from the scaling groups only after the lifecycle hooks time out. The period of time before the lifecycle hooks time out is specified by the HeartbeatTimeout parameter. Before lifecycle hooks time out, you can initialize the configurations of ECS instances and query data on the ECS instances.
        If lifecycle hooks take effect for scale-out activities, the private IP addresses of ECS instances are added to the IP address whitelists of the associated ApsaraDB RDS instances and the ECS instances are added to the backend server groups of the associated Server Load Balancer (SLB) instances only after the lifecycle hooks time out. If lifecycle hooks take effect for scale-in activities, the private IP addresses of ECS instances are removed from the IP address whitelists of the disassociated ApsaraDB RDS instances and the ECS instances are removed from the backend server groups of the disassociated SLB instances only after the lifecycle hooks time out.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook takes effect, a notification can be sent by using a Message Service (MNS) topic, an MNS queue, or an Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a RAM role for OOS. For more information, see [Grant RAM permissions to OOS](~~120810~~).
        > If your scaling group contains ECS instances and you configure an OOS template to add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the IP address whitelists of cloud databases other than ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to the IP address whitelists of the cloud databases.
        

        @param request: CreateLifecycleHookRequest

        @return: CreateLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_hook_with_options(request, runtime)

    def create_notification_configuration_with_options(self, request, runtime):
        """
        ## Description
        You can configure CloudMonitor system events, Message Service (MNS) queues, or MNS topics to receive notifications. When a specified type of scaling activity or resource change occurs in a scaling group, Auto Scaling sends notifications by using CloudMonitor or MNS.
        

        @param request: CreateNotificationConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_notification_configuration(self, request):
        """
        ## Description
        You can configure CloudMonitor system events, Message Service (MNS) queues, or MNS topics to receive notifications. When a specified type of scaling activity or resource change occurs in a scaling group, Auto Scaling sends notifications by using CloudMonitor or MNS.
        

        @param request: CreateNotificationConfigurationRequest

        @return: CreateNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_notification_configuration_with_options(request, runtime)

    def create_scaling_configuration_with_options(self, tmp_req, runtime):
        """
        Auto Scaling automatically creates Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be created in the following modes:
        *   InstancePatternInfos: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. Auto Scaling selects the instance type that has the lowest price based on the configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode reduces scale-out failures caused by insufficient inventory of instance types.
        *   InstanceType: In this mode, you must specify one instance type.
        *   InstanceTypes: In this mode, you can specify more than one instance type.
        *   InstanceTypeOverrides: In this mode, you can specify multiple instance types and weights for the instance types.
        *   Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines the range of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling creates ECS instances by using the lowest-priced instance type. This mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot specify InstanceType, InstanceTypes, InstanceTypeOverrides, and Cpu and Memory at the same time. You can specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfo at the same time. If you specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-outs. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-outs.
        

        @param tmp_req: CreateScalingConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
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
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
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
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scaling_configuration(self, request):
        """
        Auto Scaling automatically creates Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be created in the following modes:
        *   InstancePatternInfos: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. Auto Scaling selects the instance type that has the lowest price based on the configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode reduces scale-out failures caused by insufficient inventory of instance types.
        *   InstanceType: In this mode, you must specify one instance type.
        *   InstanceTypes: In this mode, you can specify more than one instance type.
        *   InstanceTypeOverrides: In this mode, you can specify multiple instance types and weights for the instance types.
        *   Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines the range of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling creates ECS instances by using the lowest-priced instance type. This mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot specify InstanceType, InstanceTypes, InstanceTypeOverrides, and Cpu and Memory at the same time. You can specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfo at the same time. If you specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-outs. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-outs.
        

        @param request: CreateScalingConfigurationRequest

        @return: CreateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    def create_scaling_group_with_options(self, request, runtime):
        """
        A scaling group is a group of Elastic Compute Service (ECS) instances that can be used in similar business scenarios.
        You can create only a limited number of scaling groups in a region. Go to Quota Center to check the quota of the scaling groups.
        A scaling group does not immediately take effect after you create the scaling group. You must call the EnableScalingGroup operation to enable the scaling group. After you enable the scaling group, Auto Scaling can execute scaling rules to trigger scaling activities in the scaling group.
        The Classic Load Balancer (CLB) instances and ApsaraDB RDS instances that you want to associate with a scaling group must reside in the same region as the scaling group. CLB instances are formerly known as Server Load Balancer (SLB) instances. For more information, see the "Regions and zones" topic.
        If you associate a CLB instance when you create a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the backend server group of the associated CLB instance. You can specify a server group to which ECS instances can be added. You can add ECS instances to the following types of server groups:
        *   Default server group: a group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group.
        *   vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based forwarding rules, you can use vServer groups.
        > If you specify the default server group and multiple vServer groups at the same time, ECS instances are added to all specified server groups.
        The default weight of an ECS instance that is added as a backend server of a CLB instance is 50. The CLB instance that you want to associate with your scaling group must meet the following requirements:
        *   The CLB instance must be in the Active state. You can call the DescribeLoadBalancers operation to query the state of the CLB instance.
        *   The health check feature must be enabled on all listener ports that are configured for the CLB instance. Otherwise, the scaling group fails to be created.
        If you associate an Application Load Balancer (ALB) server group with a scaling group, Auto Scaling automatically adds ECS instances that are in the scaling group to the ALB server group to process requests distributed by the ALB instance to which the ALB server group belongs. You can specify multiple ALB server groups. The server groups must reside in the same virtual private cloud (VPC) as the scaling group. For more information, see the "AttachAlbServerGroups" topic.
        If you associate an ApsaraDB RDS instance with a scaling group, Auto Scaling automatically adds the private IP addresses of the ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance. The ApsaraDB RDS instance that you want to associate with your scaling group must meet the following requirements:
        *   The ApsaraDB RDS instance must be in the Running state. You can call the DescribeDBInstances operation to query the state of the ApsaraDB RDS instance.
        *   The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance cannot exceed the upper limit. For more information, see the "Configure whitelists" topic.
        If you set the MultiAZPolicy parameter of the scaling group to COST_OPTIMIZED, take note of the following items:
        *   You can use the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools parameters to specify the instance allocation method based on the cost optimization policy. This instance allocation method is prioritized during scaling.
        *   If you do not specify the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools parameter, the instance types that are provided at the lowest price are used to create instances based on the cost optimization policy.
        If you set the `Tags.Propagate` parameter of the scaling group to true, the following rules apply:
        *   Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        *   If you specify instance tags in the scaling configuration that is used to create instances and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        *   If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group of the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        

        @param request: CreateScalingGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not UtilClient.is_unset(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scaling_group(self, request):
        """
        A scaling group is a group of Elastic Compute Service (ECS) instances that can be used in similar business scenarios.
        You can create only a limited number of scaling groups in a region. Go to Quota Center to check the quota of the scaling groups.
        A scaling group does not immediately take effect after you create the scaling group. You must call the EnableScalingGroup operation to enable the scaling group. After you enable the scaling group, Auto Scaling can execute scaling rules to trigger scaling activities in the scaling group.
        The Classic Load Balancer (CLB) instances and ApsaraDB RDS instances that you want to associate with a scaling group must reside in the same region as the scaling group. CLB instances are formerly known as Server Load Balancer (SLB) instances. For more information, see the "Regions and zones" topic.
        If you associate a CLB instance when you create a scaling group, Auto Scaling automatically adds ECS instances in the scaling group to the backend server group of the associated CLB instance. You can specify a server group to which ECS instances can be added. You can add ECS instances to the following types of server groups:
        *   Default server group: a group of ECS instances that are used to receive requests. If you do not specify a vServer group or a primary/secondary server group for a listener, requests are forwarded to the ECS instances in the default server group.
        *   vServer group: If you want to forward requests to backend servers that are not in the default server group or configure domain name-based or URL-based forwarding rules, you can use vServer groups.
        > If you specify the default server group and multiple vServer groups at the same time, ECS instances are added to all specified server groups.
        The default weight of an ECS instance that is added as a backend server of a CLB instance is 50. The CLB instance that you want to associate with your scaling group must meet the following requirements:
        *   The CLB instance must be in the Active state. You can call the DescribeLoadBalancers operation to query the state of the CLB instance.
        *   The health check feature must be enabled on all listener ports that are configured for the CLB instance. Otherwise, the scaling group fails to be created.
        If you associate an Application Load Balancer (ALB) server group with a scaling group, Auto Scaling automatically adds ECS instances that are in the scaling group to the ALB server group to process requests distributed by the ALB instance to which the ALB server group belongs. You can specify multiple ALB server groups. The server groups must reside in the same virtual private cloud (VPC) as the scaling group. For more information, see the "AttachAlbServerGroups" topic.
        If you associate an ApsaraDB RDS instance with a scaling group, Auto Scaling automatically adds the private IP addresses of the ECS instances in the scaling group to the IP address whitelist of the ApsaraDB RDS instance. The ApsaraDB RDS instance that you want to associate with your scaling group must meet the following requirements:
        *   The ApsaraDB RDS instance must be in the Running state. You can call the DescribeDBInstances operation to query the state of the ApsaraDB RDS instance.
        *   The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance cannot exceed the upper limit. For more information, see the "Configure whitelists" topic.
        If you set the MultiAZPolicy parameter of the scaling group to COST_OPTIMIZED, take note of the following items:
        *   You can use the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools parameters to specify the instance allocation method based on the cost optimization policy. This instance allocation method is prioritized during scaling.
        *   If you do not specify the OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools parameter, the instance types that are provided at the lowest price are used to create instances based on the cost optimization policy.
        If you set the `Tags.Propagate` parameter of the scaling group to true, the following rules apply:
        *   Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        *   If you specify instance tags in the scaling configuration that is used to create instances and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        *   If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group of the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        

        @param request: CreateScalingGroupRequest

        @return: CreateScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    def create_scaling_rule_with_options(self, request, runtime):
        """
        ## Description
        A scaling rule defines a specific scaling activity, such as adding or removing N instances. If the number of Elastic Compute Service (ECS) instances in a scaling group is less than the minimum number allowed or greater than the maximum number allowed after a scaling rule is executed, Auto Scaling adjusts the number of ECS instances that you want to add or remove. This way, the number of ECS instances can be maintained within the valid range after the scaling rule is executed. The number of ECS instances that is specified in the scaling rule remains unchanged. Example:
        *   If your scaling group contains two ECS instances and allows up to three ECS instances, only one ECS instance is added to your scaling group after you execute a scale-out rule in which three ECS instances are specified. The number of ECS instances that is specified in the scaling rule remains unchanged.
        *   If your scaling group contains three ECS instances and requires at least two ECS instances, only one ECS instance is removed from your scaling group after you execute a scale-in rule in which five ECS instances are specified. The number of ECS instances that is specified in the scaling rule remains unchanged.
        Before you call this operation, take note of the following items:
        *   If you set the AdjustmentType parameter to TotalCapacity, the number of ECS instances in the scaling group is adjusted to the specified value. The value of the AdjustmentValue parameter must be greater than or equal to 0.
        *   If you set the AdjustmentType parameter to QuantityChangeInCapacity or PercentChangeInCapacity, a positive value of AdjustmentValue specifies the number of ECS instances that are added to the scaling group, and a negative value of AdjustmentValue specifies the number of ECS instances that are removed from the scaling group.
        *   If you set the AdjustmentType parameter to PercentChangeInCapacity, Auto Scaling uses the following formula to calculate a value, and then rounds the value to the nearest integer to obtain the number of ECS instances that need to be scaled: Value of TotalCapacity × Value of AdjustmentValue/100.
        *   If the cooldown time is specified in a scaling rule, the specified time applies to the scaling group after the rule is executed. Otherwise, the value of the DefaultCooldown parameter of the scaling group applies to the scaling group.
        *   You can create only a limited number of scaling rules for a scaling group. For more information, see the "Limits" topic.
        *   The unique identifier (ScalingRuleAri) of a scaling rule can be used by the following operations:
        *   ExecuteScalingRule: You can call this operation to manually execute a specific scaling rule by setting the ScalingRuleAri parameter to the unique identifier of the scaling rule.
        *   CreateScheduledTask: You can call this operation to create a scheduled task for a specific scaling rule by setting the ScheduledAction parameter to the unique identifier of the scaling rule.
        

        @param request: CreateScalingRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scaling_rule(self, request):
        """
        ## Description
        A scaling rule defines a specific scaling activity, such as adding or removing N instances. If the number of Elastic Compute Service (ECS) instances in a scaling group is less than the minimum number allowed or greater than the maximum number allowed after a scaling rule is executed, Auto Scaling adjusts the number of ECS instances that you want to add or remove. This way, the number of ECS instances can be maintained within the valid range after the scaling rule is executed. The number of ECS instances that is specified in the scaling rule remains unchanged. Example:
        *   If your scaling group contains two ECS instances and allows up to three ECS instances, only one ECS instance is added to your scaling group after you execute a scale-out rule in which three ECS instances are specified. The number of ECS instances that is specified in the scaling rule remains unchanged.
        *   If your scaling group contains three ECS instances and requires at least two ECS instances, only one ECS instance is removed from your scaling group after you execute a scale-in rule in which five ECS instances are specified. The number of ECS instances that is specified in the scaling rule remains unchanged.
        Before you call this operation, take note of the following items:
        *   If you set the AdjustmentType parameter to TotalCapacity, the number of ECS instances in the scaling group is adjusted to the specified value. The value of the AdjustmentValue parameter must be greater than or equal to 0.
        *   If you set the AdjustmentType parameter to QuantityChangeInCapacity or PercentChangeInCapacity, a positive value of AdjustmentValue specifies the number of ECS instances that are added to the scaling group, and a negative value of AdjustmentValue specifies the number of ECS instances that are removed from the scaling group.
        *   If you set the AdjustmentType parameter to PercentChangeInCapacity, Auto Scaling uses the following formula to calculate a value, and then rounds the value to the nearest integer to obtain the number of ECS instances that need to be scaled: Value of TotalCapacity × Value of AdjustmentValue/100.
        *   If the cooldown time is specified in a scaling rule, the specified time applies to the scaling group after the rule is executed. Otherwise, the value of the DefaultCooldown parameter of the scaling group applies to the scaling group.
        *   You can create only a limited number of scaling rules for a scaling group. For more information, see the "Limits" topic.
        *   The unique identifier (ScalingRuleAri) of a scaling rule can be used by the following operations:
        *   ExecuteScalingRule: You can call this operation to manually execute a specific scaling rule by setting the ScalingRuleAri parameter to the unique identifier of the scaling rule.
        *   CreateScheduledTask: You can call this operation to create a scheduled task for a specific scaling rule by setting the ScheduledAction parameter to the unique identifier of the scaling rule.
        

        @param request: CreateScalingRuleRequest

        @return: CreateScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    def create_scheduled_task_with_options(self, request, runtime):
        """
        If a scheduled task fails to trigger a scaling activity due to an ongoing scaling activity in a scaling group or because the scaling group is disabled, the scheduled task is automatically retried during the period that is specified by the LaunchExpirationTime parameter. If the scheduled task still fails to trigger a scaling activity after the period ends, the task is automatically skipped.
        *   If multiple tasks are scheduled at similar points in time to trigger scaling activities in the same scaling group, the earliest task triggers the scaling activity first. Other tasks trigger scaling activities within their launch expiration time. Only one scaling activity can be triggered in a scaling group at a time.`` If the previous scaling activity is complete and another scheduled task attempts to trigger a scaling activity, Auto Scaling executes the scaling rule that is specified in the scheduled task and then triggers a scaling activity.``
        *   A scheduled task supports the following scaling methods:
        *   `ScheduledAction`: Specify an existing scaling rule that you want Auto Scaling to execute when the scheduled task is triggered.
        *   `ScalingGroupId`: Specify the minimum number, maximum number, or expected number of instances for the scaling group for which you created the scheduled task.
        > You cannot specify the `ScheduledAction` and ScalingGroupId parameters at the same time.
        

        @param request: CreateScheduledTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scheduled_task(self, request):
        """
        If a scheduled task fails to trigger a scaling activity due to an ongoing scaling activity in a scaling group or because the scaling group is disabled, the scheduled task is automatically retried during the period that is specified by the LaunchExpirationTime parameter. If the scheduled task still fails to trigger a scaling activity after the period ends, the task is automatically skipped.
        *   If multiple tasks are scheduled at similar points in time to trigger scaling activities in the same scaling group, the earliest task triggers the scaling activity first. Other tasks trigger scaling activities within their launch expiration time. Only one scaling activity can be triggered in a scaling group at a time.`` If the previous scaling activity is complete and another scheduled task attempts to trigger a scaling activity, Auto Scaling executes the scaling rule that is specified in the scheduled task and then triggers a scaling activity.``
        *   A scheduled task supports the following scaling methods:
        *   `ScheduledAction`: Specify an existing scaling rule that you want Auto Scaling to execute when the scheduled task is triggered.
        *   `ScalingGroupId`: Specify the minimum number, maximum number, or expected number of instances for the scaling group for which you created the scheduled task.
        > You cannot specify the `ScheduledAction` and ScalingGroupId parameters at the same time.
        

        @param request: CreateScheduledTaskRequest

        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    def deactivate_scaling_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeactivateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def deactivate_scaling_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deactivate_scaling_configuration_with_options(request, runtime)

    def delete_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    def delete_eci_scaling_configuration_with_options(self, request, runtime):
        """
        You cannot delete a scaling configuration that is used to create elastic container instances in the following scenarios:
        *   The scaling configuration is in the Active state.
        *   The scaling group contains elastic container instances that are created based on the scaling configuration.
        

        @param request: DeleteEciScalingConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteEciScalingConfigurationResponse
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
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_eci_scaling_configuration(self, request):
        """
        You cannot delete a scaling configuration that is used to create elastic container instances in the following scenarios:
        *   The scaling configuration is in the Active state.
        *   The scaling group contains elastic container instances that are created based on the scaling configuration.
        

        @param request: DeleteEciScalingConfigurationRequest

        @return: DeleteEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_eci_scaling_configuration_with_options(request, runtime)

    def delete_lifecycle_hook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_lifecycle_hook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_hook_with_options(request, runtime)

    def delete_notification_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_notification_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_configuration_with_options(request, runtime)

    def delete_scaling_configuration_with_options(self, request, runtime):
        """
        You cannot delete a scaling configuration in one of the following scenarios:
        *   The scaling configuration in your scaling group is in the Active state.
        *   The scaling group contains ECS instances that were created based on the scaling configuration.
        

        @param request: DeleteScalingConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scaling_configuration(self, request):
        """
        You cannot delete a scaling configuration in one of the following scenarios:
        *   The scaling configuration in your scaling group is in the Active state.
        *   The scaling group contains ECS instances that were created based on the scaling configuration.
        

        @param request: DeleteScalingConfigurationRequest

        @return: DeleteScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    def delete_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    def delete_scaling_rule_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    def delete_scheduled_task_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scheduled_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    def describe_alarms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    def describe_eci_scaling_configuration_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_format):
            query['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurationDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_eci_scaling_configuration_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_scaling_configuration_detail_with_options(request, runtime)

    def describe_eci_scaling_configurations_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_eci_scaling_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_scaling_configurations_with_options(request, runtime)

    def describe_lifecycle_actions_with_options(self, request, runtime):
        """
        If a scaling activity is executed and a lifecycle hook is created for the scaling activity, the lifecycle hook triggers a lifecycle action. A lifecycle action can be in one of the following states:
        *   If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        *   If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action expires and ECS instances are added to or removed from a scaling group.
        *   If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        If you do not specify the action to perform, such as execute a specific OOS template, after a lifecycle hook ends, you can call this operation to obtain the token of the lifecycle action that corresponds to the lifecycle hook. Then, you can specify a custom action to perform after the lifecycle hook ends.
        

        @param request: DescribeLifecycleActionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLifecycleActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleActions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lifecycle_actions(self, request):
        """
        If a scaling activity is executed and a lifecycle hook is created for the scaling activity, the lifecycle hook triggers a lifecycle action. A lifecycle action can be in one of the following states:
        *   If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        *   If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action expires and ECS instances are added to or removed from a scaling group.
        *   If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        If you do not specify the action to perform, such as execute a specific OOS template, after a lifecycle hook ends, you can call this operation to obtain the token of the lifecycle action that corresponds to the lifecycle hook. Then, you can specify a custom action to perform after the lifecycle hook ends.
        

        @param request: DescribeLifecycleActionsRequest

        @return: DescribeLifecycleActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_actions_with_options(request, runtime)

    def describe_lifecycle_hooks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleHooks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleHooksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_lifecycle_hooks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_hooks_with_options(request, runtime)

    def describe_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLimitation',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_limitation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    def describe_notification_configurations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_notification_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_configurations_with_options(request, runtime)

    def describe_notification_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_notification_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_types_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action='DescribeRegions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_scaling_activities_with_options(self, request, runtime):
        """
        You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        

        @param request: DescribeScalingActivitiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeScalingActivitiesResponse
        """
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
        if not UtilClient.is_unset(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_activities(self, request):
        """
        You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        

        @param request: DescribeScalingActivitiesRequest

        @return: DescribeScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    def describe_scaling_activity_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivityDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivityDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_activity_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    def describe_scaling_configurations_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    def describe_scaling_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_format):
            query['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_detail_with_options(request, runtime)

    def describe_scaling_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
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
        if not UtilClient.is_unset(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_groups_with_options(request, runtime)

    def describe_scaling_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.creation_types):
            query['CreationTypes'] = request.creation_types
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not UtilClient.is_unset(request.lifecycle_states):
            query['LifecycleStates'] = request.lifecycle_states
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
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    def describe_scaling_rules_with_options(self, request, runtime):
        """
        You can specify a scaling group ID to query all scaling rules in the scaling group. You can also specify the scaling rule ID, name, unique identifier, and type in the request parameters as filter conditions.
        

        @param request: DescribeScalingRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeScalingRulesResponse
        """
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not UtilClient.is_unset(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not UtilClient.is_unset(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scaling_rules(self, request):
        """
        You can specify a scaling group ID to query all scaling rules in the scaling group. You can also specify the scaling rule ID, name, unique identifier, and type in the request parameters as filter conditions.
        

        @param request: DescribeScalingRulesRequest

        @return: DescribeScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    def describe_scheduled_tasks_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not UtilClient.is_unset(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scheduled_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    def detach_alb_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_alb_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_alb_server_groups_with_options(request, runtime)

    def detach_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_dbinstances_with_options(request, runtime)

    def detach_instances_with_options(self, request, runtime):
        """
        After ECS instances or elastic container instances are removed from a scaling group, you can call the AttachInstances operation to add the ECS instances or elastic container instances that are removed from the scaling group to other scaling groups.
        After you remove an ECS instance or elastic container instance by calling the DetachInstances operation, the instance is not stopped or released.
        Before you call this operation, make sure that the following conditions are met:
        *   The specified scaling group is enabled.
        *   No scaling activities in the specified scaling group are in progress.
        > If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates only that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        The number of ECS instances or elastic container instances in a scaling group after you remove a specific number of instances from the scaling group must be equal to or greater than the value of the MinSize parameter. Otherwise, an error is reported when you call the DetachInstances operation.
        

        @param request: DetachInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_instances(self, request):
        """
        After ECS instances or elastic container instances are removed from a scaling group, you can call the AttachInstances operation to add the ECS instances or elastic container instances that are removed from the scaling group to other scaling groups.
        After you remove an ECS instance or elastic container instance by calling the DetachInstances operation, the instance is not stopped or released.
        Before you call this operation, make sure that the following conditions are met:
        *   The specified scaling group is enabled.
        *   No scaling activities in the specified scaling group are in progress.
        > If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates only that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        The number of ECS instances or elastic container instances in a scaling group after you remove a specific number of instances from the scaling group must be equal to or greater than the value of the MinSize parameter. Otherwise, an error is reported when you call the DetachInstances operation.
        

        @param request: DetachInstancesRequest

        @return: DetachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    def detach_load_balancers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_load_balancers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_load_balancers_with_options(request, runtime)

    def detach_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_server_groups_with_options(request, runtime)

    def detach_vserver_groups_with_options(self, request, runtime):
        """
        You can use the following parameters to specify the vServer groups that you want to detach from your scaling group.
        *   LoadBalancerId: the ID of the Classic Load Balancer (CLB) instance.
        *   VServerGroupId: the ID of the vServer group.
        *   Port: the port number of the vServer group.
        If the vServer group that is specified in this call matches the vServer group associated with your scaling group, the vServer group can be detached. Otherwise, the request for detaching the vServer group is ignored, and no error is reported.
        

        @param request: DetachVServerGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_vserver_groups(self, request):
        """
        You can use the following parameters to specify the vServer groups that you want to detach from your scaling group.
        *   LoadBalancerId: the ID of the Classic Load Balancer (CLB) instance.
        *   VServerGroupId: the ID of the vServer group.
        *   Port: the port number of the vServer group.
        If the vServer group that is specified in this call matches the vServer group associated with your scaling group, the vServer group can be detached. Otherwise, the request for detaching the vServer group is ignored, and no error is reported.
        

        @param request: DetachVServerGroupsRequest

        @return: DetachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_vserver_groups_with_options(request, runtime)

    def disable_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    def disable_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    def enable_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    def enable_scaling_group_with_options(self, request, runtime):
        """
        You can call this operation to enable a scaling group that is in the Inactive state and has an instance configuration source. The instance configuration source can be a scaling configuration, a launch template, or an Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If a scaling group is not in the Inactive state or does not have an active instance configuration source, you cannot call this operation to enable the scaling group.
        > A scaling group can have only one active instance configuration source. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If an instance configuration source has been configured for the scaling group before you call this operation, the scaling configuration or launch template that you specify in the request overwrites the original scaling configuration or launch template.
        If you specify a value for the InstanceIds parameter when you call the operation, Auto Scaling checks whether the total number of ECS instances is within the range allowed in the scaling group after you call the operation.
        *   If the total number of ECS instances is less than the minimum number of instances required in the scaling group after you call the operation, Auto Scaling automatically creates the required number of pay-as-you-go ECS instances and adds the instances to the scaling group to reach the minimum number. For example, if the minimum number of instances required in your scaling group is five, and you specify the InstanceIds parameter to add two ECS instances to the scaling group, Auto Scaling automatically creates three instances in the scaling group after the two instances are added.
        *   If the value of the TotalCapacity parameter is greater than the value of the MaxSize parameter, the call fails.
        

        @param request: EnableScalingGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_scaling_group(self, request):
        """
        You can call this operation to enable a scaling group that is in the Inactive state and has an instance configuration source. The instance configuration source can be a scaling configuration, a launch template, or an Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If a scaling group is not in the Inactive state or does not have an active instance configuration source, you cannot call this operation to enable the scaling group.
        > A scaling group can have only one active instance configuration source. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If an instance configuration source has been configured for the scaling group before you call this operation, the scaling configuration or launch template that you specify in the request overwrites the original scaling configuration or launch template.
        If you specify a value for the InstanceIds parameter when you call the operation, Auto Scaling checks whether the total number of ECS instances is within the range allowed in the scaling group after you call the operation.
        *   If the total number of ECS instances is less than the minimum number of instances required in the scaling group after you call the operation, Auto Scaling automatically creates the required number of pay-as-you-go ECS instances and adds the instances to the scaling group to reach the minimum number. For example, if the minimum number of instances required in your scaling group is five, and you specify the InstanceIds parameter to add two ECS instances to the scaling group, Auto Scaling automatically creates three instances in the scaling group after the two instances are added.
        *   If the value of the TotalCapacity parameter is greater than the value of the MaxSize parameter, the call fails.
        

        @param request: EnableScalingGroupRequest

        @return: EnableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    def enter_standby_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnterStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnterStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    def enter_standby(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enter_standby_with_options(request, runtime)

    def execute_scaling_rule_with_options(self, request, runtime):
        """
        Before you call this operation, take note of the following items:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        You can specify only a limited number of ECS instances in each adjustment. For more information, see the description of the AdjustmentValue parameter in the CreateScalingRule topic.
        

        @param request: ExecuteScalingRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExecuteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.metric_value):
            query['MetricValue'] = request.metric_value
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
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExecuteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_scaling_rule(self, request):
        """
        Before you call this operation, take note of the following items:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        You can specify only a limited number of ECS instances in each adjustment. For more information, see the description of the AdjustmentValue parameter in the CreateScalingRule topic.
        

        @param request: ExecuteScalingRuleRequest

        @return: ExecuteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    def exit_standby_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExitStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExitStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    def exit_standby(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exit_standby_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def modify_alarm_with_options(self, request, runtime):
        """
        If you set MetricType to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Custom monitoring event-triggered tasks](~~74861~~).
        *   When you create an event-triggered task, you must specify MetricName, DimensionKey, and DimensionValue to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances in a scaling group within an Alibaba Cloud account.
        *   If you set MetricType to custom, the valid values are your custom metrics.
        *   For information about the metrics that are supported if you set MetricType to system, see [Event-triggered task for system monitoring](~~74854~~).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see `DimensionKey` and `DimensionValue` in the "Request parameters" section of this topic.
        

        @param request: ModifyAlarmRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_alarm(self, request):
        """
        If you set MetricType to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Custom monitoring event-triggered tasks](~~74861~~).
        *   When you create an event-triggered task, you must specify MetricName, DimensionKey, and DimensionValue to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances in a scaling group within an Alibaba Cloud account.
        *   If you set MetricType to custom, the valid values are your custom metrics.
        *   For information about the metrics that are supported if you set MetricType to system, see [Event-triggered task for system monitoring](~~74854~~).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see `DimensionKey` and `DimensionValue` in the "Request parameters" section of this topic.
        

        @param request: ModifyAlarmRequest

        @return: ModifyAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_alarm_with_options(request, runtime)

    def modify_eci_scaling_configuration_with_options(self, request, runtime):
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        

        @param request: ModifyEciScalingConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_eci_scaling_configuration(self, request):
        """
        If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        

        @param request: ModifyEciScalingConfigurationRequest

        @return: ModifyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_eci_scaling_configuration_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_lifecycle_hook_with_options(self, request, runtime):
        """
        You can use one of the following methods to specify the lifecycle hook that you want to modify:
        *   Specify the lifecycle hook ID by using the LifecycleHookId parameter. When you use this method, the ScalingGroupId and LifecycleHookName parameters are ignored.
        *   Specify the scaling group ID by using the ScalingGroupId parameter and specify the lifecycle hook name by using the LifecycleHookName parameter.
        

        @param request: ModifyLifecycleHookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_lifecycle_hook(self, request):
        """
        You can use one of the following methods to specify the lifecycle hook that you want to modify:
        *   Specify the lifecycle hook ID by using the LifecycleHookId parameter. When you use this method, the ScalingGroupId and LifecycleHookName parameters are ignored.
        *   Specify the scaling group ID by using the ScalingGroupId parameter and specify the lifecycle hook name by using the LifecycleHookName parameter.
        

        @param request: ModifyLifecycleHookRequest

        @return: ModifyLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_hook_with_options(request, runtime)

    def modify_notification_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_notification_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_notification_configuration_with_options(request, runtime)

    def modify_scaling_configuration_with_options(self, tmp_req, runtime):
        """
        You can change the name of a scaling configuration in a scaling group. The name must be unique within the scaling group.
        

        @param tmp_req: ModifyScalingConfigurationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scaling_configuration(self, request):
        """
        You can change the name of a scaling configuration in a scaling group. The name must be unique within the scaling group.
        

        @param request: ModifyScalingConfigurationRequest

        @return: ModifyScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_configuration_with_options(request, runtime)

    def modify_scaling_group_with_options(self, request, runtime):
        """
        You cannot call this operation to modify the settings of the following parameters:
        *   RegionId
        *   LoadBalancerId
        > If you want to change the CLB instances that are associated with your scaling group, call the AttachLoadBalancers and DetachLoadBalancers operations.
        *   DBInstanceId
        **\
        **Note**If you want to change the ApsaraDB RDS instances that are associated with your scaling group, call the AttachDBInstances and DetachDBInstances operations.
        *   You can modify only scaling groups that are in the Active or Inactive state.
        *   If you enable a new scaling configuration, Elastic Compute Service (ECS) instances that are created based on the previous scaling configuration still run as expected in the scaling group.
        *   If the total number of instances in the scaling group is greater than the allowed maximum number after you change the value of the MaxSize parameter, Auto Scaling automatically removes instances from the scaling group to ensure that the number of instances is within the new range.
        *   If the total number of instances in the scaling group is less than the allowed minimum number after you change the value of the MinSize parameter, Auto Scaling automatically adds instances to the scaling group to ensure that the number of instances is within the new range.
        *   If the total number of instances in the scaling group does not match the expected number of instances after you change the value of the DesiredCapacity parameter, Auto Scaling automatically adds instances to or removes instances from the scaling group to ensure that the number of instances matches the value of the DesiredCapacity parameter.
        

        @param request: ModifyScalingGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.disable_desired_capacity):
            query['DisableDesiredCapacity'] = request.disable_desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scaling_group(self, request):
        """
        You cannot call this operation to modify the settings of the following parameters:
        *   RegionId
        *   LoadBalancerId
        > If you want to change the CLB instances that are associated with your scaling group, call the AttachLoadBalancers and DetachLoadBalancers operations.
        *   DBInstanceId
        **\
        **Note**If you want to change the ApsaraDB RDS instances that are associated with your scaling group, call the AttachDBInstances and DetachDBInstances operations.
        *   You can modify only scaling groups that are in the Active or Inactive state.
        *   If you enable a new scaling configuration, Elastic Compute Service (ECS) instances that are created based on the previous scaling configuration still run as expected in the scaling group.
        *   If the total number of instances in the scaling group is greater than the allowed maximum number after you change the value of the MaxSize parameter, Auto Scaling automatically removes instances from the scaling group to ensure that the number of instances is within the new range.
        *   If the total number of instances in the scaling group is less than the allowed minimum number after you change the value of the MinSize parameter, Auto Scaling automatically adds instances to the scaling group to ensure that the number of instances is within the new range.
        *   If the total number of instances in the scaling group does not match the expected number of instances after you change the value of the DesiredCapacity parameter, Auto Scaling automatically adds instances to or removes instances from the scaling group to ensure that the number of instances matches the value of the DesiredCapacity parameter.
        

        @param request: ModifyScalingGroupRequest

        @return: ModifyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    def modify_scaling_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    def modify_scheduled_task_with_options(self, request, runtime):
        """
        You can use the following parameters to specify the scaling method of a scheduled task:
        *   If you use the `ScheduledAction` parameter, you must select an existing scaling rule for the scheduled task.
        *   If you use the `ScalingGroupId` parameter, you must specify the minimum number, maximum number, or expected number of instances in the scheduled task.
        > You cannot specify the `ScheduledAction` and `ScalingGroupId` parameters at the same time.
        

        @param request: ModifyScheduledTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scheduled_task(self, request):
        """
        You can use the following parameters to specify the scaling method of a scheduled task:
        *   If you use the `ScheduledAction` parameter, you must select an existing scaling rule for the scheduled task.
        *   If you use the `ScalingGroupId` parameter, you must specify the minimum number, maximum number, or expected number of instances in the scheduled task.
        > You cannot specify the `ScheduledAction` and `ScalingGroupId` parameters at the same time.
        

        @param request: ModifyScheduledTaskRequest

        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    def rebalance_instances_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RebalanceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def rebalance_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebalance_instances_with_options(request, runtime)

    def record_lifecycle_action_heartbeat_with_options(self, request, runtime):
        """
        You can call this operation to prolong the length of a lifecycle hook up to 20 times. Take note that the total length of a lifecycle hook cannot exceed 6 hours.
        

        @param request: RecordLifecycleActionHeartbeatRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RecordLifecycleActionHeartbeatResponse
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
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordLifecycleActionHeartbeat',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RecordLifecycleActionHeartbeatResponse(),
            self.call_api(params, req, runtime)
        )

    def record_lifecycle_action_heartbeat(self, request):
        """
        You can call this operation to prolong the length of a lifecycle hook up to 20 times. Take note that the total length of a lifecycle hook cannot exceed 6 hours.
        

        @param request: RecordLifecycleActionHeartbeatRequest

        @return: RecordLifecycleActionHeartbeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.record_lifecycle_action_heartbeat_with_options(request, runtime)

    def remove_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RemoveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    def resume_processes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ResumeProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_processes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_processes_with_options(request, runtime)

    def scale_with_adjustment_with_options(self, tmp_req, runtime):
        """
        Compared with the ExecuteScalingRule operation, the ScaleWithAdjustment operation does not require a scaling rule to be created in advance. Before you call the ScaleWithAdjustment operation, take note of the following items:
        *   The following conditions must be met:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        *   If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        *   If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        *   If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the `ScalingActivityId` parameter in the response.
        

        @param tmp_req: ScaleWithAdjustmentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ScaleWithAdjustmentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ScaleWithAdjustmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        if not UtilClient.is_unset(tmp_req.overrides):
            request.overrides_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.overrides, 'Overrides', 'json')
        query = {}
        if not UtilClient.is_unset(request.activity_metadata):
            query['ActivityMetadata'] = request.activity_metadata
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.overrides_shrink):
            query['Overrides'] = request.overrides_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleWithAdjustment',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ScaleWithAdjustmentResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_with_adjustment(self, request):
        """
        Compared with the ExecuteScalingRule operation, the ScaleWithAdjustment operation does not require a scaling rule to be created in advance. Before you call the ScaleWithAdjustment operation, take note of the following items:
        *   The following conditions must be met:
        *   The scaling group is in the Active state.
        *   No scaling activities in the scaling group are in progress.
        *   If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        *   If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        *   If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the `ScalingActivityId` parameter in the response.
        

        @param request: ScaleWithAdjustmentRequest

        @return: ScaleWithAdjustmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scale_with_adjustment_with_options(request, runtime)

    def set_group_deletion_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGroupDeletionProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetGroupDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_group_deletion_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_deletion_protection_with_options(request, runtime)

    def set_instance_health_with_options(self, request, runtime):
        """
        Configures the health check feature for Elastic Compute Service (ECS) instances.
        

        @param request: SetInstanceHealthRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceHealth',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstanceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    def set_instance_health(self, request):
        """
        Configures the health check feature for Elastic Compute Service (ECS) instances.
        

        @param request: SetInstanceHealthRequest

        @return: SetInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instance_health_with_options(request, runtime)

    def set_instances_protection_with_options(self, request, runtime):
        """
        Puts one or more Elastic Compute Service (ECS) instances into the Protected state.
        

        @param request: SetInstancesProtectionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetInstancesProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstancesProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstancesProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_instances_protection(self, request):
        """
        Puts one or more Elastic Compute Service (ECS) instances into the Protected state.
        

        @param request: SetInstancesProtectionRequest

        @return: SetInstancesProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instances_protection_with_options(request, runtime)

    def suspend_processes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SuspendProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_processes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_processes_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def verify_authentication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.only_check):
            query['OnlyCheck'] = request.only_check
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyAuthentication',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_authentication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    def verify_user_with_options(self, request, runtime):
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUser',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_user_with_options(request, runtime)
