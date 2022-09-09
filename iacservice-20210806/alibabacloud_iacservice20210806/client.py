# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iacservice20210806 import models as ia_cservice_20210806_models
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
        self._endpoint = self.get_endpoint('iacservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def associate_parameter_set(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_parameter_set_with_options(request, headers, runtime)

    def associate_parameter_set_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameter_set_ids):
            body['parameterSetIds'] = request.parameter_set_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets/operations/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_task_group(self, project_id, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_task_group_with_options(project_id, group_id, request, headers, runtime)

    def associate_task_group_with_options(self, project_id, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateTaskGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/groups/%s/associate' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_rabbitmq_publisher(self, publisher_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_rabbitmq_publisher_with_options(publisher_id, request, headers, runtime)

    def attach_rabbitmq_publisher_with_options(self, publisher_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers/%s/attach' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(publisher_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AttachRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_resource_export_task(self, export_task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_resource_export_task_with_options(export_task_id, request, headers, runtime)

    def cancel_resource_export_task_with_options(self, export_task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/cancel/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def clone_module(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_module_with_options(request, headers, runtime)

    def clone_module_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_source):
            body['moduleSource'] = request.module_source
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/operations/clone',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CloneModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_authorization_with_options(request, headers, runtime)

    def create_authorization_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.uid):
            body['uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAuthorization',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/authorizations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    def create_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job(self, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(task_id, request, headers, runtime)

    def create_job_with_options(self, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s/jobs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_module(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_with_options(request, headers, runtime)

    def create_module_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_module_market(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_market_with_options(request, headers, runtime)

    def create_module_market_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_url):
            body['codeUrl'] = request.code_url
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_detail):
            body['moduleDetail'] = request.module_detail
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleMarket',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/moduleMarkets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleMarketResponse(),
            self.call_api(params, req, runtime)
        )

    def create_module_version(self, module_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_version_with_options(module_id, request, headers, runtime)

    def create_module_version_with_options(self, module_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/%s/versions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_parameter_set(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_parameter_set_with_options(request, headers, runtime)

    def create_parameter_set_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project_build(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_build_with_options(project_id, request, headers, runtime)

    def create_project_build_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_build_action):
            body['projectBuildAction'] = request.project_build_action
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        if not UtilClient.is_unset(request.task_policies):
            body['taskPolicies'] = request.task_policies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectBuild',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/build' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectBuildResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rabbitmq_publisher(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rabbitmq_publisher_with_options(request, headers, runtime)

    def create_rabbitmq_publisher_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exchange_name):
            body['exchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['exchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.host_name):
            body['hostName'] = request.host_name
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['port'] = request.port
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.virtual_host):
            body['virtualHost'] = request.virtual_host
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_export_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_export_task_with_options(request, headers, runtime)

    def create_resource_export_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exclude_rules):
            body['excludeRules'] = request.exclude_rules
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    def create_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_authorization(self, authorization_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_authorization_with_options(authorization_id, headers, runtime)

    def delete_authorization_with_options(self, authorization_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAuthorization',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/authorizations/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(authorization_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(id, headers, runtime)

    def delete_group_with_options(self, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/group/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_module(self, module_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_module_with_options(module_id, headers, runtime)

    def delete_module_with_options(self, module_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_parameter_set(self, parameter_set_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_parameter_set_with_options(parameter_set_id, headers, runtime)

    def delete_parameter_set_with_options(self, parameter_set_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(parameter_set_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(id, headers, runtime)

    def delete_project_with_options(self, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rabbitmq_publisher(self, publisher_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_rabbitmq_publisher_with_options(publisher_id, headers, runtime)

    def delete_rabbitmq_publisher_with_options(self, publisher_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(publisher_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_export_task(self, export_task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_export_task_with_options(export_task_id, headers, runtime)

    def delete_resource_export_task_with_options(self, export_task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_link_with_options(request, headers, runtime)

    def delete_resource_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_type_code):
            query['resourceTypeCode'] = request.resource_type_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceLink',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/resources',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteResourceLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(task_id, headers, runtime)

    def delete_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_rabbitmq_publisher(self, publisher_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detach_rabbitmq_publisher_with_options(publisher_id, request, headers, runtime)

    def detach_rabbitmq_publisher_with_options(self, publisher_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers/%s/detach' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(publisher_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DetachRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_parameter_set(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_parameter_set_with_options(request, headers, runtime)

    def dissociate_parameter_set_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parameter_set_ids):
            body['parameterSetIds'] = request.parameter_set_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets/operations/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_task_group(self, project_id, group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_task_group_with_options(project_id, group_id, request, headers, runtime)

    def dissociate_task_group_with_options(self, project_id, group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateTaskGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/groups/%s/dissociate' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(group_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_resource_export_task(self, export_task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_resource_export_task_with_options(export_task_id, request, headers, runtime)

    def execute_resource_export_task_with_options(self, export_task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/execute/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group(self, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(id, headers, runtime)

    def get_group_with_options(self, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/group/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job(self, task_id, job_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(task_id, job_id, headers, runtime)

    def get_job_with_options(self, task_id, job_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s/jobs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_module(self, module_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_with_options(module_id, headers, runtime)

    def get_module_with_options(self, module_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_module_market(self, module_market_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_market_with_options(module_market_id, headers, runtime)

    def get_module_market_with_options(self, module_market_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleMarket',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/moduleMarkets/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_market_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleMarketResponse(),
            self.call_api(params, req, runtime)
        )

    def get_module_version(self, module_id, module_version):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_version_with_options(module_id, module_version, headers, runtime)

    def get_module_version_with_options(self, module_id, module_version, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/%s/versions/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_version))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_parameter_set(self, parameter_set_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_parameter_set_with_options(parameter_set_id, headers, runtime)

    def get_parameter_set_with_options(self, parameter_set_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetParameterSet',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(parameter_set_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetParameterSetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project(self, id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(id, headers, runtime)

    def get_project_with_options(self, id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_build_config(self, project_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_build_config_with_options(project_id, request, headers, runtime)

    def get_project_build_config_with_options(self, project_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_build_id):
            query['projectBuildId'] = request.project_build_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectBuildConfig',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/buildConfig' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectBuildConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_build_context(self, project_id, project_build_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_build_context_with_options(project_id, project_build_id, headers, runtime)

    def get_project_build_context_with_options(self, project_id, project_build_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectBuildContext',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/build/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_build_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectBuildContextResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_job_summary(self, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_job_summary_with_options(project_id, headers, runtime)

    def get_project_job_summary_with_options(self, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectJobSummary',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/job/statistics' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectJobSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_project_resource_summary(self, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_resource_summary_with_options(project_id, headers, runtime)

    def get_project_resource_summary_with_options(self, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectResourceSummary',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/resource/statistics' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResourceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rabbitmq_publisher(self, publisher_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_rabbitmq_publisher_with_options(publisher_id, headers, runtime)

    def get_rabbitmq_publisher_with_options(self, publisher_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRabbitmqPublisher',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(publisher_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRabbitmqPublisherResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_export_task(self, export_task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_export_task_with_options(export_task_id, request, headers, runtime)

    def get_resource_export_task_with_options(self, export_task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_link_with_options(request, headers, runtime)

    def get_resource_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_type_code):
            query['resourceTypeCode'] = request.resource_type_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceLink',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    def get_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_context(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_context_with_options(task_id, headers, runtime)

    def get_task_context_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskContext',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s/context' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskContextResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authorizations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_authorizations_with_options(request, headers, runtime)

    def list_authorizations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_id):
            query['authorizationId'] = request.authorization_id
        if not UtilClient.is_unset(request.authorization_type):
            query['authorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizations',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/authorizations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListAuthorizationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    def list_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/group',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(task_id, request, headers, runtime)

    def list_jobs_with_options(self, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s/jobs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_module_markets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_module_markets_with_options(request, headers, runtime)

    def list_module_markets_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleMarkets',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/moduleMarkets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleMarketsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_module_version(self, module_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_module_version_with_options(module_id, request, headers, runtime)

    def list_module_version_with_options(self, module_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/%s/versions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_modules(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_modules_with_options(request, headers, runtime)

    def list_modules_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_parameter_set_relation(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parameter_set_relation_with_options(request, headers, runtime)

    def list_parameter_set_relation_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterSetRelation',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets/operations/relation',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListParameterSetRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_parameter_sets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_parameter_sets_with_options(request, headers, runtime)

    def list_parameter_sets_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParameterSets',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListParameterSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    def list_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def list_project_builds(self, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_builds_with_options(project_id, headers, runtime)

    def list_project_builds_with_options(self, project_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectBuilds',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s/build' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectBuildsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_rabbitmq_publishers(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rabbitmq_publishers_with_options(request, headers, runtime)

    def list_rabbitmq_publishers_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRabbitmqPublishers',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRabbitmqPublishersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_relation_modules(self, type):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_relation_modules_with_options(type, headers, runtime)

    def list_relation_modules_with_options(self, type, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRelationModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/relation/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(type)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRelationModulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_relation_tasks(self, type, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_relation_tasks_with_options(type, request, headers, runtime)

    def list_relation_tasks_with_options(self, type, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRelationTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/relation/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(type)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRelationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_export_task_versions(self, export_task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_task_versions_with_options(export_task_id, request, headers, runtime)

    def list_resource_export_task_versions_with_options(self, export_task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/%s/exportVersions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_export_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_tasks_with_options(request, headers, runtime)

    def list_resource_export_tasks_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    def list_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_value):
            query['sourceValue'] = request.source_value
        if not UtilClient.is_unset(request.spec_type):
            query['specType'] = request.spec_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/resources/stateparser',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_task_resource(self, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_resource_with_options(task_id, request, headers, runtime)

    def list_task_resource_with_options(self, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskResource',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s/resources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTaskResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    def list_tasks_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_job(self, task_id, job_id, operation_type, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.operate_job_with_options(task_id, job_id, operation_type, request, headers, runtime)

    def operate_job_with_options(self, task_id, job_id, operation_type, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s/jobs/%s/operation/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(job_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(operation_type))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.OperateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_resource_export_task_version(self, export_task_id, export_version):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_resource_export_task_version_with_options(export_task_id, export_version, headers, runtime)

    def remove_resource_export_task_version_with_options(self, export_task_id, export_version, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveResourceExportTaskVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/%s/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_version))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.RemoveResourceExportTaskVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_authorization_attribute(self, authorization_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_authorization_attribute_with_options(authorization_id, request, headers, runtime)

    def update_authorization_attribute_with_options(self, authorization_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAuthorizationAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/authorizations/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(authorization_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateAuthorizationAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_group(self, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(id, request, headers, runtime)

    def update_group_with_options(self, id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/group/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_module_attribute(self, module_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_module_attribute_with_options(module_id, request, headers, runtime)

    def update_module_attribute_with_options(self, module_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/modules/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_module_market_attribute(self, module_market_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_module_market_attribute_with_options(module_market_id, request, headers, runtime)

    def update_module_market_attribute_with_options(self, module_market_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_detail):
            body['moduleDetail'] = request.module_detail
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleMarketAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/moduleMarkets/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(module_market_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleMarketAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_parameter_set_attribute(self, parameter_set_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_parameter_set_attribute_with_options(parameter_set_id, request, headers, runtime)

    def update_parameter_set_attribute_with_options(self, parameter_set_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateParameterSetAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/parameterSets/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(parameter_set_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateParameterSetAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project(self, id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(id, request, headers, runtime)

    def update_project_with_options(self, id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/project/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rabbitmq_publisher_attribute(self, publisher_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rabbitmq_publisher_attribute_with_options(publisher_id, request, headers, runtime)

    def update_rabbitmq_publisher_attribute_with_options(self, publisher_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exchange_name):
            body['exchangeName'] = request.exchange_name
        if not UtilClient.is_unset(request.exchange_type):
            body['exchangeType'] = request.exchange_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRabbitmqPublisherAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/publishers/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(publisher_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRabbitmqPublisherAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_export_task_attribute(self, export_task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_export_task_attribute_with_options(export_task_id, request, headers, runtime)

    def update_resource_export_task_attribute_with_options(self, export_task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.exclude_rules):
            body['excludeRules'] = request.exclude_rules
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/exportTasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(export_task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_task_attribute(self, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_attribute_with_options(task_id, request, headers, runtime)

    def update_task_attribute_with_options(self, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname='/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )
