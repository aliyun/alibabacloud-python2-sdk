# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imp20210630 import models as imp_20210630_models
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
        self._endpoint = self.get_endpoint('imp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def verify_domain_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.VerifyDomainOwnerResponse(),
            self.do_rpcrequest('VerifyDomainOwner', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)

    def create_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveResponse(),
            self.do_rpcrequest('CreateLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_with_options(request, runtime)

    def remove_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.RemoveMemberResponse(),
            self.do_rpcrequest('RemoveMember', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_member_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def list_apply_link_mic_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListApplyLinkMicUsersResponse(),
            self.do_rpcrequest('ListApplyLinkMicUsers', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apply_link_mic_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apply_link_mic_users_with_options(request, runtime)

    def list_room_lives_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomLivesResponse(),
            self.do_rpcrequest('ListRoomLives', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_room_lives(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_lives_with_options(request, runtime)

    def update_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateRoomResponse(),
            self.do_rpcrequest('UpdateRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_room_with_options(request, runtime)

    def get_app_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppTemplateResponse(),
            self.do_rpcrequest('GetAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_template_with_options(request, runtime)

    def get_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRoomResponse(),
            self.do_rpcrequest('GetRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_room_with_options(request, runtime)

    def create_app_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppTemplateResponse(),
            self.do_rpcrequest('CreateAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_template_with_options(request, runtime)

    def get_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetConferenceResponse(),
            self.do_rpcrequest('GetConference', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conference_with_options(request, runtime)

    def reject_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.RejectLinkMicResponse(),
            self.do_rpcrequest('RejectLinkMic', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reject_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_link_mic_with_options(request, runtime)

    def list_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppsResponse(),
            self.do_rpcrequest('ListApps', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    def add_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.AddMemberResponse(),
            self.do_rpcrequest('AddMember', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_member_with_options(request, runtime)

    def list_rooms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomsResponse(),
            self.do_rpcrequest('ListRooms', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rooms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rooms_with_options(request, runtime)

    def delete_app_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppTemplateResponse(),
            self.do_rpcrequest('DeleteAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_template_with_options(request, runtime)

    def list_conference_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListConferenceUsersResponse(),
            self.do_rpcrequest('ListConferenceUsers', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_conference_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_conference_users_with_options(request, runtime)

    def list_app_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppTemplatesResponse(),
            self.do_rpcrequest('ListAppTemplates', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    def list_components_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ListComponentsResponse(),
            self.do_rpcrequest('ListComponents', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_components(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    def update_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveResponse(),
            self.do_rpcrequest('UpdateLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_with_options(request, runtime)

    def update_app_template_config_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateConfigResponse(),
            self.do_rpcrequest('UpdateAppTemplateConfig', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_template_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_config_with_options(request, runtime)

    def apply_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.ApplyLinkMicResponse(),
            self.do_rpcrequest('ApplyLinkMic', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_link_mic_with_options(request, runtime)

    def cancel_apply_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelApplyLinkMicResponse(),
            self.do_rpcrequest('CancelApplyLinkMic', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_apply_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_apply_link_mic_with_options(request, runtime)

    def stop_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveResponse(),
            self.do_rpcrequest('StopLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_with_options(request, runtime)

    def get_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppResponse(),
            self.do_rpcrequest('GetApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    def create_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateConferenceResponse(),
            self.do_rpcrequest('CreateConference', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_conference_with_options(request, runtime)

    def delete_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveResponse(),
            self.do_rpcrequest('DeleteLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_with_options(request, runtime)

    def get_live_domain_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.GetLiveDomainStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_domain_list):
            request.live_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_domain_list, 'LiveDomainList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveDomainStatusResponse(),
            self.do_rpcrequest('GetLiveDomainStatus', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_live_domain_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_domain_status_with_options(request, runtime)

    def send_custom_message_to_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToAllResponse(),
            self.do_rpcrequest('SendCustomMessageToAll', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_message_to_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_all_with_options(request, runtime)

    def agree_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.AgreeLinkMicResponse(),
            self.do_rpcrequest('AgreeLinkMic', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def agree_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.agree_link_mic_with_options(request, runtime)

    def get_domain_owner_verify_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetDomainOwnerVerifyContentResponse(),
            self.do_rpcrequest('GetDomainOwnerVerifyContent', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_domain_owner_verify_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_owner_verify_content_with_options(request, runtime)

    def send_custom_message_to_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToUsersResponse(),
            self.do_rpcrequest('SendCustomMessageToUsers', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_message_to_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_users_with_options(request, runtime)

    def get_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAuthTokenResponse(),
            self.do_rpcrequest('GetAuthToken', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    def update_app_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateResponse(),
            self.do_rpcrequest('UpdateAppTemplate', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_with_options(request, runtime)

    def get_imp_product_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            imp_20210630_models.GetImpProductStatusResponse(),
            self.do_rpcrequest('GetImpProductStatus', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_imp_product_status(self):
        runtime = util_models.RuntimeOptions()
        return self.get_imp_product_status_with_options(runtime)

    def publish_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveResponse(),
            self.do_rpcrequest('PublishLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_live_with_options(request, runtime)

    def get_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveResponse(),
            self.do_rpcrequest('GetLive', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_with_options(request, runtime)

    def delete_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRoomResponse(),
            self.do_rpcrequest('DeleteRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_room_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateRoomResponse(),
            self.do_rpcrequest('CreateRoom', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    def update_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateConferenceResponse(),
            self.do_rpcrequest('UpdateConference', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_conference_with_options(request, runtime)

    def delete_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteConferenceResponse(),
            self.do_rpcrequest('DeleteConference', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_conference_with_options(request, runtime)

    def update_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppResponse(),
            self.do_rpcrequest('UpdateApp', '2021-06-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)
