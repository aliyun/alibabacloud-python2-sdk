# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gemp20210413 import models as gemp20210413_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('gemp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_problem_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProblemServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/addServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.AddProblemServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_problem_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_problem_service_group_with_options(request, headers, runtime)

    def billing_statistics_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BillingStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/charging/details',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.BillingStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def billing_statistics(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.billing_statistics_with_options(headers, runtime)

    def cancel_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cancel_reason):
            body['cancelReason'] = request.cancel_reason
        if not UtilClient.is_unset(request.cancel_reason_description):
            body['cancelReasonDescription'] = request.cancel_reason_description
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CancelProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_problem_with_options(request, headers, runtime)

    def check_webhook_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.webhook):
            body['webhook'] = request.webhook
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/check/webhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CheckWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def check_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_webhook_with_options(request, headers, runtime)

    def confirm_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/confirm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ConfirmIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_integration_config_with_options(request, headers, runtime)

    def create_escalation_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_description):
            body['escalationPlanDescription'] = request.escalation_plan_description
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.escalation_plan_rules):
            body['escalationPlanRules'] = request.escalation_plan_rules
        if not UtilClient.is_unset(request.escalation_plan_scope_objects):
            body['escalationPlanScopeObjects'] = request.escalation_plan_scope_objects
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_escalation_plan_with_options(request, headers, runtime)

    def create_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_user_id):
            body['assignUserId'] = request.assign_user_id
        if not UtilClient.is_unset(request.channels):
            body['channels'] = request.channels
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_description):
            body['incidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/manualSave',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_incident_with_options(request, headers, runtime)

    def create_incident_subtotal_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIncidentSubtotal',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/save/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentSubtotalResponse(),
            self.call_api(params, req, runtime)
        )

    def create_incident_subtotal(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_incident_subtotal_with_options(request, headers, runtime)

    def create_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_integration_config_with_options(request, headers, runtime)

    def create_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.affect_service_ids):
            body['affectServiceIds'] = request.affect_service_ids
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.discover_time):
            body['discoverTime'] = request.discover_time
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.preliminary_reason):
            body['preliminaryReason'] = request.preliminary_reason
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_name):
            body['problemName'] = request.problem_name
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.problem_status):
            body['problemStatus'] = request.problem_status
        if not UtilClient.is_unset(request.progress_summary):
            body['progressSummary'] = request.progress_summary
        if not UtilClient.is_unset(request.progress_summary_rich_text_id):
            body['progressSummaryRichTextId'] = request.progress_summary_rich_text_id
        if not UtilClient.is_unset(request.recovery_time):
            body['recoveryTime'] = request.recovery_time
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_with_options(request, headers, runtime)

    def create_problem_effection_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/effectionService/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_effection_service_with_options(request, headers, runtime)

    def create_problem_measure_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_standard):
            body['checkStandard'] = request.check_standard
        if not UtilClient.is_unset(request.check_user_id):
            body['checkUserId'] = request.check_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.director_id):
            body['directorId'] = request.director_id
        if not UtilClient.is_unset(request.plan_finish_time):
            body['planFinishTime'] = request.plan_finish_time
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.stalker_id):
            body['stalkerId'] = request.stalker_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/improvement/measure/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    def create_problem_measure(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_measure_with_options(request, headers, runtime)

    def create_problem_subtotal_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemSubtotal',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/save/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemSubtotalResponse(),
            self.call_api(params, req, runtime)
        )

    def create_problem_subtotal(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_subtotal_with_options(request, headers, runtime)

    def create_problem_timeline_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.key_node):
            body['keyNode'] = request.key_node
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.time):
            body['time'] = request.time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/timeline/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_problem_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_timeline_with_options(request, headers, runtime)

    def create_problem_timelines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.timeline_nodes):
            body['timelineNodes'] = request.timeline_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/timeline/batchCreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_problem_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_timelines_with_options(request, headers, runtime)

    def create_rich_text_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text):
            body['richText'] = request.rich_text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/rich/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateRichTextResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rich_text(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rich_text_with_options(request, headers, runtime)

    def create_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.child_rule_relation):
            body['childRuleRelation'] = request.child_rule_relation
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.convergence_fields):
            body['convergenceFields'] = request.convergence_fields
        if not UtilClient.is_unset(request.convergence_type):
            body['convergenceType'] = request.convergence_type
        if not UtilClient.is_unset(request.coverage_problem_levels):
            body['coverageProblemLevels'] = request.coverage_problem_levels
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.enable_status):
            body['enableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
        if not UtilClient.is_unset(request.problem_effection_services):
            body['problemEffectionServices'] = request.problem_effection_services
        if not UtilClient.is_unset(request.problem_level_group):
            body['problemLevelGroup'] = request.problem_level_group
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.route_child_rules):
            body['routeChildRules'] = request.route_child_rules
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.time_window):
            body['timeWindow'] = request.time_window
        if not UtilClient.is_unset(request.time_window_unit):
            body['timeWindowUnit'] = request.time_window_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_route_rule_with_options(request, headers, runtime)

    def create_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_description):
            body['serviceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    def create_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
        if not UtilClient.is_unset(request.monitor_source_templates):
            body['monitorSourceTemplates'] = request.monitor_source_templates
        if not UtilClient.is_unset(request.service_group_description):
            body['serviceGroupDescription'] = request.service_group_description
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.webhook_link):
            body['webhookLink'] = request.webhook_link
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/insert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_group_with_options(request, headers, runtime)

    def create_service_group_scheduling_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_group_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_group_scheduling_with_options(request, headers, runtime)

    def create_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.expired_type):
            body['expiredType'] = request.expired_type
        if not UtilClient.is_unset(request.notify_object_list):
            body['notifyObjectList'] = request.notify_object_list
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.notify_strategy_list):
            body['notifyStrategyList'] = request.notify_strategy_list
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object_list):
            body['scopeObjectList'] = request.scope_object_list
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_subscription_with_options(request, headers, runtime)

    def create_tenant_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantApplication',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/mobileApp/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateTenantApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tenant_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tenant_application_with_options(request, headers, runtime)

    def create_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    def delete_escalation_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_escalation_plan_with_options(request, headers, runtime)

    def delete_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_incident_with_options(request, headers, runtime)

    def delete_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_integration_config_with_options(request, headers, runtime)

    def delete_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_with_options(request, headers, runtime)

    def delete_problem_effection_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/effectionService/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_effection_service_with_options(request, headers, runtime)

    def delete_problem_measure_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.measure_id):
            body['measureId'] = request.measure_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/improvement/measure/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_problem_measure(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_measure_with_options(request, headers, runtime)

    def delete_problem_timeline_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_timeline_id):
            body['problemTimelineId'] = request.problem_timeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/timeline/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_problem_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_timeline_with_options(request, headers, runtime)

    def delete_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_route_rule_with_options(request, headers, runtime)

    def delete_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(request, headers, runtime)

    def delete_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_with_options(request, headers, runtime)

    def delete_service_group_scheduling_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_group_scheduling(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_scheduling_with_options(headers, runtime)

    def delete_service_group_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_user_id):
            body['newUserId'] = request.new_user_id
        if not UtilClient.is_unset(request.old_user_id):
            body['oldUserId'] = request.old_user_id
        if not UtilClient.is_unset(request.remove_user):
            body['removeUser'] = request.remove_user
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroupUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/deleteServiceGroupUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_group_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_user_with_options(request, headers, runtime)

    def delete_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_subscription_with_options(request, headers, runtime)

    def delete_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

    def deliver_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_user_id):
            body['assignUserId'] = request.assign_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeliverIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/deliver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeliverIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def deliver_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deliver_incident_with_options(request, headers, runtime)

    def disable_escalation_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_escalation_plan_with_options(request, headers, runtime)

    def disable_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_integration_config_with_options(request, headers, runtime)

    def disable_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_route_rule_with_options(request, headers, runtime)

    def disable_service_group_webhook_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableServiceGroupWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/disableWebhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableServiceGroupWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_service_group_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_service_group_webhook_with_options(request, headers, runtime)

    def disable_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/doDisable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_subscription_with_options(request, headers, runtime)

    def enable_escalation_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_escalation_plan_with_options(request, headers, runtime)

    def enable_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_integration_config_with_options(request, headers, runtime)

    def enable_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_route_rule_with_options(request, headers, runtime)

    def enable_service_group_webhook_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableServiceGroupWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/enableWebhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableServiceGroupWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_service_group_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_service_group_webhook_with_options(request, headers, runtime)

    def enable_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_subscription_with_options(request, headers, runtime)

    def finish_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_finish_reason):
            body['incidentFinishReason'] = request.incident_finish_reason
        if not UtilClient.is_unset(request.incident_finish_reason_description):
            body['incidentFinishReasonDescription'] = request.incident_finish_reason_description
        if not UtilClient.is_unset(request.incident_finish_solution):
            body['incidentFinishSolution'] = request.incident_finish_solution
        if not UtilClient.is_unset(request.incident_finish_solution_description):
            body['incidentFinishSolutionDescription'] = request.incident_finish_solution_description
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/finish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.FinishIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def finish_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_incident_with_options(request, headers, runtime)

    def finish_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/finish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.FinishProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def finish_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_problem_with_options(request, headers, runtime)

    def generate_picture_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GeneratePictureLink',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/rich/oss/getPictureLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GeneratePictureLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_picture_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_picture_link_with_options(request, headers, runtime)

    def generate_picture_upload_sign_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GeneratePictureUploadSign',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/rich/oss/generatePostPolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GeneratePictureUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_picture_upload_sign(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_picture_upload_sign_with_options(request, headers, runtime)

    def generate_problem_picture_link_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProblemPictureLink',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/oss/getPresignedLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_problem_picture_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_problem_picture_link_with_options(request, headers, runtime)

    def generate_problem_picture_upload_sign_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            body['fileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_type):
            body['fileType'] = request.file_type
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProblemPictureUploadSign',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/oss/generatePostPolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_problem_picture_upload_sign(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_problem_picture_upload_sign_with_options(request, headers, runtime)

    def get_escalation_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def get_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_escalation_plan_with_options(request, headers, runtime)

    def get_event_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvent',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/events/getLastTimeEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEventResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_event_with_options(request, headers, runtime)

    def get_home_page_guidance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHomePageGuidance',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/guidance/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetHomePageGuidanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_home_page_guidance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_home_page_guidance_with_options(request, headers, runtime)

    def get_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_with_options(request, headers, runtime)

    def get_incident_list_by_id_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id_list):
            body['incidentIdList'] = request.incident_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentListByIdList',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/getIncidentListByIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentListByIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_incident_list_by_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_list_by_id_list_with_options(request, headers, runtime)

    def get_incident_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_incident_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_statistics_with_options(request, headers, runtime)

    def get_incident_subtotal_count_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentSubtotalCount',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/subtotal/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentSubtotalCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_incident_subtotal_count(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_subtotal_count_with_options(request, headers, runtime)

    def get_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_integration_config_with_options(request, headers, runtime)

    def get_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def get_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_with_options(request, headers, runtime)

    def get_problem_effection_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/effectionService/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_effection_service_with_options(request, headers, runtime)

    def get_problem_improvement_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemImprovement',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/improvement/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemImprovementResponse(),
            self.call_api(params, req, runtime)
        )

    def get_problem_improvement(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_improvement_with_options(request, headers, runtime)

    def get_problem_preview_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect_service_ids):
            body['effectServiceIds'] = request.effect_service_ids
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemPreview',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/preview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_problem_preview(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_preview_with_options(request, headers, runtime)

    def get_resource_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourceStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/config/resource/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetResourceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_statistics_with_options(request, headers, runtime)

    def get_rich_text_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text_id):
            body['richTextId'] = request.rich_text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/rich/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetRichTextResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rich_text(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_rich_text_with_options(request, headers, runtime)

    def get_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_route_rule_with_options(request, headers, runtime)

    def get_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(request, headers, runtime)

    def get_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_with_options(request, headers, runtime)

    def get_service_group_person_scheduling_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupPersonScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/user/getScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupPersonSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_group_person_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_person_scheduling_with_options(request, headers, runtime)

    def get_service_group_scheduling_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_group_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_scheduling_with_options(request, headers, runtime)

    def get_service_group_scheduling_preview_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupSchedulingPreview',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/preview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_group_scheduling_preview(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_scheduling_preview_with_options(request, headers, runtime)

    def get_service_group_special_person_scheduling_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupSpecialPersonScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/getUserScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_group_special_person_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_special_person_scheduling_with_options(request, headers, runtime)

    def get_similar_incident_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.events):
            body['events'] = request.events
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSimilarIncidentStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/similarIncident/statistics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSimilarIncidentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_similar_incident_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similar_incident_statistics_with_options(request, headers, runtime)

    def get_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.not_filter_scope_object_deleted):
            body['notFilterScopeObjectDeleted'] = request.not_filter_scope_object_deleted
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subscription_with_options(request, headers, runtime)

    def get_tenant_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTenantApplication',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/mobileApp/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tenant_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_application_with_options(request, headers, runtime)

    def get_tenant_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_ram_id):
            body['tenantRamId'] = request.tenant_ram_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTenantStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/tenant/getTenantStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tenant_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_status_with_options(request, headers, runtime)

    def get_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/getUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    def get_user_guide_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGuideStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/guide/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserGuideStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_guide_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_guide_status_with_options(request, headers, runtime)

    def list_alerts_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_level):
            body['alertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_name):
            body['alertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_source_name):
            body['alertSourceName'] = request.alert_source_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/alerts/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alerts(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alerts_with_options(request, headers, runtime)

    def list_by_monitor_source_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListByMonitorSourceId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/listByMonitorSourceId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListByMonitorSourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_by_monitor_source_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_by_monitor_source_id_with_options(request, headers, runtime)

    def list_chart_data_for_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChartDataForServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/statistics/chartDataForServiceGroup/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chart_data_for_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chart_data_for_service_group_with_options(request, headers, runtime)

    def list_chart_data_for_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChartDataForUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/statistics/chartDataForUser/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chart_data_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chart_data_for_user_with_options(request, headers, runtime)

    def list_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/config/all',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(request, headers, runtime)

    def list_data_report_for_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReportForServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/statistics/listDataReportForServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_report_for_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_report_for_service_group_with_options(request, headers, runtime)

    def list_data_report_for_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReportForUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/statistics/listDataReportForUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_report_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_report_for_user_with_options(request, headers, runtime)

    def list_dictionaries_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDictionaries',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/dict/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDictionariesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dictionaries(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dictionaries_with_options(request, headers, runtime)

    def list_escalation_plan_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlanServices',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlanServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_escalation_plan_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plan_services_with_options(request, headers, runtime)

    def list_escalation_plans_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlans',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def list_escalation_plans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plans_with_options(request, headers, runtime)

    def list_escalation_plans_by_notice_object_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notice_object_id):
            body['noticeObjectId'] = request.notice_object_id
        if not UtilClient.is_unset(request.notice_object_type):
            body['noticeObjectType'] = request.notice_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlansByNoticeObject',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/listByNoticeObject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansByNoticeObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def list_escalation_plans_by_notice_object(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plans_by_notice_object_with_options(request, headers, runtime)

    def list_incident_detail_escalation_plans_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentDetailEscalationPlans',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/detail/escalation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailEscalationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def list_incident_detail_escalation_plans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_detail_escalation_plans_with_options(request, headers, runtime)

    def list_incident_detail_timelines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id_sort):
            body['idSort'] = request.id_sort
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentDetailTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/detail/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_incident_detail_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_detail_timelines_with_options(request, headers, runtime)

    def list_incident_subtotals_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentSubtotals',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/list/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentSubtotalsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_incident_subtotals(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_subtotals_with_options(request, headers, runtime)

    def list_incident_timelines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_incident_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_timelines_with_options(request, headers, runtime)

    def list_incidents_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_status):
            body['incidentStatus'] = request.incident_status
        if not UtilClient.is_unset(request.me):
            body['me'] = request.me
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.relation_service_id):
            body['relationServiceId'] = request.relation_service_id
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidents',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_incidents(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incidents_with_options(request, headers, runtime)

    def list_integration_config_timelines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntegrationConfigTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_integration_config_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_config_timelines_with_options(request, headers, runtime)

    def list_integration_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.monitor_source_name):
            body['monitorSourceName'] = request.monitor_source_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntegrationConfigs',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_integration_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_configs_with_options(request, headers, runtime)

    def list_monitor_sources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMonitorSources',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/monitorSource/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListMonitorSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_monitor_sources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_monitor_sources_with_options(request, headers, runtime)

    def list_problem_detail_operations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time_sort):
            body['createTimeSort'] = request.create_time_sort
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemDetailOperations',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/detail/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemDetailOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_problem_detail_operations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_detail_operations_with_options(request, headers, runtime)

    def list_problem_operations_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemOperations',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_problem_operations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_operations_with_options(request, headers, runtime)

    def list_problem_subtotals_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemSubtotals',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/list/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemSubtotalsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_problem_subtotals(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_subtotals_with_options(request, headers, runtime)

    def list_problem_time_lines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemTimeLines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/detail/timeLines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemTimeLinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_problem_time_lines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_time_lines_with_options(request, headers, runtime)

    def list_problems_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.affect_service_id):
            body['affectServiceId'] = request.affect_service_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.discovery_end_time):
            body['discoveryEndTime'] = request.discovery_end_time
        if not UtilClient.is_unset(request.discovery_start_time):
            body['discoveryStartTime'] = request.discovery_start_time
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_status):
            body['problemStatus'] = request.problem_status
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.repeater_id):
            body['repeaterId'] = request.repeater_id
        if not UtilClient.is_unset(request.restore_end_time):
            body['restoreEndTime'] = request.restore_end_time
        if not UtilClient.is_unset(request.restore_start_time):
            body['restoreStartTime'] = request.restore_start_time
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblems',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/listProblems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_problems(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problems_with_options(request, headers, runtime)

    def list_route_rules_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.not_filter_route_rule_deleted):
            body['notFilterRouteRuleDeleted'] = request.not_filter_route_rule_deleted
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRouteRules',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_route_rules(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_with_options(request, headers, runtime)

    def list_route_rules_by_assign_who_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_who_id):
            body['assignWhoId'] = request.assign_who_id
        if not UtilClient.is_unset(request.assign_who_type):
            body['assignWhoType'] = request.assign_who_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRouteRulesByAssignWhoId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/listByAssignWhoId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesByAssignWhoIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_route_rules_by_assign_who_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_by_assign_who_id_with_options(request, headers, runtime)

    def list_route_rules_by_service_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRouteRulesByService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/listByService',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesByServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_route_rules_by_service(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_by_service_with_options(headers, runtime)

    def list_service_group_monitor_source_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceGroupMonitorSourceTemplates',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/listServiceGroupMonitorSourceTemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_group_monitor_source_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_group_monitor_source_templates_with_options(request, headers, runtime)

    def list_service_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.is_scheduled):
            body['isScheduled'] = request.is_scheduled
        if not UtilClient.is_unset(request.order_by_schedule_status):
            body['orderByScheduleStatus'] = request.order_by_schedule_status
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_name):
            body['queryName'] = request.query_name
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_groups_with_options(request, headers, runtime)

    def list_service_groups_by_user_id_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceGroupsByUserId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/listByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_groups_by_user_id(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_groups_by_user_id_with_options(headers, runtime)

    def list_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    def list_source_events_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_row_key):
            body['startRowKey'] = request.start_row_key
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_row_key):
            body['stopRowKey'] = request.stop_row_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSourceEvents',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/events/listOriginalEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_source_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_source_events_with_options(request, headers, runtime)

    def list_source_events_for_monitor_source_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSourceEventsForMonitorSource',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/events/queryLastestEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsForMonitorSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_source_events_for_monitor_source(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_source_events_for_monitor_source_with_options(request, headers, runtime)

    def list_subscription_service_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubscriptionServiceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/serviceGroup/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subscription_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subscription_service_groups_with_options(request, headers, runtime)

    def list_subscriptions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.not_filter_scope_object_deleted):
            body['notFilterScopeObjectDeleted'] = request.not_filter_scope_object_deleted
        if not UtilClient.is_unset(request.notify_object):
            body['notifyObject'] = request.notify_object
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object):
            body['scopeObject'] = request.scope_object
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubscriptions',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subscriptions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subscriptions_with_options(request, headers, runtime)

    def list_trend_for_source_event_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.time_unit):
            body['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrendForSourceEvent',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/events/querySourceEventTrend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListTrendForSourceEventResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trend_for_source_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_trend_for_source_event_with_options(request, headers, runtime)

    def list_user_serivce_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserSerivceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/preview/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListUserSerivceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_serivce_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_serivce_groups_with_options(request, headers, runtime)

    def list_users_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.synergy_channel):
            body['synergyChannel'] = request.synergy_channel
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    def push_monitor_with_options(self, api_key, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PushMonitor',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/api/monitor/push/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(api_key)),
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.PushMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def push_monitor(self, api_key, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_monitor_with_options(api_key, request, headers, runtime)

    def recover_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.recovery_time):
            body['recoveryTime'] = request.recovery_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/recovery',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RecoverProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def recover_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_problem_with_options(request, headers, runtime)

    def refresh_integration_config_key_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshIntegrationConfigKey',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/refreshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RefreshIntegrationConfigKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_integration_config_key(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_integration_config_key_with_options(request, headers, runtime)

    def remove_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RemoveIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_integration_config_with_options(request, headers, runtime)

    def remove_problem_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveProblemServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/removeServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RemoveProblemServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_problem_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_problem_service_group_with_options(request, headers, runtime)

    def replay_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.replay_duty_user_id):
            body['replayDutyUserId'] = request.replay_duty_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReplayProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/replay',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ReplayProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def replay_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.replay_problem_with_options(request, headers, runtime)

    def respond_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RespondIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RespondIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def respond_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.respond_incident_with_options(request, headers, runtime)

    def revoke_problem_recovery_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeProblemRecovery',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RevokeProblemRecoveryResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_problem_recovery(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_problem_recovery_with_options(request, headers, runtime)

    def unbind_user_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/unbind',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UnbindUserResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_user(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_user_with_options(headers, runtime)

    def update_escalation_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_description):
            body['escalationPlanDescription'] = request.escalation_plan_description
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.escalation_plan_rules):
            body['escalationPlanRules'] = request.escalation_plan_rules
        if not UtilClient.is_unset(request.escalation_plan_scope_objects):
            body['escalationPlanScopeObjects'] = request.escalation_plan_scope_objects
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/escalationPlan/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_escalation_plan_with_options(request, headers, runtime)

    def update_incident_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/incident/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_incident_with_options(request, headers, runtime)

    def update_integration_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/integrationConfig/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_integration_config_with_options(request, headers, runtime)

    def update_problem_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['feedback'] = request.feedback
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.preliminary_reason):
            body['preliminaryReason'] = request.preliminary_reason
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_name):
            body['problemName'] = request.problem_name
        if not UtilClient.is_unset(request.progress_summary):
            body['progressSummary'] = request.progress_summary
        if not UtilClient.is_unset(request.progress_summary_rich_text_id):
            body['progressSummaryRichTextId'] = request.progress_summary_rich_text_id
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_with_options(request, headers, runtime)

    def update_problem_effection_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.pic_url):
            body['picUrl'] = request.pic_url
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/effectionService/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_effection_service_with_options(request, headers, runtime)

    def update_problem_improvement_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_problem_reason):
            body['customProblemReason'] = request.custom_problem_reason
        if not UtilClient.is_unset(request.discover_source):
            body['discoverSource'] = request.discover_source
        if not UtilClient.is_unset(request.duty_department_id):
            body['dutyDepartmentId'] = request.duty_department_id
        if not UtilClient.is_unset(request.duty_department_name):
            body['dutyDepartmentName'] = request.duty_department_name
        if not UtilClient.is_unset(request.duty_user_id):
            body['dutyUserId'] = request.duty_user_id
        if not UtilClient.is_unset(request.injection_mode):
            body['injectionMode'] = request.injection_mode
        if not UtilClient.is_unset(request.monitor_source_name):
            body['monitorSourceName'] = request.monitor_source_name
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_reason):
            body['problemReason'] = request.problem_reason
        if not UtilClient.is_unset(request.recent_activity):
            body['recentActivity'] = request.recent_activity
        if not UtilClient.is_unset(request.recovery_mode):
            body['recoveryMode'] = request.recovery_mode
        if not UtilClient.is_unset(request.relation_changes):
            body['relationChanges'] = request.relation_changes
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.replay_duty_user_id):
            body['replayDutyUserId'] = request.replay_duty_user_id
        if not UtilClient.is_unset(request.user_report):
            body['userReport'] = request.user_report
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemImprovement',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/improvement/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemImprovementResponse(),
            self.call_api(params, req, runtime)
        )

    def update_problem_improvement(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_improvement_with_options(request, headers, runtime)

    def update_problem_measure_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_standard):
            body['checkStandard'] = request.check_standard
        if not UtilClient.is_unset(request.check_user_id):
            body['checkUserId'] = request.check_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.director_id):
            body['directorId'] = request.director_id
        if not UtilClient.is_unset(request.measure_id):
            body['measureId'] = request.measure_id
        if not UtilClient.is_unset(request.plan_finish_time):
            body['planFinishTime'] = request.plan_finish_time
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.stalker_id):
            body['stalkerId'] = request.stalker_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/improvement/measure/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    def update_problem_measure(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_measure_with_options(request, headers, runtime)

    def update_problem_notice_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemNotice',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/notify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_problem_notice(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_notice_with_options(request, headers, runtime)

    def update_problem_timeline_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.key_node):
            body['keyNode'] = request.key_node
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_timeline_id):
            body['problemTimelineId'] = request.problem_timeline_id
        if not UtilClient.is_unset(request.time):
            body['time'] = request.time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/problem/process/timeline/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_problem_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_timeline_with_options(request, headers, runtime)

    def update_rich_text_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text):
            body['richText'] = request.rich_text
        if not UtilClient.is_unset(request.rich_text_id):
            body['richTextId'] = request.rich_text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/rich/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateRichTextResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rich_text(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rich_text_with_options(request, headers, runtime)

    def update_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.child_rule_relation):
            body['childRuleRelation'] = request.child_rule_relation
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.convergence_fields):
            body['convergenceFields'] = request.convergence_fields
        if not UtilClient.is_unset(request.convergence_type):
            body['convergenceType'] = request.convergence_type
        if not UtilClient.is_unset(request.coverage_problem_levels):
            body['coverageProblemLevels'] = request.coverage_problem_levels
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
        if not UtilClient.is_unset(request.problem_effection_services):
            body['problemEffectionServices'] = request.problem_effection_services
        if not UtilClient.is_unset(request.problem_level_group):
            body['problemLevelGroup'] = request.problem_level_group
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.route_child_rules):
            body['routeChildRules'] = request.route_child_rules
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.time_window):
            body['timeWindow'] = request.time_window
        if not UtilClient.is_unset(request.time_window_unit):
            body['timeWindowUnit'] = request.time_window_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_route_rule_with_options(request, headers, runtime)

    def update_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_description):
            body['serviceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(request, headers, runtime)

    def update_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
        if not UtilClient.is_unset(request.monitor_source_templates):
            body['monitorSourceTemplates'] = request.monitor_source_templates
        if not UtilClient.is_unset(request.service_group_description):
            body['serviceGroupDescription'] = request.service_group_description
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.webhook_link):
            body['webhookLink'] = request.webhook_link
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/modify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_with_options(request, headers, runtime)

    def update_service_group_scheduling_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_group_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_scheduling_with_options(request, headers, runtime)

    def update_service_group_special_day_scheduling_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.scheduling_date):
            body['schedulingDate'] = request.scheduling_date
        if not UtilClient.is_unset(request.scheduling_special_days):
            body['schedulingSpecialDays'] = request.scheduling_special_days
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroupSpecialDayScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/services/group/scheduling/updateSpecialDayScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_group_special_day_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_special_day_scheduling_with_options(request, headers, runtime)

    def update_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.expired_type):
            body['expiredType'] = request.expired_type
        if not UtilClient.is_unset(request.notify_object_list):
            body['notifyObjectList'] = request.notify_object_list
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.notify_strategy_list):
            body['notifyStrategyList'] = request.notify_strategy_list
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object_list):
            body['scopeObjectList'] = request.scope_object_list
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/notify/subscription/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_subscription_with_options(request, headers, runtime)

    def update_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    def update_user_guide_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.guide_action):
            body['guideAction'] = request.guide_action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGuideStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/user/update/guide/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserGuideStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_guide_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_guide_status_with_options(request, headers, runtime)

    def verify_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        if not UtilClient.is_unset(request.test_source_events):
            body['testSourceEvents'] = request.test_source_events
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname='/routeRule/verify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.VerifyRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_route_rule_with_options(request, headers, runtime)
