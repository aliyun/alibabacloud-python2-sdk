# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ccc20170705 import models as ccc20170705_models
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

    def add_agent_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.AddAgentDeviceResponse().from_map(
            self.do_rpcrequest('AddAgentDevice', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_agent_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_agent_device_with_options(request, runtime)

    def add_bulk_phone_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.AddBulkPhoneNumbersResponse().from_map(
            self.do_rpcrequest('AddBulkPhoneNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bulk_phone_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_bulk_phone_numbers_with_options(request, runtime)

    def add_phone_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.AddPhoneNumberResponse().from_map(
            self.do_rpcrequest('AddPhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_phone_number_with_options(request, runtime)

    def add_phone_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.AddPhoneTagsResponse().from_map(
            self.do_rpcrequest('AddPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_phone_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_phone_tags_with_options(request, runtime)

    def assign_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.AssignJobsResponse().from_map(
            self.do_rpcrequest('AssignJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_jobs_with_options(request, runtime)

    def assign_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.AssignUsersResponse().from_map(
            self.do_rpcrequest('AssignUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_users_with_options(request, runtime)

    def call_online_privacy_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CallOnlinePrivacyNumberResponse().from_map(
            self.do_rpcrequest('CallOnlinePrivacyNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def call_online_privacy_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.call_online_privacy_number_with_options(request, runtime)

    def cancel_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CancelJobsResponse().from_map(
            self.do_rpcrequest('CancelJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_jobs_with_options(request, runtime)

    def check_number_avaliable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CheckNumberAvaliableResponse().from_map(
            self.do_rpcrequest('CheckNumberAvaliable', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_number_avaliable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_number_avaliable_with_options(request, runtime)

    def commit_contact_flow_version_modification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CommitContactFlowVersionModificationResponse().from_map(
            self.do_rpcrequest('CommitContactFlowVersionModification', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commit_contact_flow_version_modification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.commit_contact_flow_version_modification_with_options(request, runtime)

    def create_batch_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateBatchJobsResponse().from_map(
            self.do_rpcrequest('CreateBatchJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_batch_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_batch_jobs_with_options(request, runtime)

    def create_cab_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateCabInstanceResponse().from_map(
            self.do_rpcrequest('CreateCabInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cab_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cab_instance_with_options(request, runtime)

    def create_contact_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateContactFlowResponse().from_map(
            self.do_rpcrequest('CreateContactFlow', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_contact_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_contact_flow_with_options(request, runtime)

    def create_fault_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateFaultResponse().from_map(
            self.do_rpcrequest('CreateFault', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fault(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_fault_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_job_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateJobGroupResponse().from_map(
            self.do_rpcrequest('CreateJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_group_with_options(request, runtime)

    def create_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateMediaResponse().from_map(
            self.do_rpcrequest('CreateMedia', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_media_with_options(request, runtime)

    def create_predictive_job_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreatePredictiveJobGroupResponse().from_map(
            self.do_rpcrequest('CreatePredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_predictive_job_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_predictive_job_group_with_options(request, runtime)

    def create_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateScenarioResponse().from_map(
            self.do_rpcrequest('CreateScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scenario_with_options(request, runtime)

    def create_scenario_from_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateScenarioFromTemplateResponse().from_map(
            self.do_rpcrequest('CreateScenarioFromTemplate', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scenario_from_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scenario_from_template_with_options(request, runtime)

    def create_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateSkillGroupResponse().from_map(
            self.do_rpcrequest('CreateSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_with_options(request, runtime)

    def create_survey_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateSurveyResponse().from_map(
            self.do_rpcrequest('CreateSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_survey(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_survey_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_voice_appraise_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.CreateVoiceAppraiseResponse().from_map(
            self.do_rpcrequest('CreateVoiceAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_voice_appraise(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_voice_appraise_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_job_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DeleteJobGroupResponse().from_map(
            self.do_rpcrequest('DeleteJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_group_with_options(request, runtime)

    def delete_media_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DeleteMediaResponse().from_map(
            self.do_rpcrequest('DeleteMedia', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_media_with_options(request, runtime)

    def delete_phone_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DeletePhoneTagsResponse().from_map(
            self.do_rpcrequest('DeletePhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_phone_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_phone_tags_with_options(request, runtime)

    def delete_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DeleteSkillGroupResponse().from_map(
            self.do_rpcrequest('DeleteSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_with_options(request, runtime)

    def delete_survey_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DeleteSurveyResponse().from_map(
            self.do_rpcrequest('DeleteSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_survey(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_survey_with_options(request, runtime)

    def dial_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DialExResponse().from_map(
            self.do_rpcrequest('DialEx', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dial_ex(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dial_ex_with_options(request, runtime)

    def dialogue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DialogueResponse().from_map(
            self.do_rpcrequest('Dialogue', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dialogue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    def disable_trunk_providers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DisableTrunkProvidersResponse().from_map(
            self.do_rpcrequest('DisableTrunkProviders', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_trunk_providers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_trunk_providers_with_options(request, runtime)

    def download_all_type_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DownloadAllTypeRecordingResponse().from_map(
            self.do_rpcrequest('DownloadAllTypeRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_all_type_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_all_type_recording_with_options(request, runtime)

    def download_cab_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DownloadCabRecordingResponse().from_map(
            self.do_rpcrequest('DownloadCabRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_cab_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_cab_recording_with_options(request, runtime)

    def download_original_statistics_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DownloadOriginalStatisticsReportResponse().from_map(
            self.do_rpcrequest('DownloadOriginalStatisticsReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_original_statistics_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_original_statistics_report_with_options(request, runtime)

    def download_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DownloadRecordingResponse().from_map(
            self.do_rpcrequest('DownloadRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_recording_with_options(request, runtime)

    def download_unreachable_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.DownloadUnreachableContactsResponse().from_map(
            self.do_rpcrequest('DownloadUnreachableContacts', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_unreachable_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_unreachable_contacts_with_options(request, runtime)

    def find_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.FindUsersResponse().from_map(
            self.do_rpcrequest('FindUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_users_with_options(request, runtime)

    def generate_agent_statistic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GenerateAgentStatisticReportResponse().from_map(
            self.do_rpcrequest('GenerateAgentStatisticReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_agent_statistic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_agent_statistic_report_with_options(request, runtime)

    def get_agent_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetAgentDataResponse().from_map(
            self.do_rpcrequest('GetAgentData', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_agent_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_data_with_options(request, runtime)

    def get_call_measure_summary_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetCallMeasureSummaryReportResponse().from_map(
            self.do_rpcrequest('GetCallMeasureSummaryReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_call_measure_summary_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_call_measure_summary_report_with_options(request, runtime)

    def get_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetConfigResponse().from_map(
            self.do_rpcrequest('GetConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_config_with_options(request, runtime)

    def get_conversation_detail_by_contact_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetConversationDetailByContactIdResponse().from_map(
            self.do_rpcrequest('GetConversationDetailByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conversation_detail_by_contact_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_detail_by_contact_id_with_options(request, runtime)

    def get_conversation_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetConversationListResponse().from_map(
            self.do_rpcrequest('GetConversationList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conversation_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_list_with_options(request, runtime)

    def get_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetInstanceResponse().from_map(
            self.do_rpcrequest('GetInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    def get_instance_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetInstanceStateResponse().from_map(
            self.do_rpcrequest('GetInstanceState', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_state_with_options(request, runtime)

    def get_instance_summary_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetInstanceSummaryReportResponse().from_map(
            self.do_rpcrequest('GetInstanceSummaryReport', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_summary_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_summary_report_with_options(request, runtime)

    def get_instance_summary_report_by_interval_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetInstanceSummaryReportByIntervalResponse().from_map(
            self.do_rpcrequest('GetInstanceSummaryReportByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_summary_report_by_interval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_summary_report_by_interval_with_options(request, runtime)

    def get_instance_summary_report_since_midnight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetInstanceSummaryReportSinceMidnightResponse().from_map(
            self.do_rpcrequest('GetInstanceSummaryReportSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_summary_report_since_midnight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_summary_report_since_midnight_with_options(request, runtime)

    def get_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobResponse().from_map(
            self.do_rpcrequest('GetJob', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    def get_job_data_upload_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobDataUploadParamsResponse().from_map(
            self.do_rpcrequest('GetJobDataUploadParams', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_data_upload_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_data_upload_params_with_options(request, runtime)

    def get_job_file_upload_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobFileUploadUrlResponse().from_map(
            self.do_rpcrequest('GetJobFileUploadUrl', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_file_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_file_upload_url_with_options(request, runtime)

    def get_job_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobGroupResponse().from_map(
            self.do_rpcrequest('GetJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_group_with_options(request, runtime)

    def get_job_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobListResponse().from_map(
            self.do_rpcrequest('GetJobList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_list_with_options(request, runtime)

    def get_job_status_by_call_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobStatusByCallIdResponse().from_map(
            self.do_rpcrequest('GetJobStatusByCallId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_status_by_call_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_by_call_id_with_options(request, runtime)

    def get_job_template_download_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetJobTemplateDownloadParamsResponse().from_map(
            self.do_rpcrequest('GetJobTemplateDownloadParams', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_template_download_params(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_job_template_download_params_with_options(request, runtime)

    def get_number_region_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetNumberRegionInfoResponse().from_map(
            self.do_rpcrequest('GetNumberRegionInfo', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_number_region_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_number_region_info_with_options(request, runtime)

    def get_record_oss_upload_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetRecordOssUploadParamResponse().from_map(
            self.do_rpcrequest('GetRecordOssUploadParam', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_record_oss_upload_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_record_oss_upload_param_with_options(request, runtime)

    def get_route_point_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetRoutePointResponse().from_map(
            self.do_rpcrequest('GetRoutePoint', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_route_point(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_route_point_with_options(request, runtime)

    def get_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetScenarioResponse().from_map(
            self.do_rpcrequest('GetScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_with_options(request, runtime)

    def get_service_extensions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetServiceExtensionsResponse().from_map(
            self.do_rpcrequest('GetServiceExtensions', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_extensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_extensions_with_options(request, runtime)

    def get_sms_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetSmsConfigResponse().from_map(
            self.do_rpcrequest('GetSmsConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sms_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sms_config_with_options(request, runtime)

    def get_survey_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetSurveyResponse().from_map(
            self.do_rpcrequest('GetSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_survey(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_survey_with_options(request, runtime)

    def get_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetTaskListResponse().from_map(
            self.do_rpcrequest('GetTaskList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_list_with_options(request, runtime)

    def get_turncredentials_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetTURNCredentialsResponse().from_map(
            self.do_rpcrequest('GetTURNCredentials', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turncredentials(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_turncredentials_with_options(request, runtime)

    def get_turnserver_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetTURNServerListResponse().from_map(
            self.do_rpcrequest('GetTURNServerList', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_turnserver_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_turnserver_list_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetUserResponse().from_map(
            self.do_rpcrequest('GetUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def get_user_by_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.GetUserByExtensionResponse().from_map(
            self.do_rpcrequest('GetUserByExtension', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_by_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_extension_with_options(request, runtime)

    def inflight_task_timeout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.InflightTaskTimeoutResponse().from_map(
            self.do_rpcrequest('InflightTaskTimeout', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def inflight_task_timeout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.inflight_task_timeout_with_options(request, runtime)

    def launch_appraise_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.LaunchAppraiseResponse().from_map(
            self.do_rpcrequest('LaunchAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_appraise(self, request):
        runtime = util_models.RuntimeOptions()
        return self.launch_appraise_with_options(request, runtime)

    def launch_short_message_appraise_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.LaunchShortMessageAppraiseResponse().from_map(
            self.do_rpcrequest('LaunchShortMessageAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_short_message_appraise(self, request):
        runtime = util_models.RuntimeOptions()
        return self.launch_short_message_appraise_with_options(request, runtime)

    def list_agent_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentDevicesResponse().from_map(
            self.do_rpcrequest('ListAgentDevices', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_devices_with_options(request, runtime)

    def list_agent_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentEventsResponse().from_map(
            self.do_rpcrequest('ListAgentEvents', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_events_with_options(request, runtime)

    def list_agent_state_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentStateLogsResponse().from_map(
            self.do_rpcrequest('ListAgentStateLogs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_state_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_state_logs_with_options(request, runtime)

    def list_agent_states_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentStatesResponse().from_map(
            self.do_rpcrequest('ListAgentStates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_states(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_states_with_options(request, runtime)

    def list_agent_summary_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentSummaryReportsResponse().from_map(
            self.do_rpcrequest('ListAgentSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_summary_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_with_options(request, runtime)

    def list_agent_summary_reports_by_interval_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentSummaryReportsByIntervalResponse().from_map(
            self.do_rpcrequest('ListAgentSummaryReportsByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_summary_reports_by_interval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_by_interval_with_options(request, runtime)

    def list_agent_summary_reports_since_midnight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListAgentSummaryReportsSinceMidnightResponse().from_map(
            self.do_rpcrequest('ListAgentSummaryReportsSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_agent_summary_reports_since_midnight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_agent_summary_reports_since_midnight_with_options(request, runtime)

    def list_basic_statistics_report_sub_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListBasicStatisticsReportSubItemsResponse().from_map(
            self.do_rpcrequest('ListBasicStatisticsReportSubItems', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_basic_statistics_report_sub_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_basic_statistics_report_sub_items_with_options(request, runtime)

    def list_call_detail_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListCallDetailRecordsResponse().from_map(
            self.do_rpcrequest('ListCallDetailRecords', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_detail_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_call_detail_records_with_options(request, runtime)

    def list_call_event_detail_by_contact_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListCallEventDetailByContactIdResponse().from_map(
            self.do_rpcrequest('ListCallEventDetailByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_event_detail_by_contact_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_call_event_detail_by_contact_id_with_options(request, runtime)

    def list_call_measure_summary_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListCallMeasureSummaryReportsResponse().from_map(
            self.do_rpcrequest('ListCallMeasureSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_measure_summary_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_call_measure_summary_reports_with_options(request, runtime)

    def list_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListConfigResponse().from_map(
            self.do_rpcrequest('ListConfig', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_config_with_options(request, runtime)

    def list_contact_flows_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListContactFlowsResponse().from_map(
            self.do_rpcrequest('ListContactFlows', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_contact_flows(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_contact_flows_with_options(request, runtime)

    def list_instances_of_user_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return ccc20170705_models.ListInstancesOfUserResponse().from_map(
            self.do_rpcrequest('ListInstancesOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances_of_user(self):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_of_user_with_options(runtime)

    def list_ivr_tracking_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListIvrTrackingDetailResponse().from_map(
            self.do_rpcrequest('ListIvrTrackingDetail', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ivr_tracking_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ivr_tracking_detail_with_options(request, runtime)

    def list_job_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListJobGroupsResponse().from_map(
            self.do_rpcrequest('ListJobGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_groups_with_options(request, runtime)

    def list_jobs_by_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListJobsByGroupResponse().from_map(
            self.do_rpcrequest('ListJobsByGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jobs_by_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_by_group_with_options(request, runtime)

    def list_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListJobStatusResponse().from_map(
            self.do_rpcrequest('ListJobStatus', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_status_with_options(request, runtime)

    def list_medias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListMediasResponse().from_map(
            self.do_rpcrequest('ListMedias', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_medias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_medias_with_options(request, runtime)

    def list_outbound_phone_number_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListOutboundPhoneNumberOfUserResponse().from_map(
            self.do_rpcrequest('ListOutboundPhoneNumberOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_phone_number_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_phone_number_of_user_with_options(request, runtime)

    def list_phone_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListPhoneNumbersResponse().from_map(
            self.do_rpcrequest('ListPhoneNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_phone_numbers_with_options(request, runtime)

    def list_phone_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListPhoneTagsResponse().from_map(
            self.do_rpcrequest('ListPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_phone_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_phone_tags_with_options(request, runtime)

    def list_real_time_agent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListRealTimeAgentResponse().from_map(
            self.do_rpcrequest('ListRealTimeAgent', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_real_time_agent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_real_time_agent_with_options(request, runtime)

    def list_recent_call_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListRecentCallRecordsResponse().from_map(
            self.do_rpcrequest('ListRecentCallRecords', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recent_call_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_recent_call_records_with_options(request, runtime)

    def list_recording_of_dual_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListRecordingOfDualTrackResponse().from_map(
            self.do_rpcrequest('ListRecordingOfDualTrack', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recording_of_dual_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_recording_of_dual_track_with_options(request, runtime)

    def list_recordings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListRecordingsResponse().from_map(
            self.do_rpcrequest('ListRecordings', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recordings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_recordings_with_options(request, runtime)

    def list_recordings_by_contact_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListRecordingsByContactIdResponse().from_map(
            self.do_rpcrequest('ListRecordingsByContactId', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_recordings_by_contact_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_recordings_by_contact_id_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListRolesResponse().from_map(
            self.do_rpcrequest('ListRoles', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def list_scenarios_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListScenariosResponse().from_map(
            self.do_rpcrequest('ListScenarios', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenarios(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scenarios_with_options(request, runtime)

    def list_scenario_templates_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return ccc20170705_models.ListScenarioTemplatesResponse().from_map(
            self.do_rpcrequest('ListScenarioTemplates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenario_templates(self):
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_templates_with_options(runtime)

    def list_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSkillGroupsResponse().from_map(
            self.do_rpcrequest('ListSkillGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_with_options(request, runtime)

    def list_skill_groups_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSkillGroupsOfUserResponse().from_map(
            self.do_rpcrequest('ListSkillGroupsOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_groups_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_groups_of_user_with_options(request, runtime)

    def list_skill_group_states_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSkillGroupStatesResponse().from_map(
            self.do_rpcrequest('ListSkillGroupStates', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_states(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_states_with_options(request, runtime)

    def list_skill_group_summary_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSkillGroupSummaryReportsResponse().from_map(
            self.do_rpcrequest('ListSkillGroupSummaryReports', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_summary_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_with_options(request, runtime)

    def list_skill_group_summary_reports_by_interval_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSkillGroupSummaryReportsByIntervalResponse().from_map(
            self.do_rpcrequest('ListSkillGroupSummaryReportsByInterval', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_summary_reports_by_interval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_by_interval_with_options(request, runtime)

    def list_skill_group_summary_reports_since_midnight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSkillGroupSummaryReportsSinceMidnightResponse().from_map(
            self.do_rpcrequest('ListSkillGroupSummaryReportsSinceMidnight', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_summary_reports_since_midnight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_summary_reports_since_midnight_with_options(request, runtime)

    def list_surveys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListSurveysResponse().from_map(
            self.do_rpcrequest('ListSurveys', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_surveys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_surveys_with_options(request, runtime)

    def list_transferable_skill_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListTransferableSkillGroupsResponse().from_map(
            self.do_rpcrequest('ListTransferableSkillGroups', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_transferable_skill_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_transferable_skill_groups_with_options(request, runtime)

    def list_trunk_providers_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return ccc20170705_models.ListTrunkProvidersResponse().from_map(
            self.do_rpcrequest('ListTrunkProviders', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trunk_providers(self):
        runtime = util_models.RuntimeOptions()
        return self.list_trunk_providers_with_options(runtime)

    def list_trunks_of_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListTrunksOfSkillGroupResponse().from_map(
            self.do_rpcrequest('ListTrunksOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trunks_of_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trunks_of_skill_group_with_options(request, runtime)

    def list_unreachable_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListUnreachableContactsResponse().from_map(
            self.do_rpcrequest('ListUnreachableContacts', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_unreachable_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_unreachable_contacts_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_users_of_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListUsersOfSkillGroupResponse().from_map(
            self.do_rpcrequest('ListUsersOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users_of_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_of_skill_group_with_options(request, runtime)

    def list_voice_appraise_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ListVoiceAppraiseResponse().from_map(
            self.do_rpcrequest('ListVoiceAppraise', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_voice_appraise(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_voice_appraise_with_options(request, runtime)

    def modify_agent_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyAgentDeviceResponse().from_map(
            self.do_rpcrequest('ModifyAgentDevice', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_agent_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_agent_device_with_options(request, runtime)

    def modify_cab_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyCabInstanceResponse().from_map(
            self.do_rpcrequest('ModifyCabInstance', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cab_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_cab_instance_with_options(request, runtime)

    def modify_phone_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyPhoneNumberResponse().from_map(
            self.do_rpcrequest('ModifyPhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_number_with_options(request, runtime)

    def modify_phone_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyPhoneTagsResponse().from_map(
            self.do_rpcrequest('ModifyPhoneTags', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_phone_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_tags_with_options(request, runtime)

    def modify_primary_trunks_of_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyPrimaryTrunksOfSkillGroupResponse().from_map(
            self.do_rpcrequest('ModifyPrimaryTrunksOfSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_primary_trunks_of_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_primary_trunks_of_skill_group_with_options(request, runtime)

    def modify_privacy_number_call_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyPrivacyNumberCallDetailResponse().from_map(
            self.do_rpcrequest('ModifyPrivacyNumberCallDetail', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_privacy_number_call_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_privacy_number_call_detail_with_options(request, runtime)

    def modify_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyScenarioResponse().from_map(
            self.do_rpcrequest('ModifyScenario', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_scenario_with_options(request, runtime)

    def modify_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifySkillGroupResponse().from_map(
            self.do_rpcrequest('ModifySkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_with_options(request, runtime)

    def modify_skill_group_of_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifySkillGroupOfUserResponse().from_map(
            self.do_rpcrequest('ModifySkillGroupOfUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group_of_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_of_user_with_options(request, runtime)

    def modify_skill_group_outbound_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifySkillGroupOutboundNumbersResponse().from_map(
            self.do_rpcrequest('ModifySkillGroupOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_skill_group_outbound_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_skill_group_outbound_numbers_with_options(request, runtime)

    def modify_survey_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifySurveyResponse().from_map(
            self.do_rpcrequest('ModifySurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_survey(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_survey_with_options(request, runtime)

    def modify_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ModifyUserResponse().from_map(
            self.do_rpcrequest('ModifyUser', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    def pick_global_outbound_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.PickGlobalOutboundNumbersResponse().from_map(
            self.do_rpcrequest('PickGlobalOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_global_outbound_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pick_global_outbound_numbers_with_options(request, runtime)

    def pick_local_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.PickLocalNumberResponse().from_map(
            self.do_rpcrequest('PickLocalNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_local_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pick_local_number_with_options(request, runtime)

    def pick_outbound_numbers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.PickOutboundNumbersResponse().from_map(
            self.do_rpcrequest('PickOutboundNumbers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pick_outbound_numbers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pick_outbound_numbers_with_options(request, runtime)

    def publish_contact_flow_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.PublishContactFlowVersionResponse().from_map(
            self.do_rpcrequest('PublishContactFlowVersion', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_contact_flow_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_contact_flow_version_with_options(request, runtime)

    def publish_predictive_job_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.PublishPredictiveJobGroupResponse().from_map(
            self.do_rpcrequest('PublishPredictiveJobGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_predictive_job_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_predictive_job_group_with_options(request, runtime)

    def publish_survey_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.PublishSurveyResponse().from_map(
            self.do_rpcrequest('PublishSurvey', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_survey(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_survey_with_options(request, runtime)

    def refresh_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.RefreshTokenResponse().from_map(
            self.do_rpcrequest('RefreshToken', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_token_with_options(request, runtime)

    def remove_phone_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.RemovePhoneNumberResponse().from_map(
            self.do_rpcrequest('RemovePhoneNumber', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_phone_number_with_options(request, runtime)

    def remove_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.RemoveUsersResponse().from_map(
            self.do_rpcrequest('RemoveUsers', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    def remove_users_from_skill_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.RemoveUsersFromSkillGroupResponse().from_map(
            self.do_rpcrequest('RemoveUsersFromSkillGroup', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users_from_skill_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_skill_group_with_options(request, runtime)

    def request_login_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.RequestLoginInfoResponse().from_map(
            self.do_rpcrequest('RequestLoginInfo', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def request_login_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_login_info_with_options(request, runtime)

    def reset_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ResetUserStatusResponse().from_map(
            self.do_rpcrequest('ResetUserStatus', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_user_status_with_options(request, runtime)

    def resume_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ResumeJobsResponse().from_map(
            self.do_rpcrequest('ResumeJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_jobs_with_options(request, runtime)

    def resume_predictive_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.ResumePredictiveJobsResponse().from_map(
            self.do_rpcrequest('ResumePredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_predictive_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_predictive_jobs_with_options(request, runtime)

    def save_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SaveStatsResponse().from_map(
            self.do_rpcrequest('SaveStats', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_stats_with_options(request, runtime)

    def save_web_rtcstats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SaveWebRTCStatsResponse().from_map(
            self.do_rpcrequest('SaveWebRTCStats', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_web_rtcstats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_web_rtcstats_with_options(request, runtime)

    def send_predefined_short_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SendPredefinedShortMessageResponse().from_map(
            self.do_rpcrequest('SendPredefinedShortMessage', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_predefined_short_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_predefined_short_message_with_options(request, runtime)

    def start_back_2back_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.StartBack2BackCallResponse().from_map(
            self.do_rpcrequest('StartBack2BackCall', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_back_2back_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_back_2back_call_with_options(request, runtime)

    def start_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.StartJobResponse().from_map(
            self.do_rpcrequest('StartJob', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_job_with_options(request, runtime)

    def submit_batch_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SubmitBatchJobsResponse().from_map(
            self.do_rpcrequest('SubmitBatchJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_batch_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_batch_jobs_with_options(request, runtime)

    def submit_cab_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SubmitCabRecordingResponse().from_map(
            self.do_rpcrequest('SubmitCabRecording', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_cab_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_cab_recording_with_options(request, runtime)

    def suspend_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SuspendJobsResponse().from_map(
            self.do_rpcrequest('SuspendJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_jobs_with_options(request, runtime)

    def suspend_predictive_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.SuspendPredictiveJobsResponse().from_map(
            self.do_rpcrequest('SuspendPredictiveJobs', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_predictive_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_predictive_jobs_with_options(request, runtime)

    def task_preparing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ccc20170705_models.TaskPreparingResponse().from_map(
            self.do_rpcrequest('TaskPreparing', '2017-07-05', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def task_preparing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.task_preparing_with_options(request, runtime)
