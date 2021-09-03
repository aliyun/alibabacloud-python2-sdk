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

    def cancel_update_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.CancelUpdateStackResponse(),
            self.do_rpcrequest('CancelUpdateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_update_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    def continue_create_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ContinueCreateStackResponse(),
            self.do_rpcrequest('ContinueCreateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continue_create_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    def create_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.CreateChangeSetResponse(),
            self.do_rpcrequest('CreateChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    def create_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackResponse(),
            self.do_rpcrequest('CreateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    def create_stack_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.auto_deployment), 'AutoDeployment', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackGroupResponse(),
            self.do_rpcrequest('CreateStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.deployment_targets), 'DeploymentTargets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackInstancesResponse(),
            self.do_rpcrequest('CreateStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateResponse(),
            self.do_rpcrequest('CreateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def delete_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteChangeSetResponse(),
            self.do_rpcrequest('DeleteChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    def delete_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackResponse(),
            self.do_rpcrequest('DeleteStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    def delete_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackGroupResponse(),
            self.do_rpcrequest('DeleteStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.deployment_targets), 'DeploymentTargets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackInstancesResponse(),
            self.do_rpcrequest('DeleteStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateResponse(),
            self.do_rpcrequest('DeleteTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def detect_stack_drift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackDriftResponse(),
            self.do_rpcrequest('DetectStackDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackGroupDriftResponse(),
            self.do_rpcrequest('DetectStackGroupDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_stack_group_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    def detect_stack_resource_drift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackResourceDriftResponse(),
            self.do_rpcrequest('DetectStackResourceDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_stack_resource_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    def execute_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ExecuteChangeSetResponse(),
            self.do_rpcrequest('ExecuteChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    def generate_template_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplatePolicyResponse(),
            self.do_rpcrequest('GenerateTemplatePolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_template_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    def get_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetChangeSetResponse(),
            self.do_rpcrequest('GetChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    def get_resource_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeResponse(),
            self.do_rpcrequest('GetResourceType', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    def get_resource_type_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeTemplateResponse(),
            self.do_rpcrequest('GetResourceTypeTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_type_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    def get_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResponse(),
            self.do_rpcrequest('GetStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    def get_stack_drift_detection_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackDriftDetectionStatusResponse(),
            self.do_rpcrequest('GetStackDriftDetectionStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_drift_detection_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    def get_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupResponse(),
            self.do_rpcrequest('GetStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    def get_stack_group_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupOperationResponse(),
            self.do_rpcrequest('GetStackGroupOperation', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_group_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    def get_stack_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackInstanceResponse(),
            self.do_rpcrequest('GetStackInstance', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    def get_stack_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackPolicyResponse(),
            self.do_rpcrequest('GetStackPolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    def get_stack_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResourceResponse(),
            self.do_rpcrequest('GetStackResource', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def get_template_estimate_cost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateEstimateCostResponse(),
            self.do_rpcrequest('GetTemplateEstimateCost', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template_estimate_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    def get_template_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateSummaryResponse(),
            self.do_rpcrequest('GetTemplateSummary', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    def list_change_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListChangeSetsResponse(),
            self.do_rpcrequest('ListChangeSets', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_change_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    def list_resource_types_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypesResponse(),
            self.do_rpcrequest('ListResourceTypes', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_types(self):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(runtime)

    def list_stack_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackEventsResponse(),
            self.do_rpcrequest('ListStackEvents', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    def list_stack_group_operation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationResultsResponse(),
            self.do_rpcrequest('ListStackGroupOperationResults', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_group_operation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    def list_stack_group_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationsResponse(),
            self.do_rpcrequest('ListStackGroupOperations', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_group_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    def list_stack_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupsResponse(),
            self.do_rpcrequest('ListStackGroups', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    def list_stack_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackInstancesResponse(),
            self.do_rpcrequest('ListStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    def list_stack_operation_risks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackOperationRisksResponse(),
            self.do_rpcrequest('ListStackOperationRisks', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_operation_risks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    def list_stack_resource_drifts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourceDriftsResponse(),
            self.do_rpcrequest('ListStackResourceDrifts', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_resource_drifts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    def list_stack_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourcesResponse(),
            self.do_rpcrequest('ListStackResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    def list_stacks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListStacksResponse(),
            self.do_rpcrequest('ListStacks', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stacks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplatesResponse(),
            self.do_rpcrequest('ListTemplates', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def list_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateVersionsResponse(),
            self.do_rpcrequest('ListTemplateVersions', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_template_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def preview_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.PreviewStackResponse(),
            self.do_rpcrequest('PreviewStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preview_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    def set_deletion_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.SetDeletionProtectionResponse(),
            self.do_rpcrequest('SetDeletionProtection', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_deletion_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    def set_stack_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.SetStackPolicyResponse(),
            self.do_rpcrequest('SetStackPolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_stack_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    def set_template_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.SetTemplatePermissionResponse(),
            self.do_rpcrequest('SetTemplatePermission', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_template_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    def signal_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.SignalResourceResponse(),
            self.do_rpcrequest('SignalResource', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def signal_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    def stop_stack_group_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.StopStackGroupOperationResponse(),
            self.do_rpcrequest('StopStackGroupOperation', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_stack_group_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackResponse(),
            self.do_rpcrequest('UpdateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.auto_deployment), 'AutoDeployment', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.deployment_targets), 'DeploymentTargets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackGroupResponse(),
            self.do_rpcrequest('UpdateStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.deployment_targets), 'DeploymentTargets', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackInstancesResponse(),
            self.do_rpcrequest('UpdateStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    def update_stack_template_by_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackTemplateByResourcesResponse(),
            self.do_rpcrequest('UpdateStackTemplateByResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stack_template_by_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    def update_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateResponse(),
            self.do_rpcrequest('UpdateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    def validate_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ros20190910_models.ValidateTemplateResponse(),
            self.do_rpcrequest('ValidateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_template_with_options(request, runtime)
