# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

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

    def create_host_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_host_group_with_options(organization_id, request, headers, runtime)

    def create_host_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_member(self, organization_id, resource_type, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_member_with_options(organization_id, resource_type, resource_id, request, headers, runtime)

    def create_resource_member_with_options(self, organization_id, resource_type, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/{resourceType}/{resourceId}/members' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ssh_key(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ssh_key_with_options(organization_id, headers, runtime)

    def create_ssh_key_with_options(self, organization_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sshKey' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_variable_group(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_variable_group_with_options(organization_id, request, headers, runtime)

    def create_variable_group_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    def create_workspace_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.code_version):
            body['codeVersion'] = request.code_version
        if not UtilClient.is_unset(request.file_path):
            body['filePath'] = request.file_path
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.request_from):
            body['requestFrom'] = request.request_from
        if not UtilClient.is_unset(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not UtilClient.is_unset(request.reuse):
            body['reuse'] = request.reuse
        if not UtilClient.is_unset(request.workspace_template):
            body['workspaceTemplate'] = request.workspace_template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_host_group_with_options(organization_id, id, headers, runtime)

    def delete_host_group_with_options(self, organization_id, id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups/{id}' % TeaConverter.to_unicode(organization_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipeline(self, organization_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    def delete_pipeline_with_options(self, organization_id, pipeline_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}' % TeaConverter.to_unicode(organization_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_member(self, organization_id, resource_type, resource_id, account_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_member_with_options(organization_id, resource_type, resource_id, account_id, headers, runtime)

    def delete_resource_member_with_options(self, organization_id, resource_type, resource_id, account_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/{resourceType}/{resourceId}/members/{accountId}' % TeaConverter.to_unicode(organization_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_variable_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_variable_group_with_options(organization_id, id, headers, runtime)

    def delete_variable_group_with_options(self, organization_id, id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups/{id}' % TeaConverter.to_unicode(organization_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.DeleteVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def frozen_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.frozen_workspace_with_options(workspace_id, headers, runtime)

    def frozen_workspace_with_options(self, workspace_id, headers, runtime):
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FrozenWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces/%s/frozen' % TeaConverter.to_unicode(workspace_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.FrozenWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_host_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_host_group_with_options(organization_id, id, headers, runtime)

    def get_host_group_with_options(self, organization_id, id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups/{id}' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_organization_member(self, organization_id, account_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_organization_member_with_options(organization_id, account_id, headers, runtime)

    def get_organization_member_with_options(self, organization_id, account_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrganizationMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/members/{accountId}' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline(self, organization_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(organization_id, pipeline_id, headers, runtime)

    def get_pipeline_with_options(self, organization_id, pipeline_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_run(self, organization_id, pipeline_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def get_pipeline_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    def get_vmdeploy_order(self, organization_id, pipeline_id, deploy_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def get_vmdeploy_order_with_options(self, organization_id, pipeline_id, deploy_order_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/deploy/{deployOrderId}' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_variable_group(self, organization_id, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_variable_group_with_options(organization_id, id, headers, runtime)

    def get_variable_group_with_options(self, organization_id, id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups/{id}' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_id, headers, runtime)

    def get_workspace_with_options(self, workspace_id, headers, runtime):
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces/%s' % TeaConverter.to_unicode(workspace_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_host_groups_with_options(organization_id, request, headers, runtime)

    def list_host_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_organization_members(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_organization_members_with_options(organization_id, request, headers, runtime)

    def list_organization_members_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.extern_uid):
            query['externUid'] = request.extern_uid
        if not UtilClient.is_unset(request.join_time_from):
            query['joinTimeFrom'] = request.join_time_from
        if not UtilClient.is_unset(request.join_time_to):
            query['joinTimeTo'] = request.join_time_to
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.organization_member_name):
            query['organizationMemberName'] = request.organization_member_name
        if not UtilClient.is_unset(request.provider):
            query['provider'] = request.provider
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/members' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_runs(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_runs_with_options(organization_id, pipeline_id, request, headers, runtime)

    def list_pipeline_runs_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.trigger_mode):
            query['triggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineRuns',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelineRunsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipelines(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(organization_id, request, headers, runtime)

    def list_pipelines_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.creator_account_ids):
            query['creatorAccountIds'] = request.creator_account_ids
        if not UtilClient.is_unset(request.execute_account_ids):
            query['executeAccountIds'] = request.execute_account_ids
        if not UtilClient.is_unset(request.execute_end_time):
            query['executeEndTime'] = request.execute_end_time
        if not UtilClient.is_unset(request.execute_start_time):
            query['executeStartTime'] = request.execute_start_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.pipeline_name):
            query['pipelineName'] = request.pipeline_name
        if not UtilClient.is_unset(request.status_list):
            query['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_members(self, organization_id, resource_type, resource_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_members_with_options(organization_id, resource_type, resource_id, headers, runtime)

    def list_resource_members_with_options(self, organization_id, resource_type, resource_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceMembers',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/{resourceType}/{resourceId}/members' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListResourceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_connections(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_connections_with_options(organization_id, request, headers, runtime)

    def list_service_connections_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.serice_connection_type):
            query['sericeConnectionType'] = request.serice_connection_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceConnections',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/serviceConnections' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListServiceConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_variable_groups(self, organization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_variable_groups_with_options(organization_id, request, headers, runtime)

    def list_variable_groups_with_options(self, organization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_order):
            query['pageOrder'] = request.page_order
        if not UtilClient.is_unset(request.page_sort):
            query['pageSort'] = request.page_sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVariableGroups',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListVariableGroupsResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.workspace_template_list_shrink):
            query['workspaceTemplateList'] = request.workspace_template_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def log_pipeline_job_run(self, organization_id, pipeline_id, job_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_pipeline_job_run_with_options(organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime)

    def log_pipeline_job_run_with_options(self, organization_id, pipeline_id, job_id, pipeline_run_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipeline/{pipelineId}/pipelineRun/{pipelineRunId}/job/{jobId}/logs' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def log_vmdeploy_machine(self, organization_id, pipeline_id, deploy_order_id, machine_sn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def log_vmdeploy_machine_with_options(self, organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='LogVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/deploy/{deployOrderId}/machine/{machineSn}/log' % TeaConverter.to_unicode(organization_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.LogVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def pass_pipeline_validate(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pass_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def pass_pipeline_validate_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PassPipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}/jobs/{jobId}/pass' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.PassPipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    def refuse_pipeline_validate(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refuse_pipeline_validate_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def refuse_pipeline_validate_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RefusePipelineValidate',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}/jobs/{jobId}/refuse' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RefusePipelineValidateResponse(),
            self.call_api(params, req, runtime)
        )

    def release_workspace(self, workspace_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_workspace_with_options(workspace_id, headers, runtime)

    def release_workspace_with_options(self, workspace_id, headers, runtime):
        workspace_id = OpenApiUtilClient.get_encode_param(workspace_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseWorkspace',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/api/workspaces/%s/release' % TeaConverter.to_unicode(workspace_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ReleaseWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_ssh_key(self, organization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_ssh_key_with_options(organization_id, headers, runtime)

    def reset_ssh_key_with_options(self, organization_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResetSshKey',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/sshKey' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResetSshKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_vmdeploy_order(self, organization_id, pipeline_id, deploy_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def resume_vmdeploy_order_with_options(self, organization_id, pipeline_id, deploy_order_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/deploy/{deployOrderId}/resume' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.ResumeVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def retry_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}/jobs/{jobId}' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_vmdeploy_machine(self, organization_id, pipeline_id, deploy_order_id, machine_sn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def retry_vmdeploy_machine_with_options(self, organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/deploy/{deployOrderId}/machine/{machineSn}/retry' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.RetryVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def skip_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}/jobs/{jobId}/skip' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def skip_vmdeploy_machine(self, organization_id, pipeline_id, deploy_order_id, machine_sn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.skip_vmdeploy_machine_with_options(organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime)

    def skip_vmdeploy_machine_with_options(self, organization_id, pipeline_id, deploy_order_id, machine_sn, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        machine_sn = OpenApiUtilClient.get_encode_param(machine_sn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SkipVMDeployMachine',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/deploy/{deployOrderId}/machine/{machineSn}/skip' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.SkipVMDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def start_pipeline_run(self, organization_id, pipeline_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_run_with_options(organization_id, pipeline_id, request, headers, runtime)

    def start_pipeline_run_with_options(self, organization_id, pipeline_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organizations/%s/pipelines/{pipelineId}/run' % TeaConverter.to_unicode(organization_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StartPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_pipeline_job_run(self, organization_id, pipeline_id, pipeline_run_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_job_run_with_options(organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime)

    def stop_pipeline_job_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, job_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineJobRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}/jobs/{jobId}/stop' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_pipeline_run(self, organization_id, pipeline_id, pipeline_run_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipeline_run_with_options(organization_id, pipeline_id, pipeline_run_id, headers, runtime)

    def stop_pipeline_run_with_options(self, organization_id, pipeline_id, pipeline_run_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        pipeline_run_id = OpenApiUtilClient.get_encode_param(pipeline_run_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopPipelineRun',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/pipelineRuns/{pipelineRunId}/stop' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopPipelineRunResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_vmdeploy_order(self, organization_id, pipeline_id, deploy_order_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_vmdeploy_order_with_options(organization_id, pipeline_id, deploy_order_id, headers, runtime)

    def stop_vmdeploy_order_with_options(self, organization_id, pipeline_id, deploy_order_id, headers, runtime):
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        deploy_order_id = OpenApiUtilClient.get_encode_param(deploy_order_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopVMDeployOrder',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/pipelines/{pipelineId}/deploy/{deployOrderId}/stop' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.StopVMDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_host_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_host_group_with_options(organization_id, id, request, headers, runtime)

    def update_host_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        body = {}
        if not UtilClient.is_unset(request.aliyun_region):
            body['aliyunRegion'] = request.aliyun_region
        if not UtilClient.is_unset(request.ecs_label_key):
            body['ecsLabelKey'] = request.ecs_label_key
        if not UtilClient.is_unset(request.ecs_label_value):
            body['ecsLabelValue'] = request.ecs_label_value
        if not UtilClient.is_unset(request.ecs_type):
            body['ecsType'] = request.ecs_type
        if not UtilClient.is_unset(request.env_id):
            body['envId'] = request.env_id
        if not UtilClient.is_unset(request.machine_infos):
            body['machineInfos'] = request.machine_infos
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.service_connection_id):
            body['serviceConnectionId'] = request.service_connection_id
        if not UtilClient.is_unset(request.tag_ids):
            body['tagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateHostGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/hostGroups/{id}' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_member(self, organization_id, resource_type, resource_id, account_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_member_with_options(organization_id, resource_type, resource_id, account_id, request, headers, runtime)

    def update_resource_member_with_options(self, organization_id, resource_type, resource_id, account_id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        resource_type = OpenApiUtilClient.get_encode_param(resource_type)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        account_id = OpenApiUtilClient.get_encode_param(account_id)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceMember',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/{resourceType}/{resourceId}/members/{accountId}' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateResourceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def update_variable_group(self, organization_id, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_variable_group_with_options(organization_id, id, request, headers, runtime)

    def update_variable_group_with_options(self, organization_id, id, request, headers, runtime):
        UtilClient.validate_model(request)
        organization_id = OpenApiUtilClient.get_encode_param(organization_id)
        id = OpenApiUtilClient.get_encode_param(id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVariableGroup',
            version='2021-06-25',
            protocol='HTTPS',
            pathname='/organization/%s/variableGroups/{id}' % TeaConverter.to_unicode(organization_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            devops_20210625_models.UpdateVariableGroupResponse(),
            self.call_api(params, req, runtime)
        )
