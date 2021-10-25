# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpc20180412 import models as ehpc20180412_models
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
        self._endpoint = self.get_endpoint('ehpc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeJobResponse(),
            self.do_rpcrequest('DescribeJob', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteImageResponse(),
            self.do_rpcrequest('DeleteImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_gwscluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSClusterResponse(),
            self.do_rpcrequest('DeleteGWSCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_gwscluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gwscluster_with_options(request, runtime)

    def delete_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteUsersResponse(),
            self.do_rpcrequest('DeleteUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    def describe_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeClusterResponse(),
            self.do_rpcrequest('DescribeCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def describe_container_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeContainerAppResponse(),
            self.do_rpcrequest('DescribeContainerApp', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_container_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_app_with_options(request, runtime)

    def pull_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.PullImageResponse(),
            self.do_rpcrequest('PullImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def pull_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pull_image_with_options(request, runtime)

    def stop_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopNodesResponse(),
            self.do_rpcrequest('StopNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    def list_nodes_by_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesByQueueResponse(),
            self.do_rpcrequest('ListNodesByQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_nodes_by_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_queue_with_options(request, runtime)

    def modify_container_app_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyContainerAppAttributesResponse(),
            self.do_rpcrequest('ModifyContainerAppAttributes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_container_app_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_container_app_attributes_with_options(request, runtime)

    def set_scheduler_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetSchedulerInfoResponse(),
            self.do_rpcrequest('SetSchedulerInfo', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_scheduler_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scheduler_info_with_options(request, runtime)

    def get_cloud_metric_profiling_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricProfilingResponse(),
            self.do_rpcrequest('GetCloudMetricProfiling', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_cloud_metric_profiling(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_profiling_with_options(request, runtime)

    def describe_image_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImagePriceResponse(),
            self.do_rpcrequest('DescribeImagePrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_image_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_price_with_options(request, runtime)

    def stop_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopGWSInstanceResponse(),
            self.do_rpcrequest('StopGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_gwsinstance_with_options(request, runtime)

    def get_auto_scale_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAutoScaleConfigResponse(),
            self.do_rpcrequest('GetAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_auto_scale_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scale_config_with_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesResponse(),
            self.do_rpcrequest('ListNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def list_commands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommandsResponse(),
            self.do_rpcrequest('ListCommands', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_commands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_commands_with_options(request, runtime)

    def create_gwsimage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSImageResponse(),
            self.do_rpcrequest('CreateGWSImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_gwsimage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gwsimage_with_options(request, runtime)

    def invoke_shell_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InvokeShellCommandResponse(),
            self.do_rpcrequest('InvokeShellCommand', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def invoke_shell_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_shell_command_with_options(request, runtime)

    def list_file_system_with_mount_targets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListFileSystemWithMountTargetsResponse(),
            self.do_rpcrequest('ListFileSystemWithMountTargets', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_file_system_with_mount_targets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_system_with_mount_targets_with_options(request, runtime)

    def modify_cluster_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyClusterAttributesResponse(),
            self.do_rpcrequest('ModifyClusterAttributes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_cluster_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_attributes_with_options(request, runtime)

    def delete_job_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobTemplatesResponse(),
            self.do_rpcrequest('DeleteJobTemplates', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_job_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_templates_with_options(request, runtime)

    def get_cloud_metric_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricLogsResponse(),
            self.do_rpcrequest('GetCloudMetricLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_cloud_metric_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_logs_with_options(request, runtime)

    def create_job_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobTemplateResponse(),
            self.do_rpcrequest('CreateJobTemplate', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_job_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_template_with_options(request, runtime)

    def get_hybrid_cluster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHybridClusterConfigResponse(),
            self.do_rpcrequest('GetHybridClusterConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hybrid_cluster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hybrid_cluster_config_with_options(request, runtime)

    def describe_gwsinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSInstancesResponse(),
            self.do_rpcrequest('DescribeGWSInstances', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_gwsinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsinstances_with_options(request, runtime)

    def reset_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ResetNodesResponse(),
            self.do_rpcrequest('ResetNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def reset_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_nodes_with_options(request, runtime)

    def uninstall_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UninstallSoftwareResponse(),
            self.do_rpcrequest('UninstallSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def uninstall_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_software_with_options(request, runtime)

    def apply_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ApplyNodesResponse(),
            self.do_rpcrequest('ApplyNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def apply_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_nodes_with_options(request, runtime)

    def describe_gwsclusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClustersResponse(),
            self.do_rpcrequest('DescribeGWSClusters', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_gwsclusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsclusters_with_options(request, runtime)

    def delete_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobsResponse(),
            self.do_rpcrequest('DeleteJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    def list_container_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerImagesResponse(),
            self.do_rpcrequest('ListContainerImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_container_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    def delete_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteNodesResponse(),
            self.do_rpcrequest('DeleteNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    def list_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsResponse(),
            self.do_rpcrequest('ListJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    def list_cpfs_file_systems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCpfsFileSystemsResponse(),
            self.do_rpcrequest('ListCpfsFileSystems', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_cpfs_file_systems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cpfs_file_systems_with_options(request, runtime)

    def list_clusters_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersMetaResponse(),
            self.do_rpcrequest('ListClustersMeta', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_clusters_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_meta_with_options(request, runtime)

    def query_service_pack_and_price_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.QueryServicePackAndPriceResponse(),
            self.do_rpcrequest('QueryServicePackAndPrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_service_pack_and_price(self):
        runtime = util_models.RuntimeOptions()
        return self.query_service_pack_and_price_with_options(runtime)

    def delete_container_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteContainerAppsResponse(),
            self.do_rpcrequest('DeleteContainerApps', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_container_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_container_apps_with_options(request, runtime)

    def list_volumes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListVolumesResponse(),
            self.do_rpcrequest('ListVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_volumes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_volumes_with_options(request, runtime)

    def list_invocation_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationStatusResponse(),
            self.do_rpcrequest('ListInvocationStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_invocation_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_status_with_options(request, runtime)

    def modify_image_gateway_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyImageGatewayConfigResponse(),
            self.do_rpcrequest('ModifyImageGatewayConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_image_gateway_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_gateway_config_with_options(request, runtime)

    def list_container_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerAppsResponse(),
            self.do_rpcrequest('ListContainerApps', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_container_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_container_apps_with_options(request, runtime)

    def delete_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteSecurityGroupResponse(),
            self.do_rpcrequest('DeleteSecurityGroup', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    def describe_nfsclient_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeNFSClientStatusResponse(),
            self.do_rpcrequest('DescribeNFSClientStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_nfsclient_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nfsclient_status_with_options(request, runtime)

    def ecd_delete_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.EcdDeleteDesktopsResponse(),
            self.do_rpcrequest('EcdDeleteDesktops', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def ecd_delete_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ecd_delete_desktops_with_options(request, runtime)

    def list_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def submit_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitJobResponse(),
            self.do_rpcrequest('SubmitJob', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def submit_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_job_with_options(request, runtime)

    def get_accounting_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAccountingReportResponse(),
            self.do_rpcrequest('GetAccountingReport', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_accounting_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_accounting_report_with_options(request, runtime)

    def describe_auto_scale_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeAutoScaleConfigResponse(),
            self.do_rpcrequest('DescribeAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_auto_scale_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scale_config_with_options(request, runtime)

    def get_visual_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetVisualServiceStatusResponse(),
            self.do_rpcrequest('GetVisualServiceStatus', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_visual_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_visual_service_status_with_options(request, runtime)

    def start_visual_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartVisualServiceResponse(),
            self.do_rpcrequest('StartVisualService', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_visual_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_visual_service_with_options(request, runtime)

    def get_if_ecs_type_support_ht_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse(),
            self.do_rpcrequest('GetIfEcsTypeSupportHtConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_if_ecs_type_support_ht_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_if_ecs_type_support_ht_config_with_options(request, runtime)

    def get_scheduler_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetSchedulerInfoResponse(),
            self.do_rpcrequest('GetSchedulerInfo', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_scheduler_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scheduler_info_with_options(request, runtime)

    def set_gwsinstance_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceUserResponse(),
            self.do_rpcrequest('SetGWSInstanceUser', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_gwsinstance_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_user_with_options(request, runtime)

    def get_workbench_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetWorkbenchTokenResponse(),
            self.do_rpcrequest('GetWorkbenchToken', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_workbench_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_workbench_token_with_options(request, runtime)

    def install_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InstallSoftwareResponse(),
            self.do_rpcrequest('InstallSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def install_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_software_with_options(request, runtime)

    def list_available_ecs_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListAvailableEcsTypesResponse(),
            self.do_rpcrequest('ListAvailableEcsTypes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_available_ecs_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_ecs_types_with_options(request, runtime)

    def mount_nfswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.MountNFSResponse(),
            self.do_rpcrequest('MountNFS', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def mount_nfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mount_nfswith_options(request, runtime)

    def add_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddQueueResponse(),
            self.do_rpcrequest('AddQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_queue_with_options(request, runtime)

    def create_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSInstanceResponse(),
            self.do_rpcrequest('CreateGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gwsinstance_with_options(request, runtime)

    def list_current_client_version_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.ListCurrentClientVersionResponse(),
            self.do_rpcrequest('ListCurrentClientVersion', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_current_client_version(self):
        runtime = util_models.RuntimeOptions()
        return self.list_current_client_version_with_options(runtime)

    def update_cluster_volumes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateClusterVolumesResponse(),
            self.do_rpcrequest('UpdateClusterVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_cluster_volumes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_volumes_with_options(request, runtime)

    def start_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartGWSInstanceResponse(),
            self.do_rpcrequest('StartGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_gwsinstance_with_options(request, runtime)

    def list_invocation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationResultsResponse(),
            self.do_rpcrequest('ListInvocationResults', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_invocation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_results_with_options(request, runtime)

    def set_auto_scale_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetAutoScaleConfigResponse(),
            self.do_rpcrequest('SetAutoScaleConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_auto_scale_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_auto_scale_config_with_options(request, runtime)

    def add_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddNodesResponse(),
            self.do_rpcrequest('AddNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_nodes_with_options(request, runtime)

    def list_softwares_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSoftwaresResponse(),
            self.do_rpcrequest('ListSoftwares', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_softwares(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    def list_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSecurityGroupsResponse(),
            self.do_rpcrequest('ListSecurityGroups', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_security_groups_with_options(request, runtime)

    def describe_gwsimages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSImagesResponse(),
            self.do_rpcrequest('DescribeGWSImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_gwsimages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsimages_with_options(request, runtime)

    def stop_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopJobsResponse(),
            self.do_rpcrequest('StopJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    def start_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartNodesResponse(),
            self.do_rpcrequest('StartNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_nodes_with_options(request, runtime)

    def modify_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserGroupsResponse(),
            self.do_rpcrequest('ModifyUserGroups', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_groups_with_options(request, runtime)

    def set_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetQueueResponse(),
            self.do_rpcrequest('SetQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_queue_with_options(request, runtime)

    def start_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartClusterResponse(),
            self.do_rpcrequest('StartCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def start_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_cluster_with_options(request, runtime)

    def list_custom_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCustomImagesResponse(),
            self.do_rpcrequest('ListCustomImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_custom_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    def add_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddUsersResponse(),
            self.do_rpcrequest('AddUsers', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_users_with_options(request, runtime)

    def create_gwscluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSClusterResponse(),
            self.do_rpcrequest('CreateGWSCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_gwscluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gwscluster_with_options(request, runtime)

    def list_job_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobTemplatesResponse(),
            self.do_rpcrequest('ListJobTemplates', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_job_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_templates_with_options(request, runtime)

    def describe_image_gateway_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageGatewayConfigResponse(),
            self.do_rpcrequest('DescribeImageGatewayConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_image_gateway_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_gateway_config_with_options(request, runtime)

    def get_gwsconnect_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetGWSConnectTicketResponse(),
            self.do_rpcrequest('GetGWSConnectTicket', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_gwsconnect_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gwsconnect_ticket_with_options(request, runtime)

    def list_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTasksResponse(),
            self.do_rpcrequest('ListTasks', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    def stop_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopClusterResponse(),
            self.do_rpcrequest('StopCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cluster_with_options(request, runtime)

    def add_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddSecurityGroupResponse(),
            self.do_rpcrequest('AddSecurityGroup', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_security_group_with_options(request, runtime)

    def list_nodes_no_paging_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesNoPagingResponse(),
            self.do_rpcrequest('ListNodesNoPaging', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_nodes_no_paging(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_no_paging_with_options(request, runtime)

    def set_gwsinstance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceNameResponse(),
            self.do_rpcrequest('SetGWSInstanceName', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def set_gwsinstance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_name_with_options(request, runtime)

    def create_hybrid_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateHybridClusterResponse(),
            self.do_rpcrequest('CreateHybridCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_hybrid_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_cluster_with_options(request, runtime)

    def update_queue_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateQueueConfigResponse(),
            self.do_rpcrequest('UpdateQueueConfig', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_queue_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_queue_config_with_options(request, runtime)

    def stop_visual_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopVisualServiceResponse(),
            self.do_rpcrequest('StopVisualService', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def stop_visual_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_visual_service_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateClusterResponse(),
            self.do_rpcrequest('CreateCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def describe_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageResponse(),
            self.do_rpcrequest('DescribeImage', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_with_options(request, runtime)

    def modify_user_passwords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserPasswordsResponse(),
            self.do_rpcrequest('ModifyUserPasswords', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_user_passwords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_passwords_with_options(request, runtime)

    def delete_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteQueueResponse(),
            self.do_rpcrequest('DeleteQueue', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    def list_installed_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInstalledSoftwareResponse(),
            self.do_rpcrequest('ListInstalledSoftware', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_installed_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_installed_software_with_options(request, runtime)

    def get_health_monitor_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHealthMonitorLogsResponse(),
            self.do_rpcrequest('GetHealthMonitorLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_health_monitor_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_health_monitor_logs_with_options(request, runtime)

    def upgrade_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpgradeClientResponse(),
            self.do_rpcrequest('UpgradeClient', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def upgrade_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteClusterResponse(),
            self.do_rpcrequest('DeleteCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def list_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListImagesResponse(),
            self.do_rpcrequest('ListImages', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    def set_gwscluster_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSClusterPolicyResponse(),
            self.do_rpcrequest('SetGWSClusterPolicy', '2018-04-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_gwscluster_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gwscluster_policy_with_options(request, runtime)

    def list_queues_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListQueuesResponse(),
            self.do_rpcrequest('ListQueues', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_queues(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    def create_job_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobFileResponse(),
            self.do_rpcrequest('CreateJobFile', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_job_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_file_with_options(request, runtime)

    def list_cloud_metric_profilings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCloudMetricProfilingsResponse(),
            self.do_rpcrequest('ListCloudMetricProfilings', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_cloud_metric_profilings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_metric_profilings_with_options(request, runtime)

    def get_cluster_volumes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetClusterVolumesResponse(),
            self.do_rpcrequest('GetClusterVolumes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_cluster_volumes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_volumes_with_options(request, runtime)

    def delete_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSInstanceResponse(),
            self.do_rpcrequest('DeleteGWSInstance', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gwsinstance_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ehpc20180412_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def initialize_ehpcwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.InitializeEHPCResponse(),
            self.do_rpcrequest('InitializeEHPC', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def initialize_ehpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.initialize_ehpcwith_options(request, runtime)

    def run_cloud_metric_profiling_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RunCloudMetricProfilingResponse(),
            self.do_rpcrequest('RunCloudMetricProfiling', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def run_cloud_metric_profiling(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_metric_profiling_with_options(request, runtime)

    def add_existed_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddExistedNodesResponse(),
            self.do_rpcrequest('AddExistedNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_existed_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_existed_nodes_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribePriceResponse(),
            self.do_rpcrequest('DescribePrice', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def rerun_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RerunJobsResponse(),
            self.do_rpcrequest('RerunJobs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def rerun_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rerun_jobs_with_options(request, runtime)

    def describe_gwscluster_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClusterPolicyResponse(),
            self.do_rpcrequest('DescribeGWSClusterPolicy', '2018-04-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_gwscluster_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwscluster_policy_with_options(request, runtime)

    def add_local_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddLocalNodesResponse(),
            self.do_rpcrequest('AddLocalNodes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_local_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_local_nodes_with_options(request, runtime)

    def edit_job_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.EditJobTemplateResponse(),
            self.do_rpcrequest('EditJobTemplate', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def edit_job_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_job_template_with_options(request, runtime)

    def modify_visual_service_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyVisualServicePasswdResponse(),
            self.do_rpcrequest('ModifyVisualServicePasswd', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_visual_service_passwd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_visual_service_passwd_with_options(request, runtime)

    def list_preferred_ecs_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListPreferredEcsTypesResponse(),
            self.do_rpcrequest('ListPreferredEcsTypes', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_preferred_ecs_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_preferred_ecs_types_with_options(request, runtime)

    def add_container_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddContainerAppResponse(),
            self.do_rpcrequest('AddContainerApp', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_container_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_container_app_with_options(request, runtime)

    def list_cluster_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClusterLogsResponse(),
            self.do_rpcrequest('ListClusterLogs', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_cluster_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_logs_with_options(request, runtime)

    def recover_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ehpc20180412_models.RecoverClusterResponse(),
            self.do_rpcrequest('RecoverCluster', '2018-04-12', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recover_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recover_cluster_with_options(request, runtime)
