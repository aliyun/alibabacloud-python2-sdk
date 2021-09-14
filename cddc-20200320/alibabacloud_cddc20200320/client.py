# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cddc20200320 import models as cddc_20200320_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cddc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def modify_dbinstance_switch_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse(),
            self.do_rpcrequest('ModifyDBInstanceSwitchWeight', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_switch_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_switch_weight_with_options(request, runtime)

    def describe_available_dedicated_host_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse(),
            self.do_rpcrequest('DescribeAvailableDedicatedHostZones', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    def describe_dedicated_host_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostGroupsResponse(),
            self.do_rpcrequest('DescribeDedicatedHostGroups', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    def describe_my_base_host_over_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeMyBaseHostOverViewResponse(),
            self.do_rpcrequest('DescribeMyBaseHostOverView', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_my_base_host_over_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_my_base_host_over_view_with_options(request, runtime)

    def describe_brief_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeBriefDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeBriefDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_brief_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_brief_dedicated_hosts_with_options(request, runtime)

    def describe_dedicated_resource_advisor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse(),
            self.do_rpcrequest('DescribeDedicatedResourceAdvisor', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_resource_advisor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_resource_advisor_with_options(request, runtime)

    def describe_list_user_backup_file_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeListUserBackupFileRecordResponse(),
            self.do_rpcrequest('DescribeListUserBackupFileRecord', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_list_user_backup_file_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_list_user_backup_file_record_with_options(request, runtime)

    def create_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostAccountResponse(),
            self.do_rpcrequest('CreateDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    def delete_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostAccountResponse(),
            self.do_rpcrequest('DeleteDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    def delete_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostGroupResponse(),
            self.do_rpcrequest('DeleteDedicatedHostGroup', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    def check_user_if_authorise_my_base_system_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse(),
            self.do_rpcrequest('CheckUserIfAuthoriseMyBaseSystemRole', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_user_if_authorise_my_base_system_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_user_if_authorise_my_base_system_role_with_options(request, runtime)

    def describe_schedule_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleInstanceResponse(),
            self.do_rpcrequest('DescribeScheduleInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_instance_with_options(request, runtime)

    def excute_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ExcuteScheduleResponse(),
            self.do_rpcrequest('ExcuteSchedule', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def excute_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.excute_schedule_with_options(request, runtime)

    def replace_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ReplaceDedicatedHostResponse(),
            self.do_rpcrequest('ReplaceDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    def modify_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAccountResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    def describe_host_ecs_level_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostEcsLevelInfoResponse(),
            self.do_rpcrequest('DescribeHostEcsLevelInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_ecs_level_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_host_ecs_level_info_with_options(request, runtime)

    def allocate_host_instance_cross_vpc_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse(),
            self.do_rpcrequest('AllocateHostInstanceCrossVpcVip', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_host_instance_cross_vpc_vip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_host_instance_cross_vpc_vip_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_dedicated_host_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostDisksResponse(),
            self.do_rpcrequest('DescribeDedicatedHostDisks', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_disks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_disks_with_options(request, runtime)

    def describe_my_base_instance_over_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse(),
            self.do_rpcrequest('DescribeMyBaseInstanceOverView', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_my_base_instance_over_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_my_base_instance_over_view_with_options(request, runtime)

    def modify_schedule_method_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyScheduleMethodResponse(),
            self.do_rpcrequest('ModifyScheduleMethod', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_schedule_method(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_schedule_method_with_options(request, runtime)

    def describe_available_dedicated_host_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse(),
            self.do_rpcrequest('DescribeAvailableDedicatedHostClasses', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    def describe_check_user_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeCheckUserBackupFileResponse(),
            self.do_rpcrequest('DescribeCheckUserBackupFile', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_user_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_check_user_backup_file_with_options(request, runtime)

    def modify_dedicated_host_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostPasswordResponse(),
            self.do_rpcrequest('ModifyDedicatedHostPassword', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_password_with_options(request, runtime)

    def describe_schedule_methods_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleMethodsResponse(),
            self.do_rpcrequest('DescribeScheduleMethods', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_methods(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_methods_with_options(request, runtime)

    def clear_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ClearDedicatedHostResponse(),
            self.do_rpcrequest('ClearDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    def delete_user_backup_file_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteUserBackupFileRecordResponse(),
            self.do_rpcrequest('DeleteUserBackupFileRecord', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_backup_file_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_backup_file_record_with_options(request, runtime)

    def describe_evaluate_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeEvaluateDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_dedicated_hosts_with_options(request, runtime)

    def describe_host_instance_monitor_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse(),
            self.do_rpcrequest('DescribeHostInstanceMonitorInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_instance_monitor_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_host_instance_monitor_info_with_options(request, runtime)

    def describe_dedicated_host_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostMetricResponse(),
            self.do_rpcrequest('DescribeDedicatedHostMetric', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_metric_with_options(request, runtime)

    def create_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostResponse(),
            self.do_rpcrequest('CreateDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    def describe_dedicated_instance_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedInstanceMetricResponse(),
            self.do_rpcrequest('DescribeDedicatedInstanceMetric', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_instance_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_instance_metric_with_options(request, runtime)

    def describe_cross_vpc_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeCrossVpcInstanceResponse(),
            self.do_rpcrequest('DescribeCrossVpcInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_vpc_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_vpc_instance_with_options(request, runtime)

    def modify_dedicated_host_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostClassResponse(),
            self.do_rpcrequest('ModifyDedicatedHostClass', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_class_with_options(request, runtime)

    def describe_dedicated_hosts_check_in_bastion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse(),
            self.do_rpcrequest('DescribeDedicatedHostsCheckInBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts_check_in_bastion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_check_in_bastion_with_options(request, runtime)

    def drop_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DropDedicatedHostUserResponse(),
            self.do_rpcrequest('DropDedicatedHostUser', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    def describe_dedicated_hosts_in_bastion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsInBastionResponse(),
            self.do_rpcrequest('DescribeDedicatedHostsInBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts_in_bastion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_in_bastion_with_options(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostGroupAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    def query_host_instance_console_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostInstanceConsoleInfoResponse(),
            self.do_rpcrequest('QueryHostInstanceConsoleInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_host_instance_console_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_host_instance_console_info_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def query_host_base_info_by_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostBaseInfoByInstanceResponse(),
            self.do_rpcrequest('QueryHostBaseInfoByInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_host_base_info_by_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_host_base_info_by_instance_with_options(request, runtime)

    def describe_dedicated_instance_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse(),
            self.do_rpcrequest('DescribeDedicatedInstanceDistribution', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_instance_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_instance_distribution_with_options(request, runtime)

    def describe_schedule_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleHostResponse(),
            self.do_rpcrequest('DescribeScheduleHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_host_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def create_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostGroupResponse(),
            self.do_rpcrequest('CreateDedicatedHostGroup', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    def add_hosts_to_bastion_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AddHostsToBastionResponse(),
            self.do_rpcrequest('AddHostsToBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_hosts_to_bastion(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_hosts_to_bastion_with_options(request, runtime)

    def attach_hosts_to_bastion_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AttachHostsToBastionUserResponse(),
            self.do_rpcrequest('AttachHostsToBastionUser', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_hosts_to_bastion_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_hosts_to_bastion_user_with_options(request, runtime)

    def describe_evaluate_dedicated_hosts_for_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse(),
            self.do_rpcrequest('DescribeEvaluateDedicatedHostsForInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_dedicated_hosts_for_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_dedicated_hosts_for_instance_with_options(request, runtime)

    def restart_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.RestartDedicatedHostResponse(),
            self.do_rpcrequest('RestartDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    def describe_dedicated_host_health_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostHealthResponse(),
            self.do_rpcrequest('DescribeDedicatedHostHealth', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_health(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_health_with_options(request, runtime)

    def describe_host_web_shell_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostWebShellResponse(),
            self.do_rpcrequest('DescribeHostWebShell', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_web_shell(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_host_web_shell_with_options(request, runtime)

    def describe_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostAttributeResponse(),
            self.do_rpcrequest('DescribeDedicatedHostAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)
