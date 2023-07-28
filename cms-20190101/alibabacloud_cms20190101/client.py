# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cms20190101 import models as cms_20190101_models
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
        self._endpoint = self.get_endpoint('cms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_tags_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: AddTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: AddTagsRequest

        @return: AddTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    def apply_metric_rule_template_with_options(self, request, runtime):
        """
        The ID of the application group to which the alert template is applied.
        For more information about how to query the ID of an application group, see [DescribeMonitorGroups](~~115032~~).
        

        @param request: ApplyMetricRuleTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ApplyMetricRuleTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_mode):
            query['ApplyMode'] = request.apply_mode
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.notify_level):
            query['NotifyLevel'] = request.notify_level
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ApplyMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_metric_rule_template(self, request):
        """
        The ID of the application group to which the alert template is applied.
        For more information about how to query the ID of an application group, see [DescribeMonitorGroups](~~115032~~).
        

        @param request: ApplyMetricRuleTemplateRequest

        @return: ApplyMetricRuleTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_metric_rule_template_with_options(request, runtime)

    def batch_create_instant_site_monitor_with_options(self, request, runtime):
        """
        The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        

        @param request: BatchCreateInstantSiteMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchCreateInstantSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateInstantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchCreateInstantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_instant_site_monitor(self, request):
        """
        The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        

        @param request: BatchCreateInstantSiteMonitorRequest

        @return: BatchCreateInstantSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_instant_site_monitor_with_options(request, runtime)

    def batch_create_intant_site_monitor_with_options(self, request, runtime):
        """
        @deprecated : BatchCreateIntantSiteMonitor is deprecated, please use Cms::2019-01-01::BatchCreateInstantSiteMonitor instead.
        

        @param request: BatchCreateIntantSiteMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BatchCreateIntantSiteMonitorResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateIntantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchCreateIntantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_intant_site_monitor(self, request):
        """
        @deprecated : BatchCreateIntantSiteMonitor is deprecated, please use Cms::2019-01-01::BatchCreateInstantSiteMonitor instead.
        

        @param request: BatchCreateIntantSiteMonitorRequest

        @return: BatchCreateIntantSiteMonitorResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_intant_site_monitor_with_options(request, runtime)

    def batch_export_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.BatchExportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.measurements):
            request.measurements_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.measurements, 'Measurements', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.length):
            body['Length'] = request.length
        if not UtilClient.is_unset(request.measurements_shrink):
            body['Measurements'] = request.measurements_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchExport',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.BatchExportResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_export(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_export_with_options(request, runtime)

    def create_cms_call_num_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsCallNumOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsCallNumOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cms_call_num_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cms_call_num_order_with_options(request, runtime)

    def create_cms_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_count):
            query['ApiCount'] = request.api_count
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.custom_time_series):
            query['CustomTimeSeries'] = request.custom_time_series
        if not UtilClient.is_unset(request.event_store_num):
            query['EventStoreNum'] = request.event_store_num
        if not UtilClient.is_unset(request.event_store_time):
            query['EventStoreTime'] = request.event_store_time
        if not UtilClient.is_unset(request.log_monitor_stream):
            query['LogMonitorStream'] = request.log_monitor_stream
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.phone_count):
            query['PhoneCount'] = request.phone_count
        if not UtilClient.is_unset(request.site_ecs_num):
            query['SiteEcsNum'] = request.site_ecs_num
        if not UtilClient.is_unset(request.site_operator_num):
            query['SiteOperatorNum'] = request.site_operator_num
        if not UtilClient.is_unset(request.site_task_num):
            query['SiteTaskNum'] = request.site_task_num
        if not UtilClient.is_unset(request.sms_count):
            query['SmsCount'] = request.sms_count
        if not UtilClient.is_unset(request.suggest_type):
            query['SuggestType'] = request.suggest_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cms_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cms_order_with_options(request, runtime)

    def create_cms_smspackage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.sms_count):
            query['SmsCount'] = request.sms_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCmsSmspackageOrder',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsSmspackageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cms_smspackage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cms_smspackage_order_with_options(request, runtime)

    def create_dynamic_tag_group_with_options(self, request, runtime):
        """
        Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        *   true: The application group automatically subscribes to event notifications.
        *   false (default value): The application group does not automatically subscribe to event notifications.
        

        @param request: CreateDynamicTagGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDynamicTagGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not UtilClient.is_unset(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not UtilClient.is_unset(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not UtilClient.is_unset(request.match_express):
            query['MatchExpress'] = request.match_express
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not UtilClient.is_unset(request.template_id_list):
            query['TemplateIdList'] = request.template_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDynamicTagGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateDynamicTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dynamic_tag_group(self, request):
        """
        Specifies whether the application group automatically subscribes to event notifications. If events whose severity level is critical or warning occur on resources in an application group, CloudMonitor sends alert notifications. Valid values:
        *   true: The application group automatically subscribes to event notifications.
        *   false (default value): The application group does not automatically subscribe to event notifications.
        

        @param request: CreateDynamicTagGroupRequest

        @return: CreateDynamicTagGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dynamic_tag_group_with_options(request, runtime)

    def create_group_metric_rules_with_options(self, request, runtime):
        """
        The details of the alert rules.
        

        @param request: CreateGroupMetricRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateGroupMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_metric_rules):
            query['GroupMetricRules'] = request.group_metric_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_metric_rules(self, request):
        """
        The details of the alert rules.
        

        @param request: CreateGroupMetricRulesRequest

        @return: CreateGroupMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_metric_rules_with_options(request, runtime)

    def create_group_monitoring_agent_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.match_express):
            query['MatchExpress'] = request.match_express
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_monitoring_agent_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_monitoring_agent_process_with_options(request, runtime)

    def create_host_availability_with_options(self, request, runtime):
        """
        The ID of the resource for which alerts are triggered.
        

        @param request: CreateHostAvailabilityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHostAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not UtilClient.is_unset(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_host_availability(self, request):
        """
        The ID of the resource for which alerts are triggered.
        

        @param request: CreateHostAvailabilityRequest

        @return: CreateHostAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_host_availability_with_options(request, runtime)

    def create_hybrid_monitor_namespace_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: CreateHybridMonitorNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hybrid_monitor_namespace(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: CreateHybridMonitorNamespaceRequest

        @return: CreateHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_monitor_namespace_with_options(request, runtime)

    def create_hybrid_monitor_slsgroup_with_options(self, request, runtime):
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        

        @param request: CreateHybridMonitorSLSGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not UtilClient.is_unset(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hybrid_monitor_slsgroup(self, request):
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        

        @param request: CreateHybridMonitorSLSGroupRequest

        @return: CreateHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_monitor_slsgroup_with_options(request, runtime)

    def create_hybrid_monitor_task_with_options(self, request, runtime):
        """
        The dimension based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        

        @param request: CreateHybridMonitorTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not UtilClient.is_unset(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not UtilClient.is_unset(request.collect_target_type):
            query['CollectTargetType'] = request.collect_target_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.target_user_id_list):
            query['TargetUserIdList'] = request.target_user_id_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.yarmconfig):
            query['YARMConfig'] = request.yarmconfig
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hybrid_monitor_task(self, request):
        """
        The dimension based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        

        @param request: CreateHybridMonitorTaskRequest

        @return: CreateHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hybrid_monitor_task_with_options(request, runtime)

    def create_instant_site_monitor_with_options(self, request, runtime):
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to create an instant test task. The name of the task is `task1`. The tested address is `http://www.aliyun.com`. The test type is `HTTP`. The number of detection points is `1`.
        

        @param request: CreateInstantSiteMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstantSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.random_isp_city):
            query['RandomIspCity'] = request.random_isp_city
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstantSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateInstantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instant_site_monitor(self, request):
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to create an instant test task. The name of the task is `task1`. The tested address is `http://www.aliyun.com`. The test type is `HTTP`. The number of detection points is `1`.
        

        @param request: CreateInstantSiteMonitorRequest

        @return: CreateInstantSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instant_site_monitor_with_options(request, runtime)

    def create_metric_rule_black_list_with_options(self, request, runtime):
        """
        The name of the metric.
        Valid values of N: 1 to 10
        

        @param request: CreateMetricRuleBlackListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMetricRuleBlackListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def create_metric_rule_black_list(self, request):
        """
        The name of the metric.
        Valid values of N: 1 to 10
        

        @param request: CreateMetricRuleBlackListRequest

        @return: CreateMetricRuleBlackListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_metric_rule_black_list_with_options(request, runtime)

    def create_metric_rule_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_metric_rule_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_metric_rule_resources_with_options(request, runtime)

    def create_metric_rule_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_metric_rule_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_metric_rule_template_with_options(request, runtime)

    def create_monitor_agent_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_agent_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_agent_process_with_options(request, runtime)

    def create_monitor_group_with_options(self, request, runtime):
        """
        The name of the application group.
        

        @param request: CreateMonitorGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMonitorGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_group(self, request):
        """
        The name of the application group.
        

        @param request: CreateMonitorGroupRequest

        @return: CreateMonitorGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    def create_monitor_group_by_resource_group_id_with_options(self, request, runtime):
        """
        The ID of the region where the resource group resides.
        For information about how to obtain the ID of the region where a resource group resides, see [GetResourceGroup](~~158866~~).
        

        @param request: CreateMonitorGroupByResourceGroupIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMonitorGroupByResourceGroupIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not UtilClient.is_unset(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not UtilClient.is_unset(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupByResourceGroupId',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_group_by_resource_group_id(self, request):
        """
        The ID of the region where the resource group resides.
        For information about how to obtain the ID of the region where a resource group resides, see [GetResourceGroup](~~158866~~).
        

        @param request: CreateMonitorGroupByResourceGroupIdRequest

        @return: CreateMonitorGroupByResourceGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_by_resource_group_id_with_options(request, runtime)

    def create_monitor_group_instances_with_options(self, request, runtime):
        """
        The abbreviation of the Alibaba Cloud service name.
        To obtain the abbreviation of an Alibaba Cloud service name, call the [DescribeProjectMeta](~~114916~~) operation. The `metricCategory` tag in the `Labels` response parameter indicates the abbreviation of the Alibaba Cloud service name.
        

        @param request: CreateMonitorGroupInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMonitorGroupInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_group_instances(self, request):
        """
        The abbreviation of the Alibaba Cloud service name.
        To obtain the abbreviation of an Alibaba Cloud service name, call the [DescribeProjectMeta](~~114916~~) operation. The `metricCategory` tag in the `Labels` response parameter indicates the abbreviation of the Alibaba Cloud service name.
        

        @param request: CreateMonitorGroupInstancesRequest

        @return: CreateMonitorGroupInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_instances_with_options(request, runtime)

    def create_monitor_group_notify_policy_with_options(self, request, runtime):
        """
        The type of the policy. Valid value: PauseNotify.
        

        @param request: CreateMonitorGroupNotifyPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMonitorGroupNotifyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroupNotifyPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_group_notify_policy(self, request):
        """
        The type of the policy. Valid value: PauseNotify.
        

        @param request: CreateMonitorGroupNotifyPolicyRequest

        @return: CreateMonitorGroupNotifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_notify_policy_with_options(request, runtime)

    def create_monitoring_agent_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        if not UtilClient.is_unset(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitoring_agent_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_monitoring_agent_process_with_options(request, runtime)

    def create_site_monitor_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: CreateSiteMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_site_monitor(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: CreateSiteMonitorRequest

        @return: CreateSiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_site_monitor_with_options(request, runtime)

    def cursor_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.CursorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.matchers):
            request.matchers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cursor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.CursorResponse(),
            self.call_api(params, req, runtime)
        )

    def cursor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cursor_with_options(request, runtime)

    def delete_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    def delete_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_group_with_options(request, runtime)

    def delete_custom_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomMetric',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_metric_with_options(request, runtime)

    def delete_dynamic_tag_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicTagGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteDynamicTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dynamic_tag_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_tag_group_with_options(request, runtime)

    def delete_event_rule_targets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_rule_targets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_rule_targets_with_options(request, runtime)

    def delete_event_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_rules_with_options(request, runtime)

    def delete_exporter_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_name):
            query['DestName'] = request.dest_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExporterOutput',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_exporter_output(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_exporter_output_with_options(request, runtime)

    def delete_exporter_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExporterRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_exporter_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_exporter_rule_with_options(request, runtime)

    def delete_group_monitoring_agent_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_monitoring_agent_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_monitoring_agent_process_with_options(request, runtime)

    def delete_host_availability_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host_availability(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_host_availability_with_options(request, runtime)

    def delete_hybrid_monitor_namespace_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DeleteHybridMonitorNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hybrid_monitor_namespace(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DeleteHybridMonitorNamespaceRequest

        @return: DeleteHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_monitor_namespace_with_options(request, runtime)

    def delete_hybrid_monitor_slsgroup_with_options(self, request, runtime):
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        

        @param request: DeleteHybridMonitorSLSGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hybrid_monitor_slsgroup(self, request):
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        

        @param request: DeleteHybridMonitorSLSGroupRequest

        @return: DeleteHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_monitor_slsgroup_with_options(request, runtime)

    def delete_hybrid_monitor_task_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DeleteHybridMonitorTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hybrid_monitor_task(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DeleteHybridMonitorTaskRequest

        @return: DeleteHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hybrid_monitor_task_with_options(request, runtime)

    def delete_log_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_id):
            query['LogId'] = request.log_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteLogMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_log_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_log_monitor_with_options(request, runtime)

    def delete_metric_rule_black_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_metric_rule_black_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_black_list_with_options(request, runtime)

    def delete_metric_rule_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_metric_rule_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_resources_with_options(request, runtime)

    def delete_metric_rule_targets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_metric_rule_targets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_targets_with_options(request, runtime)

    def delete_metric_rule_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_metric_rule_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rule_template_with_options(request, runtime)

    def delete_metric_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_metric_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_metric_rules_with_options(request, runtime)

    def delete_monitor_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_monitor_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_with_options(request, runtime)

    def delete_monitor_group_dynamic_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupDynamicRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_monitor_group_dynamic_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_dynamic_rule_with_options(request, runtime)

    def delete_monitor_group_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_monitor_group_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_instances_with_options(request, runtime)

    def delete_monitor_group_notify_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroupNotifyPolicy',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_monitor_group_notify_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_notify_policy_with_options(request, runtime)

    def delete_monitoring_agent_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_monitoring_agent_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_monitoring_agent_process_with_options(request, runtime)

    def delete_site_monitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_delete_alarms):
            query['IsDeleteAlarms'] = request.is_delete_alarms
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_site_monitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_site_monitors_with_options(request, runtime)

    def describe_active_metric_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeActiveMetricRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeActiveMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_active_metric_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_active_metric_rule_list_with_options(request, runtime)

    def describe_alert_history_list_with_options(self, request, runtime):
        """
        @deprecated : DescribeAlertHistoryList is deprecated, please use Cms::2019-01-01::DescribeAlertLogList instead.
        This API operation is no longer maintained. We recommend that you call the [DescribeAlertLogList](~~201087~~) operation.
        

        @param request: DescribeAlertHistoryListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAlertHistoryListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascending):
            query['Ascending'] = request.ascending
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertHistoryList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_history_list(self, request):
        """
        @deprecated : DescribeAlertHistoryList is deprecated, please use Cms::2019-01-01::DescribeAlertLogList instead.
        This API operation is no longer maintained. We recommend that you call the [DescribeAlertLogList](~~201087~~) operation.
        

        @param request: DescribeAlertHistoryListRequest

        @return: DescribeAlertHistoryListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_history_list_with_options(request, runtime)

    def describe_alert_log_count_with_options(self, request, runtime):
        """
        This topic provides an example to show how to query the statistics of alert logs for Elastic Compute Service (ECS) based on the `product` dimension.
        

        @param request: DescribeAlertLogCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAlertLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_log_count(self, request):
        """
        This topic provides an example to show how to query the statistics of alert logs for Elastic Compute Service (ECS) based on the `product` dimension.
        

        @param request: DescribeAlertLogCountRequest

        @return: DescribeAlertLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_count_with_options(request, runtime)

    def describe_alert_log_histogram_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeAlertLogHistogram.
        

        @param request: DescribeAlertLogHistogramRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAlertLogHistogramResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_log_histogram(self, request):
        """
        The operation that you want to perform. Set the value to DescribeAlertLogHistogram.
        

        @param request: DescribeAlertLogHistogramRequest

        @return: DescribeAlertLogHistogramResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_histogram_with_options(request, runtime)

    def describe_alert_log_list_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DescribeAlertLogListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAlertLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.last_min):
            query['LastMin'] = request.last_min
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.send_status):
            query['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertLogList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_log_list(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DescribeAlertLogListRequest

        @return: DescribeAlertLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_list_with_options(request, runtime)

    def describe_alerting_metric_rule_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertingMetricRuleResources',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alerting_metric_rule_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alerting_metric_rule_resources_with_options(request, runtime)

    def describe_contact_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactGroupList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_contact_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_group_list_with_options(request, runtime)

    def describe_contact_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chanel_type):
            query['ChanelType'] = request.chanel_type
        if not UtilClient.is_unset(request.chanel_value):
            query['ChanelValue'] = request.chanel_value
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_contact_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_list_with_options(request, runtime)

    def describe_contact_list_by_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactListByContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListByContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_contact_list_by_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_list_by_contact_group_with_options(request, runtime)

    def describe_custom_event_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_event_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_attribute_with_options(request, runtime)

    def describe_custom_event_count_with_options(self, request, runtime):
        """
        The name of the custom event.
        

        @param request: DescribeCustomEventCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCustomEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_event_count(self, request):
        """
        The name of the custom event.
        

        @param request: DescribeCustomEventCountRequest

        @return: DescribeCustomEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_count_with_options(request, runtime)

    def describe_custom_event_histogram_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomEventHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_event_histogram(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_histogram_with_options(request, runtime)

    def describe_custom_metric_list_with_options(self, request, runtime):
        """
        The ID of the application group.
        For more information, see [DescribeMonitorGroups](~~115032~~).
        

        @param request: DescribeCustomMetricListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCustomMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomMetricList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_metric_list(self, request):
        """
        The ID of the application group.
        For more information, see [DescribeMonitorGroups](~~115032~~).
        

        @param request: DescribeCustomMetricListRequest

        @return: DescribeCustomMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_metric_list_with_options(request, runtime)

    def describe_dynamic_tag_rule_list_with_options(self, request, runtime):
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        

        @param request: DescribeDynamicTagRuleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDynamicTagRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDynamicTagRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeDynamicTagRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dynamic_tag_rule_list(self, request):
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        

        @param request: DescribeDynamicTagRuleListRequest

        @return: DescribeDynamicTagRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dynamic_tag_rule_list_with_options(request, runtime)

    def describe_event_rule_attribute_with_options(self, request, runtime):
        """
        The name of the event-triggered alert rule.
        For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](~~114996~~).
        

        @param request: DescribeEventRuleAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_rule_attribute(self, request):
        """
        The name of the event-triggered alert rule.
        For information about how to obtain the name of an event-triggered alert rule, see [DescribeEventRuleList](~~114996~~).
        

        @param request: DescribeEventRuleAttributeRequest

        @return: DescribeEventRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_attribute_with_options(request, runtime)

    def describe_event_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_list_with_options(request, runtime)

    def describe_event_rule_target_list_with_options(self, request, runtime):
        """
        The error message.
        

        @param request: DescribeEventRuleTargetListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventRuleTargetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventRuleTargetList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleTargetListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_rule_target_list(self, request):
        """
        The error message.
        

        @param request: DescribeEventRuleTargetListRequest

        @return: DescribeEventRuleTargetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_target_list_with_options(request, runtime)

    def describe_exporter_output_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExporterOutputList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterOutputListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exporter_output_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exporter_output_list_with_options(request, runtime)

    def describe_exporter_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExporterRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exporter_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_exporter_rule_list_with_options(request, runtime)

    def describe_group_monitoring_agent_process_with_options(self, request, runtime):
        """
        The ID of the application group.
        

        @param request: DescribeGroupMonitoringAgentProcessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupMonitoringAgentProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_monitoring_agent_process(self, request):
        """
        The ID of the application group.
        

        @param request: DescribeGroupMonitoringAgentProcessRequest

        @return: DescribeGroupMonitoringAgentProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_monitoring_agent_process_with_options(request, runtime)

    def describe_host_availability_list_with_options(self, request, runtime):
        """
        The ID of the availability monitoring task.
        

        @param request: DescribeHostAvailabilityListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHostAvailabilityListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHostAvailabilityList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHostAvailabilityListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_host_availability_list(self, request):
        """
        The ID of the availability monitoring task.
        

        @param request: DescribeHostAvailabilityListRequest

        @return: DescribeHostAvailabilityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_host_availability_list_with_options(request, runtime)

    def describe_hybrid_monitor_data_list_with_options(self, request, runtime):
        """
        The tag key.
        

        @param request: DescribeHybridMonitorDataListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHybridMonitorDataListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.prom_sql):
            query['PromSQL'] = request.prom_sql
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorDataList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hybrid_monitor_data_list(self, request):
        """
        The tag key.
        

        @param request: DescribeHybridMonitorDataListRequest

        @return: DescribeHybridMonitorDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_data_list_with_options(request, runtime)

    def describe_hybrid_monitor_namespace_list_with_options(self, request, runtime):
        """
        The data retention period. Valid values:
        *   cms.s1.large: Data is stored for 15 days.
        *   cms.s1.xlarge: Data is stored for 32 days.
        *   cms.s1.2xlarge: Data is stored for 63 days.
        *   cms.s1.3xlarge: Data is stored for 93 days.
        *   cms.s1.6xlarge: Data is stored for 185 days.
        *   cms.s1.12xlarge: Data is stored for 376 days.
        

        @param request: DescribeHybridMonitorNamespaceListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHybridMonitorNamespaceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_task_statistic):
            query['ShowTaskStatistic'] = request.show_task_statistic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorNamespaceList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hybrid_monitor_namespace_list(self, request):
        """
        The data retention period. Valid values:
        *   cms.s1.large: Data is stored for 15 days.
        *   cms.s1.xlarge: Data is stored for 32 days.
        *   cms.s1.2xlarge: Data is stored for 63 days.
        *   cms.s1.3xlarge: Data is stored for 93 days.
        *   cms.s1.6xlarge: Data is stored for 185 days.
        *   cms.s1.12xlarge: Data is stored for 376 days.
        

        @param request: DescribeHybridMonitorNamespaceListRequest

        @return: DescribeHybridMonitorNamespaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_namespace_list_with_options(request, runtime)

    def describe_hybrid_monitor_slsgroup_with_options(self, request, runtime):
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        

        @param request: DescribeHybridMonitorSLSGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hybrid_monitor_slsgroup(self, request):
        """
        Indicates whether the call is successful. Valid values:
        *   true: The call is successful.
        *   false: The call fails.
        

        @param request: DescribeHybridMonitorSLSGroupRequest

        @return: DescribeHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_slsgroup_with_options(request, runtime)

    def describe_hybrid_monitor_task_list_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DescribeHybridMonitorTaskListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHybridMonitorTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.include_aliyun_task):
            query['IncludeAliyunTask'] = request.include_aliyun_task
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHybridMonitorTaskList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHybridMonitorTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hybrid_monitor_task_list(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: DescribeHybridMonitorTaskListRequest

        @return: DescribeHybridMonitorTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hybrid_monitor_task_list_with_options(request, runtime)

    def describe_log_monitor_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMonitorAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_monitor_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_monitor_attribute_with_options(request, runtime)

    def describe_log_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogMonitorList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_monitor_list_with_options(request, runtime)

    def describe_metric_data_with_options(self, request, runtime):
        """
        The statistical period of the metric.
        Valid values: 15, 60, 900, and 3600.
        Unit: seconds.
        >
        *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        *   For more information about the statistical period of a metric that is specified by the `MetricName` parameter, see [Appendix 1: Metrics](~~163515~~).
        

        @param request: DescribeMetricDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_data(self, request):
        """
        The statistical period of the metric.
        Valid values: 15, 60, 900, and 3600.
        Unit: seconds.
        >
        *   If this parameter is not specified, monitoring data is queried based on the period in which metric values are reported.
        *   For more information about the statistical period of a metric that is specified by the `MetricName` parameter, see [Appendix 1: Metrics](~~163515~~).
        

        @param request: DescribeMetricDataRequest

        @return: DescribeMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_data_with_options(request, runtime)

    def describe_metric_last_with_options(self, request, runtime):
        """
        The number of entries to return on each page.
        Default value: 1000. This value indicates that a maximum of 1,000 entries of monitoring data can be returned on each page.
        >  The maximum value of the Length parameter in a request is 1440.
        

        @param request: DescribeMetricLastRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricLastResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricLast',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_last(self, request):
        """
        The number of entries to return on each page.
        Default value: 1000. This value indicates that a maximum of 1,000 entries of monitoring data can be returned on each page.
        >  The maximum value of the Length parameter in a request is 1440.
        

        @param request: DescribeMetricLastRequest

        @return: DescribeMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_last_with_options(request, runtime)

    def describe_metric_list_with_options(self, request, runtime):
        """
        The name of the metric.
        For more information about metric names, see [Appendix 1: Metrics](~~163515~~).
        

        @param request: DescribeMetricListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_list(self, request):
        """
        The name of the metric.
        For more information about metric names, see [Appendix 1: Metrics](~~163515~~).
        

        @param request: DescribeMetricListRequest

        @return: DescribeMetricListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    def describe_metric_meta_list_with_options(self, request, runtime):
        """
        The namespace of the service.
        For more information, see [Appendix 1: Metrics](~~163515~~).
        

        @param request: DescribeMetricMetaListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricMetaList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_meta_list(self, request):
        """
        The namespace of the service.
        For more information, see [Appendix 1: Metrics](~~163515~~).
        

        @param request: DescribeMetricMetaListRequest

        @return: DescribeMetricMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_meta_list_with_options(request, runtime)

    def describe_metric_rule_black_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_rule_black_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_black_list_with_options(request, runtime)

    def describe_metric_rule_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_rule_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_count_with_options(request, runtime)

    def describe_metric_rule_list_with_options(self, request, runtime):
        """
        This topic provides an example on how to query all alert rules within your Alibaba Cloud account. The returned result shows that only one alert rule is found. The name of the alert rule is `Rule_01` and the ID is `applyTemplate344cfd42-0f32-4fd6-805a-88d7908a***`.
        

        @param request: DescribeMetricRuleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_state):
            query['AlertState'] = request.alert_state
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.enable_state):
            query['EnableState'] = request.enable_state
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_rule_list(self, request):
        """
        This topic provides an example on how to query all alert rules within your Alibaba Cloud account. The returned result shows that only one alert rule is found. The name of the alert rule is `Rule_01` and the ID is `applyTemplate344cfd42-0f32-4fd6-805a-88d7908a***`.
        

        @param request: DescribeMetricRuleListRequest

        @return: DescribeMetricRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_list_with_options(request, runtime)

    def describe_metric_rule_targets_with_options(self, request, runtime):
        """
        The parameters of the alert callback. The parameters are in the JSON format.
        

        @param request: DescribeMetricRuleTargetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_rule_targets(self, request):
        """
        The parameters of the alert callback. The parameters are in the JSON format.
        

        @param request: DescribeMetricRuleTargetsRequest

        @return: DescribeMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_targets_with_options(request, runtime)

    def describe_metric_rule_template_attribute_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeMetricRuleTemplateAttribute.
        

        @param request: DescribeMetricRuleTemplateAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricRuleTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTemplateAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_rule_template_attribute(self, request):
        """
        The operation that you want to perform. Set the value to DescribeMetricRuleTemplateAttribute.
        

        @param request: DescribeMetricRuleTemplateAttributeRequest

        @return: DescribeMetricRuleTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_template_attribute_with_options(request, runtime)

    def describe_metric_rule_template_list_with_options(self, request, runtime):
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        

        @param request: DescribeMetricRuleTemplateListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricRuleTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.history):
            query['History'] = request.history
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricRuleTemplateList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_rule_template_list(self, request):
        """
        The HTTP status code.
        >  The status code 200 indicates that the call was successful.
        

        @param request: DescribeMetricRuleTemplateListRequest

        @return: DescribeMetricRuleTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_template_list_with_options(request, runtime)

    def describe_metric_top_with_options(self, request, runtime):
        """
        The order in which data is sorted. Valid values:
        *   True: sorts data in ascending order.
        *   False (default value): sorts data in descending order.
        

        @param request: DescribeMetricTopRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMetricTopResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.express):
            query['Express'] = request.express
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetricTop',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricTopResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_metric_top(self, request):
        """
        The order in which data is sorted. Valid values:
        *   True: sorts data in ascending order.
        *   False (default value): sorts data in descending order.
        

        @param request: DescribeMetricTopRequest

        @return: DescribeMetricTopResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_top_with_options(request, runtime)

    def describe_monitor_group_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupCategories',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_group_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_categories_with_options(request, runtime)

    def describe_monitor_group_dynamic_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupDynamicRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_group_dynamic_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_dynamic_rules_with_options(request, runtime)

    def describe_monitor_group_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupInstanceAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_group_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_instance_attribute_with_options(request, runtime)

    def describe_monitor_group_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_group_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_instances_with_options(request, runtime)

    def describe_monitor_group_notify_policy_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroupNotifyPolicyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_group_notify_policy_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_group_notify_policy_list_with_options(request, runtime)

    def describe_monitor_groups_with_options(self, request, runtime):
        """
        This topic provides an example of how to query the application groups of the current account. The response shows that the current account has two application groups: `testGroup124` and `test123`.
        

        @param request: DescribeMonitorGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMonitorGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not UtilClient.is_unset(request.group_founder_tag_key):
            query['GroupFounderTagKey'] = request.group_founder_tag_key
        if not UtilClient.is_unset(request.group_founder_tag_value):
            query['GroupFounderTagValue'] = request.group_founder_tag_value
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.include_template_history):
            query['IncludeTemplateHistory'] = request.include_template_history
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorGroups',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_groups(self, request):
        """
        This topic provides an example of how to query the application groups of the current account. The response shows that the current account has two application groups: `testGroup124` and `test123`.
        

        @param request: DescribeMonitorGroupsRequest

        @return: DescribeMonitorGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_groups_with_options(request, runtime)

    def describe_monitor_resource_quota_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.show_used):
            query['ShowUsed'] = request.show_used
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorResourceQuotaAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_resource_quota_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_resource_quota_attribute_with_options(request, runtime)

    def describe_monitoring_agent_access_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringAgentAccessKey',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitoring_agent_access_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_access_key_with_options(request, runtime)

    def describe_monitoring_agent_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringAgentConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitoring_agent_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_config_with_options(request, runtime)

    def describe_monitoring_agent_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_host):
            query['AliyunHost'] = request.aliyun_host
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sysom_status):
            query['SysomStatus'] = request.sysom_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentHosts',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitoring_agent_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_hosts_with_options(request, runtime)

    def describe_monitoring_agent_processes_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeMonitoringAgentProcesses.
        

        @param request: DescribeMonitoringAgentProcessesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMonitoringAgentProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentProcesses',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitoring_agent_processes(self, request):
        """
        The operation that you want to perform. Set the value to DescribeMonitoringAgentProcesses.
        

        @param request: DescribeMonitoringAgentProcessesRequest

        @return: DescribeMonitoringAgentProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_processes_with_options(request, runtime)

    def describe_monitoring_agent_statuses_with_options(self, request, runtime):
        """
        The details of the execution error. Valid values:
        *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        

        @param request: DescribeMonitoringAgentStatusesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMonitoringAgentStatusesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_availability_task_id):
            query['HostAvailabilityTaskId'] = request.host_availability_task_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitoringAgentStatuses',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitoring_agent_statuses(self, request):
        """
        The details of the execution error. Valid values:
        *   `Command.ErrorCode.Fail.Downlaod.REGIN_ID`: Failed to obtain the region ID.
        *   `Command.ErrorCode.Fail.Downlaod.SYSAK`: Failed to download the .rpm package of System Analyse Kit (SysAK).
        *   `Command.ErrorCode.Fail.Downlaod.CMON_FILE`: Failed to download the CMON file.
        *   `Command.ErrorCode.Fail.Downlaod.BTF`: Failed to start SysAK because the BTF file is not found.
        *   `Command.ErrorCode.Fail.Start.SYSAK`: Failed to start SysAK due to an unknown error.
        

        @param request: DescribeMonitoringAgentStatusesRequest

        @return: DescribeMonitoringAgentStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_statuses_with_options(request, runtime)

    def describe_monitoring_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMonitoringConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitoring_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_config_with_options(request, runtime)

    def describe_product_resource_tag_key_list_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeProductResourceTagKeyList.
        

        @param request: DescribeProductResourceTagKeyListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeProductResourceTagKeyListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProductResourceTagKeyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductResourceTagKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_product_resource_tag_key_list(self, request):
        """
        The operation that you want to perform. Set the value to DescribeProductResourceTagKeyList.
        

        @param request: DescribeProductResourceTagKeyListRequest

        @return: DescribeProductResourceTagKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_product_resource_tag_key_list_with_options(request, runtime)

    def describe_products_of_active_metric_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeProductsOfActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_products_of_active_metric_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_products_of_active_metric_rule_with_options(request, runtime)

    def describe_project_meta_with_options(self, request, runtime):
        """
        The information obtained by this operation includes the service description, namespace, and tags.
        

        @param request: DescribeProjectMetaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeProjectMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProjectMeta',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProjectMetaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_project_meta(self, request):
        """
        The information obtained by this operation includes the service description, namespace, and tags.
        

        @param request: DescribeProjectMetaRequest

        @return: DescribeProjectMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_meta_with_options(request, runtime)

    def describe_site_monitor_attribute_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeSiteMonitorAttribute.
        

        @param request: DescribeSiteMonitorAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSiteMonitorAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_alert):
            query['IncludeAlert'] = request.include_alert
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_attribute(self, request):
        """
        The operation that you want to perform. Set the value to DescribeSiteMonitorAttribute.
        

        @param request: DescribeSiteMonitorAttributeRequest

        @return: DescribeSiteMonitorAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_attribute_with_options(request, runtime)

    def describe_site_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_data_with_options(request, runtime)

    def describe_site_monitor_ispcity_list_with_options(self, request, runtime):
        """
        This topic provides an example on how to query the detection points that are provided by China Unicom in Guiyang.
        

        @param request: DescribeSiteMonitorISPCityListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSiteMonitorISPCityListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.ipv4):
            query['IPV4'] = request.ipv4
        if not UtilClient.is_unset(request.ipv6):
            query['IPV6'] = request.ipv6
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorISPCityList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorISPCityListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_ispcity_list(self, request):
        """
        This topic provides an example on how to query the detection points that are provided by China Unicom in Guiyang.
        

        @param request: DescribeSiteMonitorISPCityListRequest

        @return: DescribeSiteMonitorISPCityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_ispcity_list_with_options(request, runtime)

    def describe_site_monitor_list_with_options(self, request, runtime):
        """
        The content of the HTTP request.
        

        @param request: DescribeSiteMonitorListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSiteMonitorListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_state):
            query['TaskState'] = request.task_state
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_list(self, request):
        """
        The content of the HTTP request.
        

        @param request: DescribeSiteMonitorListRequest

        @return: DescribeSiteMonitorListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_list_with_options(request, runtime)

    def describe_site_monitor_log_with_options(self, request, runtime):
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to query the logs of an instant test task whose ID is `afa5c3ce-f944-4363-9edb-ce919a29****`.
        

        @param request: DescribeSiteMonitorLogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSiteMonitorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorLog',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_log(self, request):
        """
        You can create an instant test task only by using the Alibaba Cloud account that you used to enable Network Analysis and Monitoring. For more information, see [Billing of Network Analysis and Monitoring](~~341649~~).
        This topic provides an example to show how to query the logs of an instant test task whose ID is `afa5c3ce-f944-4363-9edb-ce919a29****`.
        

        @param request: DescribeSiteMonitorLogRequest

        @return: DescribeSiteMonitorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_log_with_options(request, runtime)

    def describe_site_monitor_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSiteMonitorQuota',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_quota_with_options(request, runtime)

    def describe_site_monitor_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSiteMonitorStatistics',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_monitor_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_statistics_with_options(request, runtime)

    def describe_system_event_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventAttribute',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_event_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_attribute_with_options(request, runtime)

    def describe_system_event_count_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeSystemEventCount.
        

        @param request: DescribeSystemEventCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSystemEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventCount',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_event_count(self, request):
        """
        The operation that you want to perform. Set the value to DescribeSystemEventCount.
        

        @param request: DescribeSystemEventCountRequest

        @return: DescribeSystemEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_count_with_options(request, runtime)

    def describe_system_event_histogram_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemEventHistogram',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_event_histogram(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_histogram_with_options(request, runtime)

    def describe_system_event_meta_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSystemEventMetaList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_event_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_meta_list_with_options(request, runtime)

    def describe_tag_key_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagKeyList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_key_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_key_list_with_options(request, runtime)

    def describe_tag_value_list_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to DescribeTagValueList.
        

        @param request: DescribeTagValueListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagValueListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagValueList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagValueListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_value_list(self, request):
        """
        The operation that you want to perform. Set the value to DescribeTagValueList.
        

        @param request: DescribeTagValueListRequest

        @return: DescribeTagValueListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_value_list_with_options(request, runtime)

    def describe_unhealthy_host_availability_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUnhealthyHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_unhealthy_host_availability(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_unhealthy_host_availability_with_options(request, runtime)

    def disable_active_metric_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_active_metric_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_active_metric_rule_with_options(request, runtime)

    def disable_event_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_event_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_event_rules_with_options(request, runtime)

    def disable_host_availability_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_host_availability(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_host_availability_with_options(request, runtime)

    def disable_metric_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_metric_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_metric_rules_with_options(request, runtime)

    def disable_site_monitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_site_monitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_site_monitors_with_options(request, runtime)

    def enable_active_metric_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableActiveMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_active_metric_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_active_metric_rule_with_options(request, runtime)

    def enable_event_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableEventRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_event_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_event_rules_with_options(request, runtime)

    def enable_host_availability_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_host_availability(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_host_availability_with_options(request, runtime)

    def enable_metric_rule_black_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_metric_rule_black_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_metric_rule_black_list_with_options(request, runtime)

    def enable_metric_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_metric_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_metric_rules_with_options(request, runtime)

    def enable_site_monitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSiteMonitors',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_site_monitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_site_monitors_with_options(request, runtime)

    def install_monitoring_agent_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: InstallMonitoringAgentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallMonitoringAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.install_command):
            query['InstallCommand'] = request.install_command
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallMonitoringAgent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.InstallMonitoringAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def install_monitoring_agent(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: InstallMonitoringAgentRequest

        @return: InstallMonitoringAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_monitoring_agent_with_options(request, runtime)

    def modify_group_monitoring_agent_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupMonitoringAgentProcess',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_group_monitoring_agent_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_group_monitoring_agent_process_with_options(request, runtime)

    def modify_host_availability_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: ModifyHostAvailabilityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHostAvailabilityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not UtilClient.is_unset(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not UtilClient.is_unset(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not UtilClient.is_unset(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostAvailability',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_host_availability(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: ModifyHostAvailabilityRequest

        @return: ModifyHostAvailabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_availability_with_options(request, runtime)

    def modify_host_info_with_options(self, request, runtime):
        """
        ***\
        

        @param request: ModifyHostInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHostInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostInfo',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_host_info(self, request):
        """
        ***\
        

        @param request: ModifyHostInfoRequest

        @return: ModifyHostInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_info_with_options(request, runtime)

    def modify_hybrid_monitor_namespace_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: ModifyHybridMonitorNamespaceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHybridMonitorNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorNamespace',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hybrid_monitor_namespace(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: ModifyHybridMonitorNamespaceRequest

        @return: ModifyHybridMonitorNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_monitor_namespace_with_options(request, runtime)

    def modify_hybrid_monitor_slsgroup_with_options(self, request, runtime):
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        

        @param request: ModifyHybridMonitorSLSGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHybridMonitorSLSGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not UtilClient.is_unset(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not UtilClient.is_unset(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorSLSGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hybrid_monitor_slsgroup(self, request):
        """
        The Log Service projects.
        Valid values of N: 1 to 25.
        

        @param request: ModifyHybridMonitorSLSGroupRequest

        @return: ModifyHybridMonitorSLSGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_monitor_slsgroup_with_options(request, runtime)

    def modify_hybrid_monitor_task_with_options(self, request, runtime):
        """
        The alias of the extended field that specifies the result of basic operations performed on aggregation results.
        

        @param request: ModifyHybridMonitorTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyHybridMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not UtilClient.is_unset(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHybridMonitorTask',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hybrid_monitor_task(self, request):
        """
        The alias of the extended field that specifies the result of basic operations performed on aggregation results.
        

        @param request: ModifyHybridMonitorTaskRequest

        @return: ModifyHybridMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hybrid_monitor_task_with_options(request, runtime)

    def modify_metric_rule_black_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not UtilClient.is_unset(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMetricRuleBlackList',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_metric_rule_black_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_metric_rule_black_list_with_options(request, runtime)

    def modify_metric_rule_template_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: ModifyMetricRuleTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyMetricRuleTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMetricRuleTemplate',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_metric_rule_template(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: ModifyMetricRuleTemplateRequest

        @return: ModifyMetricRuleTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_metric_rule_template_with_options(request, runtime)

    def modify_monitor_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMonitorGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_monitor_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_monitor_group_with_options(request, runtime)

    def modify_monitor_group_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMonitorGroupInstances',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_monitor_group_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_monitor_group_instances_with_options(request, runtime)

    def modify_site_monitor_with_options(self, request, runtime):
        """
        The number of site monitoring tasks.
        

        @param request: ModifySiteMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySiteMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not UtilClient.is_unset(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySiteMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifySiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_site_monitor(self, request):
        """
        The number of site monitoring tasks.
        

        @param request: ModifySiteMonitorRequest

        @return: ModifySiteMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_site_monitor_with_options(request, runtime)

    def open_cms_service_with_options(self, runtime):
        """
        @deprecated
        

        @param request: OpenCmsServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenCmsServiceResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenCmsService',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.OpenCmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_cms_service(self):
        """
        @deprecated
        

        @return: OpenCmsServiceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.open_cms_service_with_options(runtime)

    def put_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.channels):
            query['Channels'] = request.channels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutContact',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactResponse(),
            self.call_api(params, req, runtime)
        )

    def put_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_contact_with_options(request, runtime)

    def put_contact_group_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to PutContactGroup.
        

        @param request: PutContactGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutContactGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_names):
            query['ContactNames'] = request.contact_names
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.enable_subscribed):
            query['EnableSubscribed'] = request.enable_subscribed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutContactGroup',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def put_contact_group(self, request):
        """
        The operation that you want to perform. Set the value to PutContactGroup.
        

        @param request: PutContactGroupRequest

        @return: PutContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_contact_group_with_options(request, runtime)

    def put_custom_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomEvent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventResponse(),
            self.call_api(params, req, runtime)
        )

    def put_custom_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_custom_event_with_options(request, runtime)

    def put_custom_event_rule_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to PutCustomEventRule.
        

        @param request: PutCustomEventRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutCustomEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomEventRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_custom_event_rule(self, request):
        """
        The operation that you want to perform. Set the value to PutCustomEventRule.
        

        @param request: PutCustomEventRuleRequest

        @return: PutCustomEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_event_rule_with_options(request, runtime)

    def put_custom_metric_with_options(self, request, runtime):
        """
        The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21.
        Set the value to a collection of key-value pairs. Format:`{"Key":"Value"}`.
        The key or value must be 1 to 64 bytes in length. Excessive characters are truncated.
        The key or value can contain letters, digits, periods (.), hyphens (-), underscores (\\_), forward slashes (/), and backslashes (\\\\).
        >  Dimensions must be formatted as a JSON string in a specified order.
        

        @param request: PutCustomMetricRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutCustomMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_list):
            query['MetricList'] = request.metric_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomMetric',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def put_custom_metric(self, request):
        """
        The dimensions that specify the resources whose monitoring data you want to query. Valid values of N: 1 to 21.
        Set the value to a collection of key-value pairs. Format:`{"Key":"Value"}`.
        The key or value must be 1 to 64 bytes in length. Excessive characters are truncated.
        The key or value can contain letters, digits, periods (.), hyphens (-), underscores (\\_), forward slashes (/), and backslashes (\\\\).
        >  Dimensions must be formatted as a JSON string in a specified order.
        

        @param request: PutCustomMetricRequest

        @return: PutCustomMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_with_options(request, runtime)

    def put_custom_metric_rule_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to PutCustomMetricRule.
        

        @param request: PutCustomMetricRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutCustomMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutCustomMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_custom_metric_rule(self, request):
        """
        The operation that you want to perform. Set the value to PutCustomMetricRule.
        

        @param request: PutCustomMetricRuleRequest

        @return: PutCustomMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_rule_with_options(request, runtime)

    def put_event_rule_with_options(self, request, runtime):
        """
        The ID of the application group to which the event-triggered alert rule belongs.
        

        @param request: PutEventRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.event_pattern):
            query['EventPattern'] = request.event_pattern
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_event_rule(self, request):
        """
        The ID of the application group to which the event-triggered alert rule belongs.
        

        @param request: PutEventRuleRequest

        @return: PutEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_event_rule_with_options(request, runtime)

    def put_event_rule_targets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not UtilClient.is_unset(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not UtilClient.is_unset(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
        if not UtilClient.is_unset(request.open_api_parameters):
            query['OpenApiParameters'] = request.open_api_parameters
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sls_parameters):
            query['SlsParameters'] = request.sls_parameters
        if not UtilClient.is_unset(request.webhook_parameters):
            query['WebhookParameters'] = request.webhook_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEventRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def put_event_rule_targets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_event_rule_targets_with_options(request, runtime)

    def put_exporter_output_with_options(self, request, runtime):
        """
        > The monitoring data can be exported only to Log Service. More services will be supported in the future.
        

        @param request: PutExporterOutputRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutExporterOutputResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_json):
            query['ConfigJson'] = request.config_json
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.dest_name):
            query['DestName'] = request.dest_name
        if not UtilClient.is_unset(request.dest_type):
            query['DestType'] = request.dest_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutExporterOutput',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterOutputResponse(),
            self.call_api(params, req, runtime)
        )

    def put_exporter_output(self, request):
        """
        > The monitoring data can be exported only to Log Service. More services will be supported in the future.
        

        @param request: PutExporterOutputRequest

        @return: PutExporterOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_exporter_output_with_options(request, runtime)

    def put_exporter_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.dst_names):
            query['DstNames'] = request.dst_names
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.target_windows):
            query['TargetWindows'] = request.target_windows
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutExporterRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_exporter_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_exporter_rule_with_options(request, runtime)

    def put_group_metric_rule_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: PutGroupMetricRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutGroupMetricRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.extra_dimension_json):
            query['ExtraDimensionJson'] = request.extra_dimension_json
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutGroupMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_group_metric_rule(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: PutGroupMetricRuleRequest

        @return: PutGroupMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_group_metric_rule_with_options(request, runtime)

    def put_hybrid_monitor_metric_data_with_options(self, request, runtime):
        """
        The tag value of the metric.
        Valid values of N: 1 to 100.
        >  You must specify a key and a value for a tag at the same time.
        

        @param request: PutHybridMonitorMetricDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutHybridMonitorMetricDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metric_list):
            query['MetricList'] = request.metric_list
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutHybridMonitorMetricData',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutHybridMonitorMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def put_hybrid_monitor_metric_data(self, request):
        """
        The tag value of the metric.
        Valid values of N: 1 to 100.
        >  You must specify a key and a value for a tag at the same time.
        

        @param request: PutHybridMonitorMetricDataRequest

        @return: PutHybridMonitorMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_hybrid_monitor_metric_data_with_options(request, runtime)

    def put_log_monitor_with_options(self, request, runtime):
        """
        The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        

        @param request: PutLogMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutLogMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aggregates):
            query['Aggregates'] = request.aggregates
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.groupbys):
            query['Groupbys'] = request.groupbys
        if not UtilClient.is_unset(request.log_id):
            query['LogId'] = request.log_id
        if not UtilClient.is_unset(request.metric_express):
            query['MetricExpress'] = request.metric_express
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        if not UtilClient.is_unset(request.tumblingwindows):
            query['Tumblingwindows'] = request.tumblingwindows
        if not UtilClient.is_unset(request.unit):
            query['Unit'] = request.unit
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        if not UtilClient.is_unset(request.value_filter_relation):
            query['ValueFilterRelation'] = request.value_filter_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLogMonitor',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutLogMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def put_log_monitor(self, request):
        """
        The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        

        @param request: PutLogMonitorRequest

        @return: PutLogMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_log_monitor_with_options(request, runtime)

    def put_metric_rule_targets_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: PutMetricRuleTargetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutMetricRuleTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMetricRuleTargets',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def put_metric_rule_targets(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: PutMetricRuleTargetsRequest

        @return: PutMetricRuleTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_metric_rule_targets_with_options(request, runtime)

    def put_monitor_group_dynamic_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_rules):
            query['GroupRules'] = request.group_rules
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMonitorGroupDynamicRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitorGroupDynamicRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_monitor_group_dynamic_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_monitor_group_dynamic_rule_with_options(request, runtime)

    def put_monitoring_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.enable_install_agent_new_ecs):
            query['EnableInstallAgentNewECS'] = request.enable_install_agent_new_ecs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMonitoringConfig',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitoringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def put_monitoring_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_monitoring_config_with_options(request, runtime)

    def put_resource_metric_rule_with_options(self, tmp_req, runtime):
        """
        The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        >  If an alert is not cleared within the mute period, a new alert notification is sent when the mute period ends.
        

        @param tmp_req: PutResourceMetricRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutResourceMetricRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20190101_models.PutResourceMetricRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.composite_expression):
            request.composite_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.composite_expression, 'CompositeExpression', 'json')
        if not UtilClient.is_unset(tmp_req.prometheus):
            request.prometheus_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prometheus, 'Prometheus', 'json')
        query = {}
        if not UtilClient.is_unset(request.composite_expression_shrink):
            query['CompositeExpression'] = request.composite_expression_shrink
        if not UtilClient.is_unset(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not UtilClient.is_unset(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not UtilClient.is_unset(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not UtilClient.is_unset(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.prometheus_shrink):
            query['Prometheus'] = request.prometheus_shrink
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        if not UtilClient.is_unset(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRule',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def put_resource_metric_rule(self, request):
        """
        The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        >  If an alert is not cleared within the mute period, a new alert notification is sent when the mute period ends.
        

        @param request: PutResourceMetricRuleRequest

        @return: PutResourceMetricRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rule_with_options(request, runtime)

    def put_resource_metric_rules_with_options(self, request, runtime):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: PutResourceMetricRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutResourceMetricRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutResourceMetricRules',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def put_resource_metric_rules(self, request):
        """
        Indicates whether the call was successful. Valid values:
        *   true: The call was successful.
        *   false: The call failed.
        

        @param request: PutResourceMetricRulesRequest

        @return: PutResourceMetricRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rules_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    def send_dry_run_system_event_with_options(self, request, runtime):
        """
        The name of the cloud service.
        >  For information about the system events supported by Cloud Monitor for Alibaba Cloud services, see [System events](~~167388~~).
        

        @param request: SendDryRunSystemEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendDryRunSystemEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_content):
            query['EventContent'] = request.event_content
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendDryRunSystemEvent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.SendDryRunSystemEventResponse(),
            self.call_api(params, req, runtime)
        )

    def send_dry_run_system_event(self, request):
        """
        The name of the cloud service.
        >  For information about the system events supported by Cloud Monitor for Alibaba Cloud services, see [System events](~~167388~~).
        

        @param request: SendDryRunSystemEventRequest

        @return: SendDryRunSystemEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_dry_run_system_event_with_options(request, runtime)

    def uninstall_monitoring_agent_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to UninstallMonitoringAgent.
        

        @param request: UninstallMonitoringAgentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallMonitoringAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallMonitoringAgent',
            version='2019-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20190101_models.UninstallMonitoringAgentResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_monitoring_agent(self, request):
        """
        The operation that you want to perform. Set the value to UninstallMonitoringAgent.
        

        @param request: UninstallMonitoringAgentRequest

        @return: UninstallMonitoringAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_monitoring_agent_with_options(request, runtime)
