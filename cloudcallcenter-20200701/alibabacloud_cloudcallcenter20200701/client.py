# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudcallcenter20200701 import models as cloud_call_center_20200701_models
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
        self._endpoint = self.get_endpoint('cloudcallcenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_campaign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.AbortCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    def abort_campaign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abort_campaign_with_options(request, runtime)

    def abort_cases_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_call_center_20200701_models.AbortCasesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.phone_number_list):
            request.phone_number_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.phone_number_list, 'PhoneNumberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.phone_number_list_shrink):
            query['PhoneNumberList'] = request.phone_number_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.AbortCasesResponse(),
            self.call_api(params, req, runtime)
        )

    def abort_cases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abort_cases_with_options(request, runtime)

    def check_demo_instance_exists_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckDemoInstanceExists',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.CheckDemoInstanceExistsResponse(),
            self.call_api(params, req, runtime)
        )

    def check_demo_instance_exists(self):
        runtime = util_models.RuntimeOptions()
        return self.check_demo_instance_exists_with_options(runtime)

    def check_mqrole_assumption_authority_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckMQRoleAssumptionAuthority',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.CheckMQRoleAssumptionAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    def check_mqrole_assumption_authority(self):
        runtime = util_models.RuntimeOptions()
        return self.check_mqrole_assumption_authority_with_options(runtime)

    def create_campaign_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_call_center_20200701_models.CreateCampaignShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.case_list):
            request.case_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.case_list, 'CaseList', 'json')
        query = {}
        if not UtilClient.is_unset(request.callable_time):
            query['CallableTime'] = request.callable_time
        if not UtilClient.is_unset(request.case_file_key):
            query['CaseFileKey'] = request.case_file_key
        if not UtilClient.is_unset(request.case_list_shrink):
            query['CaseList'] = request.case_list_shrink
        if not UtilClient.is_unset(request.contact_flow_id):
            query['ContactFlowId'] = request.contact_flow_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.executing_until_timeout):
            query['ExecutingUntilTimeout'] = request.executing_until_timeout
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_attempt_count):
            query['MaxAttemptCount'] = request.max_attempt_count
        if not UtilClient.is_unset(request.min_attempt_interval):
            query['MinAttemptInterval'] = request.min_attempt_interval
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.queue_id):
            query['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.simulation):
            query['Simulation'] = request.simulation
        if not UtilClient.is_unset(request.simulation_parameters):
            query['SimulationParameters'] = request.simulation_parameters
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy_parameters):
            query['StrategyParameters'] = request.strategy_parameters
        if not UtilClient.is_unset(request.strategy_type):
            query['StrategyType'] = request.strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.CreateCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    def create_campaign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_campaign_with_options(request, runtime)

    def create_corp_number_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCorpNumberGroup',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.CreateCorpNumberGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_corp_number_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_corp_number_group_with_options(request, runtime)

    def create_demo_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.outbound_call_whitelist):
            query['OutboundCallWhitelist'] = request.outbound_call_whitelist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDemoInstance',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.CreateDemoInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_demo_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_demo_instance_with_options(request, runtime)

    def get_campaign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.GetCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    def get_campaign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_campaign_with_options(request, runtime)

    def get_historical_campaign_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoricalCampaignReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.GetHistoricalCampaignReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_historical_campaign_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_historical_campaign_report_with_options(request, runtime)

    def get_instance_ids_by_aliyun_uid_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceIdsByAliyunUidV2',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.GetInstanceIdsByAliyunUidV2Response(),
            self.call_api(params, req, runtime)
        )

    def get_instance_ids_by_aliyun_uid_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ids_by_aliyun_uid_v2with_options(request, runtime)

    def get_realtime_campaign_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeCampaignStats',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.GetRealtimeCampaignStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_realtime_campaign_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_campaign_stats_with_options(request, runtime)

    def import_admins_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ram_id_list):
            query['RamIdList'] = request.ram_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAdmins',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ImportAdminsResponse(),
            self.call_api(params, req, runtime)
        )

    def import_admins(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_admins_with_options(request, runtime)

    def issue_softphone_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IssueSoftphoneCommand',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.IssueSoftphoneCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def issue_softphone_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.issue_softphone_command_with_options(request, runtime)

    def list_attempts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAttempts',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_attempts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_attempts_with_options(request, runtime)

    def list_campaign_trending_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaignTrendingReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListCampaignTrendingReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_campaign_trending_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_campaign_trending_report_with_options(request, runtime)

    def list_campaigns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.actual_start_time_from):
            query['ActualStartTimeFrom'] = request.actual_start_time_from
        if not UtilClient.is_unset(request.actual_start_time_to):
            query['ActualStartTimeTo'] = request.actual_start_time_to
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.planed_start_time_from):
            query['PlanedStartTimeFrom'] = request.planed_start_time_from
        if not UtilClient.is_unset(request.planed_start_time_to):
            query['PlanedStartTimeTo'] = request.planed_start_time_to
        if not UtilClient.is_unset(request.queue_id):
            query['QueueId'] = request.queue_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCampaigns',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListCampaignsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_campaigns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_campaigns_with_options(request, runtime)

    def list_cases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCases',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListCasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cases_with_options(request, runtime)

    def list_historical_agent_skill_group_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.skill_group_id_list):
            query['SkillGroupIdList'] = request.skill_group_id_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.agent_id_list):
            body['AgentIdList'] = request.agent_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHistoricalAgentSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListHistoricalAgentSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_historical_agent_skill_group_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_historical_agent_skill_group_report_with_options(request, runtime)

    def list_interval_agent_skill_group_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.skill_group_id):
            query['SkillGroupId'] = request.skill_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntervalAgentSkillGroupReport',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListIntervalAgentSkillGroupReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_interval_agent_skill_group_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_interval_agent_skill_group_report_with_options(request, runtime)

    def list_mono_recordings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMonoRecordings',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ListMonoRecordingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mono_recordings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mono_recordings_with_options(request, runtime)

    def pause_campaign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.PauseCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    def pause_campaign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pause_campaign_with_options(request, runtime)

    def replace_migration_available_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operator_name):
            query['OperatorName'] = request.operator_name
        if not UtilClient.is_unset(request.operator_uid):
            query['OperatorUid'] = request.operator_uid
        if not UtilClient.is_unset(request.v_1numbers):
            query['V1Numbers'] = request.v_1numbers
        if not UtilClient.is_unset(request.v_2numbers):
            query['V2Numbers'] = request.v_2numbers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceMigrationAvailableNumbers',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ReplaceMigrationAvailableNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_migration_available_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_migration_available_numbers_with_options(request, runtime)

    def resume_campaign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.ResumeCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_campaign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_campaign_with_options(request, runtime)

    def save_rtcstats_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.general_info):
            query['GeneralInfo'] = request.general_info
        if not UtilClient.is_unset(request.goog_address):
            query['GoogAddress'] = request.goog_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.receiver_report):
            query['ReceiverReport'] = request.receiver_report
        if not UtilClient.is_unset(request.sender_report):
            query['SenderReport'] = request.sender_report
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRTCStatsV2',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.SaveRTCStatsV2Response(),
            self.call_api(params, req, runtime)
        )

    def save_rtcstats_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_rtcstats_v2with_options(request, runtime)

    def save_terminal_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.method_name):
            query['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unique_request_id):
            query['UniqueRequestId'] = request.unique_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTerminalLog',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.SaveTerminalLogResponse(),
            self.call_api(params, req, runtime)
        )

    def save_terminal_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_terminal_log_with_options(request, runtime)

    def save_web_rtc_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_id):
            query['CallId'] = request.call_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveWebRtcInfo',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.SaveWebRtcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def save_web_rtc_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtc_info_with_options(request, runtime)

    def submit_campaign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.campaign_id):
            query['CampaignId'] = request.campaign_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitCampaign',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.SubmitCampaignResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_campaign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_campaign_with_options(request, runtime)

    def unregister_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterDevice',
            version='2020-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_call_center_20200701_models.UnregisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unregister_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unregister_device_with_options(request, runtime)
