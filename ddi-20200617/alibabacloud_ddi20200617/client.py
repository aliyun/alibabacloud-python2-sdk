# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddi20200617 import models as ddi_20200617_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-qingdao': 'ddi.cn-qingdao.aliyuncs.com',
            'cn-chengdu': 'ddi.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'ddi.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'ddi.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'ddi.cn-hongkong.aliyuncs.com',
            'ap-southeast-2': 'ddi.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'ddi.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'ddi.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'ddi.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'ddi.eu-west-1.aliyuncs.com',
            'us-east-1': 'ddi.us-east-1.aliyuncs.com',
            'eu-central-1': 'ddi.eu-central-1.aliyuncs.com',
            'me-east-1': 'ddi.me-east-1.aliyuncs.com',
            'ap-south-1': 'ddi.ap-south-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowResponse(),
            self.do_rpcrequest('CreateFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def modify_flow_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectResponse(),
            self.do_rpcrequest('ModifyFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_project_with_options(request, runtime)

    def query_knox_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.QueryKnoxUserPasswordResponse(),
            self.do_rpcrequest('QueryKnoxUserPassword', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_knox_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_knox_user_password_with_options(request, runtime)

    def describe_flow_node_instance_launcher_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            self.do_rpcrequest('DescribeFlowNodeInstanceLauncherLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance_launcher_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_launcher_log_with_options(request, runtime)

    def list_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowResponse(),
            self.do_rpcrequest('ListFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def list_flow_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterHostResponse(),
            self.do_rpcrequest('ListFlowClusterHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_host_with_options(request, runtime)

    def list_cluster_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationResponse(),
            self.do_rpcrequest('ListClusterOperation', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_with_options(request, runtime)

    def list_flow_entity_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowEntitySnapshotResponse(),
            self.do_rpcrequest('ListFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_entity_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_entity_snapshot_with_options(request, runtime)

    def delete_cluster_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteClusterTemplateResponse(),
            self.do_rpcrequest('DeleteClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_template_with_options(request, runtime)

    def cancel_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CancelOrderResponse(),
            self.do_rpcrequest('CancelOrder', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    def clone_flow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowJobResponse(),
            self.do_rpcrequest('CloneFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_job_with_options(request, runtime)

    def start_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.StartFlowResponse(),
            self.do_rpcrequest('StartFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_flow_with_options(request, runtime)

    def create_flow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowJobResponse(),
            self.do_rpcrequest('CreateFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_job_with_options(request, runtime)

    def delete_flow_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowCategoryResponse(),
            self.do_rpcrequest('DeleteFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_category_with_options(request, runtime)

    def delete_flow_edit_lock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowEditLockResponse(),
            self.do_rpcrequest('DeleteFlowEditLock', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_edit_lock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_edit_lock_with_options(request, runtime)

    def resize_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResizeClusterResponse(),
            self.do_rpcrequest('ResizeCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resize_cluster_with_options(request, runtime)

    def describe_meta_table_preview_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeMetaTablePreviewTaskResponse(),
            self.do_rpcrequest('DescribeMetaTablePreviewTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meta_table_preview_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_table_preview_task_with_options(request, runtime)

    def list_cluster_service_config_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterServiceConfigHistoryResponse(),
            self.do_rpcrequest('ListClusterServiceConfigHistory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service_config_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_config_history_with_options(request, runtime)

    def modify_scaling_config_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyScalingConfigItemResponse(),
            self.do_rpcrequest('ModifyScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_config_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_config_item_with_options(request, runtime)

    def list_flow_cluster_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllResponse(),
            self.do_rpcrequest('ListFlowClusterAll', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_all_with_options(request, runtime)

    def describe_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingGroupResponse(),
            self.do_rpcrequest('DescribeScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_with_options(request, runtime)

    def list_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingGroupResponse(),
            self.do_rpcrequest('ListScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_group_with_options(request, runtime)

    def modify_flow_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowCategoryResponse(),
            self.do_rpcrequest('ModifyFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_category_with_options(request, runtime)

    def modify_cluster_service_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterServiceConfigResponse(),
            self.do_rpcrequest('ModifyClusterServiceConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_service_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_service_config_with_options(request, runtime)

    def clone_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowResponse(),
            self.do_rpcrequest('CloneFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    def create_cluster_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterTemplateResponse(),
            self.do_rpcrequest('CreateClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_template_with_options(request, runtime)

    def update_library_install_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse(),
            self.do_rpcrequest('UpdateLibraryInstallTaskStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_library_install_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_library_install_task_status_with_options(request, runtime)

    def list_scaling_config_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingConfigItemResponse(),
            self.do_rpcrequest('ListScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_config_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_config_item_with_options(request, runtime)

    def list_flow_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowInstanceResponse(),
            self.do_rpcrequest('ListFlowInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_instance_with_options(request, runtime)

    def describe_scaling_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingMetricsResponse(),
            self.do_rpcrequest('DescribeScalingMetrics', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_metrics_with_options(request, runtime)

    def untag_resources_system_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UntagResourcesSystemTagsResponse(),
            self.do_rpcrequest('UntagResourcesSystemTags', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources_system_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_system_tags_with_options(request, runtime)

    def describe_flow_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectResponse(),
            self.do_rpcrequest('DescribeFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_project_with_options(request, runtime)

    def delete_security_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteSecurityWhiteListResponse(),
            self.do_rpcrequest('DeleteSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_security_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_white_list_with_options(request, runtime)

    def list_scaling_activity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingActivityResponse(),
            self.do_rpcrequest('ListScalingActivity', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_activity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_activity_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2020-06-17', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def list_cluster_installed_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterInstalledServiceResponse(),
            self.do_rpcrequest('ListClusterInstalledService', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_installed_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_installed_service_with_options(request, runtime)

    def run_cluster_service_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RunClusterServiceActionResponse(),
            self.do_rpcrequest('RunClusterServiceAction', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cluster_service_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_cluster_service_action_with_options(request, runtime)

    def suspend_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SuspendFlowResponse(),
            self.do_rpcrequest('SuspendFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_flow_with_options(request, runtime)

    def create_flow_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectResponse(),
            self.do_rpcrequest('CreateFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_with_options(request, runtime)

    def list_flow_node_instance_container_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse(),
            self.do_rpcrequest('ListFlowNodeInstanceContainerStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_instance_container_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_instance_container_status_with_options(request, runtime)

    def modify_cluster_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterTemplateResponse(),
            self.do_rpcrequest('ModifyClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_template_with_options(request, runtime)

    def add_security_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.AddSecurityWhiteListResponse(),
            self.do_rpcrequest('AddSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_security_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_security_white_list_with_options(request, runtime)

    def list_meta_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListMetaClusterResponse(),
            self.do_rpcrequest('ListMetaCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_meta_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_meta_cluster_with_options(request, runtime)

    def list_cluster_operation_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationHostResponse(),
            self.do_rpcrequest('ListClusterOperationHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_host_with_options(request, runtime)

    def list_cluster_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterTemplatesResponse(),
            self.do_rpcrequest('ListClusterTemplates', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_templates_with_options(request, runtime)

    def list_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def tag_resources_system_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.TagResourcesSystemTagsResponse(),
            self.do_rpcrequest('TagResourcesSystemTags', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources_system_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_system_tags_with_options(request, runtime)

    def modify_flow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowJobResponse(),
            self.do_rpcrequest('ModifyFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_job_with_options(request, runtime)

    def delete_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowResponse(),
            self.do_rpcrequest('DeleteFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    def create_flow_edit_lock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowEditLockResponse(),
            self.do_rpcrequest('CreateFlowEditLock', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_edit_lock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_edit_lock_with_options(request, runtime)

    def describe_flow_node_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceResponse(),
            self.do_rpcrequest('DescribeFlowNodeInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_with_options(request, runtime)

    def detach_and_release_cluster_eni_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DetachAndReleaseClusterEniResponse(),
            self.do_rpcrequest('DetachAndReleaseClusterEni', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_and_release_cluster_eni(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_and_release_cluster_eni_with_options(request, runtime)

    def describe_scaling_group_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingGroupInstanceResponse(),
            self.do_rpcrequest('DescribeScalingGroupInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_group_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_instance_with_options(request, runtime)

    def create_cluster_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterHostGroupResponse(),
            self.do_rpcrequest('CreateClusterHostGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_host_group_with_options(request, runtime)

    def describe_cluster_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterTemplateResponse(),
            self.do_rpcrequest('DescribeClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_template_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def commit_flow_entity_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CommitFlowEntitySnapshotResponse(),
            self.do_rpcrequest('CommitFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commit_flow_entity_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.commit_flow_entity_snapshot_with_options(request, runtime)

    def submit_flow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowJobResponse(),
            self.do_rpcrequest('SubmitFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_flow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_flow_job_with_options(request, runtime)

    def list_flow_job_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobHistoryResponse(),
            self.do_rpcrequest('ListFlowJobHistory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_job_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_job_history_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2020-06-17', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_cluster_host_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterHostComponentResponse(),
            self.do_rpcrequest('ListClusterHostComponent', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_component_with_options(request, runtime)

    def modify_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyScalingGroupResponse(),
            self.do_rpcrequest('ModifyScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    def describe_flow_project_cluster_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('DescribeFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_project_cluster_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_project_cluster_setting_with_options(request, runtime)

    def list_flow_project_cluster_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('ListFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project_cluster_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_cluster_setting_with_options(request, runtime)

    def submit_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowResponse(),
            self.do_rpcrequest('SubmitFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_flow_with_options(request, runtime)

    def describe_scaling_common_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingCommonConfigResponse(),
            self.do_rpcrequest('DescribeScalingCommonConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_common_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_common_config_with_options(request, runtime)

    def resume_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResumeFlowResponse(),
            self.do_rpcrequest('ResumeFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_flow_with_options(request, runtime)

    def restore_flow_entity_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RestoreFlowEntitySnapshotResponse(),
            self.do_rpcrequest('RestoreFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_flow_entity_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_flow_entity_snapshot_with_options(request, runtime)

    def create_library_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateLibraryResponse(),
            self.do_rpcrequest('CreateLibrary', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_library(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_library_with_options(request, runtime)

    def list_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListVswitchResponse(),
            self.do_rpcrequest('ListVswitch', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vswitch_with_options(request, runtime)

    def delete_flow_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectResponse(),
            self.do_rpcrequest('DeleteFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_with_options(request, runtime)

    def release_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ReleaseClusterResponse(),
            self.do_rpcrequest('ReleaseCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_with_options(request, runtime)

    def add_scaling_config_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.AddScalingConfigItemResponse(),
            self.do_rpcrequest('AddScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_scaling_config_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_scaling_config_item_with_options(request, runtime)

    def reset_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResetUserPasswordResponse(),
            self.do_rpcrequest('ResetUserPassword', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    def list_flow_cluster_all_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllHostsResponse(),
            self.do_rpcrequest('ListFlowClusterAllHosts', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_all_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_all_hosts_with_options(request, runtime)

    def delete_libraries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteLibrariesResponse(),
            self.do_rpcrequest('DeleteLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_libraries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_libraries_with_options(request, runtime)

    def describe_flow_category_tree_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowCategoryTreeResponse(),
            self.do_rpcrequest('DescribeFlowCategoryTree', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_category_tree(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_category_tree_with_options(request, runtime)

    def list_datasource_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListDatasourceInstancesResponse(),
            self.do_rpcrequest('ListDatasourceInstances', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_datasource_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_datasource_instances_with_options(request, runtime)

    def list_flow_node_sql_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeSqlResultResponse(),
            self.do_rpcrequest('ListFlowNodeSqlResult', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_sql_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_sql_result_with_options(request, runtime)

    def describe_flow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowJobResponse(),
            self.do_rpcrequest('DescribeFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_job_with_options(request, runtime)

    def describe_library_install_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse(),
            self.do_rpcrequest('DescribeLibraryInstallTaskDetail', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_library_install_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_library_install_task_detail_with_options(request, runtime)

    def modify_flow_for_web_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowForWebResponse(),
            self.do_rpcrequest('ModifyFlowForWeb', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_for_web(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_for_web_with_options(request, runtime)

    def remove_scaling_config_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RemoveScalingConfigItemResponse(),
            self.do_rpcrequest('RemoveScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_scaling_config_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_scaling_config_item_with_options(request, runtime)

    def describe_security_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeSecurityWhiteListResponse(),
            self.do_rpcrequest('DescribeSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_white_list_with_options(request, runtime)

    def describe_flow_node_instance_container_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse(),
            self.do_rpcrequest('DescribeFlowNodeInstanceContainerLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance_container_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_container_log_with_options(request, runtime)

    def rerun_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RerunFlowResponse(),
            self.do_rpcrequest('RerunFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rerun_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rerun_flow_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def describe_cluster_operation_host_task_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse(),
            self.do_rpcrequest('DescribeClusterOperationHostTaskLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_operation_host_task_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_operation_host_task_log_with_options(request, runtime)

    def kill_flow_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowJobResponse(),
            self.do_rpcrequest('KillFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_flow_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kill_flow_job_with_options(request, runtime)

    def uninstall_libraries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UninstallLibrariesResponse(),
            self.do_rpcrequest('UninstallLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def uninstall_libraries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_libraries_with_options(request, runtime)

    def describe_cluster_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterV2Response(),
            self.do_rpcrequest('DescribeClusterV2', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_v2with_options(request, runtime)

    def describe_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowResponse(),
            self.do_rpcrequest('DescribeFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    def list_flow_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterResponse(),
            self.do_rpcrequest('ListFlowCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_with_options(request, runtime)

    def list_ldap_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLdapUsersResponse(),
            self.do_rpcrequest('ListLdapUsers', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ldap_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ldap_users_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteUserResponse(),
            self.do_rpcrequest('DeleteUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def create_flow_project_cluster_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('CreateFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project_cluster_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_cluster_setting_with_options(request, runtime)

    def describe_flow_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowInstanceResponse(),
            self.do_rpcrequest('DescribeFlowInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_instance_with_options(request, runtime)

    def create_flow_project_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectUserResponse(),
            self.do_rpcrequest('CreateFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_user_with_options(request, runtime)

    def create_flow_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowCategoryResponse(),
            self.do_rpcrequest('CreateFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_category_with_options(request, runtime)

    def delete_flow_project_cluster_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('DeleteFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project_cluster_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_cluster_setting_with_options(request, runtime)

    def list_libraries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLibrariesResponse(),
            self.do_rpcrequest('ListLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_libraries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_libraries_with_options(request, runtime)

    def run_scaling_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RunScalingActionResponse(),
            self.do_rpcrequest('RunScalingAction', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_scaling_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_scaling_action_with_options(request, runtime)

    def install_libraries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.InstallLibrariesResponse(),
            self.do_rpcrequest('InstallLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_libraries(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_libraries_with_options(request, runtime)

    def list_flow_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobsResponse(),
            self.do_rpcrequest('ListFlowJobs', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_jobs_with_options(request, runtime)

    def modify_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowResponse(),
            self.do_rpcrequest('ModifyFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def list_library_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLibraryStatusResponse(),
            self.do_rpcrequest('ListLibraryStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_library_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_library_status_with_options(request, runtime)

    def describe_cluster_service_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterServiceConfigResponse(),
            self.do_rpcrequest('DescribeClusterServiceConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_config_with_options(request, runtime)

    def modify_flow_project_cluster_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('ModifyFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_project_cluster_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_project_cluster_setting_with_options(request, runtime)

    def delete_flow_project_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectUserResponse(),
            self.do_rpcrequest('DeleteFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_user_with_options(request, runtime)

    def create_cluster_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterV2Response(),
            self.do_rpcrequest('CreateClusterV2', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_v2with_options(request, runtime)

    def modify_cluster_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterNameResponse(),
            self.do_rpcrequest('ModifyClusterName', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_name_with_options(request, runtime)

    def list_cluster_operation_host_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationHostTaskResponse(),
            self.do_rpcrequest('ListClusterOperationHostTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_host_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_host_task_with_options(request, runtime)

    def describe_scaling_config_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingConfigItemResponse(),
            self.do_rpcrequest('DescribeScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_config_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_config_item_with_options(request, runtime)

    def list_cluster_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterHostResponse(),
            self.do_rpcrequest('ListClusterHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_with_options(request, runtime)

    def create_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateScalingGroupResponse(),
            self.do_rpcrequest('CreateScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    def describe_cluster_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterServiceResponse(),
            self.do_rpcrequest('DescribeClusterService', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_with_options(request, runtime)

    def list_flow_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectsResponse(),
            self.do_rpcrequest('ListFlowProjects', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_projects_with_options(request, runtime)

    def create_meta_table_preview_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateMetaTablePreviewTaskResponse(),
            self.do_rpcrequest('CreateMetaTablePreviewTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_meta_table_preview_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_meta_table_preview_task_with_options(request, runtime)

    def list_flow_project_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectUserResponse(),
            self.do_rpcrequest('ListFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_user_with_options(request, runtime)

    def delete_cluster_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteClusterHostGroupResponse(),
            self.do_rpcrequest('DeleteClusterHostGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_host_group_with_options(request, runtime)

    def describe_library_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeLibraryDetailResponse(),
            self.do_rpcrequest('DescribeLibraryDetail', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_library_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_library_detail_with_options(request, runtime)

    def list_flows_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowsResponse(),
            self.do_rpcrequest('ListFlows', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flows(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)
