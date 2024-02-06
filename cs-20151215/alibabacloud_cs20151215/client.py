# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cs20151215 import models as cs20151215_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'cs.aliyuncs.com',
            'cn-beijing-finance-pop': 'cs.aliyuncs.com',
            'cn-beijing-gov-1': 'cs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cs.aliyuncs.com',
            'cn-edge-1': 'cs.aliyuncs.com',
            'cn-fujian': 'cs.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cs.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cs.aliyuncs.com',
            'cn-hangzhou-test-306': 'cs.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cs.aliyuncs.com',
            'cn-qingdao-nebula': 'cs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cs.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cs.aliyuncs.com',
            'cn-shanghai-inner': 'cs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cs.aliyuncs.com',
            'cn-shenzhen-inner': 'cs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cs.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cs.aliyuncs.com',
            'cn-wuhan': 'cs.aliyuncs.com',
            'cn-yushanfang': 'cs.aliyuncs.com',
            'cn-zhangbei': 'cs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cs.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cs.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cs.aliyuncs.com',
            'eu-west-1-oxs': 'cs.aliyuncs.com',
            'rus-west-1-pop': 'cs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_instances_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/attach' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_instances(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_instances_with_options(cluster_id, request, headers, runtime)

    def attach_instances_to_node_pool_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachInstancesToNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/attach' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesToNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_instances_to_node_pool(self, cluster_id, nodepool_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_instances_to_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def cancel_cluster_upgrade_with_options(self, cluster_id, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelClusterUpgradeResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelClusterUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s/upgrade/cancel' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelClusterUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_cluster_upgrade(self, cluster_id):
        """
        @deprecated
        

        @return: CancelClusterUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_cluster_upgrade_with_options(cluster_id, headers, runtime)

    def cancel_component_upgrade_with_options(self, cluster_id, component_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/cancel' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(component_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_component_upgrade(self, cluster_id, component_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_component_upgrade_with_options(cluster_id, component_id, headers, runtime)

    def cancel_operation_plan_with_options(self, plan_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelOperationPlan',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/operation/plans/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(plan_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelOperationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_operation_plan(self, plan_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_operation_plan_with_options(plan_id, headers, runtime)

    def cancel_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tasks/%s/cancel' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    def cancel_workflow_with_options(self, workflow_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/gs/workflow/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_workflow(self, workflow_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_workflow_with_options(workflow_name, request, headers, runtime)

    def check_control_plane_log_enable_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckControlPlaneLogEnable',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/controlplanelog' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CheckControlPlaneLogEnableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_control_plane_log_enable(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_control_plane_log_enable_with_options(cluster_id, headers, runtime)

    def create_autoscaling_config_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_down_duration):
            body['cool_down_duration'] = request.cool_down_duration
        if not UtilClient.is_unset(request.daemonset_eviction_for_nodes):
            body['daemonset_eviction_for_nodes'] = request.daemonset_eviction_for_nodes
        if not UtilClient.is_unset(request.expander):
            body['expander'] = request.expander
        if not UtilClient.is_unset(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not UtilClient.is_unset(request.max_graceful_termination_sec):
            body['max_graceful_termination_sec'] = request.max_graceful_termination_sec
        if not UtilClient.is_unset(request.min_replica_count):
            body['min_replica_count'] = request.min_replica_count
        if not UtilClient.is_unset(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not UtilClient.is_unset(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not UtilClient.is_unset(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not UtilClient.is_unset(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        if not UtilClient.is_unset(request.skip_nodes_with_local_storage):
            body['skip_nodes_with_local_storage'] = request.skip_nodes_with_local_storage
        if not UtilClient.is_unset(request.skip_nodes_with_system_pods):
            body['skip_nodes_with_system_pods'] = request.skip_nodes_with_system_pods
        if not UtilClient.is_unset(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not UtilClient.is_unset(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoscalingConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/cluster/%s/autoscale/config/' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateAutoscalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_autoscaling_config(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_autoscaling_config_with_options(cluster_id, request, headers, runtime)

    def create_cluster_with_options(self, request, headers, runtime):
        """
        This topic describes all parameters for creating an ACK cluster. You can create the following types of ACK clusters.
        *   [Create an ACK managed cluster](~~90776~~)
        *   [Create an ACK dedicated cluster](~~197620~~)
        *   [Create an ACK Serverless cluster](~~144246~~)
        *   [Create an ACK Edge cluster](~~128204~~)
        *   [Create an ACK Basic cluster that supports sandboxed containers](~~196321~~)
        *   [Create an ACK Pro cluster that supports sandboxed containers](~~140623~~)
        

        @param request: CreateClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.addons):
            body['addons'] = request.addons
        if not UtilClient.is_unset(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not UtilClient.is_unset(request.charge_type):
            body['charge_type'] = request.charge_type
        if not UtilClient.is_unset(request.cis_enabled):
            body['cis_enabled'] = request.cis_enabled
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not UtilClient.is_unset(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not UtilClient.is_unset(request.controlplane_log_components):
            body['controlplane_log_components'] = request.controlplane_log_components
        if not UtilClient.is_unset(request.controlplane_log_project):
            body['controlplane_log_project'] = request.controlplane_log_project
        if not UtilClient.is_unset(request.controlplane_log_ttl):
            body['controlplane_log_ttl'] = request.controlplane_log_ttl
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.custom_san):
            body['custom_san'] = request.custom_san
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not UtilClient.is_unset(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not UtilClient.is_unset(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            body['image_type'] = request.image_type
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.ip_stack):
            body['ip_stack'] = request.ip_stack
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.logging_type):
            body['logging_type'] = request.logging_type
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not UtilClient.is_unset(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not UtilClient.is_unset(request.master_count):
            body['master_count'] = request.master_count
        if not UtilClient.is_unset(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not UtilClient.is_unset(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not UtilClient.is_unset(request.master_period):
            body['master_period'] = request.master_period
        if not UtilClient.is_unset(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not UtilClient.is_unset(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not UtilClient.is_unset(request.master_system_disk_performance_level):
            body['master_system_disk_performance_level'] = request.master_system_disk_performance_level
        if not UtilClient.is_unset(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not UtilClient.is_unset(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not UtilClient.is_unset(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not UtilClient.is_unset(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not UtilClient.is_unset(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not UtilClient.is_unset(request.nodepools):
            body['nodepools'] = request.nodepools
        if not UtilClient.is_unset(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not UtilClient.is_unset(request.os_type):
            body['os_type'] = request.os_type
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not UtilClient.is_unset(request.profile):
            body['profile'] = request.profile
        if not UtilClient.is_unset(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not UtilClient.is_unset(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not UtilClient.is_unset(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not UtilClient.is_unset(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not UtilClient.is_unset(request.soc_enabled):
            body['soc_enabled'] = request.soc_enabled
        if not UtilClient.is_unset(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.user_ca):
            body['user_ca'] = request.user_ca
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_performance_level):
            body['worker_system_disk_performance_level'] = request.worker_system_disk_performance_level
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not UtilClient.is_unset(request.zone_id):
            body['zone_id'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        """
        This topic describes all parameters for creating an ACK cluster. You can create the following types of ACK clusters.
        *   [Create an ACK managed cluster](~~90776~~)
        *   [Create an ACK dedicated cluster](~~197620~~)
        *   [Create an ACK Serverless cluster](~~144246~~)
        *   [Create an ACK Edge cluster](~~128204~~)
        *   [Create an ACK Basic cluster that supports sandboxed containers](~~196321~~)
        *   [Create an ACK Pro cluster that supports sandboxed containers](~~140623~~)
        

        @param request: CreateClusterRequest

        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    def create_cluster_node_pool_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not UtilClient.is_unset(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.max_nodes):
            body['max_nodes'] = request.max_nodes
        if not UtilClient.is_unset(request.node_config):
            body['node_config'] = request.node_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster_node_pool(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_node_pool_with_options(cluster_id, request, headers, runtime)

    def create_edge_machine_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hostname):
            body['hostname'] = request.hostname
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/edge_machines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateEdgeMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_machine(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_edge_machine_with_options(request, headers, runtime)

    def create_kubernetes_trigger_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_kubernetes_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_kubernetes_trigger_with_options(request, headers, runtime)

    def create_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    def create_trigger_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/triggers' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_trigger(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(cluster_id, request, headers, runtime)

    def delete_alert_contact_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/alert/contacts',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_with_options(headers, runtime)

    def delete_alert_contact_group_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/alert/contact_groups',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact_group(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_group_with_options(headers, runtime)

    def delete_cluster_with_options(self, cluster_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not UtilClient.is_unset(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(cluster_id, request, headers, runtime)

    def delete_cluster_nodepool_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodepool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodepoolResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster_nodepool(self, cluster_id, nodepool_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def delete_cluster_nodes_with_options(self, cluster_id, request, headers, runtime):
        """
        >
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        

        @param request: DeleteClusterNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteClusterNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster_nodes(self, cluster_id, request):
        """
        >
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        

        @param request: DeleteClusterNodesRequest

        @return: DeleteClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    def delete_edge_machine_with_options(self, edge_machineid, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/edge_machines/%5Bedge_machineid%5D',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteEdgeMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_edge_machine(self, edge_machineid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_edge_machine_with_options(edge_machineid, request, headers, runtime)

    def delete_kubernetes_trigger_with_options(self, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/triggers/revoke/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_kubernetes_trigger(self, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_kubernetes_trigger_with_options(id, headers, runtime)

    def delete_policy_instance_with_options(self, cluster_id, policy_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/policies/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeletePolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_policy_instance(self, cluster_id, policy_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    def delete_template_with_options(self, template_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/templates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(template_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, template_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_id, headers, runtime)

    def delete_trigger_with_options(self, cluster_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/triggers/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_trigger(self, cluster_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(cluster_id, id, headers, runtime)

    def deploy_policy_instance_with_options(self, cluster_id, policy_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.namespaces):
            body['namespaces'] = request.namespaces
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployPolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/policies/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeployPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_policy_instance(self, cluster_id, policy_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    def descirbe_workflow_with_options(self, workflow_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescirbeWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/gs/workflow/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescirbeWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def descirbe_workflow(self, workflow_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.descirbe_workflow_with_options(workflow_name, headers, runtime)

    def describe_addon_with_options(self, addon_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddon',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/addons/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(addon_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_addon(self, addon_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_addon_with_options(addon_name, request, headers, runtime)

    def describe_addons_with_options(self, request, headers, runtime):
        """
        @deprecated
        

        @param request: DescribeAddonsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAddonsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_profile):
            query['cluster_profile'] = request.cluster_profile
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/components/metadata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_addons(self, request):
        """
        @deprecated
        

        @param request: DescribeAddonsRequest

        @return: DescribeAddonsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_addons_with_options(request, headers, runtime)

    def describe_cluster_addon_instance_with_options(self, cluster_id, addon_name, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterAddonInstanceResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/instance' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(addon_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_addon_instance(self, cluster_id, addon_name):
        """
        @deprecated
        

        @return: DescribeClusterAddonInstanceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_instance_with_options(cluster_id, addon_name, headers, runtime)

    def describe_cluster_addon_metadata_with_options(self, cluster_id, component_id, version, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonMetadata',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/metadata' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(component_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_addon_metadata(self, cluster_id, component_id, version):
        """
        @deprecated
        

        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_metadata_with_options(cluster_id, component_id, version, headers, runtime)

    def describe_cluster_addon_upgrade_status_with_options(self, cluster_id, component_id, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterAddonUpgradeStatusResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/upgradestatus' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(component_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_addon_upgrade_status(self, cluster_id, component_id):
        """
        @deprecated
        

        @return: DescribeClusterAddonUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_upgrade_status_with_options(cluster_id, component_id, headers, runtime)

    def describe_cluster_addons_upgrade_status_with_options(self, cluster_id, tmp_req, headers, runtime):
        """
        @deprecated
        

        @param tmp_req: DescribeClusterAddonsUpgradeStatusRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterAddonsUpgradeStatusResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DescribeClusterAddonsUpgradeStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_ids):
            request.component_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_ids, 'componentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_ids_shrink):
            query['componentIds'] = request.component_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonsUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/upgradestatus' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_addons_upgrade_status(self, cluster_id, request):
        """
        @deprecated
        

        @param request: DescribeClusterAddonsUpgradeStatusRequest

        @return: DescribeClusterAddonsUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_upgrade_status_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_addons_version_with_options(self, cluster_id, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterAddonsVersionResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonsVersion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/version' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_addons_version(self, cluster_id):
        """
        @deprecated
        

        @return: DescribeClusterAddonsVersionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_version_with_options(cluster_id, headers, runtime)

    def describe_cluster_attach_scripts_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterAttachScripts',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/attachscript' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAttachScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_attach_scripts(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_attach_scripts_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_detail_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_detail(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_detail_with_options(cluster_id, headers, runtime)

    def describe_cluster_events_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterEvents',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/events' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_events(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_events_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_logs_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterLogs',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/logs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_logs(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_logs_with_options(cluster_id, headers, runtime)

    def describe_cluster_node_pool_detail_with_options(self, cluster_id, nodepool_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterNodePoolDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_node_pool_detail(self, cluster_id, nodepool_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pool_detail_with_options(cluster_id, nodepool_id, headers, runtime)

    def describe_cluster_node_pools_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterNodePools',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_node_pools(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pools_with_options(cluster_id, headers, runtime)

    def describe_cluster_nodes_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.nodepool_id):
            query['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_nodes(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_resources_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/resources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_resources(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_resources_with_options(cluster_id, headers, runtime)

    def describe_cluster_tasks_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterTasks',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/tasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_tasks(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_tasks_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_user_kubeconfig_with_options(self, cluster_id, request, headers, runtime):
        """
        *\
        ****The default validity period of a kubeconfig file is 3 years. Two months before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the secret is valid for 3 years. The previous kubeconfig secret remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        

        @param request: DescribeClusterUserKubeconfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterUserKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterUserKubeconfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/k8s/%s/user_config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterUserKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_user_kubeconfig(self, cluster_id, request):
        """
        *\
        ****The default validity period of a kubeconfig file is 3 years. Two months before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the secret is valid for 3 years. The previous kubeconfig secret remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        

        @param request: DescribeClusterUserKubeconfigRequest

        @return: DescribeClusterUserKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_v2user_kubeconfig_with_options(self, cluster_id, request, headers, runtime):
        """
        @deprecated
        

        @param request: DescribeClusterV2UserKubeconfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClusterV2UserKubeconfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2UserKubeconfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/k8s/%s/user_config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_v2user_kubeconfig(self, cluster_id, request):
        """
        @deprecated
        

        @param request: DescribeClusterV2UserKubeconfigRequest

        @return: DescribeClusterV2UserKubeconfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_v2user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    def describe_cluster_vuls_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/vuls' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterVulsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_vuls(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_vuls_with_options(cluster_id, headers, runtime)

    def describe_clusters_with_options(self, request, headers, runtime):
        """
        @deprecated
        

        @param request: DescribeClustersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeClustersResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusters',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_clusters(self, request):
        """
        @deprecated
        

        @param request: DescribeClustersRequest

        @return: DescribeClustersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_with_options(request, headers, runtime)

    def describe_clusters_v1with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersV1',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v1/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersV1Response(),
            self.call_api(params, req, runtime)
        )

    def describe_clusters_v1(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_v1with_options(request, headers, runtime)

    def describe_edge_machine_active_process_with_options(self, edge_machineid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineActiveProcess',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/edge_machines/%5Bedge_machineid%5D/activeprocess',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_edge_machine_active_process(self, edge_machineid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_active_process_with_options(edge_machineid, headers, runtime)

    def describe_edge_machine_models_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineModels',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/edge_machines/models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_edge_machine_models(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_models_with_options(headers, runtime)

    def describe_edge_machine_tunnel_config_detail_with_options(self, edge_machineid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineTunnelConfigDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/edge_machines/%5Bedge_machineid%5D/tunnelconfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_edge_machine_tunnel_config_detail(self, edge_machineid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_tunnel_config_detail_with_options(edge_machineid, headers, runtime)

    def describe_edge_machines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hostname):
            query['hostname'] = request.hostname
        if not UtilClient.is_unset(request.life_state):
            query['life_state'] = request.life_state
        if not UtilClient.is_unset(request.model):
            query['model'] = request.model
        if not UtilClient.is_unset(request.online_state):
            query['online_state'] = request.online_state
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachines',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/edge_machines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_edge_machines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machines_with_options(request, headers, runtime)

    def describe_events_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_events_with_options(request, headers, runtime)

    def describe_external_agent_with_options(self, cluster_id, request, headers, runtime):
        """
        For more information, see [Register an external Kubernetes cluster](~~121053~~).
        

        @param request: DescribeExternalAgentRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExternalAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_mode):
            query['AgentMode'] = request.agent_mode
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExternalAgent',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/k8s/%s/external/agent/deployment' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_external_agent(self, cluster_id, request):
        """
        For more information, see [Register an external Kubernetes cluster](~~121053~~).
        

        @param request: DescribeExternalAgentRequest

        @return: DescribeExternalAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_external_agent_with_options(cluster_id, request, headers, runtime)

    def describe_kubernetes_version_metadata_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.runtime):
            query['runtime'] = request.runtime
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKubernetesVersionMetadata',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v1/metadata/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_kubernetes_version_metadata(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_kubernetes_version_metadata_with_options(request, headers, runtime)

    def describe_node_pool_vuls_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.necessity):
            query['necessity'] = request.necessity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodePoolVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/vuls' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeNodePoolVulsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_pool_vuls(self, cluster_id, nodepool_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def describe_policies_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicies',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policies(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policies_with_options(headers, runtime)

    def describe_policy_details_with_options(self, policy_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyDetails',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/policies/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policy_details(self, policy_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_details_with_options(policy_name, headers, runtime)

    def describe_policy_governance_in_cluster_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyGovernanceInCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/policygovernance' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policy_governance_in_cluster(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_governance_in_cluster_with_options(cluster_id, headers, runtime)

    def describe_policy_instances_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.policy_name):
            query['policy_name'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/policies' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policy_instances(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_with_options(cluster_id, request, headers, runtime)

    def describe_policy_instances_status_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyInstancesStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/policies/status' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_policy_instances_status(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_status_with_options(cluster_id, headers, runtime)

    def describe_subaccount_k8s_cluster_user_config_with_options(self, cluster_id, uid, request, headers, runtime):
        """
        *\
        ****Only Alibaba Cloud accounts can call this API operation.
        

        @param request: DescribeSubaccountK8sClusterUserConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSubaccountK8sClusterUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubaccountK8sClusterUserConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/k8s/%s/users/%s/user_config' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(uid))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subaccount_k8s_cluster_user_config(self, cluster_id, uid, request):
        """
        *\
        ****Only Alibaba Cloud accounts can call this API operation.
        

        @param request: DescribeSubaccountK8sClusterUserConfigRequest

        @return: DescribeSubaccountK8sClusterUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_subaccount_k8s_cluster_user_config_with_options(cluster_id, uid, request, headers, runtime)

    def describe_task_info_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTaskInfo',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task_info(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_info_with_options(task_id, headers, runtime)

    def describe_template_attribute_with_options(self, template_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateAttribute',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/templates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(template_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_attribute(self, template_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_template_attribute_with_options(template_id, request, headers, runtime)

    def describe_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['page_num'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(request, headers, runtime)

    def describe_trigger_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/triggers' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trigger(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_trigger_with_options(cluster_id, request, headers, runtime)

    def describe_user_cluster_namespaces_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserClusterNamespaces',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/k8s/%s/namespaces' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_cluster_namespaces(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_cluster_namespaces_with_options(cluster_id, headers, runtime)

    def describe_user_permission_with_options(self, uid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserPermission',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/permissions/users/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(uid)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_permission(self, uid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_permission_with_options(uid, headers, runtime)

    def describe_user_quota_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserQuota',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_quota(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_quota_with_options(headers, runtime)

    def describe_workflows_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeWorkflows',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/gs/workflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_workflows(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflows_with_options(headers, runtime)

    def edge_cluster_add_edge_machine_with_options(self, clusterid, edge_machineid, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expired):
            body['expired'] = request.expired
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EdgeClusterAddEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%5Bclusterid%5D/attachedgemachine/%5Bedge_machineid%5D',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def edge_cluster_add_edge_machine(self, clusterid, edge_machineid, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edge_cluster_add_edge_machine_with_options(clusterid, edge_machineid, request, headers, runtime)

    def fix_node_pool_vuls_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        """
        1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
        2.  ACK may need to restart nodes to patch certain vulnerabilities. ACK drains a node before the node restarts. Make sure that the ACK cluster has sufficient idle nodes to host the pods evicted from the trained nodes. For example, you can scale out a node pool before you patch vulnerabilities for the nodes in the node pool.
        3.  Security Center ensures the compatibility of CVE patches. We recommend that you check the compatibility of a CVE patch with your application before you install the patch. You can pause or cancel a CVE patching task anytime.
        4.  CVE patching is a progressive task that consists of multiple batches. After you pause or cancel a CVE patching task, ACK continues to process the dispatched batches. Only the batches that have not been dispatched are paused or canceled.
        

        @param request: FixNodePoolVulsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: FixNodePoolVulsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.rollout_policy):
            body['rollout_policy'] = request.rollout_policy
        if not UtilClient.is_unset(request.vuls):
            body['vuls'] = request.vuls
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FixNodePoolVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/vuls/fix' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.FixNodePoolVulsResponse(),
            self.call_api(params, req, runtime)
        )

    def fix_node_pool_vuls(self, cluster_id, nodepool_id, request):
        """
        1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
        2.  ACK may need to restart nodes to patch certain vulnerabilities. ACK drains a node before the node restarts. Make sure that the ACK cluster has sufficient idle nodes to host the pods evicted from the trained nodes. For example, you can scale out a node pool before you patch vulnerabilities for the nodes in the node pool.
        3.  Security Center ensures the compatibility of CVE patches. We recommend that you check the compatibility of a CVE patch with your application before you install the patch. You can pause or cancel a CVE patching task anytime.
        4.  CVE patching is a progressive task that consists of multiple batches. After you pause or cancel a CVE patching task, ACK continues to process the dispatched batches. Only the batches that have not been dispatched are paused or canceled.
        

        @param request: FixNodePoolVulsRequest

        @return: FixNodePoolVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.fix_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def get_cluster_addon_instance_with_options(self, cluster_id, instance_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterAddonInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/addon_instances/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetClusterAddonInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_addon_instance(self, cluster_id, instance_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_addon_instance_with_options(cluster_id, instance_name, headers, runtime)

    def get_cluster_check_with_options(self, cluster_id, check_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterCheck',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/checks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(check_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetClusterCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_check(self, cluster_id, check_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_check_with_options(cluster_id, check_id, headers, runtime)

    def get_kubernetes_trigger_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/triggers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.GetKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_kubernetes_trigger(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_kubernetes_trigger_with_options(cluster_id, request, headers, runtime)

    def get_upgrade_status_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s/upgrade/status' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_upgrade_status(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upgrade_status_with_options(cluster_id, headers, runtime)

    def grant_permissions_with_options(self, uid, request, headers, runtime):
        """
        ***\
        *   Make sure that you have granted the RAM user at least read-only permissions on the desired ACK clusters in the RAM console. Otherwise, the `ErrorRamPolicyConfig` error code is returned. For more information about how to authorize a RAM user by attaching RAM policies, see [Create a custom RAM policy](~~86485~~).
        *   If you use a RAM user to call this API operation, make sure that the RAM user is authorized to modify the permissions of other RAM users on the desired ACK clusters. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](~~119035~~).
        *   This operation overwrites the permissions that have been granted to the specified RAM user. When you call this operation, make sure that the required permissions are included.
        

        @param request: GrantPermissionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='GrantPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/permissions/users/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(uid)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.GrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_permissions(self, uid, request):
        """
        ***\
        *   Make sure that you have granted the RAM user at least read-only permissions on the desired ACK clusters in the RAM console. Otherwise, the `ErrorRamPolicyConfig` error code is returned. For more information about how to authorize a RAM user by attaching RAM policies, see [Create a custom RAM policy](~~86485~~).
        *   If you use a RAM user to call this API operation, make sure that the RAM user is authorized to modify the permissions of other RAM users on the desired ACK clusters. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](~~119035~~).
        *   This operation overwrites the permissions that have been granted to the specified RAM user. When you call this operation, make sure that the required permissions are included.
        

        @param request: GrantPermissionsRequest

        @return: GrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_permissions_with_options(uid, request, headers, runtime)

    def install_cluster_addons_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='InstallClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/install' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.InstallClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    def install_cluster_addons(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    def list_addons_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_addons(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_addons_with_options(request, headers, runtime)

    def list_cluster_addon_instances_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterAddonInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/addon_instances' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListClusterAddonInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_addon_instances(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_addon_instances_with_options(cluster_id, headers, runtime)

    def list_cluster_checks_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterChecks',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/checks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListClusterChecksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_checks(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_checks_with_options(cluster_id, request, headers, runtime)

    def list_operation_plans_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationPlans',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/operation/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListOperationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def list_operation_plans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_operation_plans_with_options(request, headers, runtime)

    def list_tag_resources_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['next_token'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def migrate_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.oss_bucket_endpoint):
            body['oss_bucket_endpoint'] = request.oss_bucket_endpoint
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['oss_bucket_name'] = request.oss_bucket_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MigrateCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/migrate' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.MigrateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_cluster_with_options(cluster_id, request, headers, runtime)

    def modify_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not UtilClient.is_unset(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not UtilClient.is_unset(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not UtilClient.is_unset(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not UtilClient.is_unset(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_with_options(cluster_id, request, headers, runtime)

    def modify_cluster_addon_with_options(self, cluster_id, component_id, request, headers, runtime):
        """
        You can use this API operation to modify the components in a Container Service for Kubernetes (ACK) cluster or the control plane components in an ACK Pro cluster.
        *   To query the customizable parameters of a component, call the `DescribeClusterAddonMetadata` API operation. For more information, see [Query the metadata of a specified component version](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/query).
        *   For more information about the customizable parameters of control plane components in ACK Pro clusters, see [Customize the parameters of control plane components in ACK Pro clusters](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/customize-control-plane-parameters-for-a-professional-kubernetes-cluster).
        After you call this operation, the component may be redeployed and restarted. We recommend that you assess the impact before you call this operation.
        

        @param request: ModifyClusterAddonRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyClusterAddonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterAddon',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/config' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(component_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterAddonResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_addon(self, cluster_id, component_id, request):
        """
        You can use this API operation to modify the components in a Container Service for Kubernetes (ACK) cluster or the control plane components in an ACK Pro cluster.
        *   To query the customizable parameters of a component, call the `DescribeClusterAddonMetadata` API operation. For more information, see [Query the metadata of a specified component version](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/query).
        *   For more information about the customizable parameters of control plane components in ACK Pro clusters, see [Customize the parameters of control plane components in ACK Pro clusters](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/customize-control-plane-parameters-for-a-professional-kubernetes-cluster).
        After you call this operation, the component may be redeployed and restarted. We recommend that you assess the impact before you call this operation.
        

        @param request: ModifyClusterAddonRequest

        @return: ModifyClusterAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_addon_with_options(cluster_id, component_id, request, headers, runtime)

    def modify_cluster_configuration_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.customize_config):
            body['customize_config'] = request.customize_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterConfiguration',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/configuration' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_configuration(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_configuration_with_options(cluster_id, request, headers, runtime)

    def modify_cluster_node_pool_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.concurrency):
            body['concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_node_pool(self, cluster_id, nodepool_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def modify_cluster_tags_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ModifyClusterTags',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/tags' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_tags(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_tags_with_options(cluster_id, request, headers, runtime)

    def modify_node_pool_node_config_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        """
        >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        

        @param request: ModifyNodePoolNodeConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyNodePoolNodeConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolNodeConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/node_config' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyNodePoolNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_node_pool_node_config(self, cluster_id, nodepool_id, request):
        """
        >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        

        @param request: ModifyNodePoolNodeConfigRequest

        @return: ModifyNodePoolNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_node_pool_node_config_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def modify_policy_instance_with_options(self, cluster_id, policy_name, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.instance_name):
            body['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.namespaces):
            body['namespaces'] = request.namespaces
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/policies/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_policy_instance(self, cluster_id, policy_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    def open_ack_service_with_options(self, request, headers, runtime):
        """
        You can activate ACK by using Alibaba Cloud accounts.
        *   To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        

        @param request: OpenAckServiceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenAckServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAckService',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.OpenAckServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_ack_service(self, request):
        """
        You can activate ACK by using Alibaba Cloud accounts.
        *   To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        

        @param request: OpenAckServiceRequest

        @return: OpenAckServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_ack_service_with_options(request, headers, runtime)

    def pause_cluster_upgrade_with_options(self, cluster_id, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PauseClusterUpgradeResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseClusterUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s/upgrade/pause' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseClusterUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_cluster_upgrade(self, cluster_id):
        """
        @deprecated
        

        @return: PauseClusterUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_cluster_upgrade_with_options(cluster_id, headers, runtime)

    def pause_component_upgrade_with_options(self, clusterid, componentid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/pause' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(clusterid)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(componentid))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_component_upgrade(self, clusterid, componentid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    def pause_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tasks/%s/pause' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_task_with_options(task_id, headers, runtime)

    def remove_cluster_nodes_with_options(self, cluster_id, request, headers, runtime):
        """
        @deprecated
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        *   Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        *   Nodes remain in the Unschedulable state when they are being removed.
        *   You can remove only worker nodes. You cannot remove master nodes.
        

        @param request: RemoveClusterNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveClusterNodesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s/nodes/remove' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_cluster_nodes(self, cluster_id, request):
        """
        @deprecated
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        *   Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        *   Nodes remain in the Unschedulable state when they are being removed.
        *   You can remove only worker nodes. You cannot remove master nodes.
        

        @param request: RemoveClusterNodesRequest

        @return: RemoveClusterNodesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    def remove_node_pool_nodes_with_options(self, cluster_id, nodepool_id, tmp_req, headers, runtime):
        """
        *\
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        

        @param tmp_req: RemoveNodePoolNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveNodePoolNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.RemoveNodePoolNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'instance_ids', 'json')
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'nodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.drain_node):
            query['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['instance_ids'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.nodes_shrink):
            query['nodes'] = request.nodes_shrink
        if not UtilClient.is_unset(request.release_node):
            query['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveNodePoolNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/nodes' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveNodePoolNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_node_pool_nodes(self, cluster_id, nodepool_id, request):
        """
        *\
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        

        @param request: RemoveNodePoolNodesRequest

        @return: RemoveNodePoolNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_node_pool_nodes_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def remove_workflow_with_options(self, workflow_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/gs/workflow/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_workflow(self, workflow_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_workflow_with_options(workflow_name, headers, runtime)

    def repair_cluster_node_pool_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RepairClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/repair' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RepairClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    def repair_cluster_node_pool(self, cluster_id, nodepool_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.repair_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def resume_component_upgrade_with_options(self, clusterid, componentid, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/%s/resume' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(clusterid)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(componentid))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_component_upgrade(self, clusterid, componentid):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    def resume_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tasks/%s/resume' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(task_id, headers, runtime)

    def resume_upgrade_cluster_with_options(self, cluster_id, headers, runtime):
        """
        @deprecated
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeUpgradeCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s/upgrade/resume' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeUpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_upgrade_cluster(self, cluster_id):
        """
        @deprecated
        

        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_upgrade_cluster_with_options(cluster_id, headers, runtime)

    def run_cluster_check_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunClusterCheck',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/checks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RunClusterCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def run_cluster_check(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_cluster_check_with_options(cluster_id, request, headers, runtime)

    def scale_cluster_with_options(self, cluster_id, request, headers, runtime):
        """
        @deprecated
        

        @param request: ScaleClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ScaleClusterResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disk):
            body['worker_data_disk'] = request.worker_data_disk
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_cluster(self, cluster_id, request):
        """
        @deprecated
        

        @param request: ScaleClusterRequest

        @return: ScaleClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_cluster_with_options(cluster_id, request, headers, runtime)

    def scale_cluster_node_pool_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_cluster_node_pool(self, cluster_id, nodepool_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    def scale_out_cluster_with_options(self, cluster_id, request, headers, runtime):
        """
        *\
        ****The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](~~184928~~).
        

        @param request: ScaleOutClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ScaleOutClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleOutCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleOutClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_out_cluster(self, cluster_id, request):
        """
        *\
        ****The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](~~184928~~).
        

        @param request: ScaleOutClusterRequest

        @return: ScaleOutClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_out_cluster_with_options(cluster_id, request, headers, runtime)

    def scan_cluster_vuls_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ScanClusterVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/vuls/scan' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScanClusterVulsResponse(),
            self.call_api(params, req, runtime)
        )

    def scan_cluster_vuls(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_cluster_vuls_with_options(cluster_id, headers, runtime)

    def start_alert_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/alert/%s/alert_rule/start' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def start_alert(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_alert_with_options(cluster_id, headers, runtime)

    def start_workflow_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mapping_bam_out_filename):
            body['mapping_bam_out_filename'] = request.mapping_bam_out_filename
        if not UtilClient.is_unset(request.mapping_bam_out_path):
            body['mapping_bam_out_path'] = request.mapping_bam_out_path
        if not UtilClient.is_unset(request.mapping_bucket_name):
            body['mapping_bucket_name'] = request.mapping_bucket_name
        if not UtilClient.is_unset(request.mapping_fastq_first_filename):
            body['mapping_fastq_first_filename'] = request.mapping_fastq_first_filename
        if not UtilClient.is_unset(request.mapping_fastq_path):
            body['mapping_fastq_path'] = request.mapping_fastq_path
        if not UtilClient.is_unset(request.mapping_fastq_second_filename):
            body['mapping_fastq_second_filename'] = request.mapping_fastq_second_filename
        if not UtilClient.is_unset(request.mapping_is_mark_dup):
            body['mapping_is_mark_dup'] = request.mapping_is_mark_dup
        if not UtilClient.is_unset(request.mapping_oss_region):
            body['mapping_oss_region'] = request.mapping_oss_region
        if not UtilClient.is_unset(request.mapping_reference_path):
            body['mapping_reference_path'] = request.mapping_reference_path
        if not UtilClient.is_unset(request.service):
            body['service'] = request.service
        if not UtilClient.is_unset(request.wgs_bucket_name):
            body['wgs_bucket_name'] = request.wgs_bucket_name
        if not UtilClient.is_unset(request.wgs_fastq_first_filename):
            body['wgs_fastq_first_filename'] = request.wgs_fastq_first_filename
        if not UtilClient.is_unset(request.wgs_fastq_path):
            body['wgs_fastq_path'] = request.wgs_fastq_path
        if not UtilClient.is_unset(request.wgs_fastq_second_filename):
            body['wgs_fastq_second_filename'] = request.wgs_fastq_second_filename
        if not UtilClient.is_unset(request.wgs_oss_region):
            body['wgs_oss_region'] = request.wgs_oss_region
        if not UtilClient.is_unset(request.wgs_reference_path):
            body['wgs_reference_path'] = request.wgs_reference_path
        if not UtilClient.is_unset(request.wgs_vcf_out_filename):
            body['wgs_vcf_out_filename'] = request.wgs_vcf_out_filename
        if not UtilClient.is_unset(request.wgs_vcf_out_path):
            body['wgs_vcf_out_path'] = request.wgs_vcf_out_path
        if not UtilClient.is_unset(request.workflow_type):
            body['workflow_type'] = request.workflow_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/gs/workflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StartWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def start_workflow(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_workflow_with_options(request, headers, runtime)

    def stop_alert_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/alert/%s/alert_rule/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_alert(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_alert_with_options(cluster_id, headers, runtime)

    def sync_cluster_node_pool_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SyncClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/sync_nodepools' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.SyncClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_cluster_node_pool(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_cluster_node_pool_with_options(cluster_id, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tags',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def un_install_cluster_addons_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.addons)
        )
        params = open_api_models.Params(
            action='UnInstallClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/uninstall' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UnInstallClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    def un_install_cluster_addons(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    def untag_resources_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'tag_keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['tag_keys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def update_contact_group_for_alert_with_options(self, cluster_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateContactGroupForAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/alert/%s/alert_rule/contact_groups' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateContactGroupForAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def update_contact_group_for_alert(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_contact_group_for_alert_with_options(cluster_id, headers, runtime)

    def update_control_plane_log_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliuid):
            body['aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.log_project):
            body['log_project'] = request.log_project
        if not UtilClient.is_unset(request.log_ttl):
            body['log_ttl'] = request.log_ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLog',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/controlplanelog' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateControlPlaneLogResponse(),
            self.call_api(params, req, runtime)
        )

    def update_control_plane_log(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_control_plane_log_with_options(cluster_id, request, headers, runtime)

    def update_k8s_cluster_user_config_expire_with_options(self, cluster_id, request, headers, runtime):
        """
        *\
        ****\
        *   You can call this operation only with an Alibaba Cloud account. - If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        

        @param request: UpdateK8sClusterUserConfigExpireRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_hour):
            body['expire_hour'] = request.expire_hour
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sClusterUserConfigExpire',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/k8s/%s/user_config/expire' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
            self.call_api(params, req, runtime)
        )

    def update_k8s_cluster_user_config_expire(self, cluster_id, request):
        """
        *\
        ****\
        *   You can call this operation only with an Alibaba Cloud account. - If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        

        @param request: UpdateK8sClusterUserConfigExpireRequest

        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_cluster_user_config_expire_with_options(cluster_id, request, headers, runtime)

    def update_template_with_options(self, template_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/templates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(template_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template(self, template_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_id, request, headers, runtime)

    def upgrade_cluster_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['component_name'] = request.component_name
        if not UtilClient.is_unset(request.master_only):
            body['master_only'] = request.master_only
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/api/v2/clusters/%s/upgrade' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_cluster(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_with_options(cluster_id, request, headers, runtime)

    def upgrade_cluster_addons_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpgradeClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/components/upgrade' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_cluster_addons(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_addons_with_options(cluster_id, request, headers, runtime)

    def upgrade_cluster_nodepool_with_options(self, cluster_id, nodepool_id, request, headers, runtime):
        """
        This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        

        @param request: UpgradeClusterNodepoolRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeClusterNodepoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.runtime_type):
            body['runtime_type'] = request.runtime_type
        if not UtilClient.is_unset(request.runtime_version):
            body['runtime_version'] = request.runtime_version
        if not UtilClient.is_unset(request.use_replace):
            body['use_replace'] = request.use_replace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeClusterNodepool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname='/clusters/%s/nodepools/%s/upgrade' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(nodepool_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterNodepoolResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_cluster_nodepool(self, cluster_id, nodepool_id, request):
        """
        This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        

        @param request: UpgradeClusterNodepoolRequest

        @return: UpgradeClusterNodepoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)
