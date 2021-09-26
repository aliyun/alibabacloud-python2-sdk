# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_dbaudit20180320 import models as yundun_dbaudit_20180320_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_log_mask_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AddLogMaskConfigResponse(),
            self.do_rpcrequest('AddLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_log_mask_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_log_mask_config_with_options(request, runtime)

    def associate_db_to_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AssociateDbToRuleResponse(),
            self.do_rpcrequest('AssociateDbToRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_db_to_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_db_to_rule_with_options(request, runtime)

    def associate_rule_to_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.AssociateRuleToDbResponse(),
            self.do_rpcrequest('AssociateRuleToDb', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_rule_to_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_rule_to_db_with_options(request, runtime)

    def change_agent_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeAgentStatusResponse(),
            self.do_rpcrequest('ChangeAgentStatus', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_agent_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_agent_status_with_options(request, runtime)

    def change_log_mask_config_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeLogMaskConfigStateResponse(),
            self.do_rpcrequest('ChangeLogMaskConfigState', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_log_mask_config_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_log_mask_config_state_with_options(request, runtime)

    def change_rule_priority_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeRulePriorityResponse(),
            self.do_rpcrequest('ChangeRulePriority', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_rule_priority(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_rule_priority_with_options(request, runtime)

    def change_rule_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ChangeRuleStatusResponse(),
            self.do_rpcrequest('ChangeRuleStatus', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_rule_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_rule_status_with_options(request, runtime)

    def check_mail_registered_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CheckMailRegisteredResponse(),
            self.do_rpcrequest('CheckMailRegistered', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_mail_registered(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_mail_registered_with_options(request, runtime)

    def clear_agent_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ClearAgentRecordsResponse(),
            self.do_rpcrequest('ClearAgentRecords', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_agent_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_agent_records_with_options(request, runtime)

    def config_instance_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ConfigInstanceNetworkResponse(),
            self.do_rpcrequest('ConfigInstanceNetwork', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_network(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_instance_network_with_options(request, runtime)

    def create_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateDataSourceResponse(),
            self.do_rpcrequest('CreateDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    def create_grade_protection_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateGradeProtectionReportResponse(),
            self.do_rpcrequest('CreateGradeProtectionReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_grade_protection_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_grade_protection_report_with_options(request, runtime)

    def create_integrated_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateIntegratedReportResponse(),
            self.do_rpcrequest('CreateIntegratedReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_integrated_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_integrated_report_with_options(request, runtime)

    def create_log_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateLogAlarmTaskResponse(),
            self.do_rpcrequest('CreateLogAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_log_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_log_alarm_task_with_options(request, runtime)

    def create_pcireport_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreatePCIReportResponse(),
            self.do_rpcrequest('CreatePCIReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pcireport(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pcireport_with_options(request, runtime)

    def create_report_push_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateReportPushTaskResponse(),
            self.do_rpcrequest('CreateReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_report_push_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_report_push_task_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateRuleResponse(),
            self.do_rpcrequest('CreateRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateRuleGroupResponse(),
            self.do_rpcrequest('CreateRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_group_with_options(request, runtime)

    def create_soxreport_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSOXReportResponse(),
            self.do_rpcrequest('CreateSOXReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_soxreport(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_soxreport_with_options(request, runtime)

    def create_sql_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSqlRuleResponse(),
            self.do_rpcrequest('CreateSqlRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sql_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sql_rule_with_options(request, runtime)

    def create_system_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.CreateSystemAlarmTaskResponse(),
            self.do_rpcrequest('CreateSystemAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_system_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_system_alarm_task_with_options(request, runtime)

    def delete_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteAlarmTaskResponse(),
            self.do_rpcrequest('DeleteAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_task_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteDataSourceResponse(),
            self.do_rpcrequest('DeleteDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def delete_report_push_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteReportPushTaskResponse(),
            self.do_rpcrequest('DeleteReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_report_push_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_report_push_task_with_options(request, runtime)

    def delete_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteRuleResponse(),
            self.do_rpcrequest('DeleteRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    def delete_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeleteRuleGroupResponse(),
            self.do_rpcrequest('DeleteRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_group_with_options(request, runtime)

    def deregister_templates_from_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DeregisterTemplatesFromRuleResponse(),
            self.do_rpcrequest('DeregisterTemplatesFromRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_templates_from_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_templates_from_rule_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeInstanceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_login_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeLoginTicketResponse(),
            self.do_rpcrequest('DescribeLoginTicket', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_login_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_login_ticket_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_sync_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DescribeSyncInfoResponse(),
            self.do_rpcrequest('DescribeSyncInfo', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sync_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sync_info_with_options(request, runtime)

    def disable_log_mask_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DisableLogMaskConfigsResponse(),
            self.do_rpcrequest('DisableLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_log_mask_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_log_mask_configs_with_options(request, runtime)

    def dissociate_rules_from_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DissociateRulesFromDbResponse(),
            self.do_rpcrequest('DissociateRulesFromDb', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_rules_from_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_rules_from_db_with_options(request, runtime)

    def dissociate_templates_from_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.DissociateTemplatesFromRuleResponse(),
            self.do_rpcrequest('DissociateTemplatesFromRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_templates_from_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dissociate_templates_from_rule_with_options(request, runtime)

    def edit_log_mask_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.EditLogMaskConfigResponse(),
            self.do_rpcrequest('EditLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_log_mask_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_log_mask_config_with_options(request, runtime)

    def enable_log_mask_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.EnableLogMaskConfigsResponse(),
            self.do_rpcrequest('EnableLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_log_mask_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_log_mask_configs_with_options(request, runtime)

    def get_agent_file_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAgentFileUrlResponse(),
            self.do_rpcrequest('GetAgentFileUrl', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_file_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_file_url_with_options(request, runtime)

    def get_agent_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAgentListResponse(),
            self.do_rpcrequest('GetAgentList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_list_with_options(request, runtime)

    def get_appoint_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAppointOperationResponse(),
            self.do_rpcrequest('GetAppointOperation', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_appoint_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_appoint_operation_with_options(request, runtime)

    def get_audit_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAuditCountResponse(),
            self.do_rpcrequest('GetAuditCount', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audit_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audit_count_with_options(request, runtime)

    def get_audit_count_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetAuditCountDistributionResponse(),
            self.do_rpcrequest('GetAuditCountDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audit_count_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audit_count_distribution_with_options(request, runtime)

    def get_base_template_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetBaseTemplateListResponse(),
            self.do_rpcrequest('GetBaseTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_base_template_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_base_template_list_with_options(request, runtime)

    def get_das_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetDasUsageResponse(),
            self.do_rpcrequest('GetDasUsage', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_das_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_das_usage_with_options(request, runtime)

    def get_dbaudit_count_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetDBAuditCountListResponse(),
            self.do_rpcrequest('GetDBAuditCountList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dbaudit_count_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dbaudit_count_list_with_options(request, runtime)

    def get_group_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetGroupDetailResponse(),
            self.do_rpcrequest('GetGroupDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_detail_with_options(request, runtime)

    def get_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLicenseResponse(),
            self.do_rpcrequest('GetLicense', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_license_with_options(request, runtime)

    def get_log_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogDetailResponse(),
            self.do_rpcrequest('GetLogDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_detail_with_options(request, runtime)

    def get_log_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogListResponse(),
            self.do_rpcrequest('GetLogList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_list_with_options(request, runtime)

    def get_log_mask_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogMaskConfigsResponse(),
            self.do_rpcrequest('GetLogMaskConfigs', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_mask_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_mask_configs_with_options(request, runtime)

    def get_log_query_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogQueryConditionResponse(),
            self.do_rpcrequest('GetLogQueryCondition', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_query_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_query_condition_with_options(request, runtime)

    def get_log_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogStatisticsResponse(),
            self.do_rpcrequest('GetLogStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_statistics_with_options(request, runtime)

    def get_log_top_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTopDistributionResponse(),
            self.do_rpcrequest('GetLogTopDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_top_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_top_distribution_with_options(request, runtime)

    def get_log_top_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTopStatisticsResponse(),
            self.do_rpcrequest('GetLogTopStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_top_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_top_statistics_with_options(request, runtime)

    def get_log_type_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetLogTypeDistributionResponse(),
            self.do_rpcrequest('GetLogTypeDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_log_type_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_type_distribution_with_options(request, runtime)

    def get_new_sql_template_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetNewSqlTemplateListResponse(),
            self.do_rpcrequest('GetNewSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_new_sql_template_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_new_sql_template_list_with_options(request, runtime)

    def get_report_file_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetReportFileUrlResponse(),
            self.do_rpcrequest('GetReportFileUrl', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_report_file_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_report_file_url_with_options(request, runtime)

    def get_risk_level_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRiskLevelDistributionResponse(),
            self.do_rpcrequest('GetRiskLevelDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_risk_level_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_level_distribution_with_options(request, runtime)

    def get_risk_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRiskStatisticsResponse(),
            self.do_rpcrequest('GetRiskStatistics', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_risk_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_statistics_with_options(request, runtime)

    def get_rule_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRuleDetailResponse(),
            self.do_rpcrequest('GetRuleDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    def get_rule_group_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetRuleGroupNameResponse(),
            self.do_rpcrequest('GetRuleGroupName', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_group_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_group_name_with_options(request, runtime)

    def get_session_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionDetailResponse(),
            self.do_rpcrequest('GetSessionDetail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_session_detail_with_options(request, runtime)

    def get_session_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionDistributionResponse(),
            self.do_rpcrequest('GetSessionDistribution', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_session_distribution_with_options(request, runtime)

    def get_session_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionListResponse(),
            self.do_rpcrequest('GetSessionList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_session_list_with_options(request, runtime)

    def get_session_query_condition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSessionQueryConditionResponse(),
            self.do_rpcrequest('GetSessionQueryCondition', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_session_query_condition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_session_query_condition_with_options(request, runtime)

    def get_sql_template_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetSqlTemplateListResponse(),
            self.do_rpcrequest('GetSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sql_template_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sql_template_list_with_options(request, runtime)

    def get_top_sql_template_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GetTopSqlTemplateListResponse(),
            self.do_rpcrequest('GetTopSqlTemplateList', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_top_sql_template_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_top_sql_template_list_with_options(request, runtime)

    def grade_protection_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.GradeProtectionReportResponse(),
            self.do_rpcrequest('GradeProtectionReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grade_protection_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grade_protection_report_with_options(request, runtime)

    def import_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ImportDataSourceResponse(),
            self.do_rpcrequest('ImportDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_data_source_with_options(request, runtime)

    def integrated_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.IntegratedReportResponse(),
            self.do_rpcrequest('IntegratedReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def integrated_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.integrated_report_with_options(request, runtime)

    def list_associated_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListAssociatedRulesResponse(),
            self.do_rpcrequest('ListAssociatedRules', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_associated_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_associated_rules_with_options(request, runtime)

    def list_data_source_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListDataSourceAttributeResponse(),
            self.do_rpcrequest('ListDataSourceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_source_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_attribute_with_options(request, runtime)

    def list_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListDataSourcesResponse(),
            self.do_rpcrequest('ListDataSources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    def list_log_alarm_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListLogAlarmTasksResponse(),
            self.do_rpcrequest('ListLogAlarmTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_log_alarm_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_log_alarm_tasks_with_options(request, runtime)

    def list_report_push_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListReportPushTasksResponse(),
            self.do_rpcrequest('ListReportPushTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_report_push_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_report_push_tasks_with_options(request, runtime)

    def list_rule_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListRuleGroupsResponse(),
            self.do_rpcrequest('ListRuleGroups', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rule_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_groups_with_options(request, runtime)

    def list_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListRulesResponse(),
            self.do_rpcrequest('ListRules', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    def list_sql_type_keys_for_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSqlTypeKeysForRuleResponse(),
            self.do_rpcrequest('ListSqlTypeKeysForRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sql_type_keys_for_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sql_type_keys_for_rule_with_options(request, runtime)

    def list_sql_types_for_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSqlTypesForRuleResponse(),
            self.do_rpcrequest('ListSqlTypesForRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sql_types_for_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sql_types_for_rule_with_options(request, runtime)

    def list_support_db_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSupportDbTypesResponse(),
            self.do_rpcrequest('ListSupportDbTypes', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_support_db_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_support_db_types_with_options(request, runtime)

    def list_system_alarms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSystemAlarmsResponse(),
            self.do_rpcrequest('ListSystemAlarms', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_system_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_alarms_with_options(request, runtime)

    def list_system_alarm_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListSystemAlarmTasksResponse(),
            self.do_rpcrequest('ListSystemAlarmTasks', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_system_alarm_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_system_alarm_tasks_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            yundun_dbaudit_20180320_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_templates_for_sql_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListTemplatesForSqlRuleResponse(),
            self.do_rpcrequest('ListTemplatesForSqlRule', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates_for_sql_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_for_sql_rule_with_options(request, runtime)

    def list_used_sql_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ListUsedSqlTypesResponse(),
            self.do_rpcrequest('ListUsedSqlTypes', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_used_sql_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_used_sql_types_with_options(request, runtime)

    def modify_base_template_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyBaseTemplateStateResponse(),
            self.do_rpcrequest('ModifyBaseTemplateState', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_base_template_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_base_template_state_with_options(request, runtime)

    def modify_custom_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyCustomNameResponse(),
            self.do_rpcrequest('ModifyCustomName', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_custom_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_custom_name_with_options(request, runtime)

    def modify_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyDataSourceResponse(),
            self.do_rpcrequest('ModifyDataSource', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_with_options(request, runtime)

    def modify_data_source_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyDataSourceAttributeResponse(),
            self.do_rpcrequest('ModifyDataSourceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_data_source_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_data_source_attribute_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyInstanceAttributeResponse(),
            self.do_rpcrequest('ModifyInstanceAttribute', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_log_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyLogAlarmTaskResponse(),
            self.do_rpcrequest('ModifyLogAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_alarm_task_with_options(request, runtime)

    def modify_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyPlanResponse(),
            self.do_rpcrequest('ModifyPlan', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_plan_with_options(request, runtime)

    def modify_report_push_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyReportPushTaskResponse(),
            self.do_rpcrequest('ModifyReportPushTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_report_push_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_report_push_task_with_options(request, runtime)

    def modify_rule_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifyRuleGroupResponse(),
            self.do_rpcrequest('ModifyRuleGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_rule_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_group_with_options(request, runtime)

    def modify_system_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ModifySystemAlarmTaskResponse(),
            self.do_rpcrequest('ModifySystemAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_system_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_system_alarm_task_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.MoveResourceGroupResponse(),
            self.do_rpcrequest('MoveResourceGroup', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def pci_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.PciReportResponse(),
            self.do_rpcrequest('PciReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pci_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pci_report_with_options(request, runtime)

    def put_login_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.PutLoginCountResponse(),
            self.do_rpcrequest('PutLoginCount', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_login_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_login_count_with_options(request, runtime)

    def read_mark_system_alarms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.ReadMarkSystemAlarmsResponse(),
            self.do_rpcrequest('ReadMarkSystemAlarms', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def read_mark_system_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.read_mark_system_alarms_with_options(request, runtime)

    def refund_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RefundInstanceResponse(),
            self.do_rpcrequest('RefundInstance', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    def register_notice_mail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RegisterNoticeMailResponse(),
            self.do_rpcrequest('RegisterNoticeMail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_notice_mail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_notice_mail_with_options(request, runtime)

    def remove_log_mask_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.RemoveLogMaskConfigResponse(),
            self.do_rpcrequest('RemoveLogMaskConfig', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_log_mask_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_log_mask_config_with_options(request, runtime)

    def send_verify_code_mail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.SendVerifyCodeMailResponse(),
            self.do_rpcrequest('SendVerifyCodeMail', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_verify_code_mail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_mail_with_options(request, runtime)

    def sox_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.SoxReportResponse(),
            self.do_rpcrequest('SoxReport', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sox_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sox_report_with_options(request, runtime)

    def start_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StartAlarmTaskResponse(),
            self.do_rpcrequest('StartAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_alarm_task_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StartInstanceResponse(),
            self.do_rpcrequest('StartInstance', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def stop_alarm_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.StopAlarmTaskResponse(),
            self.do_rpcrequest('StopAlarmTask', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_alarm_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_alarm_task_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            yundun_dbaudit_20180320_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upgrade_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            yundun_dbaudit_20180320_models.UpgradeInstanceVersionResponse(),
            self.do_rpcrequest('UpgradeInstanceVersion', '2018-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)
