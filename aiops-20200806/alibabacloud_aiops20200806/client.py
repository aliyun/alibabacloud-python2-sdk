# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiops20200806 import models as aiops_20200806_models
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
        self._endpoint = self.get_endpoint('aiops', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_algorithm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_id):
            query['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expand_information):
            query['ExpandInformation'] = request.expand_information
        if not UtilClient.is_unset(request.index_id):
            query['IndexId'] = request.index_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    def add_algorithm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_algorithm_with_options(request, runtime)

    def add_business_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.AddBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.create_user):
            query['CreateUser'] = request.create_user
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_business_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_business_group_with_options(request, runtime)

    def add_business_group_one_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.business_group_desc):
            body['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_name):
            body['BusinessGroupName'] = request.business_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddBusinessGroupOne',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddBusinessGroupOneResponse(),
            self.call_api(params, req, runtime)
        )

    def add_business_group_one(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_business_group_one_with_options(request, runtime)

    def add_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            query['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def add_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_scenario_with_options(request, runtime)

    def add_scene_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_scene_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_scene_list_with_options(request, runtime)

    def add_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handle_suggest_desc):
            query['HandleSuggestDesc'] = request.handle_suggest_desc
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.root_cause_desc):
            query['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_causes_log):
            query['RootCausesLog'] = request.root_causes_log
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.script_desc):
            query['ScriptDesc'] = request.script_desc
        if not UtilClient.is_unset(request.script_language):
            query['ScriptLanguage'] = request.script_language
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.script_version):
            query['ScriptVersion'] = request.script_version
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def add_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_script_with_options(request, runtime)

    def add_tag_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AddTagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tag_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tag_info_with_options(request, runtime)

    def again_submit_apply_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgainSubmitApplyPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.AgainSubmitApplyPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def again_submit_apply_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.again_submit_apply_permission_with_options(request, runtime)

    def apply_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ApplyAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_authorization_with_options(request, runtime)

    def check_data_source_link_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataSourceLinkConnection',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CheckDataSourceLinkConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def check_data_source_link_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_data_source_link_connection_with_options(request, runtime)

    def check_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CheckLogResponse(),
            self.call_api(params, req, runtime)
        )

    def check_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_log_with_options(request, runtime)

    def close_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.close_desc):
            query['CloseDesc'] = request.close_desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CloseEventResponse(),
            self.call_api(params, req, runtime)
        )

    def close_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_event_with_options(request, runtime)

    def confirm_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ConfirmAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_authorization_with_options(request, runtime)

    def count_latest_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountLatestReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CountLatestReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def count_latest_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_latest_reports_with_options(request, runtime)

    def create_alert_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.webhook):
            body['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    def create_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_contact_group_json):
            body['AlertContactGroupJson'] = request.alert_contact_group_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    def create_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def create_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    def create_dump_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDump',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateDumpResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dump(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dump_with_options(request, runtime)

    def create_inspection_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInspectionRecord',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateInspectionRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_inspection_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_inspection_record_with_options(request, runtime)

    def create_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMessage',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_message_with_options(request, runtime)

    def create_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.metric_list_json):
            body['MetricListJson'] = request.metric_list_json
        if not UtilClient.is_unset(request.node_list_json):
            body['NodeListJson'] = request.node_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_desc):
            body['SceneDesc'] = request.scene_desc
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_owner):
            body['SceneOwner'] = request.scene_owner
        if not UtilClient.is_unset(request.scene_webhook):
            body['SceneWebhook'] = request.scene_webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_with_options(request, runtime)

    def create_scene_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fc_function_name):
            body['FcFunctionName'] = request.fc_function_name
        if not UtilClient.is_unset(request.fc_handler):
            body['FcHandler'] = request.fc_handler
        if not UtilClient.is_unset(request.fc_initializer):
            body['FcInitializer'] = request.fc_initializer
        if not UtilClient.is_unset(request.fc_region_no):
            body['FcRegionNo'] = request.fc_region_no
        if not UtilClient.is_unset(request.fc_service_name):
            body['FcServiceName'] = request.fc_service_name
        if not UtilClient.is_unset(request.model_desc):
            body['ModelDesc'] = request.model_desc
        if not UtilClient.is_unset(request.model_language):
            body['ModelLanguage'] = request.model_language
        if not UtilClient.is_unset(request.model_memo):
            body['ModelMemo'] = request.model_memo
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.root_cause_desc):
            body['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_cause_solution):
            body['RootCauseSolution'] = request.root_cause_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scene_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_model_with_options(request, runtime)

    def create_scene_model_apply_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSceneModelApply',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.CreateSceneModelApplyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scene_model_apply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_model_apply_with_options(request, runtime)

    def del_business_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DelBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def del_business_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_business_group_with_options(request, runtime)

    def delete_alert_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    def delete_alert_contact_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactFromGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_from_group_with_options(request, runtime)

    def delete_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    def delete_alert_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_setting_with_options(request, runtime)

    def delete_alert_setting_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.customer_ids_json):
            body['CustomerIdsJson'] = request.customer_ids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAlertSettingList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlertSettingListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_setting_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_setting_list_with_options(request, runtime)

    def delete_algorithm_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlgorithmInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteAlgorithmInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_algorithm_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_algorithm_info_with_options(request, runtime)

    def delete_business_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_business_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_group_with_options(request, runtime)

    def delete_business_resource_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessResourceTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteBusinessResourceTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_business_resource_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_resource_tag_with_options(request, runtime)

    def delete_data_source_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_config_with_options(request, runtime)

    def delete_group_topology_tag_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroupTopologyTagLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteGroupTopologyTagLogResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group_topology_tag_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_topology_tag_log_with_options(request, runtime)

    def delete_real_scene_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRealSceneInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteRealSceneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_real_scene_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_real_scene_info_with_options(request, runtime)

    def delete_report_email_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mail_config_id):
            body['MailConfigId'] = request.mail_config_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteReportEmailConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteReportEmailConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_report_email_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_report_email_config_with_options(request, runtime)

    def delete_resource_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inspection_whitelist_id):
            body['InspectionWhitelistId'] = request.inspection_whitelist_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceWhitelist',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteResourceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_whitelist_with_options(request, runtime)

    def delete_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    def delete_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_with_options(request, runtime)

    def delete_scene_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scene_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_list_with_options(request, runtime)

    def delete_scene_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.sure_delete):
            body['SureDelete'] = request.sure_delete
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scene_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_model_with_options(request, runtime)

    def delete_tag_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DeleteTagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_info_with_options(request, runtime)

    def describe_account_alert_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAlertEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAccountAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_account_alert_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_alert_event_with_options(request, runtime)

    def describe_advisor_inspection_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorInspectionProducts',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAdvisorInspectionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advisor_inspection_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_inspection_products_with_options(request, runtime)

    def describe_alert_business_group_with_alert_setting_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertBusinessGroupWithAlertSettingId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertBusinessGroupWithAlertSettingIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_business_group_with_alert_setting_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_business_group_with_alert_setting_id_with_options(request, runtime)

    def describe_alert_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_by):
            body['SearchBy'] = request.search_by
        if not UtilClient.is_unset(request.search_like):
            body['SearchLike'] = request.search_like
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_with_options(request, runtime)

    def describe_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_like):
            body['SearchLike'] = request.search_like
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_group_with_options(request, runtime)

    def describe_alert_contact_with_alert_setting_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.contact_type):
            body['ContactType'] = request.contact_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactWithAlertSettingId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactWithAlertSettingIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_contact_with_alert_setting_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_with_alert_setting_id_with_options(request, runtime)

    def describe_alert_contact_with_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertContactWithGroupId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertContactWithGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_contact_with_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_contact_with_group_id_with_options(request, runtime)

    def describe_alert_detail_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertDetailData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_detail_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_detail_data_with_options(request, runtime)

    def describe_alert_detail_trend_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertDetailTrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_detail_trend_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_detail_trend_data_with_options(request, runtime)

    def describe_alert_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_event_with_options(request, runtime)

    def describe_alert_final_data_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertFinalDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertFinalDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_final_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_final_data_list_with_options(request, runtime)

    def describe_alert_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_resource_with_options(request, runtime)

    def describe_alert_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.customer_name):
            body['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not UtilClient.is_unset(request.setting_status):
            body['SettingStatus'] = request.setting_status
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_setting_with_options(request, runtime)

    def describe_alert_setting_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSettingById',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAlertSettingByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_setting_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_setting_by_id_with_options(request, runtime)

    def describe_all_alert_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_alert_contact_with_options(request, runtime)

    def describe_all_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAllAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_alert_contact_group_with_options(request, runtime)

    def describe_all_business_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllBusinessGroupInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllBusinessGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_business_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_business_group_info_with_options(request, runtime)

    def describe_all_scene_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAllSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAllSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_scene_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_all_scene_model_with_options(request, runtime)

    def describe_analysis_data_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_extend):
            query['MetricExtend'] = request.metric_extend
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeAnalysisDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_analysis_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_analysis_data_list_with_options(request, runtime)

    def describe_business_analysis_data_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBusinessAnalysisDataList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeBusinessAnalysisDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_business_analysis_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_business_analysis_data_list_with_options(request, runtime)

    def describe_diagnose_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnose',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeDiagnoseResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnose(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnose_with_options(request, runtime)

    def describe_diagnose_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnoseResult',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeDiagnoseResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnose_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnose_result_with_options(request, runtime)

    def describe_event_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTopology',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeEventTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_topology_with_options(request, runtime)

    def describe_event_topology_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTopologyDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeEventTopologyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_topology_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_topology_detail_with_options(request, runtime)

    def describe_fc_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcFunction',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fc_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fc_function_with_options(request, runtime)

    def describe_fc_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcRegion',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fc_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fc_region_with_options(request, runtime)

    def describe_fc_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.prefix):
            body['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFcService',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeFcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fc_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fc_service_with_options(request, runtime)

    def describe_history_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.last_find_time_end):
            body['LastFindTimeEnd'] = request.last_find_time_end
        if not UtilClient.is_unset(request.last_find_time_start):
            body['LastFindTimeStart'] = request.last_find_time_start
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeHistoryRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeHistoryRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_history_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_history_risk_with_options(request, runtime)

    def describe_inspection_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.inspection_record_id):
            body['InspectionRecordId'] = request.inspection_record_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionProgress',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inspection_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_progress_with_options(request, runtime)

    def describe_inspection_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionResources',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inspection_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_resources_with_options(request, runtime)

    def describe_inspection_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionResult',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inspection_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_result_with_options(request, runtime)

    def describe_inspection_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.risk_desc):
            body['RiskDesc'] = request.risk_desc
        if not UtilClient.is_unset(request.risk_enable_status):
            body['RiskEnableStatus'] = request.risk_enable_status
        if not UtilClient.is_unset(request.risk_name):
            body['RiskName'] = request.risk_name
        if not UtilClient.is_unset(request.risk_type):
            body['RiskType'] = request.risk_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionSettings',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inspection_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_settings_with_options(request, runtime)

    def describe_inspection_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionThreshold',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inspection_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_threshold_with_options(request, runtime)

    def describe_inspection_whitelists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInspectionWhitelists',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInspectionWhitelistsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_inspection_whitelists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_inspection_whitelists_with_options(request, runtime)

    def describe_invocation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResults',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeInvocationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_invocation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_results_with_options(request, runtime)

    def describe_last_inspection_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLastInspectionSummary',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeLastInspectionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_last_inspection_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_last_inspection_summary_with_options(request, runtime)

    def describe_model_relation_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeModelRelationScenes',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeModelRelationScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_model_relation_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_model_relation_scenes_with_options(request, runtime)

    def describe_product_risk_pie_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductRiskPie',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeProductRiskPieResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_product_risk_pie(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_product_risk_pie_with_options(request, runtime)

    def describe_report_data_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeReportData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_report_data(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_report_data_with_options(runtime)

    def describe_report_email_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReportEmailConfigs',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportEmailConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_report_email_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_report_email_configs_with_options(request, runtime)

    def describe_report_subscriptions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReportSubscriptions',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeReportSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_report_subscriptions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_report_subscriptions_with_options(request, runtime)

    def describe_resource_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.first_load):
            query['FirstLoad'] = request.first_load
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeResourceMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_resource_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_metric_with_options(request, runtime)

    def describe_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_with_options(request, runtime)

    def describe_risk_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_config_with_options(request, runtime)

    def describe_risk_event_details_with_options(self, request, runtime):
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
            action='DescribeRiskEventDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_event_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_details_with_options(request, runtime)

    def describe_risk_event_list_with_options(self, request, runtime):
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
            action='DescribeRiskEventList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_list_with_options(request, runtime)

    def describe_risk_event_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventTopology',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskEventTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_event_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_topology_with_options(request, runtime)

    def describe_risk_result_severity_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskResultSeveritySummary',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResultSeveritySummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_result_severity_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_result_severity_summary_with_options(request, runtime)

    def describe_risk_result_statistical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.continuous_days):
            body['ContinuousDays'] = request.continuous_days
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRiskResultStatistical',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeRiskResultStatisticalResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_result_statistical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_result_statistical_with_options(request, runtime)

    def describe_scene_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_detail_with_options(request, runtime)

    def describe_scene_model_by_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelByType',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_model_by_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_model_by_type_with_options(request, runtime)

    def describe_scene_model_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_model_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_model_detail_with_options(request, runtime)

    def describe_scene_model_version_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModelVersionHistory',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelVersionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_model_version_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_model_version_history_with_options(request, runtime)

    def describe_scene_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_status):
            body['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneModels',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_models_with_options(request, runtime)

    def describe_scene_system_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_status):
            body['ModelStatus'] = request.model_status
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type_id):
            body['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSceneSystemModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeSceneSystemModelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_system_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_system_model_with_options(request, runtime)

    def describe_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_status):
            body['SceneStatus'] = request.scene_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeScenes',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scenes_with_options(request, runtime)

    def describe_statistical_data_by_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalDataByProduct',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeStatisticalDataByProductResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_statistical_data_by_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_by_product_with_options(request, runtime)

    def describe_statistical_data_by_risk_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalDataByRiskCode',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeStatisticalDataByRiskCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_statistical_data_by_risk_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_by_risk_code_with_options(request, runtime)

    def describe_whitelist_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWhitelistResources',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.DescribeWhitelistResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_whitelist_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_whitelist_resources_with_options(request, runtime)

    def end_script_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.EndScriptListResponse(),
            self.call_api(params, req, runtime)
        )

    def end_script_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.end_script_list_with_options(request, runtime)

    def feedback_alert_algorithm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.algorithm_accurate_describe):
            query['AlgorithmAccurateDescribe'] = request.algorithm_accurate_describe
        if not UtilClient.is_unset(request.algorithm_accurate_state):
            query['AlgorithmAccurateState'] = request.algorithm_accurate_state
        if not UtilClient.is_unset(request.feedback_type):
            query['FeedbackType'] = request.feedback_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FeedbackAlertAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.FeedbackAlertAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    def feedback_alert_algorithm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.feedback_alert_algorithm_with_options(request, runtime)

    def get_aiops_event_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.event_unique_id):
            query['EventUniqueId'] = request.event_unique_id
        if not UtilClient.is_unset(request.feedback_status):
            query['FeedbackStatus'] = request.feedback_status
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prediction_state):
            query['PredictionState'] = request.prediction_state
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiopsEventList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAiopsEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aiops_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_aiops_event_list_with_options(request, runtime)

    def get_aiops_event_new_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAiopsEventNewList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAiopsEventNewListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aiops_event_new_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_aiops_event_new_list_with_options(request, runtime)

    def get_alert_detail_trend_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.abnormal_id):
            query['AbnormalId'] = request.abnormal_id
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertDetailTrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alert_detail_trend_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alert_detail_trend_data_with_options(request, runtime)

    def get_alert_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alert_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alert_list_with_options(request, runtime)

    def get_alert_trent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlertTrentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alert_trent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alert_trent_with_options(request, runtime)

    def get_algorithm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expand_information):
            query['ExpandInformation'] = request.expand_information
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_with_options(request, runtime)

    def get_algorithm_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm_type_code):
            query['AlgorithmTypeCode'] = request.algorithm_type_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_config_with_options(request, runtime)

    def get_algorithm_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_data_with_options(request, runtime)

    def get_algorithm_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_details_with_options(request, runtime)

    def get_algorithm_forecast_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmForecastData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmForecastDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm_forecast_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_forecast_data_with_options(request, runtime)

    def get_algorithm_forecast_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmForecastDetails',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmForecastDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm_forecast_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_forecast_details_with_options(request, runtime)

    def get_algorithm_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlgorithmList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAlgorithmListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_algorithm_list_with_options(request, runtime)

    def get_all_algorithm_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllAlgorithmConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAllAlgorithmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_algorithm_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_all_algorithm_config_with_options(request, runtime)

    def get_all_tag_resource_num_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllTagResourceNumList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAllTagResourceNumListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_tag_resource_num_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_all_tag_resource_num_list_with_options(request, runtime)

    def get_analysis_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnalysisProcess',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAnalysisProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def get_analysis_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_analysis_process_with_options(request, runtime)

    def get_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_with_options(request, runtime)

    def get_avg_repair_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAvgRepairTime',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetAvgRepairTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_avg_repair_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_avg_repair_time_with_options(request, runtime)

    def get_back_script_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBackScriptListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_back_script_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_back_script_list_with_options(request, runtime)

    def get_business_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_with_options(request, runtime)

    def get_business_group_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupAllResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_group_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_all_with_options(request, runtime)

    def get_business_group_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupIndex',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_group_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_index_with_options(request, runtime)

    def get_business_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_info_with_options(request, runtime)

    def get_business_group_overview_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessGroupOverviewList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessGroupOverviewListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_group_overview_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_group_overview_list_with_options(request, runtime)

    def get_business_log_alert_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_log_alert_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_log_alert_detail_with_options(request, runtime)

    def get_business_log_alert_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_log_alert_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_log_alert_list_with_options(request, runtime)

    def get_business_log_alert_top_nwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessLogAlertTopN',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessLogAlertTopNResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_log_alert_top_n(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_log_alert_top_nwith_options(request, runtime)

    def get_business_metric_alert_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_alert_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_alert_detail_list_with_options(request, runtime)

    def get_business_metric_alert_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_alert_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_alert_list_with_options(request, runtime)

    def get_business_metric_alert_top_nwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.top_num):
            query['TopNum'] = request.top_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAlertTopN',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAlertTopNResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_alert_top_n(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_alert_top_nwith_options(request, runtime)

    def get_business_metric_all_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricAllList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricAllListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_all_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_all_list_with_options(request, runtime)

    def get_business_metric_forecast_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricForecastList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricForecastListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_forecast_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_forecast_list_with_options(request, runtime)

    def get_business_metric_resource_by_metric_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricResourceByMetricId',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricResourceByMetricIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_resource_by_metric_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_resource_by_metric_id_with_options(request, runtime)

    def get_business_metric_scene_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessMetricSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetBusinessMetricSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_metric_scene_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_metric_scene_list_with_options(request, runtime)

    def get_cid_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCidInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCidInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cid_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cid_info_with_options(request, runtime)

    def get_cloud_all_resource_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudAllResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudAllResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_all_resource_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_all_resource_list_with_options(request, runtime)

    def get_cloud_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_resource_with_options(request, runtime)

    def get_cloud_resource_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_region_id):
            query['CloudRegionId'] = request.cloud_region_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_optional):
            query['IsOptional'] = request.is_optional
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIp'] = request.private_ip
        if not UtilClient.is_unset(request.release_status):
            query['ReleaseStatus'] = request.release_status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetCloudResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_resource_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_resource_list_with_options(request, runtime)

    def get_connect_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectInstances',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetConnectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_connect_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connect_instances_with_options(request, runtime)

    def get_data_source_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_detail_with_options(request, runtime)

    def get_data_source_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_list_with_options(request, runtime)

    def get_data_source_target_param_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataSourceTargetParamList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataSourceTargetParamListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source_target_param_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_target_param_list_with_options(request, runtime)

    def get_data_volume_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataVolume',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_volume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_volume_with_options(request, runtime)

    def get_diag_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.diagnostic_id):
            query['DiagnosticId'] = request.diagnostic_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDiagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_diag_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_diag_info_with_options(request, runtime)

    def get_domain_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_config_with_options(request, runtime)

    def get_event_ab_normal_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_ab_normal_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_ab_normal_detail_with_options(request, runtime)

    def get_event_ab_normal_detail_trend_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalDetailTrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalDetailTrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_ab_normal_detail_trend_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_ab_normal_detail_trend_data_with_options(request, runtime)

    def get_event_ab_normal_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventAbNormalList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventAbNormalListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_ab_normal_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_ab_normal_list_with_options(request, runtime)

    def get_event_business_metric_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventBusinessMetricList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventBusinessMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_business_metric_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_business_metric_list_with_options(request, runtime)

    def get_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_detail_with_options(request, runtime)

    def get_event_root_cause_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_root_cause(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_root_cause_with_options(request, runtime)

    def get_event_sequential_trent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventSequentialTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventSequentialTrentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_sequential_trent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_sequential_trent_with_options(request, runtime)

    def get_event_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_statistics_with_options(request, runtime)

    def get_event_trent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity_type):
            query['GranularityType'] = request.granularity_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_type):
            query['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventTrentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_trent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_trent_with_options(request, runtime)

    def get_event_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEventType',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetEventTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_event_type_with_options(request, runtime)

    def get_exceptions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExceptions',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetExceptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_exceptions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_exceptions_with_options(request, runtime)

    def get_extend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExtend',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetExtendResponse(),
            self.call_api(params, req, runtime)
        )

    def get_extend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_extend_with_options(request, runtime)

    def get_forecast_business_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetForecastBusinessMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetForecastBusinessMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def get_forecast_business_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_forecast_business_metric_with_options(request, runtime)

    def get_function_valid_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.function_name):
            body['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFunctionValidInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetFunctionValidInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function_valid_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_function_valid_info_with_options(request, runtime)

    def get_group_by_dimension_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupByDimensionData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupByDimensionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_by_dimension_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_by_dimension_data_with_options(request, runtime)

    def get_group_resource_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupResourceNum',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupResourceNumResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_resource_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_resource_num_with_options(request, runtime)

    def get_group_topology_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroupTopologyTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetGroupTopologyTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group_topology_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_topology_tag_with_options(request, runtime)

    def get_incident_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIncidentAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIncidentAllResponse(),
            self.call_api(params, req, runtime)
        )

    def get_incident_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_incident_all_with_options(request, runtime)

    def get_index_dialysis_array_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisArray',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisArrayResponse(),
            self.call_api(params, req, runtime)
        )

    def get_index_dialysis_array(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_index_dialysis_array_with_options(request, runtime)

    def get_index_dialysis_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_index_dialysis_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_index_dialysis_list_with_options(request, runtime)

    def get_index_dialysis_list_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cloud_resource_id):
            query['CloudResourceId'] = request.cloud_resource_id
        if not UtilClient.is_unset(request.cloud_type_name):
            query['CloudTypeName'] = request.cloud_type_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.index_code):
            query['IndexCode'] = request.index_code
        if not UtilClient.is_unset(request.metric_extend):
            query['MetricExtend'] = request.metric_extend
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIndexDialysisListLine',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetIndexDialysisListLineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_index_dialysis_list_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_index_dialysis_list_line_with_options(request, runtime)

    def get_inspection_report_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.download_report_list_json):
            body['DownloadReportListJson'] = request.download_report_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInspectionReportDownloadUrl',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetInspectionReportDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_inspection_report_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_inspection_report_download_url_with_options(request, runtime)

    def get_instances_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstancesNum',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetInstancesNumResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instances_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instances_num_with_options(request, runtime)

    def get_log_sample_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_field):
            query['AppField'] = request.app_field
        if not UtilClient.is_unset(request.app_value):
            query['AppValue'] = request.app_value
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.log_field):
            query['LogField'] = request.log_field
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogSample',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetLogSampleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_log_sample(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_sample_with_options(request, runtime)

    def get_log_sample_column_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogSampleColumn',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetLogSampleColumnResponse(),
            self.call_api(params, req, runtime)
        )

    def get_log_sample_column(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_sample_column_with_options(request, runtime)

    def get_metric_event_sequential_trent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetricEventSequentialTrent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetMetricEventSequentialTrentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_metric_event_sequential_trent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_metric_event_sequential_trent_with_options(request, runtime)

    def get_new_optimization_item_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNewOptimizationItemData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetNewOptimizationItemDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_new_optimization_item_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_new_optimization_item_data_with_options(request, runtime)

    def get_patrol_inspection_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_patrol_inspection_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_detail_list_with_options(request, runtime)

    def get_patrol_inspection_detail_thrend_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.request_content):
            query['RequestContent'] = request.request_content
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionDetailThrendData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionDetailThrendDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_patrol_inspection_detail_thrend_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_detail_thrend_data_with_options(request, runtime)

    def get_patrol_inspection_items_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionItemsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionItemsListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_patrol_inspection_items_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_items_list_with_options(request, runtime)

    def get_patrol_inspection_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_patrol_inspection_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_list_with_options(request, runtime)

    def get_patrol_inspection_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPatrolInspectionStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetPatrolInspectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_patrol_inspection_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_patrol_inspection_status_with_options(request, runtime)

    def get_product_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductInstance',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetProductInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_product_instance_with_options(request, runtime)

    def get_product_metric_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetProductMetricList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetProductMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_metric_list(self):
        runtime = util_models.RuntimeOptions()
        return self.get_product_metric_list_with_options(runtime)

    def get_real_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.flow_name):
            query['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRealDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_real_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_real_data_with_options(request, runtime)

    def get_region_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRegionList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_region_list(self):
        runtime = util_models.RuntimeOptions()
        return self.get_region_list_with_options(runtime)

    def get_repair_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepairScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRepairScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repair_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_repair_script_with_options(request, runtime)

    def get_resource_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_list_with_options(request, runtime)

    def get_resource_tag_drop_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTagDropList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceTagDropListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_tag_drop_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_tag_drop_list_with_options(request, runtime)

    def get_resource_type_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceTypeList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetResourceTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_type_list(self):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_list_with_options(runtime)

    def get_risk_in_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.screen):
            query['Screen'] = request.screen
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInAll',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInAllResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_in_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_in_all_with_options(request, runtime)

    def get_risk_inspect_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInspectStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInspectStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_inspect_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_inspect_statistics_with_options(request, runtime)

    def get_risk_inspection_type_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskInspectionTypeList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskInspectionTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_inspection_type_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_inspection_type_list_with_options(request, runtime)

    def get_risk_patrol_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolDetailList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_patrol_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_detail_list_with_options(request, runtime)

    def get_risk_patrol_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.patrol_id):
            query['PatrolId'] = request.patrol_id
        if not UtilClient.is_unset(request.risk_patrol_item):
            query['RiskPatrolItem'] = request.risk_patrol_item
        if not UtilClient.is_unset(request.severity_level):
            query['SeverityLevel'] = request.severity_level
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_patrol_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_list_with_options(request, runtime)

    def get_risk_patrol_statistical_trends_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatisticalTrends',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatisticalTrendsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_patrol_statistical_trends(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_statistical_trends_with_options(request, runtime)

    def get_risk_patrol_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatistics',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_patrol_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_statistics_with_options(request, runtime)

    def get_risk_patrol_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRiskPatrolStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRiskPatrolStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_risk_patrol_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_risk_patrol_status_with_options(request, runtime)

    def get_role_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRole',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_role(self):
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(runtime)

    def get_root_cause_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_root_cause(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_root_cause_with_options(request, runtime)

    def get_scenario_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioDetail',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scenario_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_detail_with_options(request, runtime)

    def get_scenario_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scenario_name):
            query['ScenarioName'] = request.scenario_name
        if not UtilClient.is_unset(request.scene_select_label):
            query['SceneSelectLabel'] = request.scene_select_label
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scenario_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_list_with_options(request, runtime)

    def get_scenario_statistics_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scenario_ids):
            query['ScenarioIds'] = request.scenario_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScenarioStatisticsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScenarioStatisticsListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scenario_statistics_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scenario_statistics_list_with_options(request, runtime)

    def get_scene_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneById',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_by_id_with_options(request, runtime)

    def get_scene_details_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneDetailsList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneDetailsListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_details_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_details_list_with_options(request, runtime)

    def get_scene_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_total):
            query['PageTotal'] = request.page_total
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_list_with_options(request, runtime)

    def get_scene_metric_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneMetricTable',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSceneMetricTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_metric_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_metric_table_with_options(request, runtime)

    def get_script_event_root_cause_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScriptEventRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetScriptEventRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_script_event_root_cause(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_script_event_root_cause_with_options(request, runtime)

    def get_sls_log_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSlsLogData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSlsLogDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sls_log_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sls_log_data_with_options(request, runtime)

    def get_syn_cloud_resource_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSynCloudResourceList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetSynCloudResourceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_syn_cloud_resource_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_syn_cloud_resource_list_with_options(request, runtime)

    def get_tag_business_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagBusinessGroupList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTagBusinessGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tag_business_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_tag_business_group_list_with_options(request, runtime)

    def get_tag_drop_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTagDropList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTagDropListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tag_drop_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_tag_drop_list_with_options(request, runtime)

    def get_target_dimension_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.flag):
            query['Flag'] = request.flag
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTargetDimensionData',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTargetDimensionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_target_dimension_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_target_dimension_data_with_options(request, runtime)

    def get_threshold_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThresholdList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetThresholdListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_threshold_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_threshold_list_with_options(request, runtime)

    def get_through_put_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThroughPut',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetThroughPutResponse(),
            self.call_api(params, req, runtime)
        )

    def get_through_put(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_through_put_with_options(request, runtime)

    def get_trend_sls_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrendSlsReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetTrendSlsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trend_sls_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trend_sls_reports_with_options(request, runtime)

    def get_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    def get_user_login_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_principal_name):
            query['AccountPrincipalName'] = request.account_principal_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.current_pk):
            query['CurrentPk'] = request.current_pk
        if not UtilClient.is_unset(request.main_account_pk):
            query['MainAccountPk'] = request.main_account_pk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserLoginInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserLoginInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_login_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_login_info_with_options(request, runtime)

    def get_user_order_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserOrderConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.GetUserOrderConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_order_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_order_config_with_options(request, runtime)

    def ignore_alarms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IgnoreAlarms',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.IgnoreAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    def ignore_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ignore_alarms_with_options(request, runtime)

    def list_apply_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplyAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListApplyAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apply_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apply_authorization_with_options(request, runtime)

    def list_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuth',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def list_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_auth_with_options(request, runtime)

    def list_authorized_uid_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAuthorizedUid',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListAuthorizedUidResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authorized_uid(self):
        runtime = util_models.RuntimeOptions()
        return self.list_authorized_uid_with_options(runtime)

    def list_cause_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCausePlan',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListCausePlanResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cause_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cause_plan_with_options(request, runtime)

    def list_confirm_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfirmAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListConfirmAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_confirm_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_confirm_authorization_with_options(request, runtime)

    def list_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvent',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListEventResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_with_options(request, runtime)

    def list_not_authorized_uid_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListNotAuthorizedUid',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListNotAuthorizedUidResponse(),
            self.call_api(params, req, runtime)
        )

    def list_not_authorized_uid(self):
        runtime = util_models.RuntimeOptions()
        return self.list_not_authorized_uid_with_options(runtime)

    def list_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_reports_with_options(request, runtime)

    def list_root_cause_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.root_cause_id):
            query['RootCauseId'] = request.root_cause_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRootCause',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListRootCauseResponse(),
            self.call_api(params, req, runtime)
        )

    def list_root_cause(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_root_cause_with_options(request, runtime)

    def list_sls_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlsReports',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ListSlsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sls_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_sls_reports_with_options(request, runtime)

    def put_alert_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.webhook):
            body['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContact',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_contact_with_options(request, runtime)

    def put_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.alert_contact_group_json):
            body['AlertContactGroupJson'] = request.alert_contact_group_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContactGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_contact_group_with_options(request, runtime)

    def put_alert_contact_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        body = {}
        if not UtilClient.is_unset(request.contact_id_list_json):
            body['ContactIdListJson'] = request.contact_id_list_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id_list_json):
            body['GroupIdListJson'] = request.group_id_list_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertContactToGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertContactToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_contact_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_contact_to_group_with_options(request, runtime)

    def put_alert_ignore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAlertIgnore',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertIgnoreResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_ignore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_ignore_with_options(request, runtime)

    def put_alert_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_silence_config):
            query['AlertSilenceConfig'] = request.alert_silence_config
        body = {}
        if not UtilClient.is_unset(request.alarm_level):
            body['AlarmLevel'] = request.alarm_level
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.business_group_ids_json):
            body['BusinessGroupIdsJson'] = request.business_group_ids_json
        if not UtilClient.is_unset(request.contact_group_ids_json):
            body['ContactGroupIdsJson'] = request.contact_group_ids_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        if not UtilClient.is_unset(request.customer_uid):
            body['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.send_dingtalk_notice):
            body['SendDingtalkNotice'] = request.send_dingtalk_notice
        if not UtilClient.is_unset(request.send_email_notice):
            body['SendEmailNotice'] = request.send_email_notice
        if not UtilClient.is_unset(request.send_sms_notice):
            body['SendSmsNotice'] = request.send_sms_notice
        if not UtilClient.is_unset(request.stop_duration):
            body['StopDuration'] = request.stop_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSetting',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_setting_with_options(request, runtime)

    def put_alert_setting_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_edit_request_list_json):
            body['AlertSettingEditRequestListJson'] = request.alert_setting_edit_request_list_json
        if not UtilClient.is_unset(request.contact_group_ids_json):
            body['ContactGroupIdsJson'] = request.contact_group_ids_json
        if not UtilClient.is_unset(request.contact_ids_json):
            body['ContactIdsJson'] = request.contact_ids_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSettingList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingListResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_setting_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_setting_list_with_options(request, runtime)

    def put_alert_setting_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            body['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.setting_status):
            body['SettingStatus'] = request.setting_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAlertSettingStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutAlertSettingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def put_alert_setting_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_alert_setting_status_with_options(request, runtime)

    def put_data_source_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_describe):
            query['DataSourceDescribe'] = request.data_source_describe
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_params_mapping):
            query['DataSourceParamsMapping'] = request.data_source_params_mapping
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def put_data_source_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_data_source_config_with_options(request, runtime)

    def put_group_resource_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupResourceTag',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutGroupResourceTagResponse(),
            self.call_api(params, req, runtime)
        )

    def put_group_resource_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_group_resource_tag_with_options(request, runtime)

    def put_group_topology_tag_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutGroupTopologyTagLog',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutGroupTopologyTagLogResponse(),
            self.call_api(params, req, runtime)
        )

    def put_group_topology_tag_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_group_topology_tag_log_with_options(request, runtime)

    def put_report_email_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutReportEmailConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutReportEmailConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def put_report_email_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_report_email_config_with_options(request, runtime)

    def put_resource_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutResourceWhitelist',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.PutResourceWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def put_resource_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_resource_whitelist_with_options(request, runtime)

    def replace_script_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceScriptList',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.ReplaceScriptListResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_script_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_script_list_with_options(request, runtime)

    def revoke_submit_apply_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSubmitApplyPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RevokeSubmitApplyPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_submit_apply_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_submit_apply_permission_with_options(request, runtime)

    def run_analysis_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunAnalysisProcess',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunAnalysisProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def run_analysis_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_analysis_process_with_options(request, runtime)

    def run_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def run_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    def run_forecast_analyze_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunForecastAnalyze',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunForecastAnalyzeResponse(),
            self.call_api(params, req, runtime)
        )

    def run_forecast_analyze(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_forecast_analyze_with_options(request, runtime)

    def run_patrol_inspection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunPatrolInspection',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunPatrolInspectionResponse(),
            self.call_api(params, req, runtime)
        )

    def run_patrol_inspection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_patrol_inspection_with_options(request, runtime)

    def run_repair_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunRepairScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunRepairScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def run_repair_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_repair_script_with_options(request, runtime)

    def run_risk_patrol_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunRiskPatrol',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.RunRiskPatrolResponse(),
            self.call_api(params, req, runtime)
        )

    def run_risk_patrol(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_risk_patrol_with_options(request, runtime)

    def switch_user_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchUserTop',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.SwitchUserTopResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_user_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_user_top_with_options(request, runtime)

    def upd_business_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.UpdBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def upd_business_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upd_business_group_with_options(request, runtime)

    def update_authorization_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthorization',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_authorization(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_with_options(request, runtime)

    def update_bind_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_id):
            query['MetricId'] = request.metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBindMetric',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBindMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def update_bind_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_bind_metric_with_options(request, runtime)

    def update_business_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = aiops_20200806_models.UpdateBusinessGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_group_desc):
            query['BusinessGroupDesc'] = request.business_group_desc
        if not UtilClient.is_unset(request.business_group_id):
            query['BusinessGroupId'] = request.business_group_id
        if not UtilClient.is_unset(request.business_group_name):
            query['BusinessGroupName'] = request.business_group_name
        if not UtilClient.is_unset(request.cloud_resource_type_id):
            query['CloudResourceTypeId'] = request.cloud_resource_type_id
        if not UtilClient.is_unset(request.deal_type):
            query['DealType'] = request.deal_type
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.update_user):
            query['UpdateUser'] = request.update_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessGroup',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_business_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_business_group_with_options(request, runtime)

    def update_business_metric_alert_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessMetricAlertConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessMetricAlertConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_business_metric_alert_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_business_metric_alert_config_with_options(request, runtime)

    def update_business_metric_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_metric_id):
            query['BusinessMetricId'] = request.business_metric_id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBusinessMetricResource',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateBusinessMetricResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_business_metric_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_business_metric_resource_with_options(request, runtime)

    def update_data_source_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_describe):
            query['DataSourceDescribe'] = request.data_source_describe
        if not UtilClient.is_unset(request.data_source_name):
            query['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_params):
            query['DataSourceParams'] = request.data_source_params
        if not UtilClient.is_unset(request.data_source_params_mapping):
            query['DataSourceParamsMapping'] = request.data_source_params_mapping
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceConfig',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_source_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_config_with_options(request, runtime)

    def update_handle_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHandleRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateHandleRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_handle_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_handle_risk_with_options(request, runtime)

    def update_handle_risk_base_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHandleRiskBase',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateHandleRiskBaseResponse(),
            self.call_api(params, req, runtime)
        )

    def update_handle_risk_base(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_handle_risk_base_with_options(request, runtime)

    def update_ignore_risk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIgnoreRisk',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateIgnoreRiskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ignore_risk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ignore_risk_with_options(request, runtime)

    def update_ignore_risk_base_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIgnoreRiskBase',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateIgnoreRiskBaseResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ignore_risk_base(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_ignore_risk_base_with_options(request, runtime)

    def update_inspection_setting_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.risk_enable_status):
            body['RiskEnableStatus'] = request.risk_enable_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInspectionSettingStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateInspectionSettingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_inspection_setting_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_inspection_setting_status_with_options(request, runtime)

    def update_inspection_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.risk_code):
            body['RiskCode'] = request.risk_code
        if not UtilClient.is_unset(request.threshold_item_list_json):
            body['ThresholdItemListJson'] = request.threshold_item_list_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInspectionThreshold',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateInspectionThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def update_inspection_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_inspection_threshold_with_options(request, runtime)

    def update_operation_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not UtilClient.is_unset(request.switch_front_opera_uid):
            query['SwitchFrontOperaUid'] = request.switch_front_opera_uid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOperationPermission',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateOperationPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_operation_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_operation_permission_with_options(request, runtime)

    def update_report_email_config_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_status):
            body['ConfigStatus'] = request.config_status
        if not UtilClient.is_unset(request.mail_config_id):
            body['MailConfigId'] = request.mail_config_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportEmailConfigStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateReportEmailConfigStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_report_email_config_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_report_email_config_status_with_options(request, runtime)

    def update_report_subscription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.day_of_week):
            body['DayOfWeek'] = request.day_of_week
        if not UtilClient.is_unset(request.hour_of_day):
            body['HourOfDay'] = request.hour_of_day
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.report_name):
            body['ReportName'] = request.report_name
        if not UtilClient.is_unset(request.subscribe):
            body['Subscribe'] = request.subscribe
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateReportSubscription',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateReportSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_report_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_report_subscription_with_options(request, runtime)

    def update_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_setting_id):
            query['AlertSettingId'] = request.alert_setting_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScenario',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scenario_with_options(request, runtime)

    def update_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.flow_name):
            body['FlowName'] = request.flow_name
        if not UtilClient.is_unset(request.metric_list_json):
            body['MetricListJson'] = request.metric_list_json
        if not UtilClient.is_unset(request.node_list_json):
            body['NodeListJson'] = request.node_list_json
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_desc):
            body['SceneDesc'] = request.scene_desc
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_name):
            body['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.scene_owner):
            body['SceneOwner'] = request.scene_owner
        if not UtilClient.is_unset(request.scene_webhook):
            body['SceneWebhook'] = request.scene_webhook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_with_options(request, runtime)

    def update_scene_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fc_function_name):
            body['FcFunctionName'] = request.fc_function_name
        if not UtilClient.is_unset(request.fc_handler):
            body['FcHandler'] = request.fc_handler
        if not UtilClient.is_unset(request.fc_initializer):
            body['FcInitializer'] = request.fc_initializer
        if not UtilClient.is_unset(request.fc_region_no):
            body['FcRegionNo'] = request.fc_region_no
        if not UtilClient.is_unset(request.fc_service_name):
            body['FcServiceName'] = request.fc_service_name
        if not UtilClient.is_unset(request.model_desc):
            body['ModelDesc'] = request.model_desc
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_language):
            body['ModelLanguage'] = request.model_language
        if not UtilClient.is_unset(request.model_memo):
            body['ModelMemo'] = request.model_memo
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_type):
            body['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.root_cause_desc):
            body['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_cause_solution):
            body['RootCauseSolution'] = request.root_cause_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModel',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_model_with_options(request, runtime)

    def update_scene_model_apply_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_content):
            body['ApplyContent'] = request.apply_content
        if not UtilClient.is_unset(request.apply_id):
            body['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.apply_status):
            body['ApplyStatus'] = request.apply_status
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModelApply',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelApplyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene_model_apply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_model_apply_with_options(request, runtime)

    def update_scene_model_cur_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_id):
            body['ExtId'] = request.ext_id
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneModelCurVersion',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneModelCurVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene_model_cur_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_model_cur_version_with_options(request, runtime)

    def update_scene_system_model_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_status):
            body['ModelStatus'] = request.model_status
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSceneSystemModelStatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateSceneSystemModelStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene_system_model_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_system_model_status_with_options(request, runtime)

    def update_scenestatus_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScenestatus',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScenestatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scenestatus(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scenestatus_with_options(request, runtime)

    def update_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handle_suggest_desc):
            query['HandleSuggestDesc'] = request.handle_suggest_desc
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.opera_uid):
            query['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.root_cause_desc):
            query['RootCauseDesc'] = request.root_cause_desc
        if not UtilClient.is_unset(request.root_causes_log):
            query['RootCausesLog'] = request.root_causes_log
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.script_language):
            query['ScriptLanguage'] = request.script_language
        if not UtilClient.is_unset(request.script_name):
            query['ScriptName'] = request.script_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScript',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def update_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_script_with_options(request, runtime)

    def update_status_of_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.opera_uid):
            body['OperaUid'] = request.opera_uid
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.scene_status):
            body['SceneStatus'] = request.scene_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStatusOfScene',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateStatusOfSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_status_of_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_status_of_scene_with_options(request, runtime)

    def update_tag_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTagInfo',
            version='2020-08-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiops_20200806_models.UpdateTagInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_tag_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_tag_info_with_options(request, runtime)
