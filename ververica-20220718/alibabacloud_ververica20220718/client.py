# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ververica20220718 import models as ververica_20220718_models
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
        self._endpoint = self.get_endpoint('ververica', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_deployment(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateDeploymentHeaders()
        return self.create_deployment_with_options(namespace, request, headers, runtime)

    def create_deployment_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_savepoint(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateSavepointHeaders()
        return self.create_savepoint_with_options(namespace, request, headers, runtime)

    def create_savepoint_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deployment_id):
            body['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.native_format):
            body['nativeFormat'] = request.native_format
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/savepoints' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    def create_variable(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.CreateVariableHeaders()
        return self.create_variable_with_options(namespace, request, headers, runtime)

    def create_variable_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/variables' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.CreateVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_deployment(self, namespace, deployment_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteDeploymentHeaders()
        return self.delete_deployment_with_options(namespace, deployment_id, headers, runtime)

    def delete_deployment_with_options(self, namespace, deployment_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deployment_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_job(self, namespace, job_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteJobHeaders()
        return self.delete_job_with_options(namespace, job_id, headers, runtime)

    def delete_job_with_options(self, namespace, job_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/jobs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_savepoint(self, namespace, savepoint_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteSavepointHeaders()
        return self.delete_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    def delete_savepoint_with_options(self, namespace, savepoint_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/savepoints/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(savepoint_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_variable(self, namespace, name):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.DeleteVariableHeaders()
        return self.delete_variable_with_options(namespace, name, headers, runtime)

    def delete_variable_with_options(self, namespace, name, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteVariable',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/variables/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.DeleteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def flink_api_proxy(self, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.FlinkApiProxyHeaders()
        return self.flink_api_proxy_with_options(request, headers, runtime)

    def flink_api_proxy_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flink_api_path):
            query['flinkApiPath'] = request.flink_api_path
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlinkApiProxy',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/flink-ui/v2/proxy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.FlinkApiProxyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_resource_plan_with_flink_conf_async(self, namespace, deployment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncHeaders()
        return self.generate_resource_plan_with_flink_conf_async_with_options(namespace, deployment_id, request, headers, runtime)

    def generate_resource_plan_with_flink_conf_async_with_options(self, namespace, deployment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GenerateResourcePlanWithFlinkConfAsync',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments/%s/resource-plan%%3AasyncGenerate' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deployment_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GenerateResourcePlanWithFlinkConfAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    def get_deployment(self, namespace, deployment_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetDeploymentHeaders()
        return self.get_deployment_with_options(namespace, deployment_id, headers, runtime)

    def get_deployment_with_options(self, namespace, deployment_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deployment_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_generate_resource_plan_result(self, namespace, ticket_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetGenerateResourcePlanResultHeaders()
        return self.get_generate_resource_plan_result_with_options(namespace, ticket_id, headers, runtime)

    def get_generate_resource_plan_result_with_options(self, namespace, ticket_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGenerateResourcePlanResult',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments/tickets/%s/resource-plan%%3AasyncGenerate' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(ticket_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetGenerateResourcePlanResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job(self, namespace, job_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetJobHeaders()
        return self.get_job_with_options(namespace, job_id, headers, runtime)

    def get_job_with_options(self, namespace, job_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/jobs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_savepoint(self, namespace, savepoint_id):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.GetSavepointHeaders()
        return self.get_savepoint_with_options(namespace, savepoint_id, headers, runtime)

    def get_savepoint_with_options(self, namespace, savepoint_id, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetSavepoint',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/savepoints/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(savepoint_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.GetSavepointResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deployment_targets(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentTargetsHeaders()
        return self.list_deployment_targets_with_options(namespace, request, headers, runtime)

    def list_deployment_targets_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentTargets',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployment-targets' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deployments(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListDeploymentsHeaders()
        return self.list_deployments_with_options(namespace, request, headers, runtime)

    def list_deployments_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployments',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_engine_version_metadata(self):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListEngineVersionMetadataHeaders()
        return self.list_engine_version_metadata_with_options(headers, runtime)

    def list_engine_version_metadata_with_options(self, headers, runtime):
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListEngineVersionMetadata',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/engine-version-meta.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListEngineVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListJobsHeaders()
        return self.list_jobs_with_options(namespace, request, headers, runtime)

    def list_jobs_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/jobs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_savepoints(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListSavepointsHeaders()
        return self.list_savepoints_with_options(namespace, request, headers, runtime)

    def list_savepoints_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['deploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavepoints',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/savepoints' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListSavepointsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_variables(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.ListVariablesHeaders()
        return self.list_variables_with_options(namespace, request, headers, runtime)

    def list_variables_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['pageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariables',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/variables' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.ListVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    def start_job(self, namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StartJobHeaders()
        return self.start_job_with_options(namespace, request, headers, runtime)

    def start_job_with_options(self, namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='StartJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/jobs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StartJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_job(self, namespace, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.StopJobHeaders()
        return self.stop_job_with_options(namespace, job_id, request, headers, runtime)

    def stop_job_with_options(self, namespace, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='StopJob',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/jobs/%s%%3Astop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.StopJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_deployment(self, namespace, deployment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = ververica_20220718_models.UpdateDeploymentHeaders()
        return self.update_deployment_with_options(namespace, deployment_id, request, headers, runtime)

    def update_deployment_with_options(self, namespace, deployment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.workspace):
            real_headers['workspace'] = UtilClient.to_jsonstring(headers.workspace)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateDeployment',
            version='2022-07-18',
            protocol='HTTPS',
            pathname='/api/v2/namespaces/%s/deployments/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(namespace)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deployment_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ververica_20220718_models.UpdateDeploymentResponse(),
            self.call_api(params, req, runtime)
        )
