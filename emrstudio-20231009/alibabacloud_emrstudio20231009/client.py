# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emrstudio20231009 import models as emr_studio_20231009_models
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
        self._endpoint = self.get_endpoint('emrstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_manual_task_with_options(self, project_id, manual_task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManualTask',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/manualTasks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(manual_task_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeManualTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_manual_task(self, project_id, manual_task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_manual_task_with_options(project_id, manual_task_id, request, headers, runtime)

    def describe_manual_task_instance_with_options(self, manual_task_instance_id, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManualTaskInstance',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/manualTaskInstances/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(manual_task_instance_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeManualTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_manual_task_instance(self, manual_task_instance_id, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_manual_task_instance_with_options(manual_task_instance_id, project_id, request, headers, runtime)

    def describe_project_with_options(self, code, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProject',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(code)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_project(self, code, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_project_with_options(code, request, headers, runtime)

    def describe_task_with_options(self, workflow_id, project_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/workflows/%s/tasks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task(self, workflow_id, project_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_with_options(workflow_id, project_id, task_id, request, headers, runtime)

    def describe_task_instance_with_options(self, project_id, workflow_instance_id, task_instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskInstance',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/workflows/%s/taskInstances/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_instance_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task_instance(self, project_id, workflow_instance_id, task_instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_instance_with_options(project_id, workflow_instance_id, task_instance_id, request, headers, runtime)

    def describe_workflow_with_options(self, project_id, workflow_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflow',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/processDefinitions/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_workflow(self, project_id, workflow_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflow_with_options(project_id, workflow_id, request, headers, runtime)

    def describe_workflow_instance_with_options(self, project_id, workflow_instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflowInstance',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/processInstances/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(workflow_instance_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_workflow_instance(self, project_id, workflow_instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflow_instance_with_options(project_id, workflow_instance_id, request, headers, runtime)

    def list_manual_task_instances_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_status):
            query['executionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTaskInstances',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/manualTaskInstances' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListManualTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_manual_task_instances(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_manual_task_instances_with_options(project_id, request, headers, runtime)

    def list_manual_tasks_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTasks',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/manualTasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListManualTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_manual_tasks(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_manual_tasks_with_options(project_id, request, headers, runtime)

    def list_projects_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_projects(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    def list_task_instances_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_status):
            query['executionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['workflowInstanceId'] = request.workflow_instance_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskInstances',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/taskInstances' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_task_instances(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_instances_with_options(project_id, request, headers, runtime)

    def list_tasks_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/tasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(project_id, request, headers, runtime)

    def list_workflow_instances_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowInstances',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/processInstances' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workflow_instances(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflow_instances_with_options(project_id, request, headers, runtime)

    def list_workflows_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflows',
            version='2023-10-09',
            protocol='HTTPS',
            pathname='/dolphinscheduler/v3/projects/%s/processDefinitions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workflows(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflows_with_options(project_id, request, headers, runtime)
