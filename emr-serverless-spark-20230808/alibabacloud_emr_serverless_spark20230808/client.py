# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr_serverless_spark20230808 import models as emr_serverless_spark_20230808_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('emr-serverless-spark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_job_run_with_options(self, workspace_id, job_run_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_run_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_job_run(self, workspace_id, job_run_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    def get_job_run_with_options(self, workspace_id, job_run_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_run_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job_run(self, workspace_id, job_run_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    def list_job_runs_with_options(self, workspace_id, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListJobRunsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time):
            request.end_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not UtilClient.is_unset(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not UtilClient.is_unset(request.states_shrink):
            query['states'] = request.states_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobRuns',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobRunsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_job_runs(self, workspace_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_runs_with_options(workspace_id, request, headers, runtime)

    def start_job_run_with_options(self, workspace_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_type):
            body['codeType'] = request.code_type
        if not UtilClient.is_unset(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not UtilClient.is_unset(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not UtilClient.is_unset(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname='/api/v1/workspaces/%s/jobRuns' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workspace_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def start_job_run(self, workspace_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_job_run_with_options(workspace_id, request, headers, runtime)
