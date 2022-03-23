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

    def add_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.from_user_id):
            body['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.to_user_id):
            body['ToUserId'] = request.to_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMember',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.AddMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_member_with_options(request, runtime)

    def agree_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.from_user_id):
            body['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.to_user_id):
            body['ToUserId'] = request.to_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AgreeLinkMic',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.AgreeLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    def agree_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.agree_link_mic_with_options(request, runtime)

    def apply_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyLinkMic',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ApplyLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_link_mic_with_options(request, runtime)

    def attach_standard_room_https_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.certificate_private_key):
            body['CertificatePrivateKey'] = request.certificate_private_key
        if not UtilClient.is_unset(request.certificate_public_key):
            body['CertificatePublicKey'] = request.certificate_public_key
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachStandardRoomHttpsCertificate',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.AttachStandardRoomHttpsCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_standard_room_https_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_standard_room_https_certificate_with_options(request, runtime)

    def ban_all_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BanAllComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.BanAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def ban_all_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ban_all_comment_with_options(request, runtime)

    def ban_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ban_comment_time):
            body['BanCommentTime'] = request.ban_comment_time
        if not UtilClient.is_unset(request.ban_comment_user):
            body['BanCommentUser'] = request.ban_comment_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BanComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.BanCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def ban_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ban_comment_with_options(request, runtime)

    def cancel_apply_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelApplyLinkMic',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelApplyLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_apply_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_apply_link_mic_with_options(request, runtime)

    def cancel_ban_all_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBanAllComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelBanAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_ban_all_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_ban_all_comment_with_options(request, runtime)

    def cancel_ban_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ban_comment_user):
            body['BanCommentUser'] = request.ban_comment_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBanComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelBanCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_ban_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_ban_comment_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_app_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_name):
            body['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.component_list_shrink):
            body['ComponentList'] = request.component_list_shrink
        if not UtilClient.is_unset(request.integration_mode):
            body['IntegrationMode'] = request.integration_mode
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppTemplate',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_template_with_options(request, runtime)

    def create_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.create_nickname):
            body['CreateNickname'] = request.create_nickname
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateClassResponse(),
            self.call_api(params, req, runtime)
        )

    def create_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_class_with_options(request, runtime)

    def create_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_conference_with_options(request, runtime)

    def create_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code_level):
            body['CodeLevel'] = request.code_level
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_with_options(request, runtime)

    def create_live_room_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateLiveRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_nick):
            body['AnchorNick'] = request.anchor_nick
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_room_with_options(request, runtime)

    def create_room_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_owner_id):
            body['RoomOwnerId'] = request.room_owner_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def create_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_app_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppTemplate',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_template_with_options(request, runtime)

    def delete_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteClassResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_class_with_options(request, runtime)

    def delete_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        body_flat = {}
        if not UtilClient.is_unset(request.comment_id_list):
            body_flat['CommentIdList'] = request.comment_id_list
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_comment_with_options(request, runtime)

    def delete_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_conference_with_options(request, runtime)

    def delete_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_with_options(request, runtime)

    def delete_live_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_room_with_options(request, runtime)

    def delete_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    def describe_meter_imp_watch_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpWatchTime',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DescribeMeterImpWatchTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_imp_watch_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_imp_watch_time_with_options(request, runtime)

    def get_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    def get_app_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppTemplate',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_template_with_options(request, runtime)

    def get_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    def get_class_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClassDetail',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetClassDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_class_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_class_detail_with_options(request, runtime)

    def get_class_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClassRecord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetClassRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_class_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_class_record_with_options(request, runtime)

    def get_cname_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCnameDetail',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetCnameDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cname_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cname_detail_with_options(request, runtime)

    def get_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conference_with_options(request, runtime)

    def get_domain_owner_verify_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_domain_name):
            body['LiveDomainName'] = request.live_domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDomainOwnerVerifyContent',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetDomainOwnerVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain_owner_verify_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_domain_owner_verify_content_with_options(request, runtime)

    def get_imp_product_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetImpProductStatus',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetImpProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_imp_product_status(self):
        runtime = util_models.RuntimeOptions()
        return self.get_imp_product_status_with_options(runtime)

    def get_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_with_options(request, runtime)

    def get_live_domain_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.GetLiveDomainStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_domain_list):
            request.live_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_domain_list, 'LiveDomainList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_domain_list_shrink):
            body['LiveDomainList'] = request.live_domain_list_shrink
        if not UtilClient.is_unset(request.live_domain_type):
            body['LiveDomainType'] = request.live_domain_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveDomainStatus',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_domain_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_domain_status_with_options(request, runtime)

    def get_live_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRecord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_with_options(request, runtime)

    def get_live_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_room_with_options(request, runtime)

    def get_live_room_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoomStatistics',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_room_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_room_statistics_with_options(request, runtime)

    def get_live_room_user_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoomUserStatistics',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomUserStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_live_room_user_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_live_room_user_statistics_with_options(request, runtime)

    def get_page_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageConfig',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetPageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_page_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_page_config_with_options(request, runtime)

    def get_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_room_with_options(request, runtime)

    def get_standard_room_https_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_id):
            body['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStandardRoomHttpsCertificate',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetStandardRoomHttpsCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_standard_room_https_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_standard_room_https_certificate_with_options(request, runtime)

    def get_standard_room_jump_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_nick):
            body['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStandardRoomJumpUrl',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetStandardRoomJumpUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_standard_room_jump_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_standard_room_jump_url_with_options(request, runtime)

    def get_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    def kick_room_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.block_time):
            body['BlockTime'] = request.block_time
        if not UtilClient.is_unset(request.kick_user):
            body['KickUser'] = request.kick_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KickRoomUser',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.KickRoomUserResponse(),
            self.call_api(params, req, runtime)
        )

    def kick_room_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kick_room_user_with_options(request, runtime)

    def list_app_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppTemplates',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    def list_apply_link_mic_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplyLinkMicUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListApplyLinkMicUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apply_link_mic_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apply_link_mic_users_with_options(request, runtime)

    def list_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integration_mode):
            body['IntegrationMode'] = request.integration_mode
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    def list_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListClassesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_classes_with_options(request, runtime)

    def list_comments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComments',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListCommentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_comments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_comments_with_options(request, runtime)

    def list_components_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_components(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    def list_conference_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConferenceUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListConferenceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_conference_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_conference_users_with_options(request, runtime)

    def list_live_rooms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLiveRooms',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_rooms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_rooms_with_options(request, runtime)

    def list_live_rooms_by_id_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.ListLiveRoomsByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_id_list):
            request.live_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_id_list, 'LiveIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id_list_shrink):
            body['LiveIdList'] = request.live_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLiveRoomsById',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveRoomsByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_rooms_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_rooms_by_id_with_options(request, runtime)

    def list_room_lives_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.ListRoomLivesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_id_list):
            request.room_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_id_list, 'RoomIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.query_timestamp):
            body['QueryTimestamp'] = request.query_timestamp
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_id_list_shrink):
            body['RoomIdList'] = request.room_id_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomLives',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomLivesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_room_lives(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_lives_with_options(request, runtime)

    def list_room_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_room_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_room_users_with_options(request, runtime)

    def list_rooms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRooms',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_rooms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rooms_with_options(request, runtime)

    def publish_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_live_with_options(request, runtime)

    def publish_live_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_live_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_live_room_with_options(request, runtime)

    def reject_link_mic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.from_user_id):
            body['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.to_user_id):
            body['ToUserId'] = request.to_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RejectLinkMic',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.RejectLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    def reject_link_mic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_link_mic_with_options(request, runtime)

    def remove_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.from_user_id):
            body['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.to_user_id):
            body['ToUserId'] = request.to_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMember',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.RemoveMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_member_with_options(request, runtime)

    def send_comment_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.SendCommentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.sender_id):
            body['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            body['SenderNick'] = request.sender_nick
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def send_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_comment_with_options(request, runtime)

    def send_custom_message_to_all_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToAll',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToAllResponse(),
            self.call_api(params, req, runtime)
        )

    def send_custom_message_to_all(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_all_with_options(request, runtime)

    def send_custom_message_to_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        body_flat = {}
        if not UtilClient.is_unset(request.receiver_list):
            body_flat['ReceiverList'] = request.receiver_list
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def send_custom_message_to_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_users_with_options(request, runtime)

    def stop_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopClassResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_class_with_options(request, runtime)

    def stop_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_with_options(request, runtime)

    def stop_live_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_live_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_room_with_options(request, runtime)

    def update_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            body['AppStatus'] = request.app_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    def update_app_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        if not UtilClient.is_unset(request.app_template_name):
            body['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.component_list_shrink):
            body['ComponentList'] = request.component_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppTemplate',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_with_options(request, runtime)

    def update_app_template_config_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        if not UtilClient.is_unset(request.config_list_shrink):
            body['ConfigList'] = request.config_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppTemplateConfig',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateAppTemplateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_template_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_config_with_options(request, runtime)

    def update_class_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.create_nickname):
            body['CreateNickname'] = request.create_nickname
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateClassResponse(),
            self.call_api(params, req, runtime)
        )

    def update_class(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_class_with_options(request, runtime)

    def update_conference_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_conference(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_conference_with_options(request, runtime)

    def update_live_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_with_options(request, runtime)

    def update_live_room_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateLiveRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_nick):
            body['AnchorNick'] = request.anchor_nick
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_room_with_options(request, runtime)

    def update_room_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_owner_id):
            body['RoomOwnerId'] = request.room_owner_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def update_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_room_with_options(request, runtime)

    def verify_domain_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_domain_name):
            body['LiveDomainName'] = request.live_domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyDomainOwner',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.VerifyDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)
