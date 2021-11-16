# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('gemp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_problem_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_problem_service_group_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.AddProblemServiceGroupResponse(),
            self.do_roarequest('AddProblemServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/addServiceGroup', 'json', req, runtime)
        )

    def cancel_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CancelProblemResponse(),
            self.do_roarequest('CancelProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/cancel', 'json', req, runtime)
        )

    def check_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_webhook_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CheckWebhookResponse(),
            self.do_roarequest('CheckWebhook', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/check/webhook', 'json', req, runtime)
        )

    def confirm_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ConfirmIntegrationConfigResponse(),
            self.do_roarequest('ConfirmIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/confirm', 'json', req, runtime)
        )

    def create_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_escalation_plan_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateEscalationPlanResponse(),
            self.do_roarequest('CreateEscalationPlan', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/create', 'json', req, runtime)
        )

    def create_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentResponse(),
            self.do_roarequest('CreateIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/manualSave', 'json', req, runtime)
        )

    def create_incident_subtotal(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_incident_subtotal_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentSubtotalResponse(),
            self.do_roarequest('CreateIncidentSubtotal', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/save/subtotal', 'json', req, runtime)
        )

    def create_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateIntegrationConfigResponse(),
            self.do_roarequest('CreateIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/create', 'json', req, runtime)
        )

    def create_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemResponse(),
            self.do_roarequest('CreateProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/upgrade', 'json', req, runtime)
        )

    def create_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_effection_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemEffectionServiceResponse(),
            self.do_roarequest('CreateProblemEffectionService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/effectionService/create', 'json', req, runtime)
        )

    def create_problem_measure(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_measure_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemMeasureResponse(),
            self.do_roarequest('CreateProblemMeasure', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/improvement/measure/save', 'json', req, runtime)
        )

    def create_problem_subtotal(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_subtotal_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemSubtotalResponse(),
            self.do_roarequest('CreateProblemSubtotal', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/save/subtotal', 'json', req, runtime)
        )

    def create_problem_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_timeline_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelineResponse(),
            self.do_roarequest('CreateProblemTimeline', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/timeline/create', 'json', req, runtime)
        )

    def create_problem_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_timelines_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelinesResponse(),
            self.do_roarequest('CreateProblemTimelines', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/timeline/batchCreate', 'json', req, runtime)
        )

    def create_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_route_rule_with_options(request, headers, runtime)

    def create_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        return TeaCore.from_map(
            gemp20210413_models.CreateRouteRuleResponse(),
            self.do_roarequest('CreateRouteRule', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/save', 'json', req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceResponse(),
            self.do_roarequest('CreateService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/save', 'json', req, runtime)
        )

    def create_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_group_with_options(request, headers, runtime)

    def create_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
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
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupResponse(),
            self.do_roarequest('CreateServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/insert', 'json', req, runtime)
        )

    def create_service_group_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_group_scheduling_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupSchedulingResponse(),
            self.do_roarequest('CreateServiceGroupScheduling', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/save', 'json', req, runtime)
        )

    def create_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_subscription_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateSubscriptionResponse(),
            self.do_roarequest('CreateSubscription', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/create', 'json', req, runtime)
        )

    def create_tenant_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tenant_application_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateTenantApplicationResponse(),
            self.do_roarequest('CreateTenantApplication', '2021-04-13', 'HTTPS', 'POST', 'AK', '/mobileApp/create', 'json', req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.CreateUserResponse(),
            self.do_roarequest('CreateUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/create', 'json', req, runtime)
        )

    def delete_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_escalation_plan_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteEscalationPlanResponse(),
            self.do_roarequest('DeleteEscalationPlan', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/delete', 'json', req, runtime)
        )

    def delete_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteIncidentResponse(),
            self.do_roarequest('DeleteIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/delete', 'json', req, runtime)
        )

    def delete_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteIntegrationConfigResponse(),
            self.do_roarequest('DeleteIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/delete', 'json', req, runtime)
        )

    def delete_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemResponse(),
            self.do_roarequest('DeleteProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/delete', 'json', req, runtime)
        )

    def delete_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_effection_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemEffectionServiceResponse(),
            self.do_roarequest('DeleteProblemEffectionService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/effectionService/delete', 'json', req, runtime)
        )

    def delete_problem_measure(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_measure_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemMeasureResponse(),
            self.do_roarequest('DeleteProblemMeasure', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/improvement/measure/delete', 'json', req, runtime)
        )

    def delete_problem_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_timeline_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemTimelineResponse(),
            self.do_roarequest('DeleteProblemTimeline', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/timeline/delete', 'json', req, runtime)
        )

    def delete_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_route_rule_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteRouteRuleResponse(),
            self.do_roarequest('DeleteRouteRule', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/delete', 'json', req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceResponse(),
            self.do_roarequest('DeleteService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/delete', 'json', req, runtime)
        )

    def delete_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupResponse(),
            self.do_roarequest('DeleteServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/delete', 'json', req, runtime)
        )

    def delete_service_group_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupUserResponse(),
            self.do_roarequest('DeleteServiceGroupUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/deleteServiceGroupUser', 'json', req, runtime)
        )

    def delete_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_subscription_with_options(request, headers, runtime)

    def delete_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteSubscriptionResponse(),
            self.do_roarequest('DeleteSubscription', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/delete', 'json', req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeleteUserResponse(),
            self.do_roarequest('DeleteUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/delete', 'json', req, runtime)
        )

    def deliver_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deliver_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DeliverIncidentResponse(),
            self.do_roarequest('DeliverIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/deliver', 'json', req, runtime)
        )

    def disable_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_escalation_plan_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DisableEscalationPlanResponse(),
            self.do_roarequest('DisableEscalationPlan', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/disable', 'json', req, runtime)
        )

    def disable_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DisableIntegrationConfigResponse(),
            self.do_roarequest('DisableIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/disable', 'json', req, runtime)
        )

    def disable_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_route_rule_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DisableRouteRuleResponse(),
            self.do_roarequest('DisableRouteRule', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/disable', 'json', req, runtime)
        )

    def disable_service_group_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_service_group_webhook_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.DisableServiceGroupWebhookResponse(),
            self.do_roarequest('DisableServiceGroupWebhook', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/disableWebhook', 'json', req, runtime)
        )

    def disable_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_subscription_with_options(request, headers, runtime)

    def disable_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableSubscriptionResponse(),
            self.do_roarequest('DisableSubscription', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/doDisable', 'json', req, runtime)
        )

    def enable_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_escalation_plan_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.EnableEscalationPlanResponse(),
            self.do_roarequest('EnableEscalationPlan', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/enable', 'json', req, runtime)
        )

    def enable_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.EnableIntegrationConfigResponse(),
            self.do_roarequest('EnableIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/enable', 'json', req, runtime)
        )

    def enable_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_route_rule_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.EnableRouteRuleResponse(),
            self.do_roarequest('EnableRouteRule', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/enable', 'json', req, runtime)
        )

    def enable_service_group_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_service_group_webhook_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.EnableServiceGroupWebhookResponse(),
            self.do_roarequest('EnableServiceGroupWebhook', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/enableWebhook', 'json', req, runtime)
        )

    def enable_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_subscription_with_options(request, headers, runtime)

    def enable_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableSubscriptionResponse(),
            self.do_roarequest('EnableSubscription', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/enable', 'json', req, runtime)
        )

    def finish_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.FinishIncidentResponse(),
            self.do_roarequest('FinishIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/finish', 'json', req, runtime)
        )

    def finish_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.FinishProblemResponse(),
            self.do_roarequest('FinishProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/finish', 'json', req, runtime)
        )

    def generate_problem_picture_link(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_problem_picture_link_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureLinkResponse(),
            self.do_roarequest('GenerateProblemPictureLink', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/oss/getPresignedLink', 'json', req, runtime)
        )

    def generate_problem_picture_upload_sign(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_problem_picture_upload_sign_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureUploadSignResponse(),
            self.do_roarequest('GenerateProblemPictureUploadSign', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/oss/generatePostPolicy', 'json', req, runtime)
        )

    def get_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_escalation_plan_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetEscalationPlanResponse(),
            self.do_roarequest('GetEscalationPlan', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/detail', 'json', req, runtime)
        )

    def get_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_event_with_options(request, headers, runtime)

    def get_event_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEventResponse(),
            self.do_roarequest('GetEvent', '2021-04-13', 'HTTPS', 'POST', 'AK', '/events/getLastTimeEvent', 'json', req, runtime)
        )

    def get_home_page_guidance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_home_page_guidance_with_options(request, headers, runtime)

    def get_home_page_guidance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetHomePageGuidanceResponse(),
            self.do_roarequest('GetHomePageGuidance', '2021-04-13', 'HTTPS', 'POST', 'AK', '/guidance/detail', 'json', req, runtime)
        )

    def get_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentResponse(),
            self.do_roarequest('GetIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/detail', 'json', req, runtime)
        )

    def get_incident_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_statistics_with_options(request, headers, runtime)

    def get_incident_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentStatisticsResponse(),
            self.do_roarequest('GetIncidentStatistics', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/count', 'json', req, runtime)
        )

    def get_incident_subtotal_count(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_subtotal_count_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentSubtotalCountResponse(),
            self.do_roarequest('GetIncidentSubtotalCount', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/subtotal/count', 'json', req, runtime)
        )

    def get_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetIntegrationConfigResponse(),
            self.do_roarequest('GetIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/detail', 'json', req, runtime)
        )

    def get_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetProblemResponse(),
            self.do_roarequest('GetProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/detail', 'json', req, runtime)
        )

    def get_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_effection_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetProblemEffectionServiceResponse(),
            self.do_roarequest('GetProblemEffectionService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/effectionService/detail', 'json', req, runtime)
        )

    def get_problem_improvement(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_improvement_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetProblemImprovementResponse(),
            self.do_roarequest('GetProblemImprovement', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/improvement/detail', 'json', req, runtime)
        )

    def get_problem_preview(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_preview_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetProblemPreviewResponse(),
            self.do_roarequest('GetProblemPreview', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/preview', 'json', req, runtime)
        )

    def get_resource_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_statistics_with_options(request, headers, runtime)

    def get_resource_statistics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetResourceStatisticsResponse(),
            self.do_roarequest('GetResourceStatistics', '2021-04-13', 'HTTPS', 'POST', 'AK', '/config/resource/count', 'json', req, runtime)
        )

    def get_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_route_rule_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetRouteRuleResponse(),
            self.do_roarequest('GetRouteRule', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/detail', 'json', req, runtime)
        )

    def get_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetServiceResponse(),
            self.do_roarequest('GetService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/detail', 'json', req, runtime)
        )

    def get_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupResponse(),
            self.do_roarequest('GetServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/detail', 'json', req, runtime)
        )

    def get_service_group_person_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_person_scheduling_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupPersonSchedulingResponse(),
            self.do_roarequest('GetServiceGroupPersonScheduling', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/user/getScheduling', 'json', req, runtime)
        )

    def get_service_group_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_scheduling_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingResponse(),
            self.do_roarequest('GetServiceGroupScheduling', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/detail', 'json', req, runtime)
        )

    def get_service_group_scheduling_preview(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_scheduling_preview_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingPreviewResponse(),
            self.do_roarequest('GetServiceGroupSchedulingPreview', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/preview', 'json', req, runtime)
        )

    def get_service_group_special_person_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_special_person_scheduling_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse(),
            self.do_roarequest('GetServiceGroupSpecialPersonScheduling', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/getUserScheduling', 'json', req, runtime)
        )

    def get_similar_incident_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similar_incident_statistics_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetSimilarIncidentStatisticsResponse(),
            self.do_roarequest('GetSimilarIncidentStatistics', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/similarIncident/statistics', 'json', req, runtime)
        )

    def get_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subscription_with_options(request, headers, runtime)

    def get_subscription_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSubscriptionResponse(),
            self.do_roarequest('GetSubscription', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/detail', 'json', req, runtime)
        )

    def get_tenant_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_application_with_options(request, headers, runtime)

    def get_tenant_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantApplicationResponse(),
            self.do_roarequest('GetTenantApplication', '2021-04-13', 'HTTPS', 'POST', 'AK', '/mobileApp/detail', 'json', req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.GetUserResponse(),
            self.do_roarequest('GetUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/getUser', 'json', req, runtime)
        )

    def get_user_guide_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_guide_status_with_options(request, headers, runtime)

    def get_user_guide_status_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserGuideStatusResponse(),
            self.do_roarequest('GetUserGuideStatus', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/guide/status', 'json', req, runtime)
        )

    def list_alerts(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alerts_with_options(request, headers, runtime)

    def list_alerts_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_level):
            body['alertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_name):
            body['alertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_source_name):
            body['alertSourceName'] = request.alert_source_name
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListAlertsResponse(),
            self.do_roarequest('ListAlerts', '2021-04-13', 'HTTPS', 'POST', 'AK', '/alerts/list', 'json', req, runtime)
        )

    def list_chart_data_for_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chart_data_for_service_group_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForServiceGroupResponse(),
            self.do_roarequest('ListChartDataForServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/statistics/chartDataForServiceGroup/', 'json', req, runtime)
        )

    def list_chart_data_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chart_data_for_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForUserResponse(),
            self.do_roarequest('ListChartDataForUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/statistics/chartDataForUser/', 'json', req, runtime)
        )

    def list_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(request, headers, runtime)

    def list_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListConfigsResponse(),
            self.do_roarequest('ListConfigs', '2021-04-13', 'HTTPS', 'POST', 'AK', '/config/all', 'json', req, runtime)
        )

    def list_data_report_for_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_report_for_service_group_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForServiceGroupResponse(),
            self.do_roarequest('ListDataReportForServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/statistics/listDataReportForServiceGroup', 'json', req, runtime)
        )

    def list_data_report_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_report_for_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForUserResponse(),
            self.do_roarequest('ListDataReportForUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/statistics/listDataReportForUser', 'json', req, runtime)
        )

    def list_dictionaries(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dictionaries_with_options(request, headers, runtime)

    def list_dictionaries_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDictionariesResponse(),
            self.do_roarequest('ListDictionaries', '2021-04-13', 'HTTPS', 'POST', 'AK', '/dict/list', 'json', req, runtime)
        )

    def list_escalation_plan_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plan_services_with_options(request, headers, runtime)

    def list_escalation_plan_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlanServicesResponse(),
            self.do_roarequest('ListEscalationPlanServices', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/services', 'json', req, runtime)
        )

    def list_escalation_plans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plans_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansResponse(),
            self.do_roarequest('ListEscalationPlans', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/list', 'json', req, runtime)
        )

    def list_incident_detail_escalation_plans(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_detail_escalation_plans_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailEscalationPlansResponse(),
            self.do_roarequest('ListIncidentDetailEscalationPlans', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/detail/escalation', 'json', req, runtime)
        )

    def list_incident_detail_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_detail_timelines_with_options(request, headers, runtime)

    def list_incident_detail_timelines_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailTimelinesResponse(),
            self.do_roarequest('ListIncidentDetailTimelines', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/detail/timeline', 'json', req, runtime)
        )

    def list_incident_subtotals(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_subtotals_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentSubtotalsResponse(),
            self.do_roarequest('ListIncidentSubtotals', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/list/subtotal', 'json', req, runtime)
        )

    def list_incident_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_timelines_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentTimelinesResponse(),
            self.do_roarequest('ListIncidentTimelines', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/timeline', 'json', req, runtime)
        )

    def list_incidents(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incidents_with_options(request, headers, runtime)

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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentsResponse(),
            self.do_roarequest('ListIncidents', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/list', 'json', req, runtime)
        )

    def list_integration_config_timelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_config_timelines_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigTimelinesResponse(),
            self.do_roarequest('ListIntegrationConfigTimelines', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/timeline', 'json', req, runtime)
        )

    def list_integration_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_configs_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigsResponse(),
            self.do_roarequest('ListIntegrationConfigs', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/list', 'json', req, runtime)
        )

    def list_monitor_sources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_monitor_sources_with_options(request, headers, runtime)

    def list_monitor_sources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListMonitorSourcesResponse(),
            self.do_roarequest('ListMonitorSources', '2021-04-13', 'HTTPS', 'POST', 'AK', '/monitorSource/list', 'json', req, runtime)
        )

    def list_problem_detail_operations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_detail_operations_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListProblemDetailOperationsResponse(),
            self.do_roarequest('ListProblemDetailOperations', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/detail/operations', 'json', req, runtime)
        )

    def list_problem_operations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_operations_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListProblemOperationsResponse(),
            self.do_roarequest('ListProblemOperations', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/operations', 'json', req, runtime)
        )

    def list_problem_subtotals(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_subtotals_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListProblemSubtotalsResponse(),
            self.do_roarequest('ListProblemSubtotals', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/list/subtotal', 'json', req, runtime)
        )

    def list_problem_time_lines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_time_lines_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListProblemTimeLinesResponse(),
            self.do_roarequest('ListProblemTimeLines', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/detail/timeLines', 'json', req, runtime)
        )

    def list_problems(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problems_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListProblemsResponse(),
            self.do_roarequest('ListProblems', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/listProblems', 'json', req, runtime)
        )

    def list_route_rules(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_with_options(request, headers, runtime)

    def list_route_rules_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesResponse(),
            self.do_roarequest('ListRouteRules', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/list', 'json', req, runtime)
        )

    def list_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_groups_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsResponse(),
            self.do_roarequest('ListServiceGroups', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/list', 'json', req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListServicesResponse(),
            self.do_roarequest('ListServices', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/list', 'json', req, runtime)
        )

    def list_source_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_source_events_with_options(request, headers, runtime)

    def list_source_events_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.stop_row_key):
            body['stopRowKey'] = request.stop_row_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsResponse(),
            self.do_roarequest('ListSourceEvents', '2021-04-13', 'HTTPS', 'POST', 'AK', '/events/listOriginalEvent', 'json', req, runtime)
        )

    def list_source_events_for_monitor_source(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_source_events_for_monitor_source_with_options(request, headers, runtime)

    def list_source_events_for_monitor_source_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsForMonitorSourceResponse(),
            self.do_roarequest('ListSourceEventsForMonitorSource', '2021-04-13', 'HTTPS', 'POST', 'AK', '/events/queryLastestEvents', 'json', req, runtime)
        )

    def list_subscription_service_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subscription_service_groups_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionServiceGroupsResponse(),
            self.do_roarequest('ListSubscriptionServiceGroups', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/serviceGroup/list', 'json', req, runtime)
        )

    def list_subscriptions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subscriptions_with_options(request, headers, runtime)

    def list_subscriptions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionsResponse(),
            self.do_roarequest('ListSubscriptions', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/list', 'json', req, runtime)
        )

    def list_user_serivce_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_serivce_groups_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListUserSerivceGroupsResponse(),
            self.do_roarequest('ListUserSerivceGroups', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/preview/detail', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ListUsersResponse(),
            self.do_roarequest('ListUsers', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/list', 'json', req, runtime)
        )

    def recover_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.RecoverProblemResponse(),
            self.do_roarequest('RecoverProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/recovery', 'json', req, runtime)
        )

    def refresh_integration_config_key(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_integration_config_key_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.RefreshIntegrationConfigKeyResponse(),
            self.do_roarequest('RefreshIntegrationConfigKey', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/refreshKey', 'json', req, runtime)
        )

    def remove_problem_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_problem_service_group_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.RemoveProblemServiceGroupResponse(),
            self.do_roarequest('RemoveProblemServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/removeServiceGroup', 'json', req, runtime)
        )

    def replay_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.replay_problem_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.ReplayProblemResponse(),
            self.do_roarequest('ReplayProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/replay', 'json', req, runtime)
        )

    def respond_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.respond_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.RespondIncidentResponse(),
            self.do_roarequest('RespondIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/response', 'json', req, runtime)
        )

    def revoke_problem_recovery(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_problem_recovery_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.RevokeProblemRecoveryResponse(),
            self.do_roarequest('RevokeProblemRecovery', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/revoke', 'json', req, runtime)
        )

    def update_escalation_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_escalation_plan_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateEscalationPlanResponse(),
            self.do_roarequest('UpdateEscalationPlan', '2021-04-13', 'HTTPS', 'POST', 'AK', '/escalationPlan/update', 'json', req, runtime)
        )

    def update_incident(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_incident_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateIncidentResponse(),
            self.do_roarequest('UpdateIncident', '2021-04-13', 'HTTPS', 'POST', 'AK', '/incident/update', 'json', req, runtime)
        )

    def update_integration_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_integration_config_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateIntegrationConfigResponse(),
            self.do_roarequest('UpdateIntegrationConfig', '2021-04-13', 'HTTPS', 'POST', 'AK', '/integrationConfig/update', 'json', req, runtime)
        )

    def update_problem(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_with_options(request, headers, runtime)

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
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemResponse(),
            self.do_roarequest('UpdateProblem', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/update', 'json', req, runtime)
        )

    def update_problem_effection_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_effection_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemEffectionServiceResponse(),
            self.do_roarequest('UpdateProblemEffectionService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/effectionService/update', 'json', req, runtime)
        )

    def update_problem_improvement(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_improvement_with_options(request, headers, runtime)

    def update_problem_improvement_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
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
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemImprovementResponse(),
            self.do_roarequest('UpdateProblemImprovement', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/improvement/update', 'json', req, runtime)
        )

    def update_problem_measure(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_measure_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemMeasureResponse(),
            self.do_roarequest('UpdateProblemMeasure', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/improvement/measure/update', 'json', req, runtime)
        )

    def update_problem_notice(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_notice_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemNoticeResponse(),
            self.do_roarequest('UpdateProblemNotice', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/notify', 'json', req, runtime)
        )

    def update_problem_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_timeline_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemTimelineResponse(),
            self.do_roarequest('UpdateProblemTimeline', '2021-04-13', 'HTTPS', 'POST', 'AK', '/problem/process/timeline/update', 'json', req, runtime)
        )

    def update_route_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_route_rule_with_options(request, headers, runtime)

    def update_route_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
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
        return TeaCore.from_map(
            gemp20210413_models.UpdateRouteRuleResponse(),
            self.do_roarequest('UpdateRouteRule', '2021-04-13', 'HTTPS', 'POST', 'AK', '/routeRule/edit', 'json', req, runtime)
        )

    def update_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceResponse(),
            self.do_roarequest('UpdateService', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/update', 'json', req, runtime)
        )

    def update_service_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_with_options(request, headers, runtime)

    def update_service_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
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
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupResponse(),
            self.do_roarequest('UpdateServiceGroup', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/modify', 'json', req, runtime)
        )

    def update_service_group_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_scheduling_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSchedulingResponse(),
            self.do_roarequest('UpdateServiceGroupScheduling', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/update', 'json', req, runtime)
        )

    def update_service_group_special_day_scheduling(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_special_day_scheduling_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse(),
            self.do_roarequest('UpdateServiceGroupSpecialDayScheduling', '2021-04-13', 'HTTPS', 'POST', 'AK', '/services/group/scheduling/updateSpecialDayScheduling', 'json', req, runtime)
        )

    def update_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_subscription_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateSubscriptionResponse(),
            self.do_roarequest('UpdateSubscription', '2021-04-13', 'HTTPS', 'POST', 'AK', '/notify/subscription/update', 'json', req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserResponse(),
            self.do_roarequest('UpdateUser', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/update', 'json', req, runtime)
        )

    def update_user_guide_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_guide_status_with_options(request, headers, runtime)

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
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserGuideStatusResponse(),
            self.do_roarequest('UpdateUserGuideStatus', '2021-04-13', 'HTTPS', 'POST', 'AK', '/user/update/guide/status', 'json', req, runtime)
        )
