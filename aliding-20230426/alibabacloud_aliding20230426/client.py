# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aliding20230426 import models as aliding_20230426_models
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
        self._endpoint = self.get_endpoint('aliding', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_attendee_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddAttendeeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddAttendeeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees_to_add):
            request.attendees_to_add_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees_to_add, 'AttendeesToAdd', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_to_add_shrink):
            body['AttendeesToAdd'] = request.attendees_to_add_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.chat_notification):
            body['chatNotification'] = request.chat_notification
        if not UtilClient.is_unset(request.push_notification):
            body['pushNotification'] = request.push_notification
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAttendee',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/addAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddAttendeeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_attendee(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddAttendeeHeaders()
        return self.add_attendee_with_options(request, headers, runtime)

    def add_meeting_rooms_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddMeetingRoomsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddMeetingRoomsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.meeting_rooms_to_add):
            request.meeting_rooms_to_add_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.meeting_rooms_to_add, 'MeetingRoomsToAdd', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.meeting_rooms_to_add_shrink):
            body['MeetingRoomsToAdd'] = request.meeting_rooms_to_add_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMeetingRooms',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/addMeetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddMeetingRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_meeting_rooms(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddMeetingRoomsHeaders()
        return self.add_meeting_rooms_with_options(request, headers, runtime)

    def add_scenegroup_member_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.AddScenegroupMemberShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['OpenConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddScenegroupMember',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/im/addScenegroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddScenegroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_scenegroup_member(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddScenegroupMemberHeaders()
        return self.add_scenegroup_member_with_options(request, headers, runtime)

    def add_workspace_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/addWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceHeaders()
        return self.add_workspace_with_options(request, headers, runtime)

    def add_workspace_doc_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/addWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceDocMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_workspace_doc_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceDocMembersHeaders()
        return self.add_workspace_doc_members_with_options(request, headers, runtime)

    def add_workspace_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.AddWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.AddWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/addWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.AddWorkspaceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_workspace_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.AddWorkspaceMembersHeaders()
        return self.add_workspace_members_with_options(request, headers, runtime)

    def batch_get_form_data_by_id_list_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.BatchGetFormDataByIdListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.BatchGetFormDataByIdListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.form_instance_id_list):
            request.form_instance_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.form_instance_id_list, 'FormInstanceIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_instance_id_list_shrink):
            body['FormInstanceIdList'] = request.form_instance_id_list_shrink
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.need_form_instance_value):
            body['NeedFormInstanceValue'] = request.need_form_instance_value
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetFormDataByIdList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/batchGetFormDataByIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.BatchGetFormDataByIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_form_data_by_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.BatchGetFormDataByIdListHeaders()
        return self.batch_get_form_data_by_id_list_with_options(request, headers, runtime)

    def batch_removal_by_form_instance_id_list_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.BatchRemovalByFormInstanceIdListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.BatchRemovalByFormInstanceIdListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.form_instance_id_list):
            request.form_instance_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.form_instance_id_list, 'FormInstanceIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous_execution):
            body['AsynchronousExecution'] = request.asynchronous_execution
        if not UtilClient.is_unset(request.execute_expression):
            body['ExecuteExpression'] = request.execute_expression
        if not UtilClient.is_unset(request.form_instance_id_list_shrink):
            body['FormInstanceIdList'] = request.form_instance_id_list_shrink
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchRemovalByFormInstanceIdList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/batchRemovalByFormInstanceIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.BatchRemovalByFormInstanceIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_removal_by_form_instance_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.BatchRemovalByFormInstanceIdListHeaders()
        return self.batch_removal_by_form_instance_id_list_with_options(request, headers, runtime)

    def batch_save_form_data_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.BatchSaveFormDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.BatchSaveFormDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.form_data_json_list):
            request.form_data_json_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.form_data_json_list, 'FormDataJsonList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous_execution):
            body['AsynchronousExecution'] = request.asynchronous_execution
        if not UtilClient.is_unset(request.form_data_json_list_shrink):
            body['FormDataJsonList'] = request.form_data_json_list_shrink
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.keep_running_after_exception):
            body['KeepRunningAfterException'] = request.keep_running_after_exception
        if not UtilClient.is_unset(request.no_execute_expression):
            body['NoExecuteExpression'] = request.no_execute_expression
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSaveFormData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/batchSaveFormData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.BatchSaveFormDataResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_save_form_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.BatchSaveFormDataHeaders()
        return self.batch_save_form_data_with_options(request, headers, runtime)

    def batch_update_form_data_by_instance_id_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.BatchUpdateFormDataByInstanceIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.BatchUpdateFormDataByInstanceIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.form_instance_id_list):
            request.form_instance_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.form_instance_id_list, 'FormInstanceIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous_execution):
            body['AsynchronousExecution'] = request.asynchronous_execution
        if not UtilClient.is_unset(request.form_instance_id_list_shrink):
            body['FormInstanceIdList'] = request.form_instance_id_list_shrink
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.ignore_empty):
            body['IgnoreEmpty'] = request.ignore_empty
        if not UtilClient.is_unset(request.no_execute_expression):
            body['NoExecuteExpression'] = request.no_execute_expression
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.update_form_data_json):
            body['UpdateFormDataJson'] = request.update_form_data_json
        if not UtilClient.is_unset(request.use_latest_form_schema_version):
            body['UseLatestFormSchemaVersion'] = request.use_latest_form_schema_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateFormDataByInstanceId',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/batchUpdateFormDataByInstanceId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.BatchUpdateFormDataByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_form_data_by_instance_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.BatchUpdateFormDataByInstanceIdHeaders()
        return self.batch_update_form_data_by_instance_id_with_options(request, headers, runtime)

    def batch_update_form_data_by_instance_map_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.BatchUpdateFormDataByInstanceMapShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.BatchUpdateFormDataByInstanceMapShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.update_form_data_json_map):
            request.update_form_data_json_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_form_data_json_map, 'UpdateFormDataJsonMap', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.asynchronous_execution):
            body['AsynchronousExecution'] = request.asynchronous_execution
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.ignore_empty):
            body['IgnoreEmpty'] = request.ignore_empty
        if not UtilClient.is_unset(request.no_execute_expression):
            body['NoExecuteExpression'] = request.no_execute_expression
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.update_form_data_json_map_shrink):
            body['UpdateFormDataJsonMap'] = request.update_form_data_json_map_shrink
        if not UtilClient.is_unset(request.use_latest_form_schema_version):
            body['UseLatestFormSchemaVersion'] = request.use_latest_form_schema_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateFormDataByInstanceMap',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/batchUpdateFormDataByInstanceMap',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.BatchUpdateFormDataByInstanceMapResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_form_data_by_instance_map(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.BatchUpdateFormDataByInstanceMapHeaders()
        return self.batch_update_form_data_by_instance_map_with_options(request, headers, runtime)

    def cancel_schedule_conference_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CancelScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CancelScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.schedule_conference_id):
            body['ScheduleConferenceId'] = request.schedule_conference_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/cancelScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CancelScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_schedule_conference(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CancelScheduleConferenceHeaders()
        return self.cancel_schedule_conference_with_options(request, headers, runtime)

    def clear_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ClearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ClearShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Clear',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ClearResponse(),
            self.call_api(params, req, runtime)
        )

    def clear(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ClearHeaders()
        return self.clear_with_options(request, headers, runtime)

    def clear_data_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ClearDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ClearDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClearData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/clearData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ClearDataResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ClearDataHeaders()
        return self.clear_data_with_options(request, headers, runtime)

    def comment_list_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CommentListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CommentListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommentListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/commentListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CommentListReportResponse(),
            self.call_api(params, req, runtime)
        )

    def comment_list_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CommentListReportHeaders()
        return self.comment_list_report_with_options(request, headers, runtime)

    def create_delivery_plan_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateDeliveryPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateDeliveryPlanShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.user_id_list):
            request.user_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_id_list, 'UserIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.content_shrink):
            body['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.res_id):
            body['ResId'] = request.res_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.user_id_list_shrink):
            body['UserIdList'] = request.user_id_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeliveryPlan',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/watt/createDeliveryPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateDeliveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_delivery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateDeliveryPlanHeaders()
        return self.create_delivery_plan_with_options(request, headers, runtime)

    def create_event_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateEventShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees):
            request.attendees_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees, 'Attendees', 'json')
        if not UtilClient.is_unset(tmp_req.end):
            request.end_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end, 'End', 'json')
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.online_meeting_info):
            request.online_meeting_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.online_meeting_info, 'OnlineMeetingInfo', 'json')
        if not UtilClient.is_unset(tmp_req.recurrence):
            request.recurrence_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recurrence, 'Recurrence', 'json')
        if not UtilClient.is_unset(tmp_req.reminders):
            request.reminders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reminders, 'Reminders', 'json')
        if not UtilClient.is_unset(tmp_req.ui_configs):
            request.ui_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ui_configs, 'UiConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.start):
            request.start_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start, 'start', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_shrink):
            body['Attendees'] = request.attendees_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_shrink):
            body['End'] = request.end_shrink
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_all_day):
            body['IsAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.online_meeting_info_shrink):
            body['OnlineMeetingInfo'] = request.online_meeting_info_shrink
        if not UtilClient.is_unset(request.recurrence_shrink):
            body['Recurrence'] = request.recurrence_shrink
        if not UtilClient.is_unset(request.reminders_shrink):
            body['Reminders'] = request.reminders_shrink
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        if not UtilClient.is_unset(request.ui_configs_shrink):
            body['UiConfigs'] = request.ui_configs_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['calendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.start_shrink):
            body['start'] = request.start_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/createEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateEventResponse(),
            self.call_api(params, req, runtime)
        )

    def create_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateEventHeaders()
        return self.create_event_with_options(request, headers, runtime)

    def create_live_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.pre_end_time):
            body['PreEndTime'] = request.pre_end_time
        if not UtilClient.is_unset(request.pre_start_time):
            body['PreStartTime'] = request.pre_start_time
        if not UtilClient.is_unset(request.public_type):
            body['PublicType'] = request.public_type
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/createLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateLiveHeaders()
        return self.create_live_with_options(request, headers, runtime)

    def create_meeting_room_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.reservation_authority):
            request.reservation_authority_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reservation_authority, 'ReservationAuthority', 'json')
        if not UtilClient.is_unset(tmp_req.room_label_ids):
            request.room_label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_label_ids, 'RoomLabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.room_location):
            request.room_location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_location, 'RoomLocation', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_cycle_reservation):
            body['EnableCycleReservation'] = request.enable_cycle_reservation
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.isv_room_id):
            body['IsvRoomId'] = request.isv_room_id
        if not UtilClient.is_unset(request.reservation_authority_shrink):
            body['ReservationAuthority'] = request.reservation_authority_shrink
        if not UtilClient.is_unset(request.room_capacity):
            body['RoomCapacity'] = request.room_capacity
        if not UtilClient.is_unset(request.room_label_ids_shrink):
            body['RoomLabelIds'] = request.room_label_ids_shrink
        if not UtilClient.is_unset(request.room_location_shrink):
            body['RoomLocation'] = request.room_location_shrink
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_picture):
            body['RoomPicture'] = request.room_picture
        if not UtilClient.is_unset(request.room_status):
            body['RoomStatus'] = request.room_status
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/createMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def create_meeting_room(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateMeetingRoomHeaders()
        return self.create_meeting_room_with_options(request, headers, runtime)

    def create_meeting_room_group_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['ParentGroupId'] = request.parent_group_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/createMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_meeting_room_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateMeetingRoomGroupHeaders()
        return self.create_meeting_room_group_with_options(request, headers, runtime)

    def create_or_update_form_data_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.CreateOrUpdateFormDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_data_json):
            body['FormDataJson'] = request.form_data_json
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.no_execute_expression):
            body['NoExecuteExpression'] = request.no_execute_expression
        if not UtilClient.is_unset(request.search_condition):
            body['SearchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateFormData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/createOrUpdateFormData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateOrUpdateFormDataResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_form_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateOrUpdateFormDataHeaders()
        return self.create_or_update_form_data_with_options(request, headers, runtime)

    def create_org_honor_template_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateOrgHonorTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateOrgHonorTemplateShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.avatar_frame_media_id):
            body['avatarFrameMediaId'] = request.avatar_frame_media_id
        if not UtilClient.is_unset(request.default_bg_color):
            body['defaultBgColor'] = request.default_bg_color
        if not UtilClient.is_unset(request.medal_desc):
            body['medalDesc'] = request.medal_desc
        if not UtilClient.is_unset(request.medal_media_id):
            body['medalMediaId'] = request.medal_media_id
        if not UtilClient.is_unset(request.medal_name):
            body['medalName'] = request.medal_name
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrgHonorTemplate',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/honor/createOrgHonorTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateOrgHonorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_org_honor_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateOrgHonorTemplateHeaders()
        return self.create_org_honor_template_with_options(request, headers, runtime)

    def create_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.to_cids):
            request.to_cids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_cids, 'ToCids', 'json')
        if not UtilClient.is_unset(tmp_req.to_userids):
            request.to_userids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.to_userids, 'ToUserids', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.dd_from):
            body['DdFrom'] = request.dd_from
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.to_chat):
            body['ToChat'] = request.to_chat
        if not UtilClient.is_unset(request.to_cids_shrink):
            body['ToCids'] = request.to_cids_shrink
        if not UtilClient.is_unset(request.to_userids_shrink):
            body['ToUserids'] = request.to_userids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/createReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateReportHeaders()
        return self.create_report_with_options(request, headers, runtime)

    def create_scenegroup_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.CreateScenegroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.add_friend_forbidden):
            body['AddFriendForbidden'] = request.add_friend_forbidden
        if not UtilClient.is_unset(request.all_members_can_create_calendar):
            body['AllMembersCanCreateCalendar'] = request.all_members_can_create_calendar
        if not UtilClient.is_unset(request.all_members_can_create_mcs_conf):
            body['AllMembersCanCreateMcsConf'] = request.all_members_can_create_mcs_conf
        if not UtilClient.is_unset(request.chat_banned_type):
            body['ChatBannedType'] = request.chat_banned_type
        if not UtilClient.is_unset(request.group_email_disabled):
            body['GroupEmailDisabled'] = request.group_email_disabled
        if not UtilClient.is_unset(request.group_live_switch):
            body['GroupLiveSwitch'] = request.group_live_switch
        if not UtilClient.is_unset(request.icon):
            body['Icon'] = request.icon
        if not UtilClient.is_unset(request.management_type):
            body['ManagementType'] = request.management_type
        if not UtilClient.is_unset(request.members_to_admin_chat):
            body['MembersToAdminChat'] = request.members_to_admin_chat
        if not UtilClient.is_unset(request.mention_all_authority):
            body['MentionAllAuthority'] = request.mention_all_authority
        if not UtilClient.is_unset(request.only_admin_can_ding):
            body['OnlyAdminCanDing'] = request.only_admin_can_ding
        if not UtilClient.is_unset(request.only_admin_can_set_msg_top):
            body['OnlyAdminCanSetMsgTop'] = request.only_admin_can_set_msg_top
        if not UtilClient.is_unset(request.searchable):
            body['Searchable'] = request.searchable
        if not UtilClient.is_unset(request.show_history_type):
            body['ShowHistoryType'] = request.show_history_type
        if not UtilClient.is_unset(request.subadmin_ids):
            body['SubadminIds'] = request.subadmin_ids
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.validation_type):
            body['ValidationType'] = request.validation_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScenegroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/im/createScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateScenegroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scenegroup(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateScenegroupHeaders()
        return self.create_scenegroup_with_options(request, headers, runtime)

    def create_schedule_conference_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/createScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_schedule_conference(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateScheduleConferenceHeaders()
        return self.create_schedule_conference_with_options(request, headers, runtime)

    def create_sheet_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateSheetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sheet(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateSheetHeaders()
        return self.create_sheet_with_options(request, headers, runtime)

    def create_subscribed_calendar_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateSubscribedCalendarShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateSubscribedCalendarShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.managers):
            request.managers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.managers, 'Managers', 'json')
        if not UtilClient.is_unset(tmp_req.subscribe_scope):
            request.subscribe_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subscribe_scope, 'SubscribeScope', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.managers_shrink):
            body['Managers'] = request.managers_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.subscribe_scope_shrink):
            body['SubscribeScope'] = request.subscribe_scope_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscribedCalendar',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/createSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateSubscribedCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subscribed_calendar(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateSubscribedCalendarHeaders()
        return self.create_subscribed_calendar_with_options(request, headers, runtime)

    def create_todo_task_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.content_field_list):
            request.content_field_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content_field_list, 'contentFieldList', 'json')
        if not UtilClient.is_unset(tmp_req.detail_url):
            request.detail_url_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detail_url, 'detailUrl', 'json')
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'executorIds', 'json')
        if not UtilClient.is_unset(tmp_req.notify_configs):
            request.notify_configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_configs, 'notifyConfigs', 'json')
        if not UtilClient.is_unset(tmp_req.participant_ids):
            request.participant_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.participant_ids, 'participantIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.operator_id):
            query['operatorId'] = request.operator_id
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.content_field_list_shrink):
            body['contentFieldList'] = request.content_field_list_shrink
        if not UtilClient.is_unset(request.creator_id):
            body['creatorId'] = request.creator_id
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.detail_url_shrink):
            body['detailUrl'] = request.detail_url_shrink
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.executor_ids_shrink):
            body['executorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.is_only_show_executor):
            body['isOnlyShowExecutor'] = request.is_only_show_executor
        if not UtilClient.is_unset(request.notify_configs_shrink):
            body['notifyConfigs'] = request.notify_configs_shrink
        if not UtilClient.is_unset(request.participant_ids_shrink):
            body['participantIds'] = request.participant_ids_shrink
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/task/createTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_todo_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateTodoTaskHeaders()
        return self.create_todo_task_with_options(request, headers, runtime)

    def create_video_conference_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateVideoConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateVideoConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.invite_user_ids):
            request.invite_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invite_user_ids, 'InviteUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.conf_title):
            body['ConfTitle'] = request.conf_title
        if not UtilClient.is_unset(request.invite_caller):
            body['InviteCaller'] = request.invite_caller
        if not UtilClient.is_unset(request.invite_user_ids_shrink):
            body['InviteUserIds'] = request.invite_user_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/createVideoConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateVideoConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_video_conference(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateVideoConferenceHeaders()
        return self.create_video_conference_with_options(request, headers, runtime)

    def create_workspace_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/createWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateWorkspaceHeaders()
        return self.create_workspace_with_options(request, headers, runtime)

    def create_workspace_doc_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateWorkspaceDocShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateWorkspaceDocShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_node_id):
            body['ParentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspaceDoc',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/createWorkspaceDoc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateWorkspaceDocResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workspace_doc(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateWorkspaceDocHeaders()
        return self.create_workspace_doc_with_options(request, headers, runtime)

    def delete_columns_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteColumnsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteColumnsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteColumns',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/deleteColumns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_columns(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteColumnsHeaders()
        return self.delete_columns_with_options(request, headers, runtime)

    def delete_event_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.push_notification):
            body['pushNotification'] = request.push_notification
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/deleteEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteEventResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteEventHeaders()
        return self.delete_event_with_options(request, headers, runtime)

    def delete_form_data_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteFormDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_instance_id):
            body['FormInstanceId'] = request.form_instance_id
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFormData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/deleteFormData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteFormDataResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_form_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteFormDataHeaders()
        return self.delete_form_data_with_options(request, headers, runtime)

    def delete_instance_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteInstanceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/deleteInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteInstanceHeaders()
        return self.delete_instance_with_options(request, headers, runtime)

    def delete_live_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/deleteLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteLiveHeaders()
        return self.delete_live_with_options(request, headers, runtime)

    def delete_meeting_room_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/deleteMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_meeting_room(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteMeetingRoomHeaders()
        return self.delete_meeting_room_with_options(request, headers, runtime)

    def delete_meeting_room_group_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/deleteMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_meeting_room_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteMeetingRoomGroupHeaders()
        return self.delete_meeting_room_group_with_options(request, headers, runtime)

    def delete_rows_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteRowsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteRowsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRows',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/deleteRows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteRowsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rows(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteRowsHeaders()
        return self.delete_rows_with_options(request, headers, runtime)

    def delete_scenegroup_member_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteScenegroupMemberShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.open_conversation_id):
            body['OpenConversationId'] = request.open_conversation_id
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteScenegroupMember',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/im/deleteScenegroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteScenegroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scenegroup_member(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteScenegroupMemberHeaders()
        return self.delete_scenegroup_member_with_options(request, headers, runtime)

    def delete_sheet_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/deleteSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteSheetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sheet(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteSheetHeaders()
        return self.delete_sheet_with_options(request, headers, runtime)

    def delete_subscribed_calendar_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.DeleteSubscribedCalendarShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubscribedCalendar',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/deleteSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteSubscribedCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subscribed_calendar(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteSubscribedCalendarHeaders()
        return self.delete_subscribed_calendar_with_options(request, headers, runtime)

    def delete_todo_task_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/task/deleteTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_todo_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteTodoTaskHeaders()
        return self.delete_todo_task_with_options(request, headers, runtime)

    def delete_workspace_doc_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/deleteWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteWorkspaceDocMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workspace_doc_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteWorkspaceDocMembersHeaders()
        return self.delete_workspace_doc_members_with_options(request, headers, runtime)

    def delete_workspace_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.DeleteWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.DeleteWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/deleteWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.DeleteWorkspaceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workspace_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.DeleteWorkspaceMembersHeaders()
        return self.delete_workspace_members_with_options(request, headers, runtime)

    def execute_platform_task_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ExecutePlatformTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_data_json):
            body['FormDataJson'] = request.form_data_json
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.no_execute_expressions):
            body['NoExecuteExpressions'] = request.no_execute_expressions
        if not UtilClient.is_unset(request.out_result):
            body['OutResult'] = request.out_result
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecutePlatformTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/executePlatformTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ExecutePlatformTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_platform_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ExecutePlatformTaskHeaders()
        return self.execute_platform_task_with_options(request, headers, runtime)

    def execute_task_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ExecuteTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.digital_sign_url):
            body['DigitalSignUrl'] = request.digital_sign_url
        if not UtilClient.is_unset(request.form_data_json):
            body['FormDataJson'] = request.form_data_json
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.no_execute_expressions):
            body['NoExecuteExpressions'] = request.no_execute_expressions
        if not UtilClient.is_unset(request.out_result):
            body['OutResult'] = request.out_result
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/executeTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ExecuteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def execute_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ExecuteTaskHeaders()
        return self.execute_task_with_options(request, headers, runtime)

    def get_activity_list_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetActivityListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_code):
            body['ProcessCode'] = request.process_code
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetActivityList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getActivityList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetActivityListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_activity_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetActivityListHeaders()
        return self.get_activity_list_with_options(request, headers, runtime)

    def get_all_sheets_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetAllSheetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetAllSheetsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAllSheets',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/getAllSheets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetAllSheetsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_sheets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetAllSheetsHeaders()
        return self.get_all_sheets_with_options(request, headers, runtime)

    def get_event_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_attendees):
            query['MaxAttendees'] = request.max_attendees
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/getEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetEventResponse(),
            self.call_api(params, req, runtime)
        )

    def get_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetEventHeaders()
        return self.get_event_with_options(request, headers, runtime)

    def get_field_def_by_uuid_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetFieldDefByUuidShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFieldDefByUuid',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getFieldDefByUuid',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetFieldDefByUuidResponse(),
            self.call_api(params, req, runtime)
        )

    def get_field_def_by_uuid(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetFieldDefByUuidHeaders()
        return self.get_field_def_by_uuid_with_options(request, headers, runtime)

    def get_form_component_definition_list_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetFormComponentDefinitionListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFormComponentDefinitionList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getFormComponentDefinitionList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetFormComponentDefinitionListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_form_component_definition_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetFormComponentDefinitionListHeaders()
        return self.get_form_component_definition_list_with_options(request, headers, runtime)

    def get_form_data_by_idwith_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetFormDataByIDShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFormDataByID',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getFormDataByID',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetFormDataByIDResponse(),
            self.call_api(params, req, runtime)
        )

    def get_form_data_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetFormDataByIDHeaders()
        return self.get_form_data_by_idwith_options(request, headers, runtime)

    def get_form_list_in_app_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetFormListInAppShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_types):
            body['FormTypes'] = request.form_types
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFormListInApp',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getFormListInApp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetFormListInAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_form_list_in_app(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetFormListInAppHeaders()
        return self.get_form_list_in_app_with_options(request, headers, runtime)

    def get_instance_by_id_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetInstanceByIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceById',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getInstanceById',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetInstanceByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetInstanceByIdHeaders()
        return self.get_instance_by_id_with_options(request, headers, runtime)

    def get_instance_id_list_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetInstanceIdListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.approved_result):
            body['ApprovedResult'] = request.approved_result
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.instance_status):
            body['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_field_json):
            body['SearchFieldJson'] = request.search_field_json
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceIdList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getInstanceIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetInstanceIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetInstanceIdListHeaders()
        return self.get_instance_id_list_with_options(request, headers, runtime)

    def get_instances_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetInstancesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.approved_result):
            body['ApprovedResult'] = request.approved_result
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.instance_status):
            body['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.order_config_json):
            body['OrderConfigJson'] = request.order_config_json
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_field_json):
            body['SearchFieldJson'] = request.search_field_json
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstances',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getInstances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetInstancesHeaders()
        return self.get_instances_with_options(request, headers, runtime)

    def get_instances_by_id_list_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetInstancesByIdListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_instance_ids):
            body['ProcessInstanceIds'] = request.process_instance_ids
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstancesByIdList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getInstancesByIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetInstancesByIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instances_by_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetInstancesByIdListHeaders()
        return self.get_instances_by_id_list_with_options(request, headers, runtime)

    def get_me_corp_submission_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetMeCorpSubmissionShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_types):
            body['AppTypes'] = request.app_types
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_codes):
            body['ProcessCodes'] = request.process_codes
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMeCorpSubmission',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getMeCorpSubmission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetMeCorpSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_me_corp_submission(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetMeCorpSubmissionHeaders()
        return self.get_me_corp_submission_with_options(request, headers, runtime)

    def get_meeting_rooms_schedule_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetMeetingRoomsScheduleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetMeetingRoomsScheduleShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.room_ids):
            request.room_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_ids, 'RoomIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.room_ids_shrink):
            body['RoomIds'] = request.room_ids_shrink
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMeetingRoomsSchedule',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/getMeetingRoomsSchedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetMeetingRoomsScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_meeting_rooms_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetMeetingRoomsScheduleHeaders()
        return self.get_meeting_rooms_schedule_with_options(request, headers, runtime)

    def get_mine_workspace_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetMineWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetMineWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMineWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getMineWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetMineWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mine_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetMineWorkspaceHeaders()
        return self.get_mine_workspace_with_options(request, headers, runtime)

    def get_node_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
        if not UtilClient.is_unset(request.with_statistical_info):
            body['WithStatisticalInfo'] = request.with_statistical_info
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNode',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getNode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodeHeaders()
        return self.get_node_with_options(request, headers, runtime)

    def get_node_by_url_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodeByUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodeByUrlShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeByUrl',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getNodeByUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodeByUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_by_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodeByUrlHeaders()
        return self.get_node_by_url_with_options(request, headers, runtime)

    def get_nodes_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetNodesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodes',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetNodesHeaders()
        return self.get_nodes_with_options(request, headers, runtime)

    def get_open_url_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetOpenUrlShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenUrl',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getOpenUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetOpenUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_open_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetOpenUrlHeaders()
        return self.get_open_url_with_options(request, headers, runtime)

    def get_operation_records_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetOperationRecordsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOperationRecords',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getOperationRecords',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetOperationRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_operation_records(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetOperationRecordsHeaders()
        return self.get_operation_records_with_options(request, headers, runtime)

    def get_process_definition_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetProcessDefinitionShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.name_space):
            body['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.order_number):
            body['OrderNumber'] = request.order_number
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProcessDefinition',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/getProcessDefinition',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetProcessDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_process_definition(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetProcessDefinitionHeaders()
        return self.get_process_definition_with_options(request, headers, runtime)

    def get_range_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetRangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetRangeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.select):
            body['Select'] = request.select
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRange',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/getRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_range(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetRangeHeaders()
        return self.get_range_with_options(request, headers, runtime)

    def get_report_template_by_name_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetReportTemplateByNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetReportTemplateByNameShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReportTemplateByName',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/getReportTemplateByName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetReportTemplateByNameResponse(),
            self.call_api(params, req, runtime)
        )

    def get_report_template_by_name(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetReportTemplateByNameHeaders()
        return self.get_report_template_by_name_with_options(request, headers, runtime)

    def get_report_un_read_count_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetReportUnReadCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetReportUnReadCountShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReportUnReadCount',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/getReportUnReadCount',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetReportUnReadCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_report_un_read_count(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetReportUnReadCountHeaders()
        return self.get_report_un_read_count_with_options(request, headers, runtime)

    def get_sheet_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/getSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSheetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sheet(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSheetHeaders()
        return self.get_sheet_with_options(request, headers, runtime)

    def get_space_directories_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetSpaceDirectoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetSpaceDirectoriesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.dentry_id):
            body['DentryId'] = request.dentry_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSpaceDirectories',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getSpaceDirectories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSpaceDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_space_directories(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSpaceDirectoriesHeaders()
        return self.get_space_directories_with_options(request, headers, runtime)

    def get_subscribed_calendar_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.GetSubscribedCalendarShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubscribedCalendar',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/getSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetSubscribedCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subscribed_calendar(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetSubscribedCalendarHeaders()
        return self.get_subscribed_calendar_with_options(request, headers, runtime)

    def get_template_list_by_user_id_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetTemplateListByUserIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetTemplateListByUserIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplateListByUserId',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/getTemplateListByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetTemplateListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_list_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetTemplateListByUserIdHeaders()
        return self.get_template_list_by_user_id_with_options(request, headers, runtime)

    def get_user_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetUserShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.language):
            body['language'] = request.language
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/im/getUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetUserHeaders()
        return self.get_user_with_options(request, headers, runtime)

    def get_workspace_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetWorkspaceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getWorkspace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetWorkspaceHeaders()
        return self.get_workspace_with_options(request, headers, runtime)

    def get_workspaces_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GetWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GetWorkspacesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.option):
            request.option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option, 'Option', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.workspace_ids):
            request.workspace_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_ids, 'WorkspaceIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.option_shrink):
            body['Option'] = request.option_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_ids_shrink):
            body['WorkspaceIds'] = request.workspace_ids_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkspaces',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/getWorkspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GetWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workspaces(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GetWorkspacesHeaders()
        return self.get_workspaces_with_options(request, headers, runtime)

    def grant_honor_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.GrantHonorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.GrantHonorShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.open_conversation_ids):
            request.open_conversation_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.open_conversation_ids, 'openConversationIds', 'json')
        if not UtilClient.is_unset(tmp_req.receiver_user_ids):
            request.receiver_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.receiver_user_ids, 'receiverUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.expiration_time):
            body['expirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.grant_reason):
            body['grantReason'] = request.grant_reason
        if not UtilClient.is_unset(request.granter_name):
            body['granterName'] = request.granter_name
        if not UtilClient.is_unset(request.honor_id):
            body['honorId'] = request.honor_id
        if not UtilClient.is_unset(request.notice_announcer):
            body['noticeAnnouncer'] = request.notice_announcer
        if not UtilClient.is_unset(request.notice_single):
            body['noticeSingle'] = request.notice_single
        if not UtilClient.is_unset(request.open_conversation_ids_shrink):
            body['openConversationIds'] = request.open_conversation_ids_shrink
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.receiver_user_ids_shrink):
            body['receiverUserIds'] = request.receiver_user_ids_shrink
        if not UtilClient.is_unset(request.sender_user_id):
            body['senderUserId'] = request.sender_user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantHonor',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/honor/grantHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.GrantHonorResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_honor(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.GrantHonorHeaders()
        return self.grant_honor_with_options(request, headers, runtime)

    def insert_columns_before_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertColumnsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertColumnsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertColumnsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/insertColumnsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertColumnsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_columns_before(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertColumnsBeforeHeaders()
        return self.insert_columns_before_with_options(request, headers, runtime)

    def insert_rows_before_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertRowsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertRowsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertRowsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertRowsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_rows_before(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertRowsBeforeHeaders()
        return self.insert_rows_before_with_options(request, headers, runtime)

    def invite_users_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InviteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InviteUsersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.invitee_list):
            request.invitee_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invitee_list, 'InviteeList', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.invitee_list_shrink):
            body['InviteeList'] = request.invitee_list_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InviteUsers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/inviteUsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InviteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def invite_users(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InviteUsersHeaders()
        return self.invite_users_with_options(request, headers, runtime)

    def list_calendars_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListCalendarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListCalendarsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCalendars',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/listCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListCalendarsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_calendars(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListCalendarsHeaders()
        return self.list_calendars_with_options(request, headers, runtime)

    def list_events_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ListEventsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.max_attendees):
            body['MaxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.series_master_id):
            body['SeriesMasterId'] = request.series_master_id
        if not UtilClient.is_unset(request.show_deleted):
            body['ShowDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.sync_token):
            body['SyncToken'] = request.sync_token
        if not UtilClient.is_unset(request.time_max):
            body['TimeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            body['TimeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEvents',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/listEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListEventsHeaders()
        return self.list_events_with_options(request, headers, runtime)

    def list_events_view_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ListEventsViewShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.max_attendees):
            body['MaxAttendees'] = request.max_attendees
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.time_max):
            body['TimeMax'] = request.time_max
        if not UtilClient.is_unset(request.time_min):
            body['TimeMin'] = request.time_min
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventsView',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/listEventsView',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListEventsViewResponse(),
            self.call_api(params, req, runtime)
        )

    def list_events_view(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListEventsViewHeaders()
        return self.list_events_view_with_options(request, headers, runtime)

    def list_form_remarks_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListFormRemarksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListFormRemarksShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.form_instance_id_list):
            request.form_instance_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.form_instance_id_list, 'FormInstanceIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_instance_id_list_shrink):
            body['FormInstanceIdList'] = request.form_instance_id_list_shrink
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFormRemarks',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/listFormRemarks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListFormRemarksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_form_remarks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListFormRemarksHeaders()
        return self.list_form_remarks_with_options(request, headers, runtime)

    def list_navigation_by_form_type_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ListNavigationByFormTypeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_type):
            body['FormType'] = request.form_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNavigationByFormType',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/listNavigationByFormType',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListNavigationByFormTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_navigation_by_form_type(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListNavigationByFormTypeHeaders()
        return self.list_navigation_by_form_type_with_options(request, headers, runtime)

    def list_nodes_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListNodesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_node_id):
            body['ParentNodeId'] = request.parent_node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/listNodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListNodesHeaders()
        return self.list_nodes_with_options(request, headers, runtime)

    def list_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.modified_end_time):
            body['ModifiedEndTime'] = request.modified_end_time
        if not UtilClient.is_unset(request.modified_start_time):
            body['ModifiedStartTime'] = request.modified_start_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/listReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListReportHeaders()
        return self.list_report_with_options(request, headers, runtime)

    def list_table_data_by_form_instance_id_table_id_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.ListTableDataByFormInstanceIdTableIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_instance_id):
            body['FormInstanceId'] = request.form_instance_id
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.table_field_id):
            body['TableFieldId'] = request.table_field_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTableDataByFormInstanceIdTableId',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/listTableDataByFormInstanceIdTableId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListTableDataByFormInstanceIdTableIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_table_data_by_form_instance_id_table_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListTableDataByFormInstanceIdTableIdHeaders()
        return self.list_table_data_by_form_instance_id_table_id_with_options(request, headers, runtime)

    def list_workspaces_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ListWorkspacesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.team_id):
            body['TeamId'] = request.team_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.with_permission_role):
            body['WithPermissionRole'] = request.with_permission_role
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/listWorkspaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workspaces(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ListWorkspacesHeaders()
        return self.list_workspaces_with_options(request, headers, runtime)

    def patch_event_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.PatchEventShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.PatchEventShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees):
            request.attendees_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees, 'Attendees', 'json')
        if not UtilClient.is_unset(tmp_req.end):
            request.end_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end, 'End', 'json')
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'Extra', 'json')
        if not UtilClient.is_unset(tmp_req.location):
            request.location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location, 'Location', 'json')
        if not UtilClient.is_unset(tmp_req.recurrence):
            request.recurrence_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recurrence, 'Recurrence', 'json')
        if not UtilClient.is_unset(tmp_req.reminders):
            request.reminders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reminders, 'Reminders', 'json')
        if not UtilClient.is_unset(tmp_req.start):
            request.start_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start, 'Start', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_shrink):
            body['Attendees'] = request.attendees_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_shrink):
            body['End'] = request.end_shrink
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.extra_shrink):
            body['Extra'] = request.extra_shrink
        if not UtilClient.is_unset(request.is_all_day):
            body['IsAllDay'] = request.is_all_day
        if not UtilClient.is_unset(request.location_shrink):
            body['Location'] = request.location_shrink
        if not UtilClient.is_unset(request.recurrence_shrink):
            body['Recurrence'] = request.recurrence_shrink
        if not UtilClient.is_unset(request.reminders_shrink):
            body['Reminders'] = request.reminders_shrink
        if not UtilClient.is_unset(request.start_shrink):
            body['Start'] = request.start_shrink
        if not UtilClient.is_unset(request.summary):
            body['Summary'] = request.summary
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchEvent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/patchEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.PatchEventResponse(),
            self.call_api(params, req, runtime)
        )

    def patch_event(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.PatchEventHeaders()
        return self.patch_event_with_options(request, headers, runtime)

    def query_cloud_record_text_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordTextShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.direction):
            body['Direction'] = request.direction
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCloudRecordText',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryCloudRecordText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordTextResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cloud_record_text(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordTextHeaders()
        return self.query_cloud_record_text_with_options(request, headers, runtime)

    def query_cloud_record_video_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordVideoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordVideoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCloudRecordVideo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryCloudRecordVideo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cloud_record_video(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordVideoHeaders()
        return self.query_cloud_record_video_with_options(request, headers, runtime)

    def query_cloud_record_video_play_info_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryCloudRecordVideoPlayInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryCloudRecordVideoPlayInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCloudRecordVideoPlayInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryCloudRecordVideoPlayInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryCloudRecordVideoPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cloud_record_video_play_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryCloudRecordVideoPlayInfoHeaders()
        return self.query_cloud_record_video_play_info_with_options(request, headers, runtime)

    def query_conference_info_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.QueryConferenceInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConferenceInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryConferenceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryConferenceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_conference_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryConferenceInfoHeaders()
        return self.query_conference_info_with_options(request, headers, runtime)

    def query_conference_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryConferenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryConferenceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConferenceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryConferenceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryConferenceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_conference_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryConferenceMembersHeaders()
        return self.query_conference_members_with_options(request, headers, runtime)

    def query_dentry_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryDentryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryDentryShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.dentry_id):
            body['DentryId'] = request.dentry_id
        if not UtilClient.is_unset(request.include_space):
            body['IncludeSpace'] = request.include_space
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDentry',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v2/documents/queryDentry',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryDentryResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dentry(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryDentryHeaders()
        return self.query_dentry_with_options(request, headers, runtime)

    def query_live_info_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveInfoShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLiveInfo',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryLiveInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_live_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveInfoHeaders()
        return self.query_live_info_with_options(request, headers, runtime)

    def query_live_watch_detail_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveWatchDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveWatchDetailShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLiveWatchDetail',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryLiveWatchDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveWatchDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_live_watch_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveWatchDetailHeaders()
        return self.query_live_watch_detail_with_options(request, headers, runtime)

    def query_live_watch_user_list_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryLiveWatchUserListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryLiveWatchUserListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLiveWatchUserList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryLiveWatchUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryLiveWatchUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_live_watch_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryLiveWatchUserListHeaders()
        return self.query_live_watch_user_list_with_options(request, headers, runtime)

    def query_meeting_room_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def query_meeting_room(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomHeaders()
        return self.query_meeting_room_with_options(request, headers, runtime)

    def query_meeting_room_group_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_meeting_room_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomGroupHeaders()
        return self.query_meeting_room_group_with_options(request, headers, runtime)

    def query_meeting_room_group_list_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomGroupListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomGroupListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.request):
            request.request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request, 'Request', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_shrink):
            body['Request'] = request.request_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMeetingRoomGroupList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryMeetingRoomGroupList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_meeting_room_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomGroupListHeaders()
        return self.query_meeting_room_group_list_with_options(request, headers, runtime)

    def query_meeting_room_list_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryMeetingRoomListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryMeetingRoomListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMeetingRoomList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryMeetingRoomList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryMeetingRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_meeting_room_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryMeetingRoomListHeaders()
        return self.query_meeting_room_list_with_options(request, headers, runtime)

    def query_org_honors_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryOrgHonorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryOrgHonorsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrgHonors',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/honor/queryOrgHonors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryOrgHonorsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_org_honors(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryOrgHonorsHeaders()
        return self.query_org_honors_with_options(request, headers, runtime)

    def query_org_todo_tasks_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryOrgTodoTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryOrgTodoTasksShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.is_done):
            body['isDone'] = request.is_done
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrgTodoTasks',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/task/queryOrgTodoTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryOrgTodoTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def query_org_todo_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryOrgTodoTasksHeaders()
        return self.query_org_todo_tasks_with_options(request, headers, runtime)

    def query_schedule_conference_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_union_id):
            body['RequestUnionId'] = request.request_union_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/queryScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_schedule_conference(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryScheduleConferenceHeaders()
        return self.query_schedule_conference_with_options(request, headers, runtime)

    def query_user_honors_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.QueryUserHonorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.QueryUserHonorsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryUserHonors',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/honor/queryUserHonors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.QueryUserHonorsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_honors(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.QueryUserHonorsHeaders()
        return self.query_user_honors_with_options(request, headers, runtime)

    def recall_honor_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.RecallHonorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.RecallHonorShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.honor_id):
            body['honorId'] = request.honor_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecallHonor',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/honor/recallHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.RecallHonorResponse(),
            self.call_api(params, req, runtime)
        )

    def recall_honor(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.RecallHonorHeaders()
        return self.recall_honor_with_options(request, headers, runtime)

    def receiver_list_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.ReceiverListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.ReceiverListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReceiverListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/receiverListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.ReceiverListReportResponse(),
            self.call_api(params, req, runtime)
        )

    def receiver_list_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.ReceiverListReportHeaders()
        return self.receiver_list_report_with_options(request, headers, runtime)

    def remove_attendee_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.RemoveAttendeeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.RemoveAttendeeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.attendees_to_remove):
            request.attendees_to_remove_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attendees_to_remove, 'AttendeesToRemove', 'json')
        body = {}
        if not UtilClient.is_unset(request.attendees_to_remove_shrink):
            body['AttendeesToRemove'] = request.attendees_to_remove_shrink
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveAttendee',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/removeAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.RemoveAttendeeResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_attendee(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.RemoveAttendeeHeaders()
        return self.remove_attendee_with_options(request, headers, runtime)

    def remove_meeting_rooms_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.RemoveMeetingRoomsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.RemoveMeetingRoomsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.meeting_rooms_to_remove):
            request.meeting_rooms_to_remove_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.meeting_rooms_to_remove, 'MeetingRoomsToRemove', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.meeting_rooms_to_remove_shrink):
            body['MeetingRoomsToRemove'] = request.meeting_rooms_to_remove_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMeetingRooms',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/removeMeetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.RemoveMeetingRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_meeting_rooms(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.RemoveMeetingRoomsHeaders()
        return self.remove_meeting_rooms_with_options(request, headers, runtime)

    def save_content_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SaveContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SaveContentShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.contents):
            request.contents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contents, 'Contents', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.contents_shrink):
            body['Contents'] = request.contents_shrink
        if not UtilClient.is_unset(request.dd_from):
            body['DdFrom'] = request.dd_from
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveContent',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/saveContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SaveContentResponse(),
            self.call_api(params, req, runtime)
        )

    def save_content(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SaveContentHeaders()
        return self.save_content_with_options(request, headers, runtime)

    def save_form_data_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SaveFormDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_data_json):
            body['FormDataJson'] = request.form_data_json
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveFormData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/saveFormData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SaveFormDataResponse(),
            self.call_api(params, req, runtime)
        )

    def save_form_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SaveFormDataHeaders()
        return self.save_form_data_with_options(request, headers, runtime)

    def search_employee_field_values_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SearchEmployeeFieldValuesShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.search_field_json):
            body['SearchFieldJson'] = request.search_field_json
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.target_field_json):
            body['TargetFieldJson'] = request.target_field_json
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchEmployeeFieldValues',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/searchEmployeeFieldValues',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SearchEmployeeFieldValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_employee_field_values(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SearchEmployeeFieldValuesHeaders()
        return self.search_employee_field_values_with_options(request, headers, runtime)

    def search_form_data_id_list_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SearchFormDataIdListShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_field_json):
            body['SearchFieldJson'] = request.search_field_json
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFormDataIdList',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/searchFormDataIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SearchFormDataIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def search_form_data_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SearchFormDataIdListHeaders()
        return self.search_form_data_id_list_with_options(request, headers, runtime)

    def search_form_data_second_generation_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SearchFormDataSecondGenerationShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.order_config_json):
            body['OrderConfigJson'] = request.order_config_json
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_condition):
            body['SearchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFormDataSecondGeneration',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/searchFormDataSecondGeneration',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SearchFormDataSecondGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    def search_form_data_second_generation(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SearchFormDataSecondGenerationHeaders()
        return self.search_form_data_second_generation_with_options(request, headers, runtime)

    def search_form_data_second_generation_no_table_field_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SearchFormDataSecondGenerationNoTableFieldShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.order_config_json):
            body['OrderConfigJson'] = request.order_config_json
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_condition):
            body['SearchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFormDataSecondGenerationNoTableField',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/searchFormDataSecondGenerationNoTableField',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SearchFormDataSecondGenerationNoTableFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def search_form_data_second_generation_no_table_field(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SearchFormDataSecondGenerationNoTableFieldHeaders()
        return self.search_form_data_second_generation_no_table_field_with_options(request, headers, runtime)

    def search_form_datas_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SearchFormDatasShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.create_from_time_gmt):
            body['CreateFromTimeGMT'] = request.create_from_time_gmt
        if not UtilClient.is_unset(request.create_to_time_gmt):
            body['CreateToTimeGMT'] = request.create_to_time_gmt
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dynamic_order):
            body['DynamicOrder'] = request.dynamic_order
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.modified_from_time_gmt):
            body['ModifiedFromTimeGMT'] = request.modified_from_time_gmt
        if not UtilClient.is_unset(request.modified_to_time_gmt):
            body['ModifiedToTimeGMT'] = request.modified_to_time_gmt
        if not UtilClient.is_unset(request.originator_id):
            body['OriginatorId'] = request.originator_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_field_json):
            body['SearchFieldJson'] = request.search_field_json
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFormDatas',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/searchFormDatas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SearchFormDatasResponse(),
            self.call_api(params, req, runtime)
        )

    def search_form_datas(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SearchFormDatasHeaders()
        return self.search_form_datas_with_options(request, headers, runtime)

    def send_banner_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SendBannerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SendBannerShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.content_shrink):
            body['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendBanner',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/watt/sendBanner',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SendBannerResponse(),
            self.call_api(params, req, runtime)
        )

    def send_banner(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SendBannerHeaders()
        return self.send_banner_with_options(request, headers, runtime)

    def send_popup_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SendPopupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SendPopupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.content_shrink):
            body['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendPopup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/watt/sendPopup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SendPopupResponse(),
            self.call_api(params, req, runtime)
        )

    def send_popup(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SendPopupHeaders()
        return self.send_popup_with_options(request, headers, runtime)

    def send_search_shade_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SendSearchShadeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SendSearchShadeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.content_shrink):
            body['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSearchShade',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/watt/sendSearchShade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SendSearchShadeResponse(),
            self.call_api(params, req, runtime)
        )

    def send_search_shade(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SendSearchShadeHeaders()
        return self.send_search_shade_with_options(request, headers, runtime)

    def set_columns_visibility_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SetColumnsVisibilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SetColumnsVisibilityShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.column_count):
            body['ColumnCount'] = request.column_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.visibility):
            body['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetColumnsVisibility',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/setColumnsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SetColumnsVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    def set_columns_visibility(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SetColumnsVisibilityHeaders()
        return self.set_columns_visibility_with_options(request, headers, runtime)

    def set_rows_visibility_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SetRowsVisibilityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SetRowsVisibilityShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.visibility):
            body['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetRowsVisibility',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/setRowsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SetRowsVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    def set_rows_visibility(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SetRowsVisibilityHeaders()
        return self.set_rows_visibility_with_options(request, headers, runtime)

    def simple_list_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.SimpleListReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.SimpleListReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['Cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SimpleListReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/simpleListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SimpleListReportResponse(),
            self.call_api(params, req, runtime)
        )

    def simple_list_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SimpleListReportHeaders()
        return self.simple_list_report_with_options(request, headers, runtime)

    def start_cloud_record_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StartCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StartCloudRecordShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.small_window_position):
            body['SmallWindowPosition'] = request.small_window_position
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartCloudRecord',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/startCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StartCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def start_cloud_record(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StartCloudRecordHeaders()
        return self.start_cloud_record_with_options(request, headers, runtime)

    def start_instance_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.StartInstanceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.department_id):
            body['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.form_data_json):
            body['FormDataJson'] = request.form_data_json
        if not UtilClient.is_unset(request.form_uuid):
            body['FormUuid'] = request.form_uuid
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_code):
            body['ProcessCode'] = request.process_code
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/startInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StartInstanceHeaders()
        return self.start_instance_with_options(request, headers, runtime)

    def statistics_list_by_type_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StatisticsListByTypeReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StatisticsListByTypeReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StatisticsListByTypeReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/statisticsListByTypeReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StatisticsListByTypeReportResponse(),
            self.call_api(params, req, runtime)
        )

    def statistics_list_by_type_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StatisticsListByTypeReportHeaders()
        return self.statistics_list_by_type_report_with_options(request, headers, runtime)

    def statistics_report_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StatisticsReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StatisticsReportShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.report_id):
            body['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StatisticsReport',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/log/statisticsReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StatisticsReportResponse(),
            self.call_api(params, req, runtime)
        )

    def statistics_report(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StatisticsReportHeaders()
        return self.statistics_report_with_options(request, headers, runtime)

    def stop_cloud_record_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.StopCloudRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.StopCloudRecordShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.conference_id):
            body['conferenceId'] = request.conference_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopCloudRecord',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/stopCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.StopCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_cloud_record(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.StopCloudRecordHeaders()
        return self.stop_cloud_record_with_options(request, headers, runtime)

    def subscribe_calendar_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.SubscribeCalendarShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubscribeCalendar',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/subscribeCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.SubscribeCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    def subscribe_calendar(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.SubscribeCalendarHeaders()
        return self.subscribe_calendar_with_options(request, headers, runtime)

    def terminate_instance_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.TerminateInstanceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateInstance',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/terminateInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.TerminateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def terminate_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.TerminateInstanceHeaders()
        return self.terminate_instance_with_options(request, headers, runtime)

    def unsubscribe_calendar_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.UnsubscribeCalendarShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnsubscribeCalendar',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/unsubscribeCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UnsubscribeCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    def unsubscribe_calendar(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UnsubscribeCalendarHeaders()
        return self.unsubscribe_calendar_with_options(request, headers, runtime)

    def update_form_data_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.UpdateFormDataShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.form_instance_id):
            body['FormInstanceId'] = request.form_instance_id
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.update_form_data_json):
            body['UpdateFormDataJson'] = request.update_form_data_json
        if not UtilClient.is_unset(request.use_latest_version):
            body['UseLatestVersion'] = request.use_latest_version
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFormData',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/updateFormData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateFormDataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_form_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateFormDataHeaders()
        return self.update_form_data_with_options(request, headers, runtime)

    def update_instance_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.UpdateInstanceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.process_instance_id):
            body['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        if not UtilClient.is_unset(request.update_form_data_json):
            body['UpdateFormDataJson'] = request.update_form_data_json
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/updateInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateInstanceHeaders()
        return self.update_instance_with_options(request, headers, runtime)

    def update_live_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateLiveShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateLiveShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.pre_end_time):
            body['PreEndTime'] = request.pre_end_time
        if not UtilClient.is_unset(request.pre_start_time):
            body['PreStartTime'] = request.pre_start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLive',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/updateLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateLiveHeaders()
        return self.update_live_with_options(request, headers, runtime)

    def update_meeting_room_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateMeetingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateMeetingRoomShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.reservation_authority):
            request.reservation_authority_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reservation_authority, 'ReservationAuthority', 'json')
        if not UtilClient.is_unset(tmp_req.room_label_ids):
            request.room_label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_label_ids, 'RoomLabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.room_location):
            request.room_location_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_location, 'RoomLocation', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_cycle_reservation):
            body['EnableCycleReservation'] = request.enable_cycle_reservation
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.isv_room_id):
            body['IsvRoomId'] = request.isv_room_id
        if not UtilClient.is_unset(request.reservation_authority_shrink):
            body['ReservationAuthority'] = request.reservation_authority_shrink
        if not UtilClient.is_unset(request.room_capacity):
            body['RoomCapacity'] = request.room_capacity
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_label_ids_shrink):
            body['RoomLabelIds'] = request.room_label_ids_shrink
        if not UtilClient.is_unset(request.room_location_shrink):
            body['RoomLocation'] = request.room_location_shrink
        if not UtilClient.is_unset(request.room_name):
            body['RoomName'] = request.room_name
        if not UtilClient.is_unset(request.room_picture):
            body['RoomPicture'] = request.room_picture
        if not UtilClient.is_unset(request.room_status):
            body['RoomStatus'] = request.room_status
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeetingRoom',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/updateMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def update_meeting_room(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateMeetingRoomHeaders()
        return self.update_meeting_room_with_options(request, headers, runtime)

    def update_meeting_room_group_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateMeetingRoomGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateMeetingRoomGroupShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeetingRoomGroup',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/updateMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_meeting_room_group(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateMeetingRoomGroupHeaders()
        return self.update_meeting_room_group_with_options(request, headers, runtime)

    def update_range_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateRangeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateRangeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.background_colors):
            request.background_colors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.background_colors, 'BackgroundColors', 'json')
        if not UtilClient.is_unset(tmp_req.hyperlinks):
            request.hyperlinks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hyperlinks, 'Hyperlinks', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.values):
            request.values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.values, 'Values', 'json')
        body = {}
        if not UtilClient.is_unset(request.background_colors_shrink):
            body['BackgroundColors'] = request.background_colors_shrink
        if not UtilClient.is_unset(request.hyperlinks_shrink):
            body['Hyperlinks'] = request.hyperlinks_shrink
        if not UtilClient.is_unset(request.number_format):
            body['NumberFormat'] = request.number_format
        if not UtilClient.is_unset(request.range_address):
            body['RangeAddress'] = request.range_address
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.values_shrink):
            body['Values'] = request.values_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRange',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/updateRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_range(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateRangeHeaders()
        return self.update_range_with_options(request, headers, runtime)

    def update_schedule_conference_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateScheduleConferenceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateScheduleConferenceShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.schedule_conference_id):
            body['ScheduleConferenceId'] = request.schedule_conference_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScheduleConference',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/ysp/updateScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_schedule_conference(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateScheduleConferenceHeaders()
        return self.update_schedule_conference_with_options(request, headers, runtime)

    def update_status_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateStatusShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.error_lines):
            request.error_lines_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.error_lines, 'ErrorLines', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.error_lines_shrink):
            body['ErrorLines'] = request.error_lines_shrink
        if not UtilClient.is_unset(request.import_sequence):
            body['ImportSequence'] = request.import_sequence
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.system_token):
            body['SystemToken'] = request.system_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStatus',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/yida/updateStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateStatusHeaders()
        return self.update_status_with_options(request, headers, runtime)

    def update_subscribed_calendars_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateSubscribedCalendarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateSubscribedCalendarsShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.managers):
            request.managers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.managers, 'Managers', 'json')
        if not UtilClient.is_unset(tmp_req.subscribe_scope):
            request.subscribe_scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.subscribe_scope, 'SubscribeScope', 'json')
        body = {}
        if not UtilClient.is_unset(request.calendar_id):
            body['CalendarId'] = request.calendar_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.managers_shrink):
            body['Managers'] = request.managers_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.subscribe_scope_shrink):
            body['SubscribeScope'] = request.subscribe_scope_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscribedCalendars',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/calendar/updateSubscribedCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateSubscribedCalendarsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_subscribed_calendars(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateSubscribedCalendarsHeaders()
        return self.update_subscribed_calendars_with_options(request, headers, runtime)

    def update_todo_task_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateTodoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateTodoTaskShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'executorIds', 'json')
        if not UtilClient.is_unset(tmp_req.participant_ids):
            request.participant_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.participant_ids, 'participantIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.done):
            body['done'] = request.done
        if not UtilClient.is_unset(request.due_time):
            body['dueTime'] = request.due_time
        if not UtilClient.is_unset(request.executor_ids_shrink):
            body['executorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.participant_ids_shrink):
            body['participantIds'] = request.participant_ids_shrink
        if not UtilClient.is_unset(request.subject):
            body['subject'] = request.subject
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTodoTask',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/task/updateTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_todo_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateTodoTaskHeaders()
        return self.update_todo_task_with_options(request, headers, runtime)

    def update_todo_task_executor_status_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateTodoTaskExecutorStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateTodoTaskExecutorStatusShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        if not UtilClient.is_unset(tmp_req.executor_status_list):
            request.executor_status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_status_list, 'executorStatusList', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.executor_status_list_shrink):
            body['executorStatusList'] = request.executor_status_list_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTodoTaskExecutorStatus',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/task/updateTodoTaskExecutorStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateTodoTaskExecutorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_todo_task_executor_status(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateTodoTaskExecutorStatusHeaders()
        return self.update_todo_task_executor_status_with_options(request, headers, runtime)

    def update_user_avatar_with_options(self, request, tmp_header, runtime):
        UtilClient.validate_model(request)
        headers = aliding_20230426_models.UpdateUserAvatarShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.avatar_media_id):
            body['AvatarMediaId'] = request.avatar_media_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserAvatar',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/contact/updateUserAvatar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateUserAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_avatar(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateUserAvatarHeaders()
        return self.update_user_avatar_with_options(request, headers, runtime)

    def update_workspace_doc_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateWorkspaceDocMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateWorkspaceDocMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceDocMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/updateWorkspaceDocMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateWorkspaceDocMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workspace_doc_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateWorkspaceDocMembersHeaders()
        return self.update_workspace_doc_members_with_options(request, headers, runtime)

    def update_workspace_members_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UpdateWorkspaceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UpdateWorkspaceMembersShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceMembers',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/dingtalk/v1/documents/updateWorkspaceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UpdateWorkspaceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workspace_members(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UpdateWorkspaceMembersHeaders()
        return self.update_workspace_members_with_options(request, headers, runtime)

    def upload_media_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.UploadMediaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.UploadMediaShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.media_name):
            body['mediaName'] = request.media_name
        if not UtilClient.is_unset(request.media_type):
            body['mediaType'] = request.media_type
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMedia',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/documents/uploadMedia',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.UploadMediaResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_media(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.UploadMediaHeaders()
        return self.upload_media_with_options(request, headers, runtime)

    def wear_org_honor_with_options(self, tmp_req, tmp_header, runtime):
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.WearOrgHonorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.WearOrgHonorShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.honor_id):
            body['honorId'] = request.honor_id
        if not UtilClient.is_unset(request.org_id):
            body['orgId'] = request.org_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.wear):
            body['wear'] = request.wear
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WearOrgHonor',
            version='2023-04-26',
            protocol='HTTPS',
            pathname='/aliding/v1/honor/wearOrgHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.WearOrgHonorResponse(),
            self.call_api(params, req, runtime)
        )

    def wear_org_honor(self, request):
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.WearOrgHonorHeaders()
        return self.wear_org_honor_with_options(request, headers, runtime)
