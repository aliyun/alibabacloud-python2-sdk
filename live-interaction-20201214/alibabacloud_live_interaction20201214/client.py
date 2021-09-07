# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_live_interaction20201214 import models as live_interaction_20201214_models
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
        self._endpoint = self.get_endpoint('live-interaction', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def list_app_infos_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListAppInfosShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListAppInfosResponse(),
            self.do_rpcrequest('ListAppInfos', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_infos_with_options(request, runtime)

    def remove_single_chat_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveSingleChatExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_single_chat_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_single_chat_extension_by_keys_with_options(request, runtime)

    def import_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportMessageResponse(),
            self.do_rpcrequest('ImportMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_message_with_options(request, runtime)

    def silence_all_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SilenceAllGroupMembersResponse(),
            self.do_rpcrequest('SilenceAllGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def silence_all_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.silence_all_group_members_with_options(request, runtime)

    def list_room_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomMessagesResponse(),
            self.do_rpcrequest('ListRoomMessages', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_room_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_messages_with_options(request, runtime)

    def set_group_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupExtensionByKeysResponse(),
            self.do_rpcrequest('SetGroupExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_extension_by_keys_with_options(request, runtime)

    def remove_group_member_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveGroupMemberExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_member_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_member_extension_by_keys_with_options(request, runtime)

    def add_group_silence_blacklist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceBlacklistResponse(),
            self.do_rpcrequest('AddGroupSilenceBlacklist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_group_silence_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_group_silence_blacklist_with_options(request, runtime)

    def remove_group_silence_whitelist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse(),
            self.do_rpcrequest('RemoveGroupSilenceWhitelist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_silence_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_silence_whitelist_with_options(request, runtime)

    def list_detail_report_statistics_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListDetailReportStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListDetailReportStatisticsResponse(),
            self.do_rpcrequest('ListDetailReportStatistics', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_detail_report_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_detail_report_statistics_with_options(request, runtime)

    def set_user_conversation_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse(),
            self.do_rpcrequest('SetUserConversationExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_user_conversation_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_user_conversation_extension_by_keys_with_options(request, runtime)

    def get_group_by_id_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupByIdResponse(),
            self.do_rpcrequest('GetGroupById', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_by_id_with_options(request, runtime)

    def update_tenant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateTenantStatusResponse(),
            self.do_rpcrequest('UpdateTenantStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_tenant_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_tenant_status_with_options(request, runtime)

    def get_common_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetCommonConfigResponse(),
            self.do_rpcrequest('GetCommonConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_common_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_common_config_with_options(request, runtime)

    def send_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendMessageResponse(),
            self.do_rpcrequest('SendMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    def update_group_members_role_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupMembersRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupMembersRoleResponse(),
            self.do_rpcrequest('UpdateGroupMembersRole', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_members_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_members_role_with_options(request, runtime)

    def cancel_silence_all_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CancelSilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse(),
            self.do_rpcrequest('CancelSilenceAllGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_silence_all_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_silence_all_group_members_with_options(request, runtime)

    def update_group_icon_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupIconShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupIconResponse(),
            self.do_rpcrequest('UpdateGroupIcon', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_icon(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_icon_with_options(request, runtime)

    def remove_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMembersResponse(),
            self.do_rpcrequest('RemoveGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_members_with_options(request, runtime)

    def list_group_all_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupAllMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupAllMembersResponse(),
            self.do_rpcrequest('ListGroupAllMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group_all_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_all_members_with_options(request, runtime)

    def get_user_mute_setting_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetUserMuteSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetUserMuteSettingResponse(),
            self.do_rpcrequest('GetUserMuteSetting', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_mute_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_mute_setting_with_options(request, runtime)

    def get_room_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetRoomStatisticsResponse(),
            self.do_rpcrequest('GetRoomStatistics', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_room_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_room_statistics_with_options(request, runtime)

    def add_group_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupMembersResponse(),
            self.do_rpcrequest('AddGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_group_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_group_members_with_options(request, runtime)

    def get_group_member_by_ids_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupMemberByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupMemberByIdsResponse(),
            self.do_rpcrequest('GetGroupMemberByIds', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group_member_by_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_group_member_by_ids_with_options(request, runtime)

    def send_custom_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageResponse(),
            self.do_rpcrequest('SendCustomMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_with_options(request, runtime)

    def update_app_name_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppNameResponse(),
            self.do_rpcrequest('UpdateAppName', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_name_with_options(request, runtime)

    def get_imconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetIMConfigResponse(),
            self.do_rpcrequest('GetIMConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_imconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_imconfig_with_options(request, runtime)

    def set_single_chat_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse(),
            self.do_rpcrequest('SetSingleChatExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_single_chat_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_single_chat_extension_by_keys_with_options(request, runtime)

    def update_app_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppStatusResponse(),
            self.do_rpcrequest('UpdateAppStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_status_with_options(request, runtime)

    def mute_users_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.MuteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.MuteUsersResponse(),
            self.do_rpcrequest('MuteUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mute_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mute_users_with_options(request, runtime)

    def recall_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RecallMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RecallMessageResponse(),
            self.do_rpcrequest('RecallMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recall_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recall_message_with_options(request, runtime)

    def add_group_silence_whitelist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceWhitelistResponse(),
            self.do_rpcrequest('AddGroupSilenceWhitelist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_group_silence_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_group_silence_whitelist_with_options(request, runtime)

    def set_group_owner_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupOwnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupOwnerResponse(),
            self.do_rpcrequest('SetGroupOwner', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_owner_with_options(request, runtime)

    def list_room_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomUsersResponse(),
            self.do_rpcrequest('ListRoomUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_room_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_users_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def remove_group_silence_blacklist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse(),
            self.do_rpcrequest('RemoveGroupSilenceBlacklist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_silence_blacklist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_silence_blacklist_with_options(request, runtime)

    def remove_message_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveMessageExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_message_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_message_extension_by_keys_with_options(request, runtime)

    def get_media_upload_url_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUploadUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUploadUrlResponse(),
            self.do_rpcrequest('GetMediaUploadUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_upload_url_with_options(request, runtime)

    def get_media_url_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUrlResponse(),
            self.do_rpcrequest('GetMediaUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_media_url_with_options(request, runtime)

    def import_single_conversation_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportSingleConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportSingleConversationResponse(),
            self.do_rpcrequest('ImportSingleConversation', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_single_conversation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_single_conversation_with_options(request, runtime)

    def update_callback_config_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateCallbackConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateCallbackConfigResponse(),
            self.do_rpcrequest('UpdateCallbackConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_callback_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_callback_config_with_options(request, runtime)

    def init_tenant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.InitTenantResponse(),
            self.do_rpcrequest('InitTenant', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_tenant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.init_tenant_with_options(request, runtime)

    def import_group_chat_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatMemberResponse(),
            self.do_rpcrequest('ImportGroupChatMember', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_group_chat_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_group_chat_member_with_options(request, runtime)

    def list_group_silence_members_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupSilenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupSilenceMembersResponse(),
            self.do_rpcrequest('ListGroupSilenceMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group_silence_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_group_silence_members_with_options(request, runtime)

    def remove_group_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveGroupExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_group_extension_by_keys_with_options(request, runtime)

    def set_group_member_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse(),
            self.do_rpcrequest('SetGroupMemberExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_member_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_member_extension_by_keys_with_options(request, runtime)

    def create_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CreateGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateGroupResponse(),
            self.do_rpcrequest('CreateGroup', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def get_message_by_id_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMessageByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMessageByIdResponse(),
            self.do_rpcrequest('GetMessageById', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_message_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_by_id_with_options(request, runtime)

    def destroy_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DestroyRoomResponse(),
            self.do_rpcrequest('DestroyRoom', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.destroy_room_with_options(request, runtime)

    def kick_off_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.KickOffShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.KickOffResponse(),
            self.do_rpcrequest('KickOff', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kick_off(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kick_off_with_options(request, runtime)

    def list_callback_api_ids_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            live_interaction_20201214_models.ListCallbackApiIdsResponse(),
            self.do_rpcrequest('ListCallbackApiIds', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_callback_api_ids(self):
        runtime = util_models.RuntimeOptions()
        return self.list_callback_api_ids_with_options(runtime)

    def set_message_read_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageReadShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageReadResponse(),
            self.do_rpcrequest('SetMessageRead', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_message_read(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_message_read_with_options(request, runtime)

    def update_msg_recall_interval_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateMsgRecallIntervalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateMsgRecallIntervalResponse(),
            self.do_rpcrequest('UpdateMsgRecallInterval', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_msg_recall_interval(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_msg_recall_interval_with_options(request, runtime)

    def send_custom_message_to_room_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse(),
            self.do_rpcrequest('SendCustomMessageToRoomUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_message_to_room_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_room_users_with_options(request, runtime)

    def update_group_title_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupTitleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupTitleResponse(),
            self.do_rpcrequest('UpdateGroupTitle', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_title(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_group_title_with_options(request, runtime)

    def get_login_token_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetLoginTokenResponse(),
            self.do_rpcrequest('GetLoginToken', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    def dismiss_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.DismissGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DismissGroupResponse(),
            self.do_rpcrequest('DismissGroup', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dismiss_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dismiss_group_with_options(request, runtime)

    def import_group_chat_conversation_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatConversationResponse(),
            self.do_rpcrequest('ImportGroupChatConversation', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_group_chat_conversation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_group_chat_conversation_with_options(request, runtime)

    def create_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateRoomResponse(),
            self.do_rpcrequest('CreateRoom', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    def remove_user_conversation_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveUserConversationExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_user_conversation_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_user_conversation_extension_by_keys_with_options(request, runtime)

    def set_message_extension_by_keys_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageExtensionByKeysResponse(),
            self.do_rpcrequest('SetMessageExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_message_extension_by_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_message_extension_by_keys_with_options(request, runtime)
