# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ess20140828 import models as ess_20140828_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'ess.aliyuncs.com',
            'cn-beijing': 'ess.aliyuncs.com',
            'cn-hangzhou': 'ess.aliyuncs.com',
            'cn-shanghai': 'ess.aliyuncs.com',
            'cn-shenzhen': 'ess.aliyuncs.com',
            'cn-hongkong': 'ess.aliyuncs.com',
            'ap-southeast-1': 'ess.aliyuncs.com',
            'us-west-1': 'ess.aliyuncs.com',
            'us-east-1': 'ess.aliyuncs.com',
            'cn-shanghai-finance-1': 'ess.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ess.aliyuncs.com',
            'cn-north-2-gov-1': 'ess.aliyuncs.com',
            'ap-northeast-2-pop': 'ess.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ess.aliyuncs.com',
            'cn-beijing-finance-pop': 'ess.aliyuncs.com',
            'cn-beijing-gov-1': 'ess.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ess.aliyuncs.com',
            'cn-edge-1': 'ess.aliyuncs.com',
            'cn-fujian': 'ess.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ess.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ess.aliyuncs.com',
            'cn-hangzhou-finance': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ess.aliyuncs.com',
            'cn-hangzhou-test-306': 'ess.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ess.aliyuncs.com',
            'cn-qingdao-nebula': 'ess.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ess.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ess.aliyuncs.com',
            'cn-shanghai-inner': 'ess.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ess.aliyuncs.com',
            'cn-shenzhen-inner': 'ess.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ess.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ess.aliyuncs.com',
            'cn-wuhan': 'ess.aliyuncs.com',
            'cn-yushanfang': 'ess.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ess.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ess.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ess.aliyuncs.com',
            'eu-west-1-oxs': 'ess.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'ess.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_alb_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.AttachAlbServerGroupsResponse(),
            self.do_rpcrequest('AttachAlbServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_alb_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_alb_server_groups_with_options(request, runtime)

    def attach_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.AttachDBInstancesResponse(),
            self.do_rpcrequest('AttachDBInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_dbinstances_with_options(request, runtime)

    def attach_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.AttachInstancesResponse(),
            self.do_rpcrequest('AttachInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    def attach_load_balancers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.AttachLoadBalancersResponse(),
            self.do_rpcrequest('AttachLoadBalancers', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_load_balancers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_load_balancers_with_options(request, runtime)

    def attach_vserver_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.AttachVServerGroupsResponse(),
            self.do_rpcrequest('AttachVServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_vserver_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_vserver_groups_with_options(request, runtime)

    def complete_lifecycle_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CompleteLifecycleActionResponse(),
            self.do_rpcrequest('CompleteLifecycleAction', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_lifecycle_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_lifecycle_action_with_options(request, runtime)

    def create_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateAlarmResponse(),
            self.do_rpcrequest('CreateAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    def create_lifecycle_hook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateLifecycleHookResponse(),
            self.do_rpcrequest('CreateLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_lifecycle_hook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_hook_with_options(request, runtime)

    def create_notification_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateNotificationConfigurationResponse(),
            self.do_rpcrequest('CreateNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_notification_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_notification_configuration_with_options(request, runtime)

    def create_scaling_configuration_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ess_20140828_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateScalingConfigurationResponse(),
            self.do_rpcrequest('CreateScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    def create_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateScalingGroupResponse(),
            self.do_rpcrequest('CreateScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    def create_scaling_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateScalingRuleResponse(),
            self.do_rpcrequest('CreateScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    def create_scheduled_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.CreateScheduledTaskResponse(),
            self.do_rpcrequest('CreateScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scheduled_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    def deactivate_scaling_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeactivateScalingConfigurationResponse(),
            self.do_rpcrequest('DeactivateScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactivate_scaling_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deactivate_scaling_configuration_with_options(request, runtime)

    def delete_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteAlarmResponse(),
            self.do_rpcrequest('DeleteAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    def delete_lifecycle_hook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteLifecycleHookResponse(),
            self.do_rpcrequest('DeleteLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_lifecycle_hook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_hook_with_options(request, runtime)

    def delete_notification_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteNotificationConfigurationResponse(),
            self.do_rpcrequest('DeleteNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_notification_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_configuration_with_options(request, runtime)

    def delete_scaling_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteScalingConfigurationResponse(),
            self.do_rpcrequest('DeleteScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    def delete_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteScalingGroupResponse(),
            self.do_rpcrequest('DeleteScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    def delete_scaling_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteScalingRuleResponse(),
            self.do_rpcrequest('DeleteScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    def delete_scheduled_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DeleteScheduledTaskResponse(),
            self.do_rpcrequest('DeleteScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scheduled_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    def describe_alarms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeAlarmsResponse(),
            self.do_rpcrequest('DescribeAlarms', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    def describe_lifecycle_actions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeLifecycleActionsResponse(),
            self.do_rpcrequest('DescribeLifecycleActions', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lifecycle_actions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_actions_with_options(request, runtime)

    def describe_lifecycle_hooks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeLifecycleHooksResponse(),
            self.do_rpcrequest('DescribeLifecycleHooks', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_lifecycle_hooks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_hooks_with_options(request, runtime)

    def describe_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeLimitationResponse(),
            self.do_rpcrequest('DescribeLimitation', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_limitation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    def describe_notification_configurations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeNotificationConfigurationsResponse(),
            self.do_rpcrequest('DescribeNotificationConfigurations', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_notification_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_configurations_with_options(request, runtime)

    def describe_notification_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeNotificationTypesResponse(),
            self.do_rpcrequest('DescribeNotificationTypes', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_notification_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_types_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_scaling_activities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeScalingActivitiesResponse(),
            self.do_rpcrequest('DescribeScalingActivities', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_activities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    def describe_scaling_activity_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeScalingActivityDetailResponse(),
            self.do_rpcrequest('DescribeScalingActivityDetail', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_activity_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    def describe_scaling_configurations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeScalingConfigurationsResponse(),
            self.do_rpcrequest('DescribeScalingConfigurations', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    def describe_scaling_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeScalingInstancesResponse(),
            self.do_rpcrequest('DescribeScalingInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    def describe_scaling_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeScalingRulesResponse(),
            self.do_rpcrequest('DescribeScalingRules', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    def describe_scheduled_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DescribeScheduledTasksResponse(),
            self.do_rpcrequest('DescribeScheduledTasks', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scheduled_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    def detach_alb_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DetachAlbServerGroupsResponse(),
            self.do_rpcrequest('DetachAlbServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_alb_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_alb_server_groups_with_options(request, runtime)

    def detach_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DetachDBInstancesResponse(),
            self.do_rpcrequest('DetachDBInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_dbinstances_with_options(request, runtime)

    def detach_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DetachInstancesResponse(),
            self.do_rpcrequest('DetachInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    def detach_load_balancers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DetachLoadBalancersResponse(),
            self.do_rpcrequest('DetachLoadBalancers', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_load_balancers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_load_balancers_with_options(request, runtime)

    def detach_vserver_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DetachVServerGroupsResponse(),
            self.do_rpcrequest('DetachVServerGroups', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_vserver_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_vserver_groups_with_options(request, runtime)

    def disable_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DisableAlarmResponse(),
            self.do_rpcrequest('DisableAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    def disable_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.DisableScalingGroupResponse(),
            self.do_rpcrequest('DisableScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    def enable_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.EnableAlarmResponse(),
            self.do_rpcrequest('EnableAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    def enable_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.EnableScalingGroupResponse(),
            self.do_rpcrequest('EnableScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    def enter_standby_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.EnterStandbyResponse(),
            self.do_rpcrequest('EnterStandby', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enter_standby(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enter_standby_with_options(request, runtime)

    def execute_scaling_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ExecuteScalingRuleResponse(),
            self.do_rpcrequest('ExecuteScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    def exit_standby_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ExitStandbyResponse(),
            self.do_rpcrequest('ExitStandby', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def exit_standby(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exit_standby_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            ess_20140828_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            ess_20140828_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def modify_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyAlarmResponse(),
            self.do_rpcrequest('ModifyAlarm', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_alarm_with_options(request, runtime)

    def modify_lifecycle_hook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyLifecycleHookResponse(),
            self.do_rpcrequest('ModifyLifecycleHook', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_lifecycle_hook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_hook_with_options(request, runtime)

    def modify_notification_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyNotificationConfigurationResponse(),
            self.do_rpcrequest('ModifyNotificationConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_notification_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_notification_configuration_with_options(request, runtime)

    def modify_scaling_configuration_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ess_20140828_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyScalingConfigurationResponse(),
            self.do_rpcrequest('ModifyScalingConfiguration', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_configuration_with_options(request, runtime)

    def modify_scaling_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyScalingGroupResponse(),
            self.do_rpcrequest('ModifyScalingGroup', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    def modify_scaling_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyScalingRuleResponse(),
            self.do_rpcrequest('ModifyScalingRule', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    def modify_scheduled_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ModifyScheduledTaskResponse(),
            self.do_rpcrequest('ModifyScheduledTask', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scheduled_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    def rebalance_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.RebalanceInstancesResponse(),
            self.do_rpcrequest('RebalanceInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rebalance_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebalance_instances_with_options(request, runtime)

    def record_lifecycle_action_heartbeat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.RecordLifecycleActionHeartbeatResponse(),
            self.do_rpcrequest('RecordLifecycleActionHeartbeat', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def record_lifecycle_action_heartbeat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.record_lifecycle_action_heartbeat_with_options(request, runtime)

    def remove_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.RemoveInstancesResponse(),
            self.do_rpcrequest('RemoveInstances', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    def resume_processes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ResumeProcessesResponse(),
            self.do_rpcrequest('ResumeProcesses', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_processes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_processes_with_options(request, runtime)

    def scale_with_adjustment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.ScaleWithAdjustmentResponse(),
            self.do_rpcrequest('ScaleWithAdjustment', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def scale_with_adjustment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scale_with_adjustment_with_options(request, runtime)

    def set_group_deletion_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.SetGroupDeletionProtectionResponse(),
            self.do_rpcrequest('SetGroupDeletionProtection', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_deletion_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_deletion_protection_with_options(request, runtime)

    def set_instance_health_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.SetInstanceHealthResponse(),
            self.do_rpcrequest('SetInstanceHealth', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_instance_health(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instance_health_with_options(request, runtime)

    def set_instances_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.SetInstancesProtectionResponse(),
            self.do_rpcrequest('SetInstancesProtection', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_instances_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instances_protection_with_options(request, runtime)

    def suspend_processes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.SuspendProcessesResponse(),
            self.do_rpcrequest('SuspendProcesses', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_processes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_processes_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            ess_20140828_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def verify_authentication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.VerifyAuthenticationResponse(),
            self.do_rpcrequest('VerifyAuthentication', '2014-08-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_authentication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    def verify_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ess_20140828_models.VerifyUserResponse(),
            self.do_rpcrequest('VerifyUser', '2014-08-28', 'HTTPS', 'POST', 'AK', 'none', req, runtime)
        )

    def verify_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_user_with_options(request, runtime)
