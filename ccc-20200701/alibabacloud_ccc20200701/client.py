# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ccc20200701 import models as ccc20200701_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'ccc.aliyuncs.com',
            'ap-south-1': 'ccc.aliyuncs.com',
            'ap-southeast-1': 'ccc.aliyuncs.com',
            'ap-southeast-2': 'ccc.aliyuncs.com',
            'ap-southeast-3': 'ccc.aliyuncs.com',
            'ap-southeast-5': 'ccc.aliyuncs.com',
            'cn-beijing': 'ccc.aliyuncs.com',
            'cn-chengdu': 'ccc.aliyuncs.com',
            'cn-hongkong': 'ccc.aliyuncs.com',
            'cn-huhehaote': 'ccc.aliyuncs.com',
            'cn-qingdao': 'ccc.aliyuncs.com',
            'cn-shenzhen': 'ccc.aliyuncs.com',
            'cn-zhangjiakou': 'ccc.aliyuncs.com',
            'eu-central-1': 'ccc.aliyuncs.com',
            'eu-west-1': 'ccc.aliyuncs.com',
            'me-east-1': 'ccc.aliyuncs.com',
            'us-east-1': 'ccc.aliyuncs.com',
            'us-west-1': 'ccc.aliyuncs.com',
            'cn-hangzhou-finance': 'ccc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ccc.aliyuncs.com',
            'cn-shanghai-finance-1': 'ccc.aliyuncs.com',
            'cn-north-2-gov-1': 'ccc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ccc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_skill_groups_to_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddSkillGroupsToUserResponse(),
            self.do_rpcrequest('AddSkillGroupsToUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_skill_groups_to_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_skill_groups_to_user_with_options(request, runtime)

    def save_web_rtcstats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRTCStatsResponse(),
            self.do_rpcrequest('SaveWebRTCStats', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_rtcstats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    def get_mono_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMonoRecordingResponse(),
            self.do_rpcrequest('GetMonoRecording', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mono_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mono_recording_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_agent_state_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListAgentStateLogsResponse(),
            self.do_rpcrequest('ListAgentStateLogs', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_state_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    def remove_phone_number_from_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumberFromSkillGroupsResponse(),
            self.do_rpcrequest('RemovePhoneNumberFromSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_number_from_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_number_from_skill_groups_with_options(request, runtime)

    def list_phone_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersResponse(),
            self.do_rpcrequest('ListPhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    def add_numbers_to_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddNumbersToSkillGroupResponse(),
            self.do_rpcrequest('AddNumbersToSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_numbers_to_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_numbers_to_skill_group_with_options(request, runtime)

    def reset_agent_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetAgentStateResponse(),
            self.do_rpcrequest('ResetAgentState', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_agent_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_agent_state_with_options(request, runtime)

    def change_work_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ChangeWorkModeResponse(),
            self.do_rpcrequest('ChangeWorkMode', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_work_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_work_mode_with_options(request, runtime)

    def get_turn_credentials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnCredentialsResponse(),
            self.do_rpcrequest('GetTurnCredentials', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turn_credentials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_turn_credentials_with_options(request, runtime)

    def add_phone_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumbersResponse(),
            self.do_rpcrequest('AddPhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_phone_numbers_with_options(request, runtime)

    def save_web_rtc_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveWebRtcInfoResponse(),
            self.do_rpcrequest('SaveWebRtcInfo', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_rtc_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtc_info_with_options(request, runtime)

    def list_interval_skill_group_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalSkillGroupReportResponse(),
            self.do_rpcrequest('ListIntervalSkillGroupReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_interval_skill_group_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interval_skill_group_report_with_options(request, runtime)

    def monitor_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MonitorCallResponse(),
            self.do_rpcrequest('MonitorCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def monitor_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.monitor_call_with_options(request, runtime)

    def remove_users_from_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersFromSkillGroupResponse(),
            self.do_rpcrequest('RemoveUsersFromSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users_from_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    def delete_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.DeleteSkillGroupResponse(),
            self.do_rpcrequest('DeleteSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    def blind_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.BlindTransferResponse(),
            self.do_rpcrequest('BlindTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def blind_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.blind_transfer_with_options(request, runtime)

    def list_skill_levels_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillLevelsOfUserResponse(),
            self.do_rpcrequest('ListSkillLevelsOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_levels_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_levels_of_user_with_options(request, runtime)

    def list_unassigned_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUnassignedNumbersResponse(),
            self.do_rpcrequest('ListUnassignedNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_unassigned_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_unassigned_numbers_with_options(request, runtime)

    def get_instance_trending_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceTrendingReportResponse(),
            self.do_rpcrequest('GetInstanceTrendingReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_trending_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_trending_report_with_options(request, runtime)

    def list_instances_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesOfUserResponse(),
            self.do_rpcrequest('ListInstancesOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_of_user_with_options(request, runtime)

    def launch_survey_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchSurveyResponse(),
            self.do_rpcrequest('LaunchSurvey', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_survey(self, request):
        runtime = util_models.RuntimeOptions()
        return self.launch_survey_with_options(request, runtime)

    def list_ivr_tracking_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIvrTrackingDetailsResponse(),
            self.do_rpcrequest('ListIvrTrackingDetails', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ivr_tracking_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ivr_tracking_details_with_options(request, runtime)

    def list_brief_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListBriefSkillGroupsResponse(),
            self.do_rpcrequest('ListBriefSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_brief_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_brief_skill_groups_with_options(request, runtime)

    def unmute_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.UnmuteCallResponse(),
            self.do_rpcrequest('UnmuteCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unmute_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unmute_call_with_options(request, runtime)

    def modify_skill_levels_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillLevelsOfUserResponse(),
            self.do_rpcrequest('ModifySkillLevelsOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_levels_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_levels_of_user_with_options(request, runtime)

    def assign_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AssignUsersResponse(),
            self.do_rpcrequest('AssignUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    def list_user_levels_of_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListUserLevelsOfSkillGroupResponse(),
            self.do_rpcrequest('ListUserLevelsOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_levels_of_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_levels_of_skill_group_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def update_config_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.UpdateConfigItemsResponse(),
            self.do_rpcrequest('UpdateConfigItems', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_config_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_config_items_with_options(request, runtime)

    def get_call_detail_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetCallDetailRecordResponse(),
            self.do_rpcrequest('GetCallDetailRecord', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_call_detail_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_call_detail_record_with_options(request, runtime)

    def modify_phone_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyPhoneNumberResponse(),
            self.do_rpcrequest('ModifyPhoneNumber', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    def coach_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CoachCallResponse(),
            self.do_rpcrequest('CoachCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def coach_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.coach_call_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateUserResponse(),
            self.do_rpcrequest('CreateUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def list_privileges_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPrivilegesOfUserResponse(),
            self.do_rpcrequest('ListPrivilegesOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_privileges_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_privileges_of_user_with_options(request, runtime)

    def add_personal_numbers_to_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPersonalNumbersToUserResponse(),
            self.do_rpcrequest('AddPersonalNumbersToUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_personal_numbers_to_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_personal_numbers_to_user_with_options(request, runtime)

    def list_historical_agent_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalAgentReportResponse(),
            self.do_rpcrequest('ListHistoricalAgentReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_historical_agent_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_historical_agent_report_with_options(request, runtime)

    def intercept_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.InterceptCallResponse(),
            self.do_rpcrequest('InterceptCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def intercept_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.intercept_call_with_options(request, runtime)

    def list_contact_flows_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListContactFlowsResponse(),
            self.do_rpcrequest('ListContactFlows', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_contact_flows(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    def list_personal_numbers_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPersonalNumbersOfUserResponse(),
            self.do_rpcrequest('ListPersonalNumbersOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_personal_numbers_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_personal_numbers_of_user_with_options(request, runtime)

    def start_predictive_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.StartPredictiveCallResponse(),
            self.do_rpcrequest('StartPredictiveCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_predictive_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_predictive_call_with_options(request, runtime)

    def list_interval_instance_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalInstanceReportResponse(),
            self.do_rpcrequest('ListIntervalInstanceReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_interval_instance_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interval_instance_report_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def remove_skill_groups_from_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveSkillGroupsFromUserResponse(),
            self.do_rpcrequest('RemoveSkillGroupsFromUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_skill_groups_from_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_groups_from_user_with_options(request, runtime)

    def list_realtime_agent_states_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeAgentStatesResponse(),
            self.do_rpcrequest('ListRealtimeAgentStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_realtime_agent_states(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_agent_states_with_options(request, runtime)

    def launch_authentication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.LaunchAuthenticationResponse(),
            self.do_rpcrequest('LaunchAuthentication', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_authentication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.launch_authentication_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def get_historical_instance_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalInstanceReportResponse(),
            self.do_rpcrequest('GetHistoricalInstanceReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_historical_instance_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_historical_instance_report_with_options(request, runtime)

    def remove_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemoveUsersResponse(),
            self.do_rpcrequest('RemoveUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    def start_back_2back_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.StartBack2BackCallResponse(),
            self.do_rpcrequest('StartBack2BackCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_back_2back_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetUserResponse(),
            self.do_rpcrequest('GetUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def remove_phone_numbers_from_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersFromSkillGroupResponse(),
            self.do_rpcrequest('RemovePhoneNumbersFromSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_numbers_from_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_from_skill_group_with_options(request, runtime)

    def complete_attended_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CompleteAttendedTransferResponse(),
            self.do_rpcrequest('CompleteAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_attended_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_attended_transfer_with_options(request, runtime)

    def reset_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ResetUserPasswordResponse(),
            self.do_rpcrequest('ResetUserPassword', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    def get_turn_server_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetTurnServerListResponse(),
            self.do_rpcrequest('GetTurnServerList', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turn_server_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_turn_server_list_with_options(request, runtime)

    def get_number_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetNumberLocationResponse(),
            self.do_rpcrequest('GetNumberLocation', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_number_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_number_location_with_options(request, runtime)

    def list_ram_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRamUsersResponse(),
            self.do_rpcrequest('ListRamUsers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ram_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ram_users_with_options(request, runtime)

    def mute_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MuteCallResponse(),
            self.do_rpcrequest('MuteCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mute_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mute_call_with_options(request, runtime)

    def answer_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AnswerCallResponse(),
            self.do_rpcrequest('AnswerCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def answer_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    def list_interval_agent_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListIntervalAgentReportResponse(),
            self.do_rpcrequest('ListIntervalAgentReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_interval_agent_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interval_agent_report_with_options(request, runtime)

    def list_call_detail_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListCallDetailRecordsResponse(),
            self.do_rpcrequest('ListCallDetailRecords', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_detail_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    def remove_phone_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePhoneNumbersResponse(),
            self.do_rpcrequest('RemovePhoneNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_numbers_with_options(request, runtime)

    def cancel_attended_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CancelAttendedTransferResponse(),
            self.do_rpcrequest('CancelAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_attended_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_attended_transfer_with_options(request, runtime)

    def take_break_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.TakeBreakResponse(),
            self.do_rpcrequest('TakeBreak', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def take_break(self, request):
        runtime = util_models.RuntimeOptions()
        return self.take_break_with_options(request, runtime)

    def list_historical_skill_group_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListHistoricalSkillGroupReportResponse(),
            self.do_rpcrequest('ListHistoricalSkillGroupReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_historical_skill_group_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_historical_skill_group_report_with_options(request, runtime)

    def send_dtmf_signaling_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SendDtmfSignalingResponse(),
            self.do_rpcrequest('SendDtmfSignaling', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_dtmf_signaling(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_dtmf_signaling_with_options(request, runtime)

    def list_recent_call_detail_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRecentCallDetailRecordsResponse(),
            self.do_rpcrequest('ListRecentCallDetailRecords', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recent_call_detail_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_recent_call_detail_records_with_options(request, runtime)

    def initiate_attended_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.InitiateAttendedTransferResponse(),
            self.do_rpcrequest('InitiateAttendedTransfer', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initiate_attended_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.initiate_attended_transfer_with_options(request, runtime)

    def make_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.MakeCallResponse(),
            self.do_rpcrequest('MakeCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetInstanceResponse(),
            self.do_rpcrequest('GetInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def add_users_to_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddUsersToSkillGroupResponse(),
            self.do_rpcrequest('AddUsersToSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_users_to_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_skill_group_with_options(request, runtime)

    def list_config_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListConfigItemsResponse(),
            self.do_rpcrequest('ListConfigItems', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_config_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_config_items_with_options(request, runtime)

    def sign_in_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SignInGroupResponse(),
            self.do_rpcrequest('SignInGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sign_in_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sign_in_group_with_options(request, runtime)

    def get_realtime_instance_states_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetRealtimeInstanceStatesResponse(),
            self.do_rpcrequest('GetRealtimeInstanceStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_realtime_instance_states(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_instance_states_with_options(request, runtime)

    def modify_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifySkillGroupResponse(),
            self.do_rpcrequest('ModifySkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    def modify_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserResponse(),
            self.do_rpcrequest('ModifyUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    def add_phone_number_to_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.AddPhoneNumberToSkillGroupsResponse(),
            self.do_rpcrequest('AddPhoneNumberToSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_number_to_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_phone_number_to_skill_groups_with_options(request, runtime)

    def list_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListDevicesResponse(),
            self.do_rpcrequest('ListDevices', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    def retrieve_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RetrieveCallResponse(),
            self.do_rpcrequest('RetrieveCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retrieve_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retrieve_call_with_options(request, runtime)

    def list_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListSkillGroupsResponse(),
            self.do_rpcrequest('ListSkillGroups', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    def hold_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.HoldCallResponse(),
            self.do_rpcrequest('HoldCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hold_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    def register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RegisterDeviceResponse(),
            self.do_rpcrequest('RegisterDevice', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    def remove_personal_numbers_from_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.RemovePersonalNumbersFromUserResponse(),
            self.do_rpcrequest('RemovePersonalNumbersFromUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_personal_numbers_from_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_personal_numbers_from_user_with_options(request, runtime)

    def modify_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyInstanceResponse(),
            self.do_rpcrequest('ModifyInstance', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    def list_outbound_numbers_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListOutboundNumbersOfUserResponse(),
            self.do_rpcrequest('ListOutboundNumbersOfUser', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_numbers_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_numbers_of_user_with_options(request, runtime)

    def poll_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.PollUserStatusResponse(),
            self.do_rpcrequest('PollUserStatus', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def poll_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.poll_user_status_with_options(request, runtime)

    def ready_for_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ReadyForServiceResponse(),
            self.do_rpcrequest('ReadyForService', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ready_for_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ready_for_service_with_options(request, runtime)

    def get_multi_channel_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetMultiChannelRecordingResponse(),
            self.do_rpcrequest('GetMultiChannelRecording', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_multi_channel_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_multi_channel_recording_with_options(request, runtime)

    def barge_in_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.BargeInCallResponse(),
            self.do_rpcrequest('BargeInCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def barge_in_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.barge_in_call_with_options(request, runtime)

    def list_phone_numbers_of_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListPhoneNumbersOfSkillGroupResponse(),
            self.do_rpcrequest('ListPhoneNumbersOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_numbers_of_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_of_skill_group_with_options(request, runtime)

    def sign_out_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SignOutGroupResponse(),
            self.do_rpcrequest('SignOutGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sign_out_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sign_out_group_with_options(request, runtime)

    def save_rtcstats_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveRTCStatsV2Response(),
            self.do_rpcrequest('SaveRTCStatsV2', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_rtcstats_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_rtcstats_v2with_options(request, runtime)

    def get_historical_caller_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetHistoricalCallerReportResponse(),
            self.do_rpcrequest('GetHistoricalCallerReport', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_historical_caller_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_historical_caller_report_with_options(request, runtime)

    def modify_user_levels_of_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ModifyUserLevelsOfSkillGroupResponse(),
            self.do_rpcrequest('ModifyUserLevelsOfSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_levels_of_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_levels_of_skill_group_with_options(request, runtime)

    def save_terminal_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.SaveTerminalLogResponse(),
            self.do_rpcrequest('SaveTerminalLog', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_terminal_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    def list_realtime_skill_group_states_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ListRealtimeSkillGroupStatesResponse(),
            self.do_rpcrequest('ListRealtimeSkillGroupStates', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_realtime_skill_group_states(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_realtime_skill_group_states_with_options(request, runtime)

    def create_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.CreateSkillGroupResponse(),
            self.do_rpcrequest('CreateSkillGroup', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    def pick_outbound_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.PickOutboundNumbersResponse(),
            self.do_rpcrequest('PickOutboundNumbers', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_outbound_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    def release_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.ReleaseCallResponse(),
            self.do_rpcrequest('ReleaseCall', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_call_with_options(request, runtime)

    def get_login_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ccc20200701_models.GetLoginDetailsResponse(),
            self.do_rpcrequest('GetLoginDetails', '2020-07-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_details_with_options(request, runtime)
