# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiccs20191015 import models as aiccs_20191015_models
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
        self._endpoint = self.get_endpoint('aiccs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def send_hotline_heart_beat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendHotlineHeartBeatResponse(),
            self.do_rpcrequest('SendHotlineHeartBeat', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_hotline_heart_beat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_hotline_heart_beat_with_options(request, runtime)

    def start_chat_work_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartChatWorkResponse(),
            self.do_rpcrequest('StartChatWork', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_chat_work(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_chat_work_with_options(request, runtime)

    def hang_up_double_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangUpDoubleCallResponse(),
            self.do_rpcrequest('HangUpDoubleCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hang_up_double_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hang_up_double_call_with_options(request, runtime)

    def update_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateAgentResponse(),
            self.do_rpcrequest('UpdateAgent', '2019-10-15', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_agent_with_options(request, runtime)

    def edit_quality_rule_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleTagResponse(),
            self.do_rpcrequest('EditQualityRuleTag', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_quality_rule_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_rule_tag_with_options(request, runtime)

    def get_online_service_volume_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineServiceVolumeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineServiceVolumeResponse(),
            self.do_rpcrequest('GetOnlineServiceVolume', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_online_service_volume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_online_service_volume_with_options(request, runtime)

    def delete_outbound_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOutboundTaskResponse(),
            self.do_rpcrequest('DeleteOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_outbound_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_outbound_task_with_options(request, runtime)

    def add_outer_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddOuterAccountResponse(),
            self.do_rpcrequest('AddOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_outer_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_outer_account_with_options(request, runtime)

    def get_agent_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentByIdResponse(),
            self.do_rpcrequest('GetAgentById', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_by_id_with_options(request, runtime)

    def get_quality_rule_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleDetailResponse(),
            self.do_rpcrequest('GetQualityRuleDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_detail_with_options(request, runtime)

    def get_quality_project_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectLogResponse(),
            self.do_rpcrequest('GetQualityProjectLog', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_project_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_log_with_options(request, runtime)

    def list_hotline_record_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordDetailResponse(),
            self.do_rpcrequest('ListHotlineRecordDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_hotline_record_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_detail_with_options(request, runtime)

    def get_hotline_message_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineMessageLogResponse(),
            self.do_rpcrequest('GetHotlineMessageLog', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_message_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_message_log_with_options(request, runtime)

    def get_quality_project_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectListResponse(),
            self.do_rpcrequest('GetQualityProjectList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_project_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_list_with_options(request, runtime)

    def create_outbound_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateOutboundTaskResponse(),
            self.do_rpcrequest('CreateOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_outbound_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_outbound_task_with_options(request, runtime)

    def get_hotline_runtime_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineRuntimeInfoResponse(),
            self.do_rpcrequest('GetHotlineRuntimeInfo', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_runtime_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_runtime_info_with_options(request, runtime)

    def make_double_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeDoubleCallResponse(),
            self.do_rpcrequest('MakeDoubleCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_double_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.make_double_call_with_options(request, runtime)

    def get_skill_group_agent_status_details_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAgentStatusDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAgentStatusDetailsResponse(),
            self.do_rpcrequest('GetSkillGroupAgentStatusDetails', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_agent_status_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_agent_status_details_with_options(request, runtime)

    def get_agent_service_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentServiceStatusResponse(),
            self.do_rpcrequest('GetAgentServiceStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_service_status_with_options(request, runtime)

    def get_num_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetNumLocationResponse(),
            self.do_rpcrequest('GetNumLocation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_num_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_num_location_with_options(request, runtime)

    def get_quality_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleListResponse(),
            self.do_rpcrequest('GetQualityRuleList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_list_with_options(request, runtime)

    def list_outbound_phone_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundPhoneNumberResponse(),
            self.do_rpcrequest('ListOutboundPhoneNumber', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_outbound_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_phone_number_with_options(request, runtime)

    def list_agent_by_skill_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListAgentBySkillGroupIdResponse(),
            self.do_rpcrequest('ListAgentBySkillGroupId', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_agent_by_skill_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_by_skill_group_id_with_options(request, runtime)

    def hangup_third_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupThirdCallResponse(),
            self.do_rpcrequest('HangupThirdCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hangup_third_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hangup_third_call_with_options(request, runtime)

    def start_hotline_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartHotlineServiceResponse(),
            self.do_rpcrequest('StartHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_hotline_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_hotline_service_with_options(request, runtime)

    def get_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentResponse(),
            self.do_rpcrequest('GetAgent', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_with_options(request, runtime)

    def get_agent_index_real_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentIndexRealTimeResponse(),
            self.do_rpcrequest('GetAgentIndexRealTime', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_index_real_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_index_real_time_with_options(request, runtime)

    def get_hotline_group_detail_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineGroupDetailReportResponse(),
            self.do_rpcrequest('GetHotlineGroupDetailReport', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_group_detail_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_group_detail_report_with_options(request, runtime)

    def encrypt_phone_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EncryptPhoneNumResponse(),
            self.do_rpcrequest('EncryptPhoneNum', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def encrypt_phone_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.encrypt_phone_num_with_options(request, runtime)

    def get_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetInstanceListResponse(),
            self.do_rpcrequest('GetInstanceList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    def get_quality_project_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityProjectDetailResponse(),
            self.do_rpcrequest('GetQualityProjectDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_project_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_project_detail_with_options(request, runtime)

    def send_cco_smart_call_operate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallOperateResponse(),
            self.do_rpcrequest('SendCcoSmartCallOperate', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_cco_smart_call_operate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_cco_smart_call_operate_with_options(request, runtime)

    def answer_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AnswerCallResponse(),
            self.do_rpcrequest('AnswerCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def answer_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.answer_call_with_options(request, runtime)

    def start_micro_outbound_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartMicroOutboundResponse(),
            self.do_rpcrequest('StartMicroOutbound', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_micro_outbound(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_micro_outbound_with_options(request, runtime)

    def suspend_hotline_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendHotlineServiceResponse(),
            self.do_rpcrequest('SuspendHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_hotline_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_hotline_service_with_options(request, runtime)

    def get_agent_statistics_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentStatisticsResponse(),
            self.do_rpcrequest('GetAgentStatistics', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_statistics_with_options(request, runtime)

    def update_outer_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateOuterAccountResponse(),
            self.do_rpcrequest('UpdateOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_outer_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_outer_account_with_options(request, runtime)

    def get_hotline_waiting_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineWaitingNumberResponse(),
            self.do_rpcrequest('GetHotlineWaitingNumber', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_waiting_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_waiting_number_with_options(request, runtime)

    def hold_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HoldCallResponse(),
            self.do_rpcrequest('HoldCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hold_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hold_call_with_options(request, runtime)

    def get_seat_information_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'depIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSeatInformationResponse(),
            self.do_rpcrequest('GetSeatInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_seat_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_seat_information_with_options(request, runtime)

    def get_rtc_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRtcTokenResponse(),
            self.do_rpcrequest('GetRtcToken', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_rtc_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    def get_skill_group_and_agent_status_summary_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupAndAgentStatusSummaryResponse(),
            self.do_rpcrequest('GetSkillGroupAndAgentStatusSummary', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_and_agent_status_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_and_agent_status_summary_with_options(request, runtime)

    def get_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetRecordDataResponse(),
            self.do_rpcrequest('GetRecordData', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_record_data_with_options(request, runtime)

    def get_skill_group_latitude_state_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupLatitudeStateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupLatitudeStateResponse(),
            self.do_rpcrequest('GetSkillGroupLatitudeState', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_latitude_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_latitude_state_with_options(request, runtime)

    def delete_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityRuleResponse(),
            self.do_rpcrequest('DeleteQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    def suspend_outbound_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SuspendOutboundTaskResponse(),
            self.do_rpcrequest('SuspendOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_outbound_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_outbound_task_with_options(request, runtime)

    def get_hotline_service_statistics_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetHotlineServiceStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineServiceStatisticsResponse(),
            self.do_rpcrequest('GetHotlineServiceStatistics', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_service_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_service_statistics_with_options(request, runtime)

    def edit_quality_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityProjectResponse(),
            self.do_rpcrequest('EditQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_quality_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_project_with_options(request, runtime)

    def list_outer_ordered_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOuterOrderedNumbersResponse(),
            self.do_rpcrequest('ListOuterOrderedNumbers', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outer_ordered_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_outer_ordered_numbers_with_options(request, runtime)

    def get_agent_basis_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentBasisStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentBasisStatusResponse(),
            self.do_rpcrequest('GetAgentBasisStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_basis_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_basis_status_with_options(request, runtime)

    def get_quality_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityResultResponse(),
            self.do_rpcrequest('GetQualityResult', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_result_with_options(request, runtime)

    def get_index_current_value_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetIndexCurrentValueResponse(),
            self.do_rpcrequest('GetIndexCurrentValue', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_index_current_value(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_index_current_value_with_options(request, runtime)

    def generate_web_socket_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GenerateWebSocketSignResponse(),
            self.do_rpcrequest('GenerateWebSocketSign', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_web_socket_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_web_socket_sign_with_options(request, runtime)

    def create_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateAgentResponse(),
            self.do_rpcrequest('CreateAgent', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_agent_with_options(request, runtime)

    def query_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTaskDetailResponse(),
            self.do_rpcrequest('QueryTaskDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_with_options(request, runtime)

    def edit_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.EditQualityRuleResponse(),
            self.do_rpcrequest('EditQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_quality_rule_with_options(request, runtime)

    def get_mcu_lvs_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetMcuLvsIpResponse(),
            self.do_rpcrequest('GetMcuLvsIp', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_mcu_lvs_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mcu_lvs_ip_with_options(request, runtime)

    def get_dep_group_tree_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepGroupTreeDataResponse(),
            self.do_rpcrequest('GetDepGroupTreeData', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_dep_group_tree_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dep_group_tree_data_with_options(request, runtime)

    def delete_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteAgentResponse(),
            self.do_rpcrequest('DeleteAgent', '2019-10-15', 'HTTPS', 'DELETE', 'AK', 'json', req, runtime)
        )

    def delete_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_agent_with_options(request, runtime)

    def get_customer_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetCustomerInfoResponse(),
            self.do_rpcrequest('GetCustomerInfo', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_customer_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customer_info_with_options(request, runtime)

    def get_hotline_agent_detail_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailReportResponse(),
            self.do_rpcrequest('GetHotlineAgentDetailReport', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_detail_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_report_with_options(request, runtime)

    def send_cco_smart_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.SendCcoSmartCallResponse(),
            self.do_rpcrequest('SendCcoSmartCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_cco_smart_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_cco_smart_call_with_options(request, runtime)

    def list_chat_record_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListChatRecordDetailResponse(),
            self.do_rpcrequest('ListChatRecordDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_chat_record_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chat_record_detail_with_options(request, runtime)

    def add_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.AddSkillGroupResponse(),
            self.do_rpcrequest('AddSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_skill_group_with_options(request, runtime)

    def hangup_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HangupCallResponse(),
            self.do_rpcrequest('HangupCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hangup_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hangup_call_with_options(request, runtime)

    def delete_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteSkillGroupResponse(),
            self.do_rpcrequest('DeleteSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    def create_quality_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityProjectResponse(),
            self.do_rpcrequest('CreateQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_project_with_options(request, runtime)

    def query_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QuerySkillGroupsResponse(),
            self.do_rpcrequest('QuerySkillGroups', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_skill_groups_with_options(request, runtime)

    def create_quality_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateQualityRuleResponse(),
            self.do_rpcrequest('CreateQualityRule', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def get_hotline_call_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineCallActionResponse(),
            self.do_rpcrequest('GetHotlineCallAction', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_call_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_call_action_with_options(request, runtime)

    def list_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListSkillGroupResponse(),
            self.do_rpcrequest('ListSkillGroup', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_with_options(request, runtime)

    def get_online_seat_information_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetOnlineSeatInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOnlineSeatInformationResponse(),
            self.do_rpcrequest('GetOnlineSeatInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_online_seat_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_online_seat_information_with_options(request, runtime)

    def delete_quality_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteQualityProjectResponse(),
            self.do_rpcrequest('DeleteQualityProject', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_project_with_options(request, runtime)

    def query_touch_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTouchListResponse(),
            self.do_rpcrequest('QueryTouchList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_touch_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_touch_list_with_options(request, runtime)

    def query_hotline_in_queue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryHotlineInQueueResponse(),
            self.do_rpcrequest('QueryHotlineInQueue', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_hotline_in_queue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_hotline_in_queue_with_options(request, runtime)

    def finish_hotline_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FinishHotlineServiceResponse(),
            self.do_rpcrequest('FinishHotlineService', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def finish_hotline_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.finish_hotline_service_with_options(request, runtime)

    def list_outbound_strategies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListOutboundStrategiesResponse(),
            self.do_rpcrequest('ListOutboundStrategies', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_strategies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_strategies_with_options(request, runtime)

    def list_hotline_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ListHotlineRecordResponse(),
            self.do_rpcrequest('ListHotlineRecord', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_hotline_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hotline_record_with_options(request, runtime)

    def change_quality_project_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeQualityProjectStatusResponse(),
            self.do_rpcrequest('ChangeQualityProjectStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_quality_project_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_quality_project_status_with_options(request, runtime)

    def transfer_call_to_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.TransferCallToSkillGroupResponse(),
            self.do_rpcrequest('TransferCallToSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_call_to_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_call_to_skill_group_with_options(request, runtime)

    def get_skill_group_service_capability_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceCapabilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceCapabilityResponse(),
            self.do_rpcrequest('GetSkillGroupServiceCapability', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_service_capability(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_service_capability_with_options(request, runtime)

    def remove_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RemoveSkillGroupResponse(),
            self.do_rpcrequest('RemoveSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_skill_group_with_options(request, runtime)

    def start_call_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallV2Response(),
            self.do_rpcrequest('StartCallV2', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_call_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_call_v2with_options(request, runtime)

    def change_chat_agent_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.ChangeChatAgentStatusResponse(),
            self.do_rpcrequest('ChangeChatAgentStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_chat_agent_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_chat_agent_status_with_options(request, runtime)

    def describe_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DescribeRecordDataResponse(),
            self.do_rpcrequest('DescribeRecordData', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_data_with_options(request, runtime)

    def delete_outer_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.DeleteOuterAccountResponse(),
            self.do_rpcrequest('DeleteOuterAccount', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_outer_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_outer_account_with_options(request, runtime)

    def get_departmental_latitude_agent_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetDepartmentalLatitudeAgentStatusResponse(),
            self.do_rpcrequest('GetDepartmentalLatitudeAgentStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_departmental_latitude_agent_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_departmental_latitude_agent_status_with_options(request, runtime)

    def get_hotline_agent_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentDetailResponse(),
            self.do_rpcrequest('GetHotlineAgentDetail', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_detail_with_options(request, runtime)

    def make_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.MakeCallResponse(),
            self.do_rpcrequest('MakeCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.make_call_with_options(request, runtime)

    def fetch_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.FetchCallResponse(),
            self.do_rpcrequest('FetchCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fetch_call_with_options(request, runtime)

    def get_hotline_agent_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetHotlineAgentStatusResponse(),
            self.do_rpcrequest('GetHotlineAgentStatus', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hotline_agent_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hotline_agent_status_with_options(request, runtime)

    def start_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.StartCallResponse(),
            self.do_rpcrequest('StartCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_call_with_options(request, runtime)

    def get_quality_rule_tag_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQualityRuleTagListResponse(),
            self.do_rpcrequest('GetQualityRuleTagList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule_tag_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_tag_list_with_options(request, runtime)

    def get_outboun_num_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetOutbounNumListResponse(),
            self.do_rpcrequest('GetOutbounNumList', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_outboun_num_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_outboun_num_list_with_options(request, runtime)

    def create_third_sso_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateThirdSsoAgentResponse(),
            self.do_rpcrequest('CreateThirdSsoAgent', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_third_sso_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_third_sso_agent_with_options(request, runtime)

    def get_skill_group_status_total_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupStatusTotalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupStatusTotalResponse(),
            self.do_rpcrequest('GetSkillGroupStatusTotal', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_status_total(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_status_total_with_options(request, runtime)

    def batch_create_quality_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.BatchCreateQualityProjectsResponse(),
            self.do_rpcrequest('BatchCreateQualityProjects', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_create_quality_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_create_quality_projects_with_options(request, runtime)

    def insert_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.InsertTaskDetailResponse(),
            self.do_rpcrequest('InsertTaskDetail', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_task_detail_with_options(request, runtime)

    def update_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.UpdateSkillGroupResponse(),
            self.do_rpcrequest('UpdateSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_with_options(request, runtime)

    def hotline_session_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.HotlineSessionQueryResponse(),
            self.do_rpcrequest('HotlineSessionQuery', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def hotline_session_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hotline_session_query_with_options(request, runtime)

    def get_queue_information_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetQueueInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetQueueInformationResponse(),
            self.do_rpcrequest('GetQueueInformation', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_queue_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_queue_information_with_options(request, runtime)

    def get_skill_group_service_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetSkillGroupServiceStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        if not UtilClient.is_unset(tmp_req.group_ids):
            request.group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_ids, 'GroupIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetSkillGroupServiceStatusResponse(),
            self.do_rpcrequest('GetSkillGroupServiceStatus', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_skill_group_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_service_status_with_options(request, runtime)

    def get_agent_detail_report_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.GetAgentDetailReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.agent_ids):
            request.agent_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.agent_ids, 'AgentIds', 'simple')
        if not UtilClient.is_unset(tmp_req.dep_ids):
            request.dep_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dep_ids, 'DepIds', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            aiccs_20191015_models.GetAgentDetailReportResponse(),
            self.do_rpcrequest('GetAgentDetailReport', '2019-10-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_detail_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_detail_report_with_options(request, runtime)

    def query_tickets_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiccs_20191015_models.QueryTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryTicketsResponse(),
            self.do_rpcrequest('QueryTickets', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tickets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tickets_with_options(request, runtime)

    def query_outbound_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.QueryOutboundTaskResponse(),
            self.do_rpcrequest('QueryOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_outbound_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_outbound_task_with_options(request, runtime)

    def join_third_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.JoinThirdCallResponse(),
            self.do_rpcrequest('JoinThirdCall', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_third_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_third_call_with_options(request, runtime)

    def create_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.CreateSkillGroupResponse(),
            self.do_rpcrequest('CreateSkillGroup', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    def restart_outbound_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aiccs_20191015_models.RestartOutboundTaskResponse(),
            self.do_rpcrequest('RestartOutboundTask', '2019-10-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_outbound_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_outbound_task_with_options(request, runtime)
