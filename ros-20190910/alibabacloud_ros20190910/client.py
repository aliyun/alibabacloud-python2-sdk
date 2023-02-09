# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ros20190910 import models as ros20190910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ros', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_stack_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allowed_stack_operations):
            query['AllowedStackOperations'] = request.allowed_stack_operations
        if not UtilClient.is_unset(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelStackOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CancelStackOperationResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_stack_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_stack_operation_with_options(request, runtime)

    def cancel_update_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelUpdateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CancelUpdateStackResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_update_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    def continue_create_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.recreating_options):
            query['RecreatingOptions'] = request.recreating_options
        if not UtilClient.is_unset(request.recreating_resources):
            query['RecreatingResources'] = request.recreating_resources
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueCreateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ContinueCreateStackResponse(),
            self.call_api(params, req, runtime)
        )

    def continue_create_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    def create_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not UtilClient.is_unset(request.change_set_type):
            query['ChangeSetType'] = request.change_set_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not UtilClient.is_unset(request.resources_to_import):
            query['ResourcesToImport'] = request.resources_to_import
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not UtilClient.is_unset(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not UtilClient.is_unset(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    def create_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_option):
            query['CreateOption'] = request.create_option
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackResponse(),
            self.call_api(params, req, runtime)
        )

    def create_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    def create_stack_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        query = {}
        if not UtilClient.is_unset(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not UtilClient.is_unset(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_group_with_options(request, runtime)

    def create_stack_instances_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def create_template_scratch_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateTemplateScratchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.preference_parameters):
            request.preference_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_resource_group):
            request.source_resource_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not UtilClient.is_unset(tmp_req.source_resources):
            request.source_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not UtilClient.is_unset(tmp_req.source_tag):
            request.source_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not UtilClient.is_unset(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not UtilClient.is_unset(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not UtilClient.is_unset(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template_scratch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_scratch_with_options(request, runtime)

    def delete_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    def delete_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    def delete_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_group_with_options(request, runtime)

    def delete_stack_instances_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.retain_stacks):
            query['RetainStacks'] = request.retain_stacks
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def delete_template_scratch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template_scratch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_scratch_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def detect_stack_drift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackDriftResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_stack_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_drift_with_options(request, runtime)

    def detect_stack_group_drift_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackGroupDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackGroupDriftResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_stack_group_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    def detect_stack_resource_drift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackResourceDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackResourceDriftResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_stack_resource_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    def execute_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ExecuteChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    def generate_template_by_scratch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provision_region_id):
            query['ProvisionRegionId'] = request.provision_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTemplateByScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplateByScratchResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_template_by_scratch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_template_by_scratch_with_options(request, runtime)

    def generate_template_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTemplatePolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_template_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    def get_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_template):
            query['ShowTemplate'] = request.show_template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    def get_feature_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature):
            query['Feature'] = request.feature
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureDetails',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetFeatureDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_feature_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_feature_details_with_options(request, runtime)

    def get_resource_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    def get_resource_type_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTypeTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_type_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    def get_service_provisions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.services):
            query['Services'] = request.services
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetServiceProvisionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_provisions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_provisions_with_options(request, runtime)

    def get_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.log_option):
            query['LogOption'] = request.log_option
        if not UtilClient.is_unset(request.output_option):
            query['OutputOption'] = request.output_option
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_resource_progress):
            query['ShowResourceProgress'] = request.show_resource_progress
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    def get_stack_drift_detection_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drift_detection_id):
            query['DriftDetectionId'] = request.drift_detection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackDriftDetectionStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackDriftDetectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack_drift_detection_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    def get_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_id):
            query['StackGroupId'] = request.stack_group_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    def get_stack_group_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackGroupOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack_group_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    def get_stack_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not UtilClient.is_unset(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackInstance',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    def get_stack_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackPolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    def get_stack_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_attributes):
            query['ResourceAttributes'] = request.resource_attributes
        if not UtilClient.is_unset(request.show_resource_attributes):
            query['ShowResourceAttributes'] = request.show_resource_attributes
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackResource',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.include_permission):
            query['IncludePermission'] = request.include_permission
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_stage):
            query['TemplateStage'] = request.template_stage
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def get_template_estimate_cost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateEstimateCost',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_estimate_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    def get_template_parameter_constraints_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.GetTemplateParameterConstraintsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters_key_filter):
            request.parameters_key_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters_key_filter, 'ParametersKeyFilter', 'json')
        if not UtilClient.is_unset(tmp_req.parameters_order):
            request.parameters_order_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters_order, 'ParametersOrder', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.parameters_key_filter_shrink):
            query['ParametersKeyFilter'] = request.parameters_key_filter_shrink
        if not UtilClient.is_unset(request.parameters_order_shrink):
            query['ParametersOrder'] = request.parameters_order_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateParameterConstraints',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_parameter_constraints(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_parameter_constraints_with_options(request, runtime)

    def get_template_scratch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_data_option):
            query['ShowDataOption'] = request.show_data_option
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_scratch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_scratch_with_options(request, runtime)

    def get_template_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateSummary',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    def list_change_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeSets',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListChangeSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_change_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    def list_resource_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    def list_stack_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackEvents',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    def list_stack_group_operation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroupOperationResults',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_group_operation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    def list_stack_group_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroupOperations',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_group_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    def list_stack_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroups',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    def list_stack_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not UtilClient.is_unset(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    def list_stack_operation_risks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackOperationRisks',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackOperationRisksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_operation_risks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    def list_stack_resource_drifts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_drift_status):
            query['ResourceDriftStatus'] = request.resource_drift_status
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackResourceDrifts',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourceDriftsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_resource_drifts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    def list_stack_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stack_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    def list_stacks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_stack_id):
            query['ParentStackId'] = request.parent_stack_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.show_nested_stack):
            query['ShowNestedStack'] = request.show_nested_stack
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_ids):
            query['StackIds'] = request.stack_ids
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStacks',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStacksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_stacks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

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
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def list_template_scratches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateScratches',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateScratchesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_template_scratches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_template_scratches_with_options(request, runtime)

    def list_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateVersions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_template_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def preview_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.enable_pre_config):
            query['EnablePreConfig'] = request.enable_pre_config
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.PreviewStackResponse(),
            self.call_api(params, req, runtime)
        )

    def preview_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    def set_deletion_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeletionProtection',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_deletion_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    def set_stack_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetStackPolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetStackPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_stack_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    def set_template_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.share_option):
            query['ShareOption'] = request.share_option
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.version_option):
            query['VersionOption'] = request.version_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTemplatePermission',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetTemplatePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_template_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    def signal_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignalResource',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SignalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def signal_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    def stop_stack_group_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStackGroupOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.StopStackGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_stack_group_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

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
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
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
            action='UntagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not UtilClient.is_unset(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not UtilClient.is_unset(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackResponse(),
            self.call_api(params, req, runtime)
        )

    def update_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_with_options(request, runtime)

    def update_stack_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not UtilClient.is_unset(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_group_with_options(request, runtime)

    def update_stack_instances_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    def update_stack_template_by_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackTemplateByResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackTemplateByResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_stack_template_by_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    def update_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    def update_template_scratch_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateTemplateScratchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.preference_parameters):
            request.preference_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_resource_group):
            request.source_resource_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not UtilClient.is_unset(tmp_req.source_resources):
            request.source_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not UtilClient.is_unset(tmp_req.source_tag):
            request.source_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not UtilClient.is_unset(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not UtilClient.is_unset(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not UtilClient.is_unset(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template_scratch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_scratch_with_options(request, runtime)

    def validate_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.validation_option):
            query['ValidationOption'] = request.validation_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ValidateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_template_with_options(request, runtime)
