# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops20210625 import models as devops_20210625_models
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
        self._endpoint = self.get_endpoint('devops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def retry_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def retry_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            self.do_roarequest('RetryPipelineJobRun', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id), TeaConverter.to_unicode(pipeline_run_id), TeaConverter.to_unicode(job_id)), 'json', req, runtime)
        )

    def list_resource_members(self, organization_id, resource_type, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_members_with_options(organization_id, resource_type, resource_id, headers, runtime)

    def list_resource_members_with_options(self, organization_id, resource_type, resource_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            self.do_roarequest('ListResourceMembers', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/%s/%s/members' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(resource_type), TeaConverter.to_unicode(resource_id)), 'json', req, runtime)
        )

    def get_host_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_group_with_options(organization_id, id, headers, runtime)

    def get_host_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            self.do_roarequest('GetHostGroup', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/hostGroups/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(id)), 'json', req, runtime)
        )

    def get_variable_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_variable_group_with_options(organization_id, id, headers, runtime)

    def get_variable_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            self.do_roarequest('GetVariableGroup', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/variableGroups/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(id)), 'json', req, runtime)
        )

    def list_pipelines(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(organization_id, request, headers, runtime)

    def list_pipelines_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            self.do_roarequest('ListPipelines', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/pipelines' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def update_resource_member(self, organization_id, resource_type, resource_id, account_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_member_with_options(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    def update_resource_member_with_options(self, organization_id, resource_type, resource_id, account_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            self.do_roarequest_with_form('UpdateResourceMember', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/%s/%s/members/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(resource_type), TeaConverter.to_unicode(resource_id), TeaConverter.to_unicode(account_id)), 'json', req, runtime)
        )

    def update_variable_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_variable_group_with_options(organization_id, id, request, headers, runtime)

    def update_variable_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            self.do_roarequest_with_form('UpdateVariableGroup', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/variableGroups/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(id)), 'json', req, runtime)
        )

    def delete_resource_member(self, organization_id, resource_type, resource_id, account_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_member_with_options(organization_id, resource_type, resource_id, account_id, headers, runtime)

    def delete_resource_member_with_options(self, organization_id, resource_type, resource_id, account_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            self.do_roarequest('DeleteResourceMember', '2021-06-25', 'HTTPS', 'DELETE', 'AK', '/organization/%s/%s/%s/members/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(resource_type), TeaConverter.to_unicode(resource_id), TeaConverter.to_unicode(account_id)), 'json', req, runtime)
        )

    def list_host_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_host_groups_with_options(organization_id, request, headers, runtime)

    def list_host_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            self.do_roarequest('ListHostGroups', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/hostGroups' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def reset_ssh_key(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_ssh_key_with_options(organization_id, headers, runtime)

    def reset_ssh_key_with_options(self, organization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            self.do_roarequest('ResetSshKey', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/sshKey' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def create_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    def create_workspace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            self.do_roarequest_with_form('CreateWorkspace', '2021-06-25', 'HTTPS', 'POST', 'AK', '/api/workspaces', 'json', req, runtime)
        )

    def list_service_connections(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_connections_with_options(organization_id, request, headers, runtime)

    def list_service_connections_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            self.do_roarequest('ListServiceConnections', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/serviceConnections' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def create_host_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_host_group_with_options(organization_id, request, headers, runtime)

    def create_host_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            self.do_roarequest_with_form('CreateHostGroup', '2021-06-25', 'HTTPS', 'POST', 'AK', '/organization/%s/hostGroups' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def stop_pipeline_run(self, organization_id, pipeline_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def stop_pipeline_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            self.do_roarequest('StopPipelineRun', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/pipelines/%s/pipelineRuns/%s/stop' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id), TeaConverter.to_unicode(pipeline_run_id)), 'json', req, runtime)
        )

    def update_host_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_host_group_with_options(organization_id, id, request, headers, runtime)

    def update_host_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            self.do_roarequest_with_form('UpdateHostGroup', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/hostGroups/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(id)), 'json', req, runtime)
        )

    def create_resource_member(self, organization_id, resource_type, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_member_with_options(organization_id, resource_type, resource_id, request, headers, runtime)

    def create_resource_member_with_options(self, organization_id, resource_type, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            self.do_roarequest_with_form('CreateResourceMember', '2021-06-25', 'HTTPS', 'POST', 'AK', '/organization/%s/%s/%s/members' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(resource_type), TeaConverter.to_unicode(resource_id)), 'json', req, runtime)
        )

    def skip_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def skip_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            self.do_roarequest('SkipPipelineJobRun', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s/skip' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id), TeaConverter.to_unicode(pipeline_run_id), TeaConverter.to_unicode(job_id)), 'json', req, runtime)
        )

    def stop_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def stop_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            self.do_roarequest('StopPipelineJobRun', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/organization/%s/pipelines/%s/pipelineRuns/%s/jobs/%s/stop' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id), TeaConverter.to_unicode(pipeline_run_id), TeaConverter.to_unicode(job_id)), 'json', req, runtime)
        )

    def start_pipeline_run(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(organization_id, pipeline_id, request, headers, runtime)

    def start_pipeline_run_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            self.do_roarequest_with_form('StartPipelineRun', '2021-06-25', 'HTTPS', 'POST', 'AK', '/organizations/%s/pipelines/%s/run' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id)), 'json', req, runtime)
        )

    def list_workspaces(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    def list_workspaces_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = devops_20210625_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        if not UtilClient.is_unset(tmp_req.workspace_template_list):
            request.workspace_template_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_template_list, 'workspaceTemplateList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            self.do_roarequest('ListWorkspaces', '2021-06-25', 'HTTPS', 'GET', 'AK', '/api/workspaces', 'json', req, runtime)
        )

    def get_pipeline_run(self, organization_id, pipeline_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def get_pipeline_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            self.do_roarequest('GetPipelineRun', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/pipelines/%s/pipelineRuns/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id), TeaConverter.to_unicode(pipeline_run_id)), 'json', req, runtime)
        )

    def get_pipeline(self, organization_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    def get_pipeline_with_options(self, organization_id, pipeline_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            self.do_roarequest('GetPipeline', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/pipelines/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id)), 'json', req, runtime)
        )

    def create_variable_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_variable_group_with_options(organization_id, request, headers, runtime)

    def create_variable_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            self.do_roarequest_with_form('CreateVariableGroup', '2021-06-25', 'HTTPS', 'POST', 'AK', '/organization/%s/variableGroups' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def delete_variable_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_variable_group_with_options(organization_id, id, headers, runtime)

    def delete_variable_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            self.do_roarequest('DeleteVariableGroup', '2021-06-25', 'HTTPS', 'DELETE', 'AK', '/organization/%s/variableGroups/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(id)), 'json', req, runtime)
        )

    def get_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    def get_workspace_with_options(self, workspace_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            self.do_roarequest('GetWorkspace', '2021-06-25', 'HTTPS', 'GET', 'AK', '/api/workspaces/%s' % TeaConverter.to_unicode(workspace_id), 'json', req, runtime)
        )

    def create_ssh_key(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(organization_id, headers, runtime)

    def create_ssh_key_with_options(self, organization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            self.do_roarequest('CreateSshKey', '2021-06-25', 'HTTPS', 'POST', 'AK', '/organization/%s/sshKey' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def delete_host_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_host_group_with_options(organization_id, id, headers, runtime)

    def delete_host_group_with_options(self, organization_id, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            self.do_roarequest('DeleteHostGroup', '2021-06-25', 'HTTPS', 'DELETE', 'AK', '/organization/%s/hostGroups/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(id)), 'json', req, runtime)
        )

    def release_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_workspace_with_options(workspace_id, headers, runtime)

    def release_workspace_with_options(self, workspace_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            self.do_roarequest('ReleaseWorkspace', '2021-06-25', 'HTTPS', 'DELETE', 'AK', '/api/workspaces/%s/release' % TeaConverter.to_unicode(workspace_id), 'json', req, runtime)
        )

    def list_variable_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_variable_groups_with_options(organization_id, request, headers, runtime)

    def list_variable_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            self.do_roarequest('ListVariableGroups', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/variableGroups' % TeaConverter.to_unicode(organization_id), 'json', req, runtime)
        )

    def delete_pipeline(self, organization_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    def delete_pipeline_with_options(self, organization_id, pipeline_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            self.do_roarequest('DeletePipeline', '2021-06-25', 'HTTPS', 'DELETE', 'AK', '/organization/%s/pipelines/%s' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id)), 'json', req, runtime)
        )

    def frozen_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.frozen_workspace_with_options(workspace_id, headers, runtime)

    def frozen_workspace_with_options(self, workspace_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            self.do_roarequest('FrozenWorkspace', '2021-06-25', 'HTTPS', 'PUT', 'AK', '/api/workspaces/%s/frozen' % TeaConverter.to_unicode(workspace_id), 'json', req, runtime)
        )

    def list_pipeline_runs(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_runs_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            self.do_roarequest('ListPipelineRuns', '2021-06-25', 'HTTPS', 'GET', 'AK', '/organization/%s/pipelines/%s/pipelineRuns' % (TeaConverter.to_unicode(organization_id), TeaConverter.to_unicode(pipeline_id)), 'json', req, runtime)
        )
