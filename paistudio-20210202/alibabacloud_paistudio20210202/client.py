# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paistudio20210202 import models as pai_studio_20210202_models
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
            'cn-beijing': 'pai.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'pai.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'pai.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'pai.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'pai.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'pai.ap-southeast-5.aliyuncs.com',
            'us-west-1': 'pai.us-west-1.aliyuncs.com',
            'us-east-1': 'pai.us-east-1.aliyuncs.com',
            'eu-central-1': 'pai.eu-central-1.aliyuncs.com',
            'me-east-1': 'pai.me-east-1.aliyuncs.com',
            'ap-south-1': 'pai.ap-south-1.aliyuncs.com',
            'cn-qingdao': 'pai.cn-qingdao.aliyuncs.com',
            'cn-zhangjiakou': 'pai.cn-zhangjiakou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('paistudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_experiment(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    def create_experiment_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateExperimentResponse(),
            self.do_roarequest('CreateExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/experiments', 'json', req, runtime)
        )

    def delete_service(self, service_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    def delete_service_with_options(self, service_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteServiceResponse(),
            self.do_roarequest('DeleteService', '2021-02-02', 'HTTPS', 'DELETE', 'AK', '/api/v1/services/%s' % TeaConverter.to_unicode(service_id), 'json', req, runtime)
        )

    def get_experiment_status(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_status_with_options(experiment_id, headers, runtime)

    def get_experiment_status_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentStatusResponse(),
            self.do_roarequest('GetExperimentStatus', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s/status' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def get_experiment_folder_children(self, folder_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_folder_children_with_options(folder_id, request, headers, runtime)

    def get_experiment_folder_children_with_options(self, folder_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.only_folder):
            query['OnlyFolder'] = request.only_folder
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentFolderChildrenResponse(),
            self.do_roarequest('GetExperimentFolderChildren', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experimentfolders/%s/children' % TeaConverter.to_unicode(folder_id), 'json', req, runtime)
        )

    def list_auth_roles(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_auth_roles_with_options(request, headers, runtime)

    def list_auth_roles_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.is_generate_token):
            query['IsGenerateToken'] = request.is_generate_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListAuthRolesResponse(),
            self.do_roarequest('ListAuthRoles', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/authorization/roles', 'json', req, runtime)
        )

    def get_node_input_schema(self, experiment_id, node_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_input_schema_with_options(experiment_id, node_id, request, headers, runtime)

    def get_node_input_schema_with_options(self, experiment_id, node_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_id):
            query['InputId'] = request.input_id
        if not UtilClient.is_unset(request.input_index):
            query['InputIndex'] = request.input_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeInputSchemaResponse(),
            self.do_roarequest('GetNodeInputSchema', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s/nodes/%s/schema' % (TeaConverter.to_unicode(experiment_id), TeaConverter.to_unicode(node_id)), 'json', req, runtime)
        )

    def list_algo_defs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_algo_defs_with_options(request, headers, runtime)

    def list_algo_defs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListAlgoDefsResponse(),
            self.do_roarequest('ListAlgoDefs', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/algo/detail', 'json', req, runtime)
        )

    def add_image_labels(self, image_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_labels_with_options(image_id, request, headers, runtime)

    def add_image_labels_with_options(self, image_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.AddImageLabelsResponse(),
            self.do_roarequest('AddImageLabels', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/images/%s/labels' % TeaConverter.to_unicode(image_id), 'json', req, runtime)
        )

    def list_experiments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    def list_experiments_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListExperimentsResponse(),
            self.do_roarequest('ListExperiments', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments', 'json', req, runtime)
        )

    def get_algorithm_tree(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_tree_with_options(request, headers, runtime)

    def get_algorithm_tree_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmTreeResponse(),
            self.do_roarequest('GetAlgorithmTree', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/algorithm/tree', 'json', req, runtime)
        )

    def create_experiment_folder(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_folder_with_options(request, headers, runtime)

    def create_experiment_folder_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateExperimentFolderResponse(),
            self.do_roarequest('CreateExperimentFolder', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/experimentfolders', 'json', req, runtime)
        )

    def get_job(self, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(job_id, request, headers, runtime)

    def get_job_with_options(self, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetJobResponse(),
            self.do_roarequest('GetJob', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/jobs/%s' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
        )

    def get_experiment_meta(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_meta_with_options(experiment_id, headers, runtime)

    def get_experiment_meta_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentMetaResponse(),
            self.do_roarequest('GetExperimentMeta', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s/meta' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def list_node_outputs(self, experiment_id, node_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_outputs_with_options(experiment_id, node_id, headers, runtime)

    def list_node_outputs_with_options(self, experiment_id, node_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListNodeOutputsResponse(),
            self.do_roarequest('ListNodeOutputs', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s/nodes/%s/outputs' % (TeaConverter.to_unicode(experiment_id), TeaConverter.to_unicode(node_id)), 'json', req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    def list_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.list):
            query['List'] = request.list
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListTemplatesResponse(),
            self.do_roarequest('ListTemplates', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/templates', 'json', req, runtime)
        )

    def update_experiment_meta(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_meta_with_options(experiment_id, request, headers, runtime)

    def update_experiment_meta_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentMetaResponse(),
            self.do_roarequest('UpdateExperimentMeta', '2021-02-02', 'HTTPS', 'PUT', 'AK', '/api/v1/experiments/%s/meta' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def list_images(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    def list_images_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListImagesResponse(),
            self.do_roarequest('ListImages', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/images', 'json', req, runtime)
        )

    def get_algorithm_defs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_defs_with_options(request, headers, runtime)

    def get_algorithm_defs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmDefsResponse(),
            self.do_roarequest('GetAlgorithmDefs', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/algorithm/defs', 'json', req, runtime)
        )

    def delete_experiment_folder(self, folder_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_folder_with_options(folder_id, headers, runtime)

    def delete_experiment_folder_with_options(self, folder_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteExperimentFolderResponse(),
            self.do_roarequest('DeleteExperimentFolder', '2021-02-02', 'HTTPS', 'DELETE', 'AK', '/api/v1/experimentfolders/%s' % TeaConverter.to_unicode(folder_id), 'json', req, runtime)
        )

    def list_image_labels(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_image_labels_with_options(request, headers, runtime)

    def list_image_labels_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListImageLabelsResponse(),
            self.do_roarequest('ListImageLabels', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/image/labels', 'json', req, runtime)
        )

    def get_algo_tree(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algo_tree_with_options(request, headers, runtime)

    def get_algo_tree_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgoTreeResponse(),
            self.do_roarequest('GetAlgoTree', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/algo/tree', 'json', req, runtime)
        )

    def get_experiment(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, headers, runtime)

    def get_experiment_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentResponse(),
            self.do_roarequest('GetExperiment', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def copy_experiment(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copy_experiment_with_options(experiment_id, request, headers, runtime)

    def copy_experiment_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CopyExperimentResponse(),
            self.do_roarequest('CopyExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/experiments/[ExperimentId]/copy', 'json', req, runtime)
        )

    def stop_job(self, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(job_id, headers, runtime)

    def stop_job_with_options(self, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.StopJobResponse(),
            self.do_roarequest('StopJob', '2021-02-02', 'HTTPS', 'PUT', 'AK', '/api/v1/jobs/%s/stop' % TeaConverter.to_unicode(job_id), 'json', req, runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    def create_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.execute_type):
            body['ExecuteType'] = request.execute_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateJobResponse(),
            self.do_roarequest('CreateJob', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/jobs', 'json', req, runtime)
        )

    def get_node_visualization(self, experiment_id, node_id, visualization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_visualization_with_options(experiment_id, node_id, visualization_id, request, headers, runtime)

    def get_node_visualization_with_options(self, experiment_id, node_id, visualization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeVisualizationResponse(),
            self.do_roarequest('GetNodeVisualization', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s/nodes/%s/visualizations/%s' % (TeaConverter.to_unicode(experiment_id), TeaConverter.to_unicode(node_id), TeaConverter.to_unicode(visualization_id)), 'json', req, runtime)
        )

    def get_node_output(self, experiment_id, node_id, output_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_output_with_options(experiment_id, node_id, output_id, request, headers, runtime)

    def get_node_output_with_options(self, experiment_id, node_id, output_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_index):
            query['OutputIndex'] = request.output_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeOutputResponse(),
            self.do_roarequest('GetNodeOutput', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/experiments/%s/nodes/%s/outputs/%s' % (TeaConverter.to_unicode(experiment_id), TeaConverter.to_unicode(node_id), TeaConverter.to_unicode(output_id)), 'json', req, runtime)
        )

    def remove_image_labels(self, image_id, label_key):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_image_labels_with_options(image_id, label_key, headers, runtime)

    def remove_image_labels_with_options(self, image_id, label_key, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.RemoveImageLabelsResponse(),
            self.do_roarequest('RemoveImageLabels', '2021-02-02', 'HTTPS', 'DELETE', 'AK', '/api/v1/images/%s/labels/%s' % (TeaConverter.to_unicode(image_id), TeaConverter.to_unicode(label_key)), 'json', req, runtime)
        )

    def preview_mctable(self, table_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.preview_mctable_with_options(table_name, request, headers, runtime)

    def preview_mctable_with_options(self, table_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.PreviewMCTableResponse(),
            self.do_roarequest('PreviewMCTable', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/datasources/maxcompute/tables/%s/preview' % TeaConverter.to_unicode(table_name), 'json', req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    def list_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListServicesResponse(),
            self.do_roarequest('ListServices', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/services', 'json', req, runtime)
        )

    def remove_image(self, image_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_image_with_options(image_id, headers, runtime)

    def remove_image_with_options(self, image_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.RemoveImageResponse(),
            self.do_roarequest('RemoveImage', '2021-02-02', 'HTTPS', 'DELETE', 'AK', '/api/v1/images/%s' % TeaConverter.to_unicode(image_id), 'json', req, runtime)
        )

    def stop_experiment(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_experiment_with_options(experiment_id, headers, runtime)

    def stop_experiment_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.StopExperimentResponse(),
            self.do_roarequest('StopExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/experiments/%s/stop' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def add_image(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_with_options(request, headers, runtime)

    def add_image_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.AddImageResponse(),
            self.do_roarequest('AddImage', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/images', 'json', req, runtime)
        )

    def search_mctables(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_mctables_with_options(request, headers, runtime)

    def search_mctables_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.SearchMCTablesResponse(),
            self.do_roarequest('SearchMCTables', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/datasources/maxcompute/tables', 'json', req, runtime)
        )

    def get_template(self, template_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(template_id, headers, runtime)

    def get_template_with_options(self, template_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetTemplateResponse(),
            self.do_roarequest('GetTemplate', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/templates/%s' % TeaConverter.to_unicode(template_id), 'json', req, runtime)
        )

    def delete_experiment(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, headers, runtime)

    def delete_experiment_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteExperimentResponse(),
            self.do_roarequest('DeleteExperiment', '2021-02-02', 'HTTPS', 'DELETE', 'AK', '/api/v1/experiments/%s' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    def create_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateServiceResponse(),
            self.do_roarequest('CreateService', '2021-02-02', 'HTTPS', 'POST', 'AK', '/api/v1/services', 'json', req, runtime)
        )

    def update_experiment_folder(self, folder_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_folder_with_options(folder_id, request, headers, runtime)

    def update_experiment_folder_with_options(self, folder_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentFolderResponse(),
            self.do_roarequest('UpdateExperimentFolder', '2021-02-02', 'HTTPS', 'PUT', 'AK', '/api/v1/experimentfolders/%s' % TeaConverter.to_unicode(folder_id), 'json', req, runtime)
        )

    def get_mctable_schema(self, table_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mctable_schema_with_options(table_name, request, headers, runtime)

    def get_mctable_schema_with_options(self, table_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetMCTableSchemaResponse(),
            self.do_roarequest('GetMCTableSchema', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/datasources/maxcompute/tables/%s/schema' % TeaConverter.to_unicode(table_name), 'json', req, runtime)
        )

    def update_experiment_content(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_content_with_options(experiment_id, request, headers, runtime)

    def update_experiment_content_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentContentResponse(),
            self.do_roarequest('UpdateExperimentContent', '2021-02-02', 'HTTPS', 'PUT', 'AK', '/api/v1/experiments/%s/content' % TeaConverter.to_unicode(experiment_id), 'json', req, runtime)
        )

    def get_algorithm_def(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_def_with_options(request, headers, runtime)

    def get_algorithm_def_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmDefResponse(),
            self.do_roarequest('GetAlgorithmDef', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/algorithm/def', 'json', req, runtime)
        )

    def get_image(self, image_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_with_options(image_id, request, headers, runtime)

    def get_image_with_options(self, image_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetImageResponse(),
            self.do_roarequest('GetImage', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/images/%s' % TeaConverter.to_unicode(image_id), 'json', req, runtime)
        )

    def get_service(self, service_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_id, request, headers, runtime)

    def get_service_with_options(self, service_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetServiceResponse(),
            self.do_roarequest('GetService', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/services/%s' % TeaConverter.to_unicode(service_id), 'json', req, runtime)
        )

    def list_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    def list_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListJobsResponse(),
            self.do_roarequest('ListJobs', '2021-02-02', 'HTTPS', 'GET', 'AK', '/api/v1/jobs', 'json', req, runtime)
        )
