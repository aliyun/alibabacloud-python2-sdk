# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_devops_rdc20200303 import models as devops_rdc_20200303_models
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
        self._endpoint = self.get_endpoint('devops-rdc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def insert_pipeline_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.InsertPipelineMemberResponse(),
            self.do_rpcrequest('InsertPipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_pipeline_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_pipeline_member_with_options(request, runtime)

    def list_devops_project_task_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsProjectTaskFlowResponse(),
            self.do_rpcrequest('ListDevopsProjectTaskFlow', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_task_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_task_flow_with_options(request, runtime)

    def get_devops_project_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetDevopsProjectMembersResponse(),
            self.do_rpcrequest('GetDevopsProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_members_with_options(request, runtime)

    def add_codeup_source_to_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.AddCodeupSourceToPipelineResponse(),
            self.do_rpcrequest('AddCodeupSourceToPipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_codeup_source_to_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_codeup_source_to_pipeline_with_options(request, runtime)

    def delete_devops_project_sprint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteDevopsProjectSprintResponse(),
            self.do_rpcrequest('DeleteDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project_sprint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_sprint_with_options(request, runtime)

    def delete_common_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteCommonGroupResponse(),
            self.do_rpcrequest('DeleteCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_common_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_common_group_with_options(request, runtime)

    def list_project_custom_fields_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListProjectCustomFieldsResponse(),
            self.do_rpcrequest('ListProjectCustomFields', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_custom_fields(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_custom_fields_with_options(request, runtime)

    def insert_devops_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.InsertDevopsUserResponse(),
            self.do_rpcrequest('InsertDevopsUser', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_devops_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_devops_user_with_options(request, runtime)

    def update_devops_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdateDevopsProjectResponse(),
            self.do_rpcrequest('UpdateDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devops_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_devops_project_with_options(request, runtime)

    def check_aliyun_account_exists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CheckAliyunAccountExistsResponse(),
            self.do_rpcrequest('CheckAliyunAccountExists', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_aliyun_account_exists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_aliyun_account_exists_with_options(request, runtime)

    def get_pipeline_instance_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineInstanceInfoResponse(),
            self.do_rpcrequest('GetPipelineInstanceInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_info_with_options(request, runtime)

    def batch_insert_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.BatchInsertMembersResponse(),
            self.do_rpcrequest('BatchInsertMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_insert_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_insert_members_with_options(request, runtime)

    def list_service_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListServiceConnectionsResponse(),
            self.do_rpcrequest('ListServiceConnections', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_service_connections_with_options(request, runtime)

    def get_user_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetUserNameResponse(),
            self.do_rpcrequest('GetUserName', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_name_with_options(request, runtime)

    def insert_project_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.InsertProjectMembersResponse(),
            self.do_rpcrequest('InsertProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_project_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_project_members_with_options(request, runtime)

    def list_devops_project_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsProjectTaskListResponse(),
            self.do_rpcrequest('ListDevopsProjectTaskList', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_task_list_with_options(request, runtime)

    def get_task_detail_base_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetTaskDetailBaseResponse(),
            self.do_rpcrequest('GetTaskDetailBase', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_detail_base(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_detail_base_with_options(request, runtime)

    def delete_devops_project_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteDevopsProjectMembersResponse(),
            self.do_rpcrequest('DeleteDevopsProjectMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_members_with_options(request, runtime)

    def create_devops_project_sprint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateDevopsProjectSprintResponse(),
            self.do_rpcrequest('CreateDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_project_sprint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_devops_project_sprint_with_options(request, runtime)

    def update_devops_project_sprint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdateDevopsProjectSprintResponse(),
            self.do_rpcrequest('UpdateDevopsProjectSprint', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devops_project_sprint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_devops_project_sprint_with_options(request, runtime)

    def delete_devops_organization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteDevopsOrganizationResponse(),
            self.do_rpcrequest('DeleteDevopsOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_organization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_organization_with_options(request, runtime)

    def cancel_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CancelPipelineResponse(),
            self.do_rpcrequest('CancelPipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_pipeline_with_options(request, runtime)

    def list_devops_project_task_flow_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsProjectTaskFlowStatusResponse(),
            self.do_rpcrequest('ListDevopsProjectTaskFlowStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_task_flow_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_task_flow_status_with_options(request, runtime)

    def list_user_organization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListUserOrganizationResponse(),
            self.do_rpcrequest('ListUserOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_organization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_organization_with_options(request, runtime)

    def update_pipeline_env_vars_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdatePipelineEnvVarsResponse(),
            self.do_rpcrequest('UpdatePipelineEnvVars', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_pipeline_env_vars(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_env_vars_with_options(request, runtime)

    def delete_devops_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteDevopsProjectResponse(),
            self.do_rpcrequest('DeleteDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_with_options(request, runtime)

    def get_pipeline_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineInstanceStatusResponse(),
            self.do_rpcrequest('GetPipelineInstanceStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_status_with_options(request, runtime)

    def get_pipeline_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineLogResponse(),
            self.do_rpcrequest('GetPipelineLog', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_log_with_options(request, runtime)

    def get_user_by_aliyun_uid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetUserByAliyunUidResponse(),
            self.do_rpcrequest('GetUserByAliyunUid', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_by_aliyun_uid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_aliyun_uid_with_options(request, runtime)

    def update_pipeline_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdatePipelineMemberResponse(),
            self.do_rpcrequest('UpdatePipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_pipeline_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_member_with_options(request, runtime)

    def list_devops_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsProjectsResponse(),
            self.do_rpcrequest('ListDevopsProjects', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_projects_with_options(request, runtime)

    def create_devops_project_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateDevopsProjectTaskResponse(),
            self.do_rpcrequest('CreateDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_project_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_devops_project_task_with_options(request, runtime)

    def get_pipeline_instance_build_number_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineInstanceBuildNumberStatusResponse(),
            self.do_rpcrequest('GetPipelineInstanceBuildNumberStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_build_number_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_build_number_status_with_options(request, runtime)

    def list_devops_project_sprints_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsProjectSprintsResponse(),
            self.do_rpcrequest('ListDevopsProjectSprints', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_sprints(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_sprints_with_options(request, runtime)

    def get_devops_project_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetDevopsProjectInfoResponse(),
            self.do_rpcrequest('GetDevopsProjectInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_info_with_options(request, runtime)

    def delete_pipeline_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeletePipelineMemberResponse(),
            self.do_rpcrequest('DeletePipelineMember', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pipeline_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_pipeline_member_with_options(request, runtime)

    def get_devops_project_sprint_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetDevopsProjectSprintInfoResponse(),
            self.do_rpcrequest('GetDevopsProjectSprintInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_sprint_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_sprint_info_with_options(request, runtime)

    def delete_devops_organization_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteDevopsOrganizationMembersResponse(),
            self.do_rpcrequest('DeleteDevopsOrganizationMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_organization_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_organization_members_with_options(request, runtime)

    def get_last_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetLastWorkspaceResponse(),
            self.do_rpcrequest('GetLastWorkspace', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_last_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_last_workspace_with_options(request, runtime)

    def create_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateCredentialResponse(),
            self.do_rpcrequest('CreateCredential', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_credential_with_options(request, runtime)

    def list_credentials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListCredentialsResponse(),
            self.do_rpcrequest('ListCredentials', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_credentials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_credentials_with_options(request, runtime)

    def create_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreatePipelineResponse(),
            self.do_rpcrequest('CreatePipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_with_options(request, runtime)

    def list_pipelines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListPipelinesResponse(),
            self.do_rpcrequest('ListPipelines', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pipelines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pipelines_with_options(request, runtime)

    def create_pipeline_from_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreatePipelineFromTemplateResponse(),
            self.do_rpcrequest('CreatePipelineFromTemplate', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pipeline_from_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_from_template_with_options(request, runtime)

    def list_smart_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListSmartGroupResponse(),
            self.do_rpcrequest('ListSmartGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_smart_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_smart_group_with_options(request, runtime)

    def transfer_pipeline_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.TransferPipelineOwnerResponse(),
            self.do_rpcrequest('TransferPipelineOwner', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_pipeline_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_pipeline_owner_with_options(request, runtime)

    def create_common_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateCommonGroupResponse(),
            self.do_rpcrequest('CreateCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_common_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_common_group_with_options(request, runtime)

    def create_devops_organization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateDevopsOrganizationResponse(),
            self.do_rpcrequest('CreateDevopsOrganization', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_organization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_devops_organization_with_options(request, runtime)

    def list_devops_scenario_field_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsScenarioFieldConfigResponse(),
            self.do_rpcrequest('ListDevopsScenarioFieldConfig', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_scenario_field_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_scenario_field_config_with_options(request, runtime)

    def list_pipeline_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListPipelineTemplatesResponse(),
            self.do_rpcrequest('ListPipelineTemplates', '2020-03-03', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_pipeline_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pipeline_templates_with_options(request, runtime)

    def update_devops_project_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdateDevopsProjectTaskResponse(),
            self.do_rpcrequest('UpdateDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_devops_project_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_devops_project_task_with_options(request, runtime)

    def get_devops_project_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetDevopsProjectTaskInfoResponse(),
            self.do_rpcrequest('GetDevopsProjectTaskInfo', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_project_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_devops_project_task_info_with_options(request, runtime)

    def get_pipeline_instance_group_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineInstanceGroupStatusResponse(),
            self.do_rpcrequest('GetPipelineInstanceGroupStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_instance_group_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_instance_group_status_with_options(request, runtime)

    def update_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdateTaskDetailResponse(),
            self.do_rpcrequest('UpdateTaskDetail', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_task_detail_with_options(request, runtime)

    def get_task_list_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetTaskListFilterResponse(),
            self.do_rpcrequest('GetTaskListFilter', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_list_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_list_filter_with_options(request, runtime)

    def get_project_option_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetProjectOptionResponse(),
            self.do_rpcrequest('GetProjectOption', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_option(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_project_option_with_options(request, runtime)

    def update_common_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.UpdateCommonGroupResponse(),
            self.do_rpcrequest('UpdateCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_common_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_common_group_with_options(request, runtime)

    def list_common_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListCommonGroupResponse(),
            self.do_rpcrequest('ListCommonGroup', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_common_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_common_group_with_options(request, runtime)

    def delete_devops_project_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.DeleteDevopsProjectTaskResponse(),
            self.do_rpcrequest('DeleteDevopsProjectTask', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_devops_project_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devops_project_task_with_options(request, runtime)

    def get_devops_organization_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetDevopsOrganizationMembersResponse(),
            self.do_rpcrequest('GetDevopsOrganizationMembers', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_devops_organization_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_devops_organization_members_with_options(request, runtime)

    def create_devops_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateDevopsProjectResponse(),
            self.do_rpcrequest('CreateDevopsProject', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_devops_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_devops_project_with_options(request, runtime)

    def get_task_detail_activity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetTaskDetailActivityResponse(),
            self.do_rpcrequest('GetTaskDetailActivity', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_detail_activity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_detail_activity_with_options(request, runtime)

    def execute_pipeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ExecutePipelineResponse(),
            self.do_rpcrequest('ExecutePipeline', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_pipeline_with_options(request, runtime)

    def create_service_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.CreateServiceConnectionResponse(),
            self.do_rpcrequest('CreateServiceConnection', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_connection_with_options(request, runtime)

    def get_pipeline_inst_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineInstHistoryResponse(),
            self.do_rpcrequest('GetPipelineInstHistory', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_inst_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_inst_history_with_options(request, runtime)

    def get_pipeline_step_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipelineStepLogResponse(),
            self.do_rpcrequest('GetPipelineStepLog', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipeline_step_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_step_log_with_options(request, runtime)

    def get_pipleine_latest_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.GetPipleineLatestInstanceStatusResponse(),
            self.do_rpcrequest('GetPipleineLatestInstanceStatus', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pipleine_latest_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pipleine_latest_instance_status_with_options(request, runtime)

    def list_devops_project_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            devops_rdc_20200303_models.ListDevopsProjectTasksResponse(),
            self.do_rpcrequest('ListDevopsProjectTasks', '2020-03-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devops_project_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devops_project_tasks_with_options(request, runtime)
