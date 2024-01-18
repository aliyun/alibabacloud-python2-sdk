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

    def add_container_app_with_options(self, request, runtime):
        """
        If you select an image for a new containerized application, the image is pulled from Docker Hub by default. However, the version of the image may not be up to date. You can call the [PullImage](~~159052~~) operation to pull the latest image.
        

        @param request: AddContainerAppRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddContainerAppResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddContainerApp',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    def add_container_app(self, request):
        """
        If you select an image for a new containerized application, the image is pulled from Docker Hub by default. However, the version of the image may not be up to date. You can call the [PullImage](~~159052~~) operation to pull the latest image.
        

        @param request: AddContainerAppRequest

        @return: AddContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_container_app_with_options(request, runtime)

    def add_existed_nodes_with_options(self, request, runtime):
        """
        The compute nodes to be added are in the Stopped state.
        *   After the compute nodes are added to the cluster, the operating systems of the nodes are replaced with the operating system specified by the ImageId parameter.
        *   The hosts of the compute nodes must be different from those of the existing compute nodes in the cluster. Otherwise, the add operation fails.
        

        @param request: AddExistedNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddExistedNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExistedNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddExistedNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_existed_nodes(self, request):
        """
        The compute nodes to be added are in the Stopped state.
        *   After the compute nodes are added to the cluster, the operating systems of the nodes are replaced with the operating system specified by the ImageId parameter.
        *   The hosts of the compute nodes must be different from those of the existing compute nodes in the cluster. Otherwise, the add operation fails.
        

        @param request: AddExistedNodesRequest

        @return: AddExistedNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_existed_nodes_with_options(request, runtime)

    def add_local_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLocalNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddLocalNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_local_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_local_nodes_with_options(request, runtime)

    def add_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_nodes_with_options(request, runtime)

    def add_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def add_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_queue_with_options(request, runtime)

    def add_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSecurityGroup',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_security_group_with_options(request, runtime)

    def add_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.AddUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_users_with_options(request, runtime)

    def apply_nodes_with_options(self, request, runtime):
        """
        ## [](#)Description
        You can call the ApplyNodes operation to specify the number of compute nodes, the number of vCPUs, and the memory size when you add nodes to a cluster.
        

        @param request: ApplyNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApplyNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ApplyNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_nodes(self, request):
        """
        ## [](#)Description
        You can call the ApplyNodes operation to specify the number of compute nodes, the number of vCPUs, and the memory size when you add nodes to a cluster.
        

        @param request: ApplyNodesRequest

        @return: ApplyNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_nodes_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        """
        After you create an Elastic High Performance Computing (E-HPC) cluster, you are charged for the cluster resources that you use. We recommend that you learn about the billing methods of E-HPC in advance. For more information, see [Billing overview](~~57844~~).
        

        @param request: CreateClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        """
        After you create an Elastic High Performance Computing (E-HPC) cluster, you are charged for the cluster resources that you use. We recommend that you learn about the billing methods of E-HPC in advance. For more information, see [Billing overview](~~57844~~).
        

        @param request: CreateClusterRequest

        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_gwscluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gwscluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gwscluster_with_options(request, runtime)

    def create_gwsimage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSImageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gwsimage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gwsimage_with_options(request, runtime)

    def create_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGWSInstance',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gwsinstance_with_options(request, runtime)

    def create_hybrid_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateHybridClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hybrid_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_cluster_with_options(request, runtime)

    def create_job_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobFile',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobFileResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_file_with_options(request, runtime)

    def create_job_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobTemplate',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.CreateJobTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_template_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        """
        After a cluster is released, the pay-as-you-go nodes and the subscription nodes that are expired are automatically released. The subscription nodes that are expired are retained. If you need to release subscription nodes that are not expired, change the billing method to pay-as-you-go. Before you release a cluster, make sure that you no longer use the cluster.
        

        @param request: DeleteClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, request):
        """
        After a cluster is released, the pay-as-you-go nodes and the subscription nodes that are expired are automatically released. The subscription nodes that are expired are retained. If you need to release subscription nodes that are not expired, change the billing method to pay-as-you-go. Before you release a cluster, make sure that you no longer use the cluster.
        

        @param request: DeleteClusterRequest

        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def delete_container_apps_with_options(self, request, runtime):
        """
        Before you delete container applications, you can call the [ListContainerApps](~~87333~~) operation to query the container applications.
        

        @param request: DeleteContainerAppsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteContainerAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContainerApps',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteContainerAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_container_apps(self, request):
        """
        Before you delete container applications, you can call the [ListContainerApps](~~87333~~) operation to query the container applications.
        

        @param request: DeleteContainerAppsRequest

        @return: DeleteContainerAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_container_apps_with_options(request, runtime)

    def delete_gwscluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGWSCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gwscluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gwscluster_with_options(request, runtime)

    def delete_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGWSInstance',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gwsinstance_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    def delete_job_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobTemplates',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_job_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_templates_with_options(request, runtime)

    def delete_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    def delete_local_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLocalImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteLocalImageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_local_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_local_image_with_options(request, runtime)

    def delete_nodes_with_options(self, request, runtime):
        """
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        

        @param request: DeleteNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nodes(self, request):
        """
        Before you delete a compute node, we recommend that you export all job data from the node to prevent data loss.
        

        @param request: DeleteNodesRequest

        @return: DeleteNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    def delete_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    def delete_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroup',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    def delete_users_with_options(self, request, runtime):
        """
        If you delete a user, only its information is deleted. The files stored in the /home directory for the user are retained. For example, if you delete a user named user1, the files in the `/home/user1/` directory of the cluster are not deleted. However, a deleted user cannot be recovered. Even if you create another user that has the same name, the data retained for the deleted user is not reused.
        

        @param request: DeleteUsersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_users(self, request):
        """
        If you delete a user, only its information is deleted. The files stored in the /home directory for the user are retained. For example, if you delete a user named user1, the files in the `/home/user1/` directory of the cluster are not deleted. However, a deleted user cannot be recovered. Even if you create another user that has the same name, the data retained for the deleted user is not reused.
        

        @param request: DeleteUsersRequest

        @return: DeleteUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    def describe_auto_scale_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_scale_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_scale_config_with_options(request, runtime)

    def describe_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    def describe_container_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerApp',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_app_with_options(request, runtime)

    def describe_estack_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEstackImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeEstackImageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_estack_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_estack_image_with_options(request, runtime)

    def describe_gwscluster_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_mode):
            query['AsyncMode'] = request.async_mode
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSClusterPolicy',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClusterPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gwscluster_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwscluster_policy_with_options(request, runtime)

    def describe_gwsclusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSClusters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gwsclusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsclusters_with_options(request, runtime)

    def describe_gwsimages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gwsimages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsimages_with_options(request, runtime)

    def describe_gwsinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGWSInstances',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeGWSInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_gwsinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gwsinstances_with_options(request, runtime)

    def describe_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_with_options(request, runtime)

    def describe_image_gateway_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageGatewayConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImageGatewayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_gateway_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_gateway_config_with_options(request, runtime)

    def describe_image_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeImagePriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_price_with_options(request, runtime)

    def describe_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    def describe_nfsclient_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNFSClientStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeNFSClientStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nfsclient_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nfsclient_status_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def describe_serverless_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.DescribeServerlessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_serverless_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_serverless_jobs_with_options(request, runtime)

    def edit_job_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditJobTemplate',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.EditJobTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_job_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_job_template_with_options(request, runtime)

    def get_accounting_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountingReport',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAccountingReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_accounting_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_accounting_report_with_options(request, runtime)

    def get_auto_scale_config_with_options(self, request, runtime):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=EHPC\\&api=GetAutoScaleConfig\\&type=RPC\\&version=2018-04-12)
        

        @param request: GetAutoScaleConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auto_scale_config(self, request):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=EHPC\\&api=GetAutoScaleConfig\\&type=RPC\\&version=2018-04-12)
        

        @param request: GetAutoScaleConfigRequest

        @return: GetAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scale_config_with_options(request, runtime)

    def get_cloud_metric_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudMetricLogs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_metric_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_logs_with_options(request, runtime)

    def get_cloud_metric_profiling_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudMetricProfiling',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCloudMetricProfilingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_metric_profiling(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_metric_profiling_with_options(request, runtime)

    def get_cluster_volumes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetClusterVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_volumes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_volumes_with_options(request, runtime)

    def get_common_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommonImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetCommonImageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_common_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_common_image_with_options(request, runtime)

    def get_gwsconnect_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGWSConnectTicket',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetGWSConnectTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gwsconnect_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gwsconnect_ticket_with_options(request, runtime)

    def get_hybrid_cluster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHybridClusterConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetHybridClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hybrid_cluster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hybrid_cluster_config_with_options(request, runtime)

    def get_if_ecs_type_support_ht_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIfEcsTypeSupportHtConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetIfEcsTypeSupportHtConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_if_ecs_type_support_ht_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_if_ecs_type_support_ht_config_with_options(request, runtime)

    def get_job_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_log_with_options(request, runtime)

    def get_post_scripts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPostScripts',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetPostScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_post_scripts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_post_scripts_with_options(request, runtime)

    def get_scheduler_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSchedulerInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetSchedulerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scheduler_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scheduler_info_with_options(request, runtime)

    def get_user_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetUserImageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_image_with_options(request, runtime)

    def get_visual_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVisualServiceStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.GetVisualServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_visual_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_visual_service_status_with_options(request, runtime)

    def initialize_ehpcwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeEHPC',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InitializeEHPCResponse(),
            self.call_api(params, req, runtime)
        )

    def initialize_ehpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.initialize_ehpcwith_options(request, runtime)

    def inspect_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InspectImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InspectImageResponse(),
            self.call_api(params, req, runtime)
        )

    def inspect_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.inspect_image_with_options(request, runtime)

    def install_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InstallSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    def install_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_software_with_options(request, runtime)

    def invoke_shell_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeShellCommand',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.InvokeShellCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_shell_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_shell_command_with_options(request, runtime)

    def list_available_ecs_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableEcsTypes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListAvailableEcsTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_ecs_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_ecs_types_with_options(request, runtime)

    def list_cloud_metric_profilings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudMetricProfilings',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCloudMetricProfilingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cloud_metric_profilings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_metric_profilings_with_options(request, runtime)

    def list_cluster_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterLogs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_logs_with_options(request, runtime)

    def list_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def list_clusters_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClustersMeta',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListClustersMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def list_clusters_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_meta_with_options(request, runtime)

    def list_commands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommands',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_commands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_commands_with_options(request, runtime)

    def list_community_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommunityImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCommunityImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_community_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_community_images_with_options(request, runtime)

    def list_container_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerApps',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_container_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_container_apps_with_options(request, runtime)

    def list_container_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListContainerImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_container_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    def list_cpfs_file_systems_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCpfsFileSystems',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCpfsFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cpfs_file_systems(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cpfs_file_systems_with_options(request, runtime)

    def list_current_client_version_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCurrentClientVersion',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCurrentClientVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_current_client_version(self):
        runtime = util_models.RuntimeOptions()
        return self.list_current_client_version_with_options(runtime)

    def list_custom_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    def list_file_system_with_mount_targets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFileSystemWithMountTargets',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListFileSystemWithMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_file_system_with_mount_targets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_file_system_with_mount_targets_with_options(request, runtime)

    def list_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    def list_installed_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstalledSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInstalledSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    def list_installed_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_installed_software_with_options(request, runtime)

    def list_invocation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvocationResults',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_invocation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_results_with_options(request, runtime)

    def list_invocation_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvocationStatus',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListInvocationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_invocation_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_status_with_options(request, runtime)

    def list_job_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobTemplates',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_job_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_templates_with_options(request, runtime)

    def list_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    def list_jobs_with_filters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobsWithFilters',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListJobsWithFiltersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs_with_filters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_filters_with_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def list_nodes_by_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesByQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesByQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes_by_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_queue_with_options(request, runtime)

    def list_nodes_no_paging_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesNoPaging',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListNodesNoPagingResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes_no_paging(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_no_paging_with_options(request, runtime)

    def list_preferred_ecs_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPreferredEcsTypes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListPreferredEcsTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_preferred_ecs_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_preferred_ecs_types_with_options(request, runtime)

    def list_queues_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueues',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_queues(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_queues_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def list_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityGroups',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_security_groups_with_options(request, runtime)

    def list_serverless_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.job_names):
            query['JobNames'] = request.job_names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_order):
            query['StartOrder'] = request.start_order
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.submit_order):
            query['SubmitOrder'] = request.submit_order
        if not UtilClient.is_unset(request.submit_time_end):
            query['SubmitTimeEnd'] = request.submit_time_end
        if not UtilClient.is_unset(request.submit_time_start):
            query['SubmitTimeStart'] = request.submit_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListServerlessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_serverless_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_serverless_jobs_with_options(request, runtime)

    def list_softwares_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwares',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    def list_softwares(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tasks_with_options(self, request, runtime):
        """
        If you succeed in calling an asynchronous API operation, a response is generated before a resulting task is completed. Therefore, to query the result of the task, you can use the TaskId parameter returned by the API operation.
        

        @param request: ListTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, request):
        """
        If you succeed in calling an asynchronous API operation, a response is generated before a resulting task is completed. Therefore, to query the result of the task, you can use the TaskId parameter returned by the API operation.
        

        @param request: ListTasksRequest

        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    def list_upgrade_clients_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUpgradeClients',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUpgradeClientsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_upgrade_clients(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_upgrade_clients_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_users_async_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersAsync',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListUsersAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users_async(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_async_with_options(request, runtime)

    def list_volumes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ListVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_volumes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_volumes_with_options(request, runtime)

    def modify_cluster_attributes_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you call this operation, you can call the [DescribeCluster](~~87126~~) operation to query details of the selected cluster.
        

        @param request: ModifyClusterAttributesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyClusterAttributesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAttributes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyClusterAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_attributes(self, request):
        """
        ## Usage notes
        Before you call this operation, you can call the [DescribeCluster](~~87126~~) operation to query details of the selected cluster.
        

        @param request: ModifyClusterAttributesRequest

        @return: ModifyClusterAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_attributes_with_options(request, runtime)

    def modify_container_app_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyContainerAppAttributes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyContainerAppAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_container_app_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_container_app_attributes_with_options(request, runtime)

    def modify_image_gateway_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageGatewayConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyImageGatewayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_image_gateway_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_gateway_config_with_options(request, runtime)

    def modify_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroups',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_groups_with_options(request, runtime)

    def modify_user_passwords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPasswords',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyUserPasswordsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_passwords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_passwords_with_options(request, runtime)

    def modify_visual_service_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVisualServicePasswd',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ModifyVisualServicePasswdResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_visual_service_passwd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_visual_service_passwd_with_options(request, runtime)

    def mount_nfswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MountNFS',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.MountNFSResponse(),
            self.call_api(params, req, runtime)
        )

    def mount_nfs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mount_nfswith_options(request, runtime)

    def pull_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullImage',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.PullImageResponse(),
            self.call_api(params, req, runtime)
        )

    def pull_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pull_image_with_options(request, runtime)

    def query_service_pack_and_price_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryServicePackAndPrice',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.QueryServicePackAndPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_service_pack_and_price(self):
        runtime = util_models.RuntimeOptions()
        return self.query_service_pack_and_price_with_options(runtime)

    def recover_cluster_with_options(self, request, runtime):
        """
        You can call the operation to reset and restore a cluster only when the cluster is in the Exception state. You can call the [ListClusters](~~87116~~) operation to query the ID and status of a cluster.
        We recommend that you export all job data before you restore a cluster. When you reset and restore a cluster, take note of the following impacts:
        *   The system disks of all nodes are changed. By default, new system disks are configured based on the settings that you specified when the cluster was created.
        *   The data on the system disks and data disks of all cluster nodes is lost. The data includes user information, job information, scheduler queue information, and configuration data of auto-scaling queues. However, the data on Apsara File Storage NAS file systems is retained.
        *   The self-managed queues in the cluster are deleted. All nodes are retained and migrated to the default queue of the cluster.
        

        @param request: RecoverClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RecoverClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RecoverClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def recover_cluster(self, request):
        """
        You can call the operation to reset and restore a cluster only when the cluster is in the Exception state. You can call the [ListClusters](~~87116~~) operation to query the ID and status of a cluster.
        We recommend that you export all job data before you restore a cluster. When you reset and restore a cluster, take note of the following impacts:
        *   The system disks of all nodes are changed. By default, new system disks are configured based on the settings that you specified when the cluster was created.
        *   The data on the system disks and data disks of all cluster nodes is lost. The data includes user information, job information, scheduler queue information, and configuration data of auto-scaling queues. However, the data on Apsara File Storage NAS file systems is retained.
        *   The self-managed queues in the cluster are deleted. All nodes are retained and migrated to the default queue of the cluster.
        

        @param request: RecoverClusterRequest

        @return: RecoverClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recover_cluster_with_options(request, runtime)

    def rerun_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RerunJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def rerun_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rerun_jobs_with_options(request, runtime)

    def reset_nodes_with_options(self, request, runtime):
        """
        After a node is reset, the operating system and software return to their initial states. To ensure that jobs run as expected, we recommend that you do not reset running nodes unless you need to perform crash recovery.
        

        @param request: ResetNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetNodesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.ResetNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_nodes(self, request):
        """
        After a node is reset, the operating system and software return to their initial states. To ensure that jobs run as expected, we recommend that you do not reset running nodes unless you need to perform crash recovery.
        

        @param request: ResetNodesRequest

        @return: ResetNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_nodes_with_options(request, runtime)

    def run_cloud_metric_profiling_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCloudMetricProfiling',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.RunCloudMetricProfilingResponse(),
            self.call_api(params, req, runtime)
        )

    def run_cloud_metric_profiling(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_cloud_metric_profiling_with_options(request, runtime)

    def set_auto_scale_config_with_options(self, request, runtime):
        """
        ## Usage notes
        If the settings in the Queue Configuration section are different from the settings in the Global Configurations section, the former prevails.
        

        @param request: SetAutoScaleConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetAutoScaleConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAutoScaleConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_auto_scale_config(self, request):
        """
        ## Usage notes
        If the settings in the Queue Configuration section are different from the settings in the Global Configurations section, the former prevails.
        

        @param request: SetAutoScaleConfigRequest

        @return: SetAutoScaleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_auto_scale_config_with_options(request, runtime)

    def set_gwscluster_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_mode):
            query['AsyncMode'] = request.async_mode
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.udp_port):
            query['UdpPort'] = request.udp_port
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSClusterPolicy',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSClusterPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_gwscluster_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gwscluster_policy_with_options(request, runtime)

    def set_gwsinstance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSInstanceName',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    def set_gwsinstance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_name_with_options(request, runtime)

    def set_gwsinstance_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGWSInstanceUser',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetGWSInstanceUserResponse(),
            self.call_api(params, req, runtime)
        )

    def set_gwsinstance_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_gwsinstance_user_with_options(request, runtime)

    def set_post_scripts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPostScripts',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetPostScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_post_scripts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_post_scripts_with_options(request, runtime)

    def set_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQueue',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetQueueResponse(),
            self.call_api(params, req, runtime)
        )

    def set_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_queue_with_options(request, runtime)

    def set_scheduler_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSchedulerInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SetSchedulerInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_scheduler_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_scheduler_info_with_options(request, runtime)

    def start_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def start_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_cluster_with_options(request, runtime)

    def start_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartGWSInstance',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_gwsinstance_with_options(request, runtime)

    def start_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def start_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_nodes_with_options(request, runtime)

    def start_visual_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVisualService',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StartVisualServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_visual_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_visual_service_with_options(request, runtime)

    def stop_cluster_with_options(self, request, runtime):
        """
        If you stop a subscription compute node, its billing is not affected. If you stop a pay-as-you-go compute node for which you have enabled the economical mode*, you are no longer charged for its computing resources. For more information, see [Economical mode](~~63353~~).
        

        @param request: StopClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopClusterResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCluster',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_cluster(self, request):
        """
        If you stop a subscription compute node, its billing is not affected. If you stop a pay-as-you-go compute node for which you have enabled the economical mode*, you are no longer charged for its computing resources. For more information, see [Economical mode](~~63353~~).
        

        @param request: StopClusterRequest

        @return: StopClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_cluster_with_options(request, runtime)

    def stop_gwsinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopGWSInstance',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopGWSInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_gwsinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_gwsinstance_with_options(request, runtime)

    def stop_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    def stop_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopNodes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    def stop_serverless_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopServerlessJobs',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopServerlessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_serverless_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_serverless_jobs_with_options(request, runtime)

    def stop_visual_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopVisualService',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.StopVisualServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_visual_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_visual_service_with_options(request, runtime)

    def submit_job_with_options(self, request, runtime):
        """
        ## Description
        Before you submit a job in a cluster, you must upload a job file to the cluster, for example, job.sh. For more information, see [CreateJobFile](~~159049~~).
        

        @param request: SubmitJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_job(self, request):
        """
        ## Description
        Before you submit a job in a cluster, you must upload a job file to the cluster, for example, job.sh. For more information, see [CreateJobFile](~~159049~~).
        

        @param request: SubmitJobRequest

        @return: SubmitJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_job_with_options(request, runtime)

    def submit_serverless_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ehpc20180412_models.SubmitServerlessJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_properties):
            request.array_properties_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_properties, 'ArrayProperties', 'json')
        if not UtilClient.is_unset(tmp_req.container):
            request.container_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container, 'Container', 'json')
        if not UtilClient.is_unset(tmp_req.depends_on):
            request.depends_on_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.depends_on, 'DependsOn', 'json')
        if not UtilClient.is_unset(tmp_req.instance_type):
            request.instance_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_type, 'InstanceType', 'json')
        if not UtilClient.is_unset(tmp_req.retry_strategy):
            request.retry_strategy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_strategy, 'RetryStrategy', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_id):
            request.v_switch_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_id, 'VSwitchId', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_properties_shrink):
            query['ArrayProperties'] = request.array_properties_shrink
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.container_shrink):
            query['Container'] = request.container_shrink
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.depends_on_shrink):
            query['DependsOn'] = request.depends_on_shrink
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.instance_type_shrink):
            query['InstanceType'] = request.instance_type_shrink
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_priority):
            query['JobPriority'] = request.job_priority
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.retry_strategy_shrink):
            query['RetryStrategy'] = request.retry_strategy_shrink
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.v_switch_id_shrink):
            query['VSwitchId'] = request.v_switch_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitServerlessJob',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SubmitServerlessJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_serverless_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_serverless_job_with_options(request, runtime)

    def summary_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryImages',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SummaryImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def summary_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.summary_images_with_options(request, runtime)

    def summary_images_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryImagesInfo',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SummaryImagesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def summary_images_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.summary_images_info_with_options(request, runtime)

    def sync_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncUsers',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.SyncUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_users_with_options(request, runtime)

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
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def un_tag_resources_with_options(self, request, runtime):
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
            action='UnTagResources',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def un_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    def uninstall_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallSoftware',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UninstallSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_software_with_options(request, runtime)

    def update_cluster_volumes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterVolumes',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateClusterVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster_volumes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_volumes_with_options(request, runtime)

    def update_queue_config_with_options(self, request, runtime):
        """
        After you update the resource group, the nodes that you add by scaling out the cluster are automatically included in the resource group.
        

        @param request: UpdateQueueConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateQueueConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQueueConfig',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpdateQueueConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_queue_config(self, request):
        """
        After you update the resource group, the nodes that you add by scaling out the cluster are automatically included in the resource group.
        

        @param request: UpdateQueueConfigRequest

        @return: UpdateQueueConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_queue_config_with_options(request, runtime)

    def upgrade_client_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2018-04-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20180412_models.UpgradeClientResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_client(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)
